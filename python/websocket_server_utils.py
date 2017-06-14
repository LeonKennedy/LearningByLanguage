# Embedded file name: common\utils\websocket_server_utils.pyo
from collections import deque
import json
import os
import re
import socket
import hashlib
import threading
import time
import struct
from base64 import b64encode
import traceback
import urllib
import logging
logger =  logging.getLogger("olenji")
cf = logging.StreamHandler()
logger.addHandler(cf)
# from common.utils.log_utils import logger
CHECK_ADDRESS_MSG_PATTERN = re.compile('\\{(.*)\\}', re.S)
g_code_length = 0
g_header_length = 0

def hex2dec(string_num):
    return str(int(string_num.upper(), 16))


def get_msg_length(msg):
    global g_header_length
    global g_code_length
    g_code_length = ord(msg[1]) & 127
    if g_code_length == 126:
        g_code_length = struct.unpack('>H', str(msg[2:4]))[0]
        g_header_length = 8
    elif g_code_length == 127:
        g_code_length = struct.unpack('>Q', str(msg[2:10]))[0]
        g_header_length = 14
    else:
        g_header_length = 6
    g_code_length = int(g_code_length)
    return g_code_length


def parse_data(msg):
    global g_code_length
    g_code_length = ord(msg[1]) & 127
    if g_code_length == 126:
        g_code_length = struct.unpack('>H', str(msg[2:4]))[0]
        masks = msg[4:8]
        data = msg[8:]
    elif g_code_length == 127:
        g_code_length = struct.unpack('>Q', str(msg[2:10]))[0]
        masks = msg[10:14]
        data = msg[14:]
    else:
        masks = msg[2:6]
        data = msg[6:]
    i = 0
    raw_str = ''
    for d in data:
        raw_str += chr(ord(d) ^ ord(masks[i % 4]))
        i += 1

    return raw_str


class WebSocket(threading.Thread):

    def __init__(self, parent, conn, client_address):
        threading.Thread.__init__(self)
        self.web_socket_server = parent
        self.conn = conn
        self.client_index = self.web_socket_server.connected_client_num
        self.client_address = client_address
        self.buffer = ''
        self.buffer_utf8 = ''
        self.buffer_length = 0
        self.exception_count = 0
        self.is_handshaken = False
        self.GUID = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'

    def send_msg_to_client(self, msg):
        message_utf_8 = msg.encode('utf-8')
        socket_msg_list = []
        socket_msg_list.append('\x81')
        data_length = len(message_utf_8)
        if data_length <= 125:
            socket_msg_list.append(chr(data_length))
        elif data_length <= 65535:
            socket_msg_list.append(struct.pack('b', 126))
            socket_msg_list.append(struct.pack('>h', data_length))
        elif data_length <= 2 ^ 63:
            socket_msg_list.append(struct.pack('b', 127))
            socket_msg_list.append(struct.pack('>q', data_length))
        else:
            logger.error('websocket: send msg too long')
        msg = ''.join(socket_msg_list)
        socket_msg = '%s%s' % (str(msg), message_utf_8)
        if socket_msg:
            self.conn.send(socket_msg)

    def run(self):
        global g_code_length
        headers = {}
        while True:
            if not self.is_handshaken:
                logger.info('websocket: client_%s_%s: start handshake' % (self.client_index, self.client_address))
                self.buffer += bytes.decode(self.conn.recv(1024))
                if self.buffer.find('\r\n\r\n') >= 0:
                    header, data = self.buffer.split('\r\n\r\n', 1)
                    for line in header.split('\r\n')[1:]:
                        key, value = line.split(': ', 1)
                        headers[key] = value

                    headers['Location'] = 'ws://%s/' % headers['Host']
                    token = b64encode(hashlib.sha1(str.encode(str(headers['Sec-WebSocket-Key'] + self.GUID))).digest())
                    handshake = 'HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: %s\r\nWebSocket-Origin: %s\r\nWebSocket-Location: %s\r\n\r\n' % (bytes.decode(token), headers['Origin'], headers['Location'])
                    self.conn.send(str.encode(str(handshake)))
                    self.is_handshaken = True
                    handshake_msg = 'client_%s_%s: handshaken success' % (self.client_index, self.client_address)
                    logger.info(handshake_msg)
                    self.send_msg_to_client(handshake_msg)
                    g_code_length = 0
            else:
                now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                try:
                    msg = self.conn.recv(8192)
                    self.exception_count = 0
                    if len(msg) <= 0:
                        continue
                    if g_code_length == 0:
                        get_msg_length(msg)
                    self.buffer += msg
                    self.buffer_length += len(msg)
                    if self.buffer_length - g_header_length < g_code_length:
                        continue
                    else:
                        self.buffer_utf8 = parse_data(self.buffer)
                        msg_unicode = self.buffer_utf8.decode('utf-8', 'ignore')
                        if msg_unicode:
                            if msg_unicode.startswith('%7B'):
                                end_pos = msg_unicode.find('%7D')
                                msg_unicode = urllib.unquote(str(msg_unicode[:end_pos + 3]))
                                msg_info = json.loads(msg_unicode)
                                msg_unicode = msg_unicode.decode('utf-8')
                            else:
                                try:
                                    msg_info = json.loads(msg_unicode)
                                except:
                                    if 'check_address' in msg_unicode:
                                        start_pos = msg_unicode.find('{')
                                        end_pos = msg_unicode.find('}')
                                        msg_info = json.loads(msg_unicode[start_pos:end_pos + 1])

                            msg_info['client_index'] = self.client_index
                            self.web_socket_server.add_to_client_msg_deque(msg_info)
                            logger.info('websocket: %s' % u'time: %s, client_%s_%s got msg: %s' % (now_time,
                             self.client_index,
                             str(self.client_address),
                             msg_info))
                            self.send_msg_to_client(msg_unicode)
                except ValueError:
                    logger.error(traceback.format_exc())
                except:
                    error_msg = traceback.format_exc()
                    logger.error(error_msg)
                    if '10053' in error_msg or '10054' in error_msg:
                        self.exception_count += 1
                        if self.exception_count >= 5:
                            self.conn.close()
                            client_key = 'client_%s' % self.client_index
                            if client_key in self.web_socket_server.connected_client_dic:
                                del self.web_socket_server.connected_client_dic[client_key]
                            logout_msg = u'time: %s, client_%s_%s logout\n' % (now_time, self.client_index, str(self.client_address))
                            logger.error('websocket: %s' % logout_msg)
                            break

            self.buffer = ''
            self.buffer_utf8 = ''
            self.buffer_length = 0
            g_code_length = 0



class WebSocketServer(object):

    def __init__(self):
        self.client_msg_deque = deque()
        self.client_msg_mutex = threading.Lock()
        self.connected_client_num = 0
        self.socket = None
        self.port = None
        self.connected_client_dic = {}
        return

    def add_to_client_msg_deque(self, msg):
        self.client_msg_mutex.acquire()
        self.client_msg_deque.append(msg)
        self.client_msg_mutex.release()

    def get_client_msg_deque(self):
        client_msg_deque = deque()
        self.client_msg_mutex.acquire()
        while self.client_msg_deque:
            client_msg_deque.append(self.client_msg_deque.pop())

        self.client_msg_mutex.release()
        return client_msg_deque

    def begin_listen(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                dos_cmd = 'netstat -nao | find "49317"'
                process_info = os.popen(dos_cmd).read()
                if process_info:
                    self.socket.bind(('127.0.0.1', 0))
                else:
                    self.socket.bind(('127.0.0.1', 49317))
            except:
                logger.error(traceback.format_exc())
                self.socket.bind(('127.0.0.1', 0))

            socket_info = self.socket.getsockname()
            self.port = socket_info[1]
            self.socket.listen(50)
            logger.info('WebSocket: Server start listen: %s' % str(socket_info))
            while True:
                conn, client_address = self.socket.accept()
                logger.info('websocket: client_%s request connect: %s' % (self.connected_client_num, client_address))
                web_socket = WebSocket(self, conn, client_address)
                web_socket.start()
                self.connected_client_dic['client_%s' % self.connected_client_num] = web_socket
                self.connected_client_num += 1

        except:
            logger.error(traceback.format_exc())
            time.sleep(20)


if __name__ == '__main__':
    server = WebSocketServer()
    server.begin_listen()
