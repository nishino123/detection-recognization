# -*- coding: UTF-8 -*-
#@Time : 2020/3/23 @Author : SUNLIN

from src import detect_faces, show_bboxes
from PIL import Image

def face_detect(filename,save_file_name):
    img = Image.open(filename)
    print(img)
    bounding_boxes, landmarks = detect_faces(img)
    img_copy=show_bboxes(img, bounding_boxes, landmarks)
    img_copy.save(save_file_name)
    return img_copy

if __name__=='__main__':
    face_detect('images/office1.jpg','images/office1_copy.jpg')
