#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2022, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@gmail.com
@file: face_pcd.py
@time: 2022/10/28 10:42
@desc:
"""
from typing import List

import cv2
import open3d as o3d
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh


def get_face_mesh():
    cap = cv2.VideoCapture(0)
    with mp_face_mesh.FaceMesh(
            max_num_faces=2,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as face_mesh:
        while 1:
            success, image = cap.read()
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(image)
            if results.multi_face_landmarks:
                break
            cv2.waitKey(10)

    cap.release()
    for face_landmarks in results.multi_face_landmarks:
        xyz = np.array([(l.x, l.y, l.z) for l in face_landmarks.landmark])
        return xyz


def get_triangles() -> List:
    return [[34, 139, 127], [0, 11, 37], [232, 120, 231], [72, 37, 39], [128, 121, 47], [232, 121, 128], [104, 67, 69],
            [171, 148, 175], [50, 101, 118], [40, 73, 39], [9, 108, 151], [48, 115, 131], [194, 211, 204],
            [40, 185, 74], [80, 42, 183], [40, 186, 92], [118, 229, 230], [202, 212, 214], [17, 18, 83], [146, 76, 61],
            [160, 29, 30], [56, 157, 173], [194, 106, 204], [192, 214, 135], [98, 203, 165], [68, 21, 71], [51, 4, 45],
            [144, 24, 23], [146, 91, 77], [50, 187, 205], [200, 201, 18], [106, 91, 182], [90, 91, 181], [17, 84, 85],
            [203, 36, 206], [140, 171, 148], [40, 92, 39], [193, 244, 189], [28, 158, 159], [161, 246, 247],
            [196, 3, 236], [104, 68, 54], [168, 193, 8], [228, 117, 31], [193, 189, 55], [97, 98, 99], [100, 126, 47],
            [218, 166, 79], [26, 154, 155], [209, 131, 49], [136, 150, 135], [217, 126, 47], [52, 53, 223],
            [51, 45, 134], [170, 211, 140], [67, 108, 69], [91, 106, 43], [120, 230, 119], [226, 247, 130],
            [52, 53, 63], [242, 20, 238], [70, 156, 46], [62, 96, 78], [53, 46, 63], [34, 227, 143], [123, 117, 111],
            [19, 44, 125], [51, 236, 134], [216, 205, 206], [153, 154, 22], [167, 37, 39], [200, 201, 208],
            [100, 36, 142], [57, 202, 212], [99, 20, 60], [28, 157, 158], [113, 226, 35], [160, 27, 159],
            [210, 202, 204], [113, 225, 46], [202, 43, 204], [76, 77, 62], [137, 123, 116], [72, 41, 38],
            [129, 203, 142], [64, 240, 98], [64, 49, 102], [73, 41, 74], [216, 212, 207], [184, 42, 74],
            [169, 170, 211], [176, 170, 149], [105, 66, 69], [168, 122, 6], [123, 147, 187], [96, 90, 77],
            [65, 107, 55], [89, 90, 180], [120, 100, 101], [104, 105, 63], [137, 227, 93], [85, 86, 15], [129, 102, 49],
            [86, 14, 87], [8, 9, 55], [121, 100, 47], [145, 22, 23], [88, 89, 179], [122, 196, 6], [88, 96, 95],
            [136, 138, 172], [58, 172, 215], [48, 115, 219], [80, 81, 42], [3, 51, 195], [146, 43, 61], [199, 171, 175],
            [81, 82, 38], [225, 53, 46], [144, 163, 110], [65, 66, 52], [117, 228, 229], [34, 234, 127], [107, 108, 69],
            [108, 109, 151], [48, 64, 235], [78, 62, 191], [129, 209, 126], [143, 35, 111], [50, 123, 117],
            [65, 52, 222], [19, 125, 141], [65, 221, 55], [3, 197, 195], [25, 33, 7], [220, 237, 44], [139, 70, 71],
            [193, 122, 245], [33, 130, 247], [162, 21, 71], [169, 170, 150], [196, 188, 174], [216, 186, 92],
            [97, 2, 167], [241, 125, 141], [164, 37, 167], [72, 12, 38], [82, 13, 38], [68, 71, 63], [226, 35, 111],
            [205, 50, 101], [92, 165, 206], [209, 217, 198], [97, 165, 167], [218, 115, 220], [112, 243, 133],
            [241, 238, 239], [169, 214, 135], [173, 190, 133], [208, 32, 171], [237, 44, 125], [178, 86, 87],
            [179, 85, 86], [180, 84, 85], [83, 84, 181], [201, 83, 182], [137, 132, 93], [76, 62, 183], [184, 76, 61],
            [57, 185, 61], [57, 186, 212], [187, 214, 207], [34, 156, 143], [239, 237, 79], [177, 137, 123], [1, 44, 4],
            [32, 201, 194], [64, 129, 102], [138, 213, 215], [59, 166, 219], [97, 242, 99], [2, 141, 94], [59, 75, 235],
            [24, 228, 110], [25, 130, 226], [24, 229, 23], [230, 22, 23], [26, 22, 231], [112, 232, 26],
            [243, 189, 190], [56, 221, 190], [56, 28, 221], [27, 28, 222], [27, 29, 223], [224, 29, 30], [225, 30, 247],
            [20, 238, 79], [75, 59, 166], [240, 75, 60], [177, 147, 215], [20, 166, 79], [187, 147, 213],
            [112, 233, 244], [128, 233, 245], [128, 114, 188], [217, 114, 174], [115, 131, 220], [217, 236, 198],
            [134, 131, 198], [177, 58, 132], [35, 124, 143], [163, 110, 7], [25, 228, 110], [368, 356, 389],
            [267, 11, 302], [452, 349, 350], [269, 302, 303], [277, 357, 343], [357, 452, 453], [297, 332, 333],
            [152, 377, 175], [330, 347, 348], [304, 270, 303], [336, 9, 337], [360, 278, 279], [418, 262, 431],
            [304, 409, 408], [407, 310, 415], [409, 410, 270], [450, 347, 348], [434, 430, 422], [313, 314, 17],
            [306, 307, 375], [387, 388, 260], [398, 414, 286], [418, 406, 335], [416, 364, 367], [327, 358, 423],
            [298, 251, 284], [281, 4, 5], [253, 373, 374], [320, 321, 307], [425, 427, 411], [313, 18, 421],
            [321, 405, 406], [320, 404, 405], [16, 17, 315], [425, 426, 266], [400, 377, 369], [322, 269, 391],
            [464, 417, 465], [257, 386, 258], [388, 466, 260], [456, 419, 399], [284, 333, 332], [8, 417, 285],
            [346, 340, 261], [441, 285, 413], [328, 460, 327], [371, 329, 355], [392, 438, 439], [256, 341, 382],
            [360, 420, 429], [394, 379, 364], [437, 277, 343], [283, 443, 444], [440, 363, 275], [369, 262, 431],
            [337, 297, 338], [321, 273, 375], [450, 451, 349], [342, 467, 446], [282, 293, 334], [458, 461, 462],
            [353, 276, 383], [308, 325, 324], [276, 293, 300], [345, 372, 447], [352, 345, 340], [1, 274, 19],
            [456, 248, 281], [425, 427, 436], [256, 252, 381], [393, 269, 391], [200, 428, 199], [329, 266, 330],
            [273, 422, 287], [328, 250, 462], [384, 258, 286], [265, 353, 342], [259, 257, 387], [424, 430, 431],
            [353, 276, 342], [424, 273, 335], [307, 292, 325], [345, 366, 447], [303, 302, 271], [266, 371, 423],
            [460, 294, 455], [294, 278, 279], [272, 304, 271], [432, 434, 427], [272, 408, 407], [394, 430, 431],
            [400, 369, 395], [299, 333, 334], [168, 417, 351], [352, 280, 411], [320, 325, 319], [296, 336, 295],
            [403, 404, 319], [330, 348, 349], [298, 333, 293], [323, 454, 447], [16, 315, 15], [429, 358, 279],
            [316, 14, 15], [336, 9, 285], [329, 349, 350], [380, 252, 374], [402, 403, 318], [419, 197, 6],
            [325, 318, 319], [364, 365, 367], [435, 397, 367], [344, 438, 439], [272, 311, 271], [281, 195, 5],
            [273, 291, 287], [428, 396, 199], [271, 268, 311], [283, 444, 445], [339, 373, 254], [296, 282, 334],
            [449, 346, 347], [264, 454, 447], [336, 296, 299], [338, 10, 151], [455, 278, 439], [415, 292, 407],
            [355, 371, 358], [372, 345, 340], [280, 346, 347], [282, 442, 443], [370, 19, 94], [441, 442, 295],
            [248, 419, 197], [255, 359, 263], [440, 274, 275], [368, 300, 383], [465, 412, 351], [466, 467, 263],
            [368, 301, 389], [379, 378, 395], [419, 412, 351], [426, 436, 322], [393, 2, 164], [370, 461, 462],
            [0, 267, 164], [11, 12, 302], [13, 268, 12], [301, 300, 293], [340, 261, 446], [425, 330, 266],
            [391, 426, 423], [355, 429, 437], [326, 327, 391], [440, 457, 438], [362, 341, 382], [457, 459, 461],
            [434, 430, 394], [362, 414, 463], [369, 396, 262], [457, 354, 461], [402, 403, 316], [315, 404, 403],
            [314, 404, 405], [313, 405, 406], [418, 421, 406], [401, 366, 361], [408, 306, 407], [408, 409, 291],
            [409, 410, 287], [432, 410, 436], [416, 434, 411], [264, 368, 383], [457, 309, 438], [352, 401, 376],
            [274, 275, 4], [428, 421, 262], [358, 294, 327], [416, 433, 367], [289, 439, 455], [326, 370, 462],
            [2, 326, 370], [305, 460, 455], [448, 449, 254], [261, 446, 255], [449, 450, 253], [450, 451, 252],
            [256, 451, 452], [453, 452, 341], [464, 413, 463], [441, 413, 414], [442, 441, 258], [257, 442, 443],
            [259, 444, 443], [444, 260, 445], [467, 445, 342], [250, 458, 459], [392, 289, 290], [328, 290, 460],
            [376, 433, 435], [392, 250, 290], [416, 433, 411], [464, 341, 463], [464, 465, 453], [465, 412, 357],
            [399, 412, 343], [360, 363, 440], [456, 437, 399], [456, 363, 420], [288, 401, 435], [353, 372, 383],
            [249, 339, 255], [448, 261, 255], [243, 133, 190], [112, 155, 133], [33, 246, 247], [33, 130, 25],
            [384, 398, 286], [362, 414, 398], [362, 341, 463], [467, 359, 263], [249, 255, 263], [466, 467, 260],
            [75, 60, 166], [79, 238, 239], [162, 139, 127], [72, 11, 37], [232, 121, 120], [72, 73, 39], [128, 114, 47],
            [232, 233, 128], [104, 67, 103], [152, 148, 175], [101, 118, 119], [40, 73, 74], [9, 107, 108],
            [48, 49, 131], [32, 194, 211], [184, 185, 74], [80, 183, 191], [40, 185, 186], [118, 230, 119],
            [202, 210, 214], [17, 83, 84], [146, 76, 77], [160, 161, 30], [56, 173, 190], [194, 106, 182],
            [192, 138, 135], [129, 98, 203], [68, 21, 54], [51, 4, 5], [144, 145, 23], [90, 91, 77], [187, 205, 207],
            [201, 18, 83], [91, 181, 182], [90, 180, 181], [16, 17, 85], [36, 205, 206], [176, 140, 148], [92, 165, 39],
            [193, 244, 245], [27, 28, 159], [161, 30, 247], [196, 236, 174], [104, 54, 103], [8, 193, 55],
            [31, 117, 111], [55, 221, 189], [240, 98, 99], [126, 100, 142], [218, 219, 166], [112, 26, 155],
            [209, 131, 198], [169, 150, 135], [217, 114, 47], [224, 53, 223], [220, 45, 134], [32, 211, 140],
            [67, 108, 109], [91, 146, 43], [120, 230, 231], [113, 226, 247], [105, 52, 63], [241, 242, 238],
            [156, 124, 46], [96, 78, 95], [46, 70, 63], [227, 116, 143], [123, 116, 111], [1, 19, 44], [51, 3, 236],
            [216, 205, 207], [26, 22, 154], [167, 165, 39], [200, 208, 199], [100, 36, 101], [57, 202, 43],
            [242, 99, 20], [56, 28, 157], [113, 35, 124], [160, 27, 29], [210, 211, 204], [113, 124, 46],
            [106, 43, 204], [96, 77, 62], [137, 227, 116], [72, 73, 41], [203, 36, 142], [64, 240, 235], [48, 49, 64],
            [41, 42, 74], [212, 214, 207], [184, 42, 183], [169, 210, 211], [176, 170, 140], [104, 105, 69],
            [168, 193, 122], [50, 123, 187], [96, 89, 90], [65, 66, 107], [89, 179, 180], [120, 101, 119],
            [104, 68, 63], [234, 227, 93], [16, 85, 15], [209, 129, 49], [86, 14, 15], [9, 107, 55], [120, 121, 100],
            [153, 145, 22], [88, 178, 179], [196, 197, 6], [88, 89, 96], [136, 138, 135], [138, 172, 215],
            [218, 115, 219], [81, 41, 42], [51, 195, 5], [57, 43, 61], [208, 171, 199], [81, 41, 38], [224, 225, 53],
            [24, 144, 110], [105, 66, 52], [117, 229, 118], [234, 34, 227], [66, 107, 69], [10, 109, 151],
            [48, 219, 235], [191, 62, 183], [129, 126, 142], [143, 116, 111], [50, 117, 118], [52, 222, 223],
            [19, 141, 94], [65, 221, 222], [3, 196, 197], [220, 45, 44], [139, 156, 70], [122, 188, 245],
            [162, 139, 71], [170, 149, 150], [122, 196, 188], [216, 92, 206], [2, 164, 167], [241, 242, 141],
            [0, 164, 37], [72, 11, 12], [12, 13, 38], [71, 70, 63], [226, 111, 31], [205, 36, 101], [203, 165, 206],
            [209, 217, 126], [97, 98, 165], [218, 220, 237], [241, 237, 239], [169, 210, 214], [32, 171, 140],
            [241, 125, 237], [178, 179, 86], [179, 180, 85], [180, 84, 181], [83, 181, 182], [201, 194, 182],
            [177, 137, 132], [184, 76, 183], [184, 185, 61], [57, 186, 185], [216, 186, 212], [192, 187, 214],
            [34, 139, 156], [218, 237, 79], [123, 177, 147], [4, 44, 45], [208, 201, 32], [64, 129, 98],
            [192, 138, 213], [59, 235, 219], [97, 242, 141], [97, 2, 141], [240, 75, 235], [24, 228, 229],
            [25, 226, 31], [229, 230, 23], [230, 22, 231], [232, 26, 231], [112, 233, 232], [243, 244, 189],
            [221, 189, 190], [28, 221, 222], [27, 222, 223], [224, 29, 223], [224, 225, 30], [113, 225, 247],
            [240, 99, 60], [147, 213, 215], [60, 20, 166], [192, 187, 213], [112, 243, 244], [233, 244, 245],
            [128, 188, 245], [114, 188, 174], [131, 220, 134], [217, 236, 174], [134, 236, 198], [177, 58, 215],
            [124, 156, 143], [25, 110, 7], [25, 228, 31], [264, 356, 368], [0, 267, 11], [451, 452, 349],
            [267, 269, 302], [277, 357, 350], [452, 357, 350], [297, 299, 333], [377, 396, 175], [280, 330, 347],
            [269, 270, 303], [337, 9, 151], [344, 360, 278], [424, 418, 431], [304, 409, 270], [272, 310, 407],
            [322, 270, 410], [449, 450, 347], [432, 434, 422], [313, 18, 17], [306, 291, 375], [259, 387, 260],
            [424, 418, 335], [416, 434, 364], [423, 327, 391], [298, 251, 301], [281, 275, 4], [253, 373, 254],
            [321, 307, 375], [280, 425, 411], [200, 18, 421], [321, 406, 335], [320, 321, 405], [17, 314, 315],
            [426, 266, 423], [377, 396, 369], [322, 269, 270], [464, 417, 413], [385, 386, 258], [248, 419, 456],
            [298, 284, 333], [168, 417, 8], [448, 346, 261], [417, 285, 413], [328, 326, 327], [329, 355, 277],
            [392, 309, 438], [256, 381, 382], [360, 429, 279], [379, 364, 365], [355, 277, 437], [283, 282, 443],
            [363, 281, 275], [369, 395, 431], [337, 297, 299], [321, 273, 335], [450, 348, 349], [467, 446, 359],
            [282, 283, 293], [458, 250, 462], [300, 276, 383], [292, 325, 308], [283, 276, 293], [264, 372, 447],
            [352, 346, 340], [19, 354, 274], [456, 281, 363], [425, 426, 436], [252, 380, 381], [393, 267, 269],
            [200, 428, 421], [329, 266, 371], [432, 422, 287], [328, 290, 250], [384, 385, 258], [265, 446, 342],
            [257, 386, 387], [424, 430, 422], [276, 445, 342], [424, 273, 422], [306, 307, 292], [352, 345, 366],
            [268, 302, 271], [371, 358, 423], [460, 294, 327], [331, 294, 279], [304, 271, 303], [432, 427, 436],
            [304, 272, 408], [394, 395, 431], [400, 378, 395], [296, 299, 334], [168, 6, 351], [376, 411, 352],
            [320, 307, 325], [336, 285, 295], [320, 404, 319], [329, 330, 349], [333, 293, 334], [323, 366, 447],
            [315, 316, 15], [331, 358, 279], [316, 317, 14], [8, 9, 285], [329, 277, 350], [252, 253, 374],
            [403, 318, 319], [419, 6, 351], [324, 325, 318], [365, 397, 367], [288, 435, 397], [344, 278, 439],
            [272, 310, 311], [248, 281, 195], [273, 291, 375], [199, 396, 175], [312, 268, 311], [283, 276, 445],
            [339, 373, 390], [296, 282, 295], [448, 449, 346], [264, 356, 454], [336, 337, 299], [337, 338, 151],
            [455, 294, 278], [308, 292, 415], [355, 429, 358], [372, 265, 340], [352, 280, 346], [442, 282, 295],
            [354, 19, 370], [441, 285, 295], [248, 195, 197], [440, 457, 274], [368, 300, 301], [417, 465, 351],
            [251, 301, 389], [379, 394, 395], [419, 412, 399], [410, 436, 322], [393, 2, 326], [354, 461, 370],
            [393, 267, 164], [268, 12, 302], [312, 268, 13], [298, 301, 293], [265, 340, 446], [280, 425, 330],
            [426, 322, 391], [420, 429, 437], [393, 326, 391], [344, 438, 440], [458, 459, 461], [434, 364, 394],
            [396, 428, 262], [457, 274, 354], [402, 316, 317], [315, 316, 403], [314, 315, 404], [313, 314, 405],
            [313, 421, 406], [361, 323, 366], [306, 292, 407], [408, 306, 291], [409, 291, 287], [432, 410, 287],
            [434, 427, 411], [264, 372, 383], [457, 459, 309], [352, 401, 366], [1, 274, 4], [418, 421, 262],
            [358, 331, 294], [433, 435, 367], [392, 289, 439], [328, 326, 462], [2, 94, 370], [289, 455, 305],
            [448, 339, 254], [255, 446, 359], [449, 253, 254], [450, 252, 253], [256, 451, 252], [256, 452, 341],
            [413, 414, 463], [441, 414, 286], [441, 258, 286], [442, 257, 258], [257, 259, 443], [444, 259, 260],
            [467, 260, 445], [250, 459, 309], [305, 290, 289], [305, 290, 460], [376, 401, 435], [392, 250, 309],
            [376, 433, 411], [464, 341, 453], [453, 465, 357], [412, 357, 343], [399, 437, 343], [344, 360, 440],
            [456, 420, 437], [360, 363, 420], [288, 361, 401], [265, 372, 353], [249, 339, 390], [448, 339, 255]]


def run():
    xyz = get_face_mesh()
    triangles = get_triangles()
    pcd = o3d.geometry.TriangleMesh()
    pcd.vertices = o3d.utility.Vector3dVector(xyz)
    pcd.compute_vertex_normals()
    pcd.triangles = o3d.utility.Vector3iVector(np.array(triangles))
    o3d.visualization.draw_geometries([pcd])


if __name__ == '__main__':
    run()
