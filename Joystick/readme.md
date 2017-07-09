## How to run
USE PYTHON 2.
 1. `git clone https://github.com/BardinPetr/LunarLandingModuleSimulator.git`
 2. Change line **#2** at *Joystick/client.py* to **sys.path.append(r" {{ Your path to root project folder (to directory Joystick/) }} ")**
 3. Install OpenCV2 and PyQT4
 4. `pip install numpy imutils pillow`
 5. `python Joystick/server.py`
 6. Open MP and connect to APM
 7. Run script *Joystick/client.py* in MP
 8. Arm - Left button + trigger
 9. Disarm - Forward button + trigger