import numpy as np
import threading
import imutils
import urllib
import math
import time
import cv2
from PIL import Image

millis = lambda: int(round(time.time() * 1000))

font = cv2.FONT_HERSHEY_SIMPLEX

pos1screen = (0, 0)
pos2screen = (0, 0)

resolution = (1360, 762)

class Video:
    def __init__(self):
        print('Starting OSD')
        self.telem = None
        self.ll = None

        self.runt = threading.Thread(target=self.run)
        self.runt.start()

        self.c = 0
        print('OSD waiting telemetry')

    def downloadImg(s, url):
        resp = urllib.urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image

    def getCams(s):
        try:
            cam1 = s.downloadImg("http://127.0.0.1:8888/out.jpg")
            cam2 = s.downloadImg("http://127.0.0.1:8889/out.jpg")
        except:
            print('Video get error')
            return None, None
        return cam1, cam2

    def processCam1(s, img):
        cv2.putText(img, 'Altitude: {}m'.format(s.telem['alt']), (10, 730), font, 1, (0, 255, 0), 2)
        img = s.createHorizont(img)
        return img

    def processCam2(s, img):
        return img

    def newTelemetry(s, telem):
        s.telem = telem

    def showErr(self):
        img = cv2.imread('media/error.png')
        cv2.imshow("Image", img)
        cv2.imshow("Image2", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def createHorizont(self, image):
        hor = cv2.imread('media/horizont.png', cv2.IMREAD_UNCHANGED)
        hor = imutils.rotate_bound(hor, self.telem['roll'])

        (wH, wW) = hor.shape[:2]
        (h, w) = image.shape[:2]

        image = np.dstack([image, np.ones((h, w), dtype="uint8") * 255])

        (B, G, R, A) = cv2.split(hor)
        B = cv2.bitwise_and(B, B, mask=A)
        G = cv2.bitwise_and(G, G, mask=A)
        R = cv2.bitwise_and(R, R, mask=A)
        hor = cv2.merge([B, G, R, A])

        overlay = np.zeros((h, w, 4), dtype="uint8")
        x = math.ceil((h - wH)/2)
        y = math.ceil((w - wW)/2)
        overlay[x:x+wH, y:y+wW] = hor

        output = image.copy()
        cv2.addWeighted(overlay, 1.0, output, 0.8, 0.7, output)

        return output

    def run(s):
        # 720x576
        start = time.time()
        stop = 0
        frames = 0
        while 1:
            if not s.telem:
                continue
            elif not s.ll:
                print('OSD initialized')
                s.ll = True

            xst = time.time()
            cam1, cam2 = s.getCams()
            xsf = time.time()
            #print('!> {}'.format(xsf-xst))
            if cam1 == None:
                cv2.destroyAllWindows()
                s.showErr()
                s.c += 1
                continue

            #cam1, cam2 = cv2.resize(cam1, resolution, interpolation=cv2.INTER_NEAREST), cv2.resize(cam2, resolution, interpolation=cv2.INTER_NEAREST)
            #cam1, cam2 = s.processCam1(cam1), s.processCam2(cam2)

            cv2.namedWindow("First camera", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("First camera", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
            cv2.namedWindow("Second camera", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Second camera", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
            cv2.imshow("First camera", cam1)
            cv2.imshow("Second camera", cam2)
            cv2.moveWindow("First camera", *pos1screen)
            cv2.moveWindow("Second camera", *pos2screen)

            frames += 1

            x = cv2.waitKey(1)
            if x == 27 or frames == 500:
                stop = time.time()
                break

        fps = 500 / (stop - start)
        print(fps)

        cv2.destroyAllWindows()

        s.run()