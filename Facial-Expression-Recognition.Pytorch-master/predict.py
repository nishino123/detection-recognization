"""
visualize results for test image
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import torch
import torch.nn as nn
import torch.nn.functional as F
import os
from torch.autograd import Variable

import transforms as transforms
from skimage import io
from skimage.transform import resize
from models import *


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])

def predict_emotion(file_name):
    raw_img = io.imread(file_name)
    cut_size = 44

    transform_test = transforms.Compose([
        transforms.TenCrop(cut_size),
        transforms.Lambda(lambda crops: torch.stack([transforms.ToTensor()(crop) for crop in crops])),
    ])

    gray = rgb2gray(raw_img)
    gray = resize(gray, (48,48), mode='symmetric').astype(np.uint8)

    img = gray[:, :, np.newaxis]

    img = np.concatenate((img, img, img), axis=2)#(48,48,3)
    img = Image.fromarray(img) #转化成PIL文件
    inputs = transform_test(img) #transform

    class_names = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

    net = VGG('VGG19')#加载网络模型
    checkpoint = torch.load(os.path.join('F:/Study/First_Grade/Winter_Vacation/Real-time-face-recognition-master/Facial-Expression-Recognition.Pytorch-master/FER2013_VGG19', 'PrivateTest_model.t7'),map_location='cpu')
    net.load_state_dict(checkpoint['net'])
    # net.cuda()
    net.eval()

    ncrops, c, h, w = np.shape(inputs)

    inputs = inputs.view(-1, c, h, w)
    # inputs = inputs.cuda()
    inputs = Variable(inputs, volatile=True)
    outputs = net(inputs)

    outputs_avg = outputs.view(ncrops, -1).mean(0)  # avg over crops
    #使用数据增强后的结果测试效果会更强
    score = F.softmax(outputs_avg)
    # print(type(score)) #tensor
    _, predicted = torch.max(score.data, 0)

    return score,predicted

if __name__=='__main__':
        print(predict_emotion('images/1.jpg'))