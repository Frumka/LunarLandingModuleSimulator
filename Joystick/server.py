from JServer import JServer
from time import sleep
from video import Video

video = Video()
server = JServer({'telem': lambda x: video.newTelemetry(x)})

#while not server.isCliennt():
#    print('', end='')

#server.send("arm")
#sleep(10)
#server.send("takeoff")