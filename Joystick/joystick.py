import pygame

class Joystick:
    def __init__(self):
        pygame.display.init()
        pygame.joystick.init()
        pygame.joystick.Joystick(0).init()

    def getButtons(self):
        try:
            pygame.event.pump()
            f2 = []
            for i in range(1, 7):
                button = pygame.joystick.Joystick(0).get_button(i)
                f2 += [button]
            return f2
        except Exception:
            print("getButtons() - Exception")
            return []

    def getAxis(self):
        try:
            pygame.event.pump()
            f1 = []
            for i in range(4):
                axis = pygame.joystick.Joystick(0).get_axis(i)
                f1 += [axis] if i != 2 else []
            return list(map(lambda x: round(x, 2), f1))
        except Exception:
            print("getAxes() - Exception")
            return []

    def __delete__(self, instance):
        pygame.quit()