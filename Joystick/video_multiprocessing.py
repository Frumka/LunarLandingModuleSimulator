# coding=utf-8
from multiprocessing import Process, Pipe, Queue
from subprocess import Popen, PIPE
import multiprocessing
from PIL import Image
import numpy as np
import threading
import imutils
import urllib
import math
import time
import cv2

millis = lambda: int(round(time.time() * 1000))

font = cv2.FONT_HERSHEY_SIMPLEX

pos1screen = (0, 0)
pos2screen = (0, 0)
resolution = (1360, 762)


def capture(imgQueue, id):
    if id == 0:
        cam = downloadImg("http://127.0.0.1:8888/out.jpg")
    else:
        cam = downloadImg("http://127.0.0.1:8889/out.jpg")

    cam = cv2.resize(cam, resolution, interpolation=cv2.INTER_NEAREST)
    imgQueue.put([id, cam])


def capture2(id):
    if id == 0:
        cam = downloadImg("http://127.0.0.1:8888/out.jpg")
    else:
        cam = downloadImg("http://127.0.0.1:8889/out.jpg")

    cam = cv2.resize(cam, resolution, interpolation=cv2.INTER_NEAREST)
    return cam

def downloadImg(url):
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


class Video:
    def __init__(self):
        self.imgQueue = Queue()
        self.videoproc = []



        '''
        s = millis()
        self.requestFrame()
        e = millis()
        time.sleep(1)
        ee = millis()
        cam1, cam2 = self.getFrame()
        '''

        multiprocessing.freeze_support()
        pool = multiprocessing.Pool(processes=1, )
        clc = time.time()
        cam1, cam2 = pool.map(capture2, [0, 1])
        clc = time.time() - clc
        print clc


        clc = time.time()
        cam = downloadImg("http://127.0.0.1:8888/out.jpg")
        cam2 = downloadImg("http://127.0.0.1:8889/out.jpg")
        cam, cam2 = cv2.resize(cam, resolution, interpolation=cv2.INTER_NEAREST), cv2.resize(cam, resolution, interpolation=cv2.INTER_NEAREST)
        clc = time.time() - clc
        print clc


    def requestFrame(self):
        p = Process(target=capture, args=(self.imgQueue,0))
        self.videoproc.append(p)
        p.start()

        p2 = Process(target=capture, args=(self.imgQueue,1))
        self.videoproc.append(p2)
        p2.start()

    def getFrame(self):
        if self.imgQueue.qsize() >= 1:
            cam1 = self.imgQueue.get()
            cam2 = self.imgQueue.get()
            if cam1[0] != 0 and cam2[0] != 0:
                cam2 = self.imgQueue.get()

            self.videoproc.pop(0).join()
            self.videoproc.pop(0).join()
            return cam1[1], cam2[1]
        return None, None


POISON_PILL = "STOP"

'''
def process_odds(in_queue, shared_list):
    while True:
        new_value = in_queue.get()

        if new_value == POISON_PILL:
            break

        shared_list.append(new_value/2)
    return

def process_evens(in_queue, shared_list):
    while True:
        new_value = in_queue.get()
        if new_value == POISON_PILL:
            break

        shared_list.append(new_value/-2)
    return
'''

def process1cam(q):
    while 1:
        print('2')
        cam = downloadImg("http://127.0.0.1:8888/out.jpg")
        q.put(cam)

def process2cam(q):
    while 1:
        print('1')
        cam = downloadImg("http://127.0.0.1:8889/out.jpg")
        q.put(cam)

def main():
    multiprocessing.freeze_support()

    manager = multiprocessing.Manager()

    cam1_queue = manager.Queue()
    cam2_queue = manager.Queue()
    telem_queue = manager.Queue()

    pool = multiprocessing.Pool()

    cam1_result = pool.apply_async(process1cam, (cam1_queue))
    cam2_result = pool.apply_async(process2cam, (cam2_queue))

    #process1cam(cam1_queue)
    #process2cam(cam2_queue)

    while 1:
        cam1, cam2 = cam1_queue.get(), cam2_queue.get()
        cv2.imshow("1", cam1)
        cv2.imshow("2", cam2)
        cv2.waitKey(1)

    pool.close()
    pool.join()

    return

if __name__ == "__main__":
    main()