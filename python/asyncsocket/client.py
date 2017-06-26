#-*- coding: utf-8 -*-
import socket, time, select, sys, thread, json

BUFSIZ = 2048
ADDR = ('127.0.0.1', 62133)
tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpCliSock.connect(ADDR)
input = [tcpCliSock, ]


class Clien:

    msg_list = [{"msg_time": "2017-06-15 14:12:52.160000", "msg": "快商通", "pin": "cntaobaosavingfly"},]
    # msg_list = list()
    def send_test(self):
        data=raw_input('>')
        tcpCliSock.sendall(data)
        data = tcpCliSock.recv(BUFSIZ)
        print("data from server : %s" % data)
        time.sleep(15)

    def recive_data(self, data):
        time.sleep(1)
        self.msg_list.append(data)

    def send(self):
        while True:
            readyInput, readyOutput, readyException = select.select(input, [tcpCliSock], input)
            for outdata in readyOutput:
                if self.msg_list:
                    data = self.get_msg()
                    outdata.send(data)
                    # print 1
            for indata in readyInput:
                data = tcpCliSock.recv(BUFSIZ)
                print(data)


        tcpCliSock.close()

    def get_msg(self):
        data = self.msg_list.pop()
        return json.dumps(data,)

if __name__ == "__main__" :
    c = Clien()
    thread.start_new_thread(c.send,())
    # c.send()

    data = dict()
    data['pin'] = "cntaobaosavingfly"
    while True:
        a = raw_input(">>")
        data['msg'] = a
        c.msg_list.append(data)
