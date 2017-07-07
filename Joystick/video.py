import numpy as np
import cv2
import sys

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Failed to initialize")
    exit(0)

ret, frame = cap.read()

if not ret:
    print("Failed to read frame")
    exit(0)

cv2.imwrite(sys.argv[1], frame)