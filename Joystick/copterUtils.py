# RC MIN/MAX 1000/2000
# Comment this to run
#Script = None
#cs = None

import sys, time
sys.path.append(r"c:\Users\Petr\Desktop\LunarLandingModuleSimulator\Joystick")

import clr
import MissionPlanner
clr.AddReference("MAVLink")
from System import Byte
import MAVLink
from MAVLink import mavlink_command_long_t
import MAVLink

class CopterUtils:
    def __init__(self, s, cs, wGPS = False):
        self.s = s
        self.cs = cs
        for chan in range(1, 9):
            s.SendRC(chan, 1500, False)
            s.SendRC(3, s.GetParam('RC3_MIN'), True)

        while cs.lat == 0 and wGPS:
            print('Waiting for GPS')
            s.Sleep(1000)

    def arm(self):
        MAV.doARM(True)

    def disarm(self):
        MAV.doARM(False)

    def delay(self, w):
        self.s.Sleep(w)
