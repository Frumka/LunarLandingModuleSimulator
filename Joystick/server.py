from JServer import JServer
from video import Video

#video = Video(False, False)
#video.newTelemetry({'alt': 41, 'roll': 24, 'pitch':16, 'yaw': 56, 'tg': 40})
#server = JServer({'telem': lambda x: video.newTelemetry(x)})
server = JServer({})
server.run()
#while not server.isCliennt():
#    print('', end='')

#server.send("arm")
#sleep(10)
#server.send("takeoff")