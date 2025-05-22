import cv2
import os.path
import random

# 检查已有图片的数量，确定本次图片抽取开始的下标
cnt = len(os.listdir('E:/design/dataSet/img')) + 1
# 视频存放路径
videoDir = os.listdir('E:/design/dataSet/video')
# 提示使用者抽取开始
print("Start!")
# 每30帧随机抽取一帧
start, ran = 0, random.randrange(0, 96)
try:
    temp = 0
    for video in videoDir:
        # 拼接视频路径
        videoPath = r'E:/design/dataSet/video/' + video

        # 打开视频流
        vc = cv2.VideoCapture(videoPath)
        # 判断是否打开成功
        if vc.isOpened():
            while True:
                # activity: 读取成功标签，frame: 读取的画面
                activity, frame = vc.read()
                # 如果读取不成功（没有下一帧），就退出
                if not activity:
                    break
                if temp == start + ran:
                    cv2.imwrite(f"E:/design/dataSet/img/{cnt}.jpg", frame)
                    cnt, start, ran = cnt + 1, start + 96, random.randrange(0, 96)
                temp = temp + 1
    vc.release()
    # 提示抽取完成
    print("Finish!")
except:
    vc.release()
    # 提示抽取出现错误
    print("Error!")