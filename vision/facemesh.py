#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2022, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@gmail.com
@file: facemesh.py
@time: 2022/10/25 11:21
@desc:
"""
import cv2
import mediapipe as mp
from mediapipe.python.solutions.drawing_utils import DrawingSpec

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh


FACEMESH_CONTOURS = frozenset().union(*[
    mp_face_mesh.FACEMESH_LEFT_EYE,
    mp_face_mesh.FACEMESH_LEFT_EYEBROW,
    mp_face_mesh.FACEMESH_RIGHT_EYE,
    mp_face_mesh.FACEMESH_RIGHT_EYEBROW,
    mp_face_mesh.FACEMESH_FACE_OVAL
])
# For webcam input:
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
TESSELATION_FLAG = True
CONTOURS_FLAG = True
IRISES_FLAG = True
LIPS_FLAG = True
MASK_FLAG = False

print("1. landmark网格")
print("2. 脸部轮廓")
print("3. 虹膜")
print("4. 嘴唇")
print("5. 面具")

ds = DrawingSpec((128, 128, 128), thickness=10)
once = False
with mp_face_mesh.FaceMesh(
        max_num_faces=2,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)

        # Draw the face mesh annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                if once:
                    mp_drawing.plot_landmarks(face_landmarks)
                    once = False
                if TESSELATION_FLAG:
                    thick = 11 if MASK_FLAG else 1
                    ds = DrawingSpec((128, 128, 128), thickness=thick)
                    mp_drawing.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=mp_face_mesh.FACEMESH_TESSELATION,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=ds)
                if CONTOURS_FLAG:
                    mp_drawing.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=FACEMESH_CONTOURS,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style())
                if IRISES_FLAG:
                    mp_drawing.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=mp_face_mesh.FACEMESH_IRISES,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style())
                if LIPS_FLAG:
                    mp_drawing.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=mp_face_mesh.FACEMESH_LIPS,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style())
        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Face Mesh', cv2.flip(image, 1))
        press_key = cv2.waitKey(5) & 0xFF
        if press_key == 27:
            break
        elif press_key == 49:
            TESSELATION_FLAG = not TESSELATION_FLAG
        elif press_key == 50:
            CONTOURS_FLAG = not CONTOURS_FLAG
        elif press_key == 51:
            IRISES_FLAG = not IRISES_FLAG
        elif press_key == 52:
            LIPS_FLAG = not LIPS_FLAG
        elif press_key == 53:
            MASK_FLAG = not MASK_FLAG
        elif press_key == 32:
            cv2.waitKey(0)
            continue
cap.release()
