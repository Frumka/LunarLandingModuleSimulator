from joystick import Joystick
import socket
import time
import threading

millis = lambda: int(round(time.time() * 1000))

class JServer:
    def __init__(self):
        self.s = None
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind(('127.0.0.1', 59667))
            self.s.listen(30)
        except:
            print('Not connected to Server!')
            self.__init__()

        self.joy = Joystick()
        self.tm = millis()
        self.r = True
        self.conn = None
        self.d = False

        self.runt = threading.Thread(target=self.run)
        self.runt.start()

        self.pingt = threading.Thread(target=self.timeout)
        self.pingt.start()

    def timeout(self):
        while self.r:
            if (millis() - self.tm) > 5000 and self.conn != None and not self.d:
                self.d = True
                try:
                    self.conn.close()
                    del self.conn
                    self.conn = None
                    self.d = False
                except:
                    print('')
                print('CLIENT TIMEOUT. DISCONNECTING')

    def accept(self):
        self.d = True
        try:
            self.conn, self.addr = self.s.accept()
            print('Connected from', self.addr)
            self.tm = millis()
            self.d = False
        except:
            print('Failed to connect to client!')

    def run(self):
        while self.r:
            if self.d:
                continue

            if self.conn == None and not self.d:
                self.accept()
            else:
                try:
                    req = self.conn.recv(4000)
                    self.tm = millis()
                    if req == b'getBtns':
                        self.conn.send('$'.join(map(str, self.joy.getButtons())).encode('utf-8'))
                    elif req == b'getAxis':
                        self.conn.send('$'.join(map(str, self.joy.getAxis())).encode('utf-8'))
                    elif req == b'cExit':
                        self.conn.close()
                        self.conn = None
                    elif req == b'exit':
                        self.r = False
                        break
                    else:
                        print("NOT RECOGNIZED! {}".format(req))
                        self.conn.close()
                        self.conn = None
                except:
                    print('GET DATA ERROR')

    def __delete__(self, instance):
        try:
            instance.s.close()
            del instance.s
            del instance.joy
            self.s.close()
            del self.s
            del self.joy
        except:
            print('', end='')