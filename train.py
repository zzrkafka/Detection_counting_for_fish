from ultralytics import YOLO

# 加载模型
# model = YOLO("yolov8n.yaml")  # 从头开始构建新模型
model = YOLO("weights/yolov8n.pt")  # 加载预训练模型（推荐用于训练）

# Use the model
if __name__ == '__main__':
    results = model.train(data="fish.yaml", epochs=20, batch=2)  # 训练模型
