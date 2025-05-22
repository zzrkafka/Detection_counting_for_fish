import os
import random
import shutil

img_src = 'E:\design\data\img'
label_src = r'E:\design\CountFish\runs\detect\predict9\labels'
dataset = 'E:\design\data\dataset'


def copyData(image, des):
    label = image[:-4] + '.txt'
    image_path = img_src + '\\' + image
    label_path = label_src + '\\' + label
    image_des = dataset + '\\images\\' + des + '\\' + image
    label_des = dataset + '\\labels\\' + des + '\\' + label
    # print(image_des)
    shutil.copyfile(image_path, image_des)
    shutil.copyfile(label_path, label_des)


images = os.listdir(img_src)
for image in images:
    label = image[:-4] + '.txt'
    if random.randint(0, 4) == 0:
        # val
        copyData(image, 'val')
    else:
        copyData(image, 'train')
