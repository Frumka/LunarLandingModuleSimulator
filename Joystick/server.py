from JServer import JServer
from video import Video

video = Video(False, True)
server = JServer({'telem': lambda x: video.newTelemetry(x)})

#while not server.isCliennt():
#    print('', end='')

#server.send("arm")
#sleep(10)
#server.send("takeoff")