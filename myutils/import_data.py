"""
将Axial和label中的数据放到data和mask中
img中的只需要直接拷贝过来

f_img_dir:
    img1.bmp
    img2.bmp
    ...
f_label_dir:
    001:
        label1.png
        label2.png
    002:
        label1.png
        ...
    ...

t_dir:
    imgs:
        ...
    labels:
        ...
"""
import os
import cv2
import numpy as np


def import_img_label(t_dir: str, f_img_dir: str, f_label_dir: str, repair: int, f_index: int, t_index: int):
    """
        数据集import到t_dir下
        数据集的img路径
        数据集的label路径
        repair方式(img不变,label变)
        从第f_index个样本
        成为第t_index个样本
    """

    # img中的3通道裁剪成单通道
    l_from_img_dir = os.listdir(f_img_dir)
    l_from_img_dir.sort()
    l_from_label_dir = os.listdir(f_label_dir)

    # 获取img数据
    img = cv2.imread(f_img_dir + '/' + l_from_img_dir[f_index])[:, :, 0]
    # 获取label数据
    label = np.zeros(img.shape)
    for d in l_from_label_dir:
        l_from_label_fnames = os.listdir(f_label_dir + '/' + d)
        l_from_label_fnames.sort()

        if repair == 1:
            l_from_label_fnames.reverse()
        tmp = cv2.imread(f_label_dir+'/'+d+'/'+l_from_label_fnames[f_index])[:,:,0]
        if repair == 1:
            tmp = cv2.rotate(tmp, cv2.ROTATE_180)

        if tmp.shape != label.shape: 
            raise Exception("label和img的维度没有对应上")

        # 将tmp中的mask添加到label上
        label[tmp!=6] = 1

    # 计算路径
    t_img_path = t_dir + '/imgs/' + str(t_index) + ".png"
    t_label_path = t_dir + '/masks/' + str(t_index) + '.png'
    t_label_view_path = t_dir + '/maskview/' + str(t_index) + '.png'
    
    cv2.imwrite(t_img_path,img)
    cv2.imwrite(t_label_path, label)
    label = label * 255
    cv2.imwrite(t_label_view_path, label)


# 调用def
repair = 1  # rotate(180) + 逆序

# 把XSC-03A的全部导入进去
f_img_dir = os.environ["HOME"] + "/data_png/img/XSC-03A Axial"
f_label_dir = os.environ["HOME"] + "/data_png/label/XSC-03A Label"
t_dir = os.environ["HOME"] + "/code/Pytorch-UNet/data"



for i in range(1000):
    import_img_label(t_dir, f_img_dir, f_label_dir, repair, i, i)
