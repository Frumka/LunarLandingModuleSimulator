import pygame

class Joystick:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

    def getButtons(self):
        try:
            f2 = []
            for i in range(1, 7):
                button = self.joystick.get_button(i)
                f2 += [button]
            return f2
        except Exception:
            print("getButtons() - Exception")
            return []

    def getAxis(self):
        try:
            f1 = []
            for i in range(4):
                axis = self.joystick.get_axis(i)
                f1 += [axis] if i != 2 else []
            return f1
        except Exception:
            print("getAxes() - Exception")
            return []

    def __delete__(self, instance):
        pygame.quit()