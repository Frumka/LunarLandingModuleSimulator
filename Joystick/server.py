from joystick import Joystick
import socket

joy = Joystick()

print('Started')

f = True
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 59667))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected from', addr)
except:
    print('Server not started! Exitting')
    f = False

while f:
    req = conn.recv(4000)
    if req == 'getBtns':
        conn.send('#'.join(map(str, joy.getButtons())))
    elif req == 'getAxis':
        conn.send('#'.join(map(str, joy.getAxes())))
    elif req == 'exit':
        break
    else:
        print("NOT RECOGNIZED! {}".format(req))

conn.close()