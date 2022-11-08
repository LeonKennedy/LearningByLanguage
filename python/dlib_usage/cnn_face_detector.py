#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2022, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@gmail.com
@file: cnn_face_detector.py
@time: 2022/11/8 17:46
@desc:
"""
import sys
import dlib
import cv2

if len(sys.argv) < 2:
    print(
        "Call this program like this:\n"
        "   ./cnn_face_detector.py  ../examples/faces/*.jpg\n"
        "You can get the mmod_human_face_detector.dat file from:\n"
        "    http://dlib.net/files/mmod_human_face_detector.dat.bz2")
    exit()

cnn_face_detector = dlib.cnn_face_detection_model_v1("./mmod_human_face_detector.dat")

for f in sys.argv[1:]:
    print("Processing file: {}".format(f))
    image = cv2.imread(f)
    img = dlib.load_rgb_image(f)
    # The 1 in the second argument indicates that we should upsample the image
    # 1 time.  This will make everything bigger and allow us to detect more
    # faces.
    dets = cnn_face_detector(img, 1)

    print("Number of faces detected: {}".format(len(dets)))
    for i, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {} Confidence: {}".format(
            i, d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom(), d.confidence))

    # rects = dlib.rectangles()
    # rects.extend([d.rect for d in dets])
    rect = dets[0].rect
    image = cv2.rectangle(image, (rect.left(), rect.top()), (rect.right(), rect.bottom()), (255, 0, 0), 2)
    cv2.imshow("face location", image)
    cv2.waitKey()
