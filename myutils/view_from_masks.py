"""
    对所有mask文件夹下的图片, 生成方便肉眼观察的mask图片到maskview文件夹下
"""

import cv2
import os
d = "/home/dengyangshen/code/Pytorch-UNet/data/"
l = os.listdir(d+'masks')
l.sort()
for fname in l[1:]:
    tmp = cv2.imread(d+'masks/'+fname)*255
    cv2.imwrite(d+'maskview/'+fname, tmp)
    print(1)