import socket
import librosa
import numpy as np


def get_response(filename):
    wav, sr = librosa.load(filename, sr=16000, mono=True, offset=1.0, duration=None, dtype=np.float32)
    print(wav[:100])
    print(wav.max())
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) as sock:
        # Connect to server and send data
        print("start")
        sock.connect(("127.0.0.1", 9492))
        sock.sendall(wav.tobytes())
        # Receive data from the server and shut down
        print("send end")
        received = bytes()
        while 1:
            block = sock.recv(100)
            print(block)
            if block == b'':
                break
            received += block
    print(str(received, "utf-8"))


if __name__ == "__main__":
    get_response("../mp3/build/test.mp3")
