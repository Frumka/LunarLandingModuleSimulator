import socket
from System.Threading import Thread, ThreadStart

class JClient:
    def ping(self):
        try:
            self.s.send('ping')
        except:
            return

    def __init__(self, cb):
        self.s = None
        self.f = True
        self.cb = cb

        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect(('127.0.0.1', 59667))
        except:
            print("Connection Error!!!")
            self.f = False
            self.__init__(cb)

        #self.getdatathread = Thread(ThreadStart(self.getDataAsync))
        #self.getdatathread.Start()

    def getAxis(self):
        if not self.f:
            return []
        try:
            self.s.send('getAxis')
            data = self.s.recv(5000)
            return list(map(float, data.split('$')))
        except:
            return []

    def getBtns(self):
        if not self.f:
            return []
        try:
            self.s.send('getBtns')
            data = self.s.recv(5000)
            return list(map(bool, map(int, data.split('$'))))
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
        instance.s.send('cExit')
        self.s.close()
        instance.s.close()

    def getDataAsync(self):
        while 1:
            if not self.f:
                print (''), ''
                continue
            try:
                pass
                #data = self.s.recv(5000)
                #print(data)
                #if data in self.cb:
                #   self.cb[data]()
            except:
                print('getDataAsync - Exception')