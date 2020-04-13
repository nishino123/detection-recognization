from PyQt5 import QtWidgets
from home import Ui_Form as HUi_Form
from detect import Ui_Form as DUi_Form
from emotion_recoginize import Ui_Form as EUi_Form

from PyQt5 import QtWidgets,QtGui,QtCore
from detect import Ui_Form
from PyQt5.QtWidgets import QFileDialog
from PIL import Image

import cv2

import sys
sys.path.append('../mtcnn-pytorch-master')
from test_on_image import face_detect

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MyWindow(QtWidgets.QWidget,HUi_Form):
   def __init__(self):
       super(MyWindow,self).__init__()
       self.setupUi(self) #实例化主窗口
       self.child=My_DUi_Form(self) #实例化子窗口
       self.Echild=My_EUi_Form(self)

   def detect(self):
        self.child.show()

   def emo_recoginize(self):
        self.Echild.show()

   def recoginize(self):
       import sys
       sys.path.append('../mtcnn-facenet-face_recognization/test')
       print('the path of tt is {}'.format(sys.path))
       from realtime import face_recoginize
       face_recoginize()

class My_DUi_Form(QtWidgets.QWidget,DUi_Form):
    def __init__(self,last_form):
        super(My_DUi_Form,self).__init__()
        self.setupUi(self)

    def select(self):
        self.file_name, ok = QFileDialog.getOpenFileName(self, '读取', 'face_detect_images')
        jpg = QtGui.QPixmap(self.file_name)
        graphicscene = QtWidgets.QGraphicsScene()
        graphicscene.addPixmap(jpg)
        self.graphicsView.setScene(graphicscene)
        self.graphicsView.show() #显示原图

        # print(file_name)
        # if ok:
        #     _f = open(file_name, 'r')
        #     with _f:
        #         data = _f.read()
        #         self.textBrowser.append(data)
        #     self.textBrowser.append("读取成功...")

    def detect(self): #显示检测后的图片
        print('detect')
        save_file_name='../mtcnn-pytorch-master/images/img_copy.png'
        face_detect(self.file_name,save_file_name)

        jpg = QtGui.QPixmap(save_file_name)
        graphicscene = QtWidgets.QGraphicsScene()
        graphicscene.addPixmap(jpg)
        self.graphicsView_2.setScene(graphicscene)
        self.graphicsView_2.show()

class My_EUi_Form(QtWidgets.QWidget,EUi_Form):
    def __init__(self,last_form):
        super(My_EUi_Form,self).__init__()
        self.setupUi(self)
    def select(self):
        filename, ok = QFileDialog.getOpenFileName(self, '读取', 'face_detect_images')
        self.show_raw_img(filename)

        import sys
        sys.path.append('../Facial-Expression-Recognition.Pytorch-master')
        print('the path of tt is {}'.format(sys.path))
        from predict import predict_emotion
        possibility,predict_ed=predict_emotion(filename)

        self.show_results(predict_ed, possibility)
        print('emotion:{}'.format(predict_ed))
        print('possibility: {}'.format(possibility))

    def show_results(self, predict_ed, possibility):
        class_names = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
        emotion=class_names[int(predict_ed.cpu().numpy())]

        # 显示表情名
        self.label_emotion.setText(QtCore.QCoreApplication.translate("Form", emotion))
        # 显示emoji
        if emotion != 'no':
            print('emotion: ',str(emotion))
            img = cv2.imread('images/' + str(emotion) + '.png')
            frame = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), (100, 100))
            self.label_rst.setPixmap(QtGui.QPixmap.fromImage(
                QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], 3 * frame.shape[1],
                             QtGui.QImage.Format_RGB888)))
        else:
            self.label_rst.setText(QtCore.QCoreApplication.translate("Form", "no result"))
        # 显示直方图
        possibility=list(possibility.data.cpu().numpy())
        print('possibility: ',possibility)
        self.show_bars(possibility)

    def show_bars(self, possbility):
        dr = MyFigureCanvas()
        dr.draw_(possbility)
        graphicscene = QtWidgets.QGraphicsScene()
        graphicscene.addWidget(dr)
        self.graphicsView.setScene(graphicscene)
        self.graphicsView.show()

    def show_raw_img(self, filename):
        import cv2
        img = cv2.imread(filename)
        frame = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), (320, 240))
        self.label_raw_pic.setPixmap(QtGui.QPixmap.fromImage(
                    QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], 3 * frame.shape[1],
                                 QtGui.QImage.Format_RGB888)))

class MyFigureCanvas(FigureCanvas):

    def __init__(self, parent=None, width=6, height=3, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.axes = fig.add_subplot(111)

    def draw_(self, possibility):
        import numpy as np
        import matplotlib.pyplot as plt
        x = ['anger', 'disgust', 'fear', 'happy', 'sad', 'surprised', 'neutral']

        color_list = ['red', 'orangered', 'darkorange', 'limegreen', 'darkgreen', 'royalblue', 'navy']
        self.axes.bar(x, possibility, align='center',color=color_list)


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec_())