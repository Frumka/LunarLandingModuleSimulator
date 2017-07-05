from JServer import JServer

server = JServer()

'''
from joystick import Joystick
import socket
import time
import threading

#t = threading.Thread(target=test)
#t.daemon = True

joy = Joystick()

millis = lambda: int(round(time.time() * 1000))

s = None
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 59667))
    s.listen(30)
except:
    print('Not connected to Server!')

print('Started')

conn = None
tm = millis()
while True:
    if conn == None:
        try:
            conn, addr = s.accept()
            conn.timeout = 2000
            print('Connected from', addr)
            tm = millis()
            #t.start()
        except:
            print('Not connected to Server!')
    else:
        req = conn.recv(4000)
        if req == b'getBtns':
            conn.send('$'.join(map(str, joy.getButtons())).encode('utf-8'))
            tm = millis()
        elif req == b'getAxis':
            conn.send('$'.join(map(str, joy.getAxis())).encode('utf-8'))
            tm = millis()
        elif req == b'cExit':
            conn.close()
            conn = None
            tm = millis()
        elif req == b'exit':
            break
        else:
            print("NOT RECOGNIZED! {}".format(req))
            conn.close()
            conn = None
    print(conn == None)


def test(interval):
    while True:
        if (millis() - tm) > 100000:
            print('CLIENT TIMEOUT. DISCONNECTING')
            try:
                conn.close()
            except:
                print('', end='')
            conn = None

s.close()
del s
del joy
'''