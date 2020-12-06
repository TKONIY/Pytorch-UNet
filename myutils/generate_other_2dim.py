"""
    从imgs中生成其他两个角度看到的数据
"""

import numpy as np
import os
import cv2
data_dir = os.environ["HOME"] + "/code/Pytorch-UNet/data"
dim1_dir = data_dir + '/imgs'
dim2_dir = data_dir + '/imgs_dim2'
dim3_dir = data_dir + '/imgs_dim3'
dim1_fname_l = os.listdir(dim1_dir)
dim1_fname_l.sort()

"""
生成一个大v
"""
img = cv2.imread(dim1_dir + '/' + dim1_fname_l[0])
v_dim1_shape = (len(dim1_fname_l), img.shape[0], img.shape[1])  # 计算整个立方体的shape
v_dim1 = np.zeros(v_dim1_shape)  # 预先分配立方体
print("dim1 shape:" + str(v_dim1.shape))
for i, fname in enumerate(dim1_fname_l):
    img = cv2.imread(dim1_dir + '/' + fname)[:, :, 0]
    v_dim1[i] = img
    print("read {}".format(i))

v_dim2 = np.transpose(v_dim1, (2, 1, 0))
print("dim2 shape:" + str(v_dim2.shape))

v_dim3 = np.transpose(v_dim1, (1, 0, 2))
print("dim3 shape:" + str(v_dim3.shape))

# 存储v_dim2
for i in range(v_dim2.shape[0]):
    p = dim2_dir + '/' + str(i) + '.png'
    cv2.imwrite(p, v_dim2[i, :, :])
    print(p)

for i in range(v_dim3.shape[0]):
    p = dim3_dir + '/' + str(i) + '.png'
    cv2.imwrite(p, v_dim3[i, :, :])
    print(p)

"""
将大vtranspose
"""
