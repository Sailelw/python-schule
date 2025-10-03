from ultralytics import YOLO

# Modell laden (Nano Version zum Starten)
model = YOLO("yolov10n.pt")

# Training starten
model.train(
    data="data.yaml",   # dein Dataset
    epochs=50,          # Anzahl Trainingsdurchläufe
    imgsz=640,          # Bildgröße
    batch=16,           # Batch-Größe
    device=0            # 0 = GPU, 'cpu' = CPU
)
