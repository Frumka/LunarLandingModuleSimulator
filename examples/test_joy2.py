import pygame

pygame.init()

clock = pygame.time.Clock()

pygame.joystick.init()

l1a = []
l2a = []

joystick = pygame.joystick.Joystick(0)
joystick.init()

def finish(xArr, btnArr, _l1a, _l2a):
    xArr = list(map(lambda x: round(x, 2), xArr))
    if (xArr != _l1a):
        print (xArr)
        _l1a = xArr
    if (btnArr != _l2a):
        print (btnArr)
        _l2a = btnArr
    return (_l1a, _l2a)

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            break
        if event.type:
            f1 = []
            f2 = []
            
            axes = joystick.get_numaxes()
            for i in range(4):
                axis = joystick.get_axis( i )
                f1 += [axis] if i != 2 else []
                        
            for i in range(1, 7):
                button = joystick.get_button( i )
                f2 += [button]
            l1a, l2a = finish(f1, f2, l1a, l2a)
                
        clock.tick(20)

pygame.quit ()