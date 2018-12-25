#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 17:51:14 2018

@author: jane
"""

import cv2
import numpy as np

#加载使用opencv自带的分类器XML，关于瞳孔的
cascade=cv2.CascadeClassifier("F:\comp\opencv-3.4.2\data\haarcascades\haarcascade_eye_tree_eyeglasses.xml")
#打开摄像头获取视频，对应编号为0是第一个摄像头，如果还有别的就1，2，3……
cap=cv2.VideoCapture(0)

while(1):
    ret,frame=cap.read()
#get frame
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#检测视频中的瞳孔，用eyes保存坐标，大小等，用矩形
    eyes=cascade.detectMultiScale(gray,1.3,5)   
#瞳孔识别
    for (x,y,w,h) in eyes:
        x=int(x+w*0.5)
        y=int(y+h*0.5)
        cv2.circle(frame,(x,y),2,(0,0,255),-1)
    #每一帧延时1ms
    k=cv2.waitKey(1) & 0xFF
    if k==ord('q') or ret==False:
        break
    #显示格式为窗口，标题为test
    #？？？？？？？？？？？？？？？？？？？？？？
    #最大疑点：怎么让显示的东西显示到vr里？
    # 将这个值置为空的变量，通过unity的C#脚本调用该文件，在unity窗口中对此进行一个指定，然后串接到python这里的对应变量中进行显示
    #对于vr环境已经在运行来说，python中的frame视图窗口到底还是电脑显示的还是说是vr中的内容
    cv2.imshow(" test",frame)
cap.release()
cv2.destroyAllWindows()