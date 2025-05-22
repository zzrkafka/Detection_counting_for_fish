from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # 加载预训练的 YOLOv8n 模型

# model.train(data='coco128.yaml') # 训练模型
# model.val() # 在验证集模型上评估模型性能
# result = model.predict(source='2.mp4', save=True)  # 对图像进行预测
# model.export(format='onnx') # 将模型导出为 ONNX 格式
