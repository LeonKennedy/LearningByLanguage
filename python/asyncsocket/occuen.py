import socket, select, sys, time, traceback, thread, json
from collections import deque


class Sever:

    def __init__(self):
        # self.startB7Lib()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.kst_receiv_msgs = deque()
        self.kst_send_msgs = deque()
        thread.start_new_thread(self.kst_socket_server, ())

    def kst_socket_server(self):
        ADDR = ('127.0.0.1', 62133)
        tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpSerSock.bind(ADDR)
        bufferzise = 1024
        tcpSerSock.listen(5)
        print("start kst server in %s" % str(ADDR))

        while True:
            tcpCliSock, addr = tcpSerSock.accept()
            print("connect from %s" % str(addr))
            inputs = [tcpCliSock]
            output = [tcpCliSock]
            errput = [tcpCliSock]
            try:
                while True:
                    r_list, w_list, e_list = select.select(inputs, output, errput, 1)
                    try:
                        for indata in r_list:
                            data = indata.recv(bufferzise)
                            self.kst_send_msgs.append(data)
                            print("kst need send data is %s" % data)
                            # send
                            # params = json.load(data)
                            # self.send_msg(**params)
                    except:
                        print(2)
                        traceback.print_exc()
                        inputs.remove(tcpCliSock)
                        output.remove(tcpCliSock)
                        errput.remove(tcpCliSock)
                        break

                    for outdata in w_list:
                        if self.kst_receiv_msgs:
                            msg = self.kst_receiv_msgs.pop()
                            print("kst revice msg is : % s" % str(msg))
                            outdata.sendall(str(msg))

                    if e_list:
                        print(3)
                        inputs.remove(tcpCliSock)
                        output.remove(tcpCliSock)
                        errput.remove(tcpCliSock)
                        break
            except:
                traceback.print_exc()
            print("restart listen!")

    def begin_listen(self):
        while True:
            tcpCliSock, addr = self.tcpSerSock.accept()
            print("..connected from %s" % str(addr))
            data = tcpCliSock.recv(self.BUFSIZ)
            print("data : %s" % str(data))
            tcpCliSock.sendall("hello client")
            tcpCliSock.close()

    def send_msg(self):
        self.kst_receiv_msgs.append("hello client")


if __name__ == "__main__":
    # begin_lis()
    s = Sever()
    # s.kst_socket_server()
    while True:
        time.sleep(5)
        print("wait 5 s and len is %d" % len(s.kst_receiv_msgs))
        s.send_msg()
