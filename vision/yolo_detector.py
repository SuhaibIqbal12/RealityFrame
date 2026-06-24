from ultralytics import YOLO


class YOLODetector:
    def __init__(self):
        print("Loading YOLO...")
        self.model = YOLO("yolov8m.pt")
        self.model.to("cuda")
        print("YOLO Loaded!")

    def detect(self, frame):
        results = self.model(frame, verbose=False)

        detections = []

        for result in results:
            for box in result.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = self.model.names[cls]

                detections.append({
                    "label": label,
                    "conf": conf,
                    "bbox": (x1, y1, x2, y2)
                })

        return detections