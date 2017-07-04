import socket

class JClient:
    def __init__(self):
        self.s = None
        self.f = True

        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s .connect(('127.0.0.1', 59667))
        except:
            print("Connection Error!!!")
            self.f = False
            self.__init__()

    def getAxis(self):
        if not self.f:
            return []
        try:
            self.s.send('getAxis')
            data = self.s.recv(5000)
            return data
        except:
            return []

    def getBtns(self):
        if not self.f:
            return []
        try:
            self.s.send('getBtns')
            data = self.s.recv(5000)
            return data
        except:
            return []
    def killServer(self):
        if not self.f:
            return None
        try:
            self.s.send('exit')
        except:
            return None

    def __delete__(self, instance):
        self.s.close()
        self.s.close()