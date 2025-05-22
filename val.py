from ultralytics import YOLO

# 加载模型
# model = YOLO("yolov8n.yaml")  # 从头开始构建新模型
model = YOLO("best.pt")  # 加载预训练模型（推荐用于训练）

# Use the model
if __name__ == '__main__':
    results = model.val(data="fish.yaml", save_hybrid=True)  # 训练模型
