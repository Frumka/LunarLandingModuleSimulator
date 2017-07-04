import sys
sys.path.append(r"c:\Users\Petr\Desktop\LunarLandingModuleSimulator\Joystick")

from JClient import JClient

cl = JClient()

print('Started')

print(cl.getAxis())
print(cl.getBtns())

del cl