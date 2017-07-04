from joystick import Joystick
import socket

joy = Joystick()


s = None
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 59667))
    s.listen(30)
except:
    print('Not connected to Server!')

print('Started')

f = True
conn = None
while f:
    if conn == None:
        try:
            conn, addr = s.accept()
            print('Connected from', addr)
        except:
            print('Not connected to Server!')
    else:
        req = conn.recv(4000)
        if req == b'getBtns':
            conn.send('$'.join(map(str, joy.getButtons())).encode('utf-8'))
        elif req == b'getAxis':
            conn.send('$'.join(map(str, joy.getAxis())).encode('utf-8'))
        elif req == b'cExit':
            conn.close()
            conn = None
        elif req == b'exit':
            break
        else:
            print("NOT RECOGNIZED! {}".format(req))
            conn.close()
            conn = None