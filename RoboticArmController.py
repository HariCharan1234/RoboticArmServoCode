import socket as sock
import time as tm


class connect:
    def __init__(self, ip):
        self.s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        self.connection = self.s.connect((ip, 80))

    def commandang(self, arm, angle):
        self.s.send(bytes(f"{arm},{angle}", "utf-8"))
        #msg = self.s.recv(1024, 80).decode("utf-8")
    def eer(self):
        self.s.send(bytes("End Effector,release", "utf-8"))
    def eee(self):
        self.s.send(bytes("End Effector,engage", "utf-8"))
