import sys, time
sys.path.append(r"c:\Users\Petr\Desktop\LunarLandingModuleSimulator\Joystick")

import clr
import MissionPlanner
clr.AddReference("MAVLink")
from System import Byte
import MAVLink
from MAVLink import mavlink_command_long_t
import MAVLink
from JClient import JClient

####################################
def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

class CopterUtils:
    def __init__(self, wGPS = False):
        for chan in range(1, 9):
            if chan == 3:
                continue
            Script.SendRC(chan, 1500, False)
        Script.SendRC(3, 1000, True)

        while cs.lat == 0 and wGPS:
            print('Waiting for GPS')
            Script.Sleep(1000)

        self.armed = False

    def arm(self):
        #Script.ChangeMode("ALTHOLD")
        self.setThr(1000)
        print('Arming')
        MAV.doARM(True)
        #self.setThr()
        print('Armed')
        self.armed = True

    def disarm(self):
        self.setThr(1000)
        Script.ChangeMode("STABILIZE")
        print('Disarming')
        MAV.doARM(False)
        print('Disarmed')
        self.armed = False

    def delay(self, w):
        Script.Sleep(w)

    def land(self):
        print('Landing')
        Script.ChangeMode("LAND")

    def takeoff(self, l=10):
        Script.ChangeMode("ALTHOLD")
        self.setThr(1600)
        self.delay(4000)
        self.setThr()

    def RCcal(self):
        for chan in range(1, 15):
            for i in range(1000, 2001, 100):
                print("{0}.{1}".format(chan, i))
                Script.SendRC(chan, i, True)
                self.delay(100)

    def setThr(self, e=1500):
        Script.SendRC(3, e, True)

    def parseButtons(self, e):
        return {"joy":e[:4], "b1": e[5], "b2": e[4]}


####################################

print ('Script started')

cu = CopterUtils(False)
cl = JClient({b"arm": cu.arm, b"disarm": cu.disarm, b"land": cu.land, b"takeoff": cu.takeoff})

#while 1:
#    cu.RCcal()
#    cu.delay(50)

mode = 1

print('Started')
while 1:
    axis = cl.getAxis()
    cu.delay(10)
    btns = cl.getBtns()
    if axis == []:
        print('SERVER ERROR')
        continue

    x = translate(axis[0], -1.0, 1.0, 1000.0, 2000.0)
    #y = translate(axis[1], -1.0, 1.0, 1000.0, 2000.0)
    z = translate(axis[2], -1.0, 1.0, 1000.0, 2000.0)

    Script.SendRC(1, x, False)
    #Script.SendRC(2, y, True)
    Script.SendRC(4, z, False)

    f = translate(0.0 if axis[1] >= 0.0 else axis[1], -1.0, 0.0, 2000.0, 1300.0)
    Script.SendRC(3, f, True)

    #print('{0}\t{1}\t{2}'.format(x,z,f))

    b = cu.parseButtons(btns)

    if b["b1"] and b["joy"][0] and not cu.armed:
        cu.arm()
    elif cu.armed:
        if b["b1"] and b["joy"][2]:
            cu.disarm()

        if mode == 1:
            if b["joy"][0]:
                Script.SendRC(2, 1600, True)
            elif b["joy"][2]:
                Script.SendRC(2, 1400, True)
            else:
                Script.SendRC(2, 1500, True)
        elif mode == 2:
            if b["b1"]:
                cu.setThr(1700)
            elif b["b2"]:
                cu.setThr(1300)
            else:
                cu.setThr()

    cl.sendTelemetry({'alt': cs.alt, 'roll': -cs.roll, 'pitch': cs.pitch, 'yaw': cs.yaw})
    cu.delay(20)

del cl