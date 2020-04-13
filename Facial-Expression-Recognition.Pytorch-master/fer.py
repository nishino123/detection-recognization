''' Fer2013 Dataset class'''

from __future__ import print_function
from PIL import Image
import numpy as np
import h5py
import torch.utils.data as data
import pickle
class FER2013(data.Dataset):
    """`FER2013 Dataset.

    Args:
        train (bool, optional): If True, creates dataset from training set, otherwise
            creates from test set.
        transform (callable, optional): A function/transform that  takes in an PIL image
            and returns a transformed version. E.g, ``transforms.RandomCrop``
    """

    def __init__(self, split='Training', transform=None):
        self.transform = transform
        self.split = split  # training set or test set
        # self.data = h5py.File('./data/data.h5', 'r', driver='core')
        train_fr=open('data/train.txt','rb')
        public_fr=open('data/public_test.txt','rb')
        private_fr=open('data/private.txt','rb')

        # now load the picked numpy arrays
        if self.split == 'Training':
            self.train_data = pickle.load(train_fr)
            self.train_labels = pickle.load(train_fr)
            self.train_data = np.asarray(self.train_data)
            self.train_data = self.train_data.reshape((28709, 48, 48))
            train_fr.close()

        elif self.split == 'PublicTest':
            self.PublicTest_data = pickle.load(public_fr)
            self.PublicTest_labels = pickle.load(public_fr)
            self.PublicTest_data = np.asarray(self.PublicTest_data)
            self.PublicTest_data = self.PublicTest_data.reshape((3589, 48, 48))
            public_fr.close()
        else:
            self.PrivateTest_data = pickle.load(private_fr)
            self.PrivateTest_labels = pickle.load(private_fr)
            self.PrivateTest_data = np.asarray(self.PrivateTest_data)
            self.PrivateTest_data = self.PrivateTest_data.reshape((3589, 48, 48))
            private_fr.close()
    def __getitem__(self, index):
        """
        Args:
            index (int): Index

        Returns:
            tuple: (image, target) where target is index of the target class.
        """
        if self.split == 'Training':
            img, target = self.train_data[index], self.train_labels[index]
        elif self.split == 'PublicTest':
            img, target = self.PublicTest_data[index], self.PublicTest_labels[index]
        else:
            img, target = self.PrivateTest_data[index], self.PrivateTest_labels[index]

        # doing this so that it is consistent with all other datasets
        # to return a PIL Image
        img = img[:, :, np.newaxis]
        img = np.concatenate((img, img, img), axis=2) #(48,48,3)
        img = Image.fromarray(np.uint8(img))   #转化成PIL文件了 np.uint8(0-255)
        if self.transform is not None:
            img = self.transform(img)
        return img, target

    def __len__(self):
        if self.split == 'Training':
            return len(self.train_data)
        elif self.split == 'PublicTest':
            return len(self.PublicTest_data)
        else:
            return len(self.PrivateTest_data)

import torchvision.transforms as transforms
# # 定义对数据的预处理
transform_train = transforms.Compose([
    transforms.RandomCrop(44), #依据给定的size随机裁剪
    transforms.RandomHorizontalFlip(), #依据概率p对PIL图片进行水平翻转,默认是0.5
    transforms.ToTensor(), #array -> Tensor
])
import cv2
import torch
if __name__ == '__main__':
    trainset = FER2013(split='Training', transform=transform_train)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=128, shuffle=True, num_workers=1)

    for i,(batch_x,batch_y) in enumerate(trainloader):
        print(batch_x.numpy().shape)  #(128,3,44,44)
        print(batch_y.numpy().shape)  #(128,)
        break
