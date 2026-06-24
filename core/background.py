import cv2
import numpy as np


class BackgroundModel:
    def __init__(self):
        self.background = None

    def capture(self, cap, frames_count=120):
        frames = []

        for i in range(frames_count):
            ret, frame = cap.read()

            if not ret:
                print("Frame read failed")
                continue

            frame = cv2.flip(frame, 1)
            frames.append(frame)

            cv2.putText(
                frame,
                f"Capturing background {i+1}/{frames_count}",
                (30, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

            cv2.imshow("RealityFrame", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        print("Frames captured:", len(frames))

        if len(frames) == 0:
            print("No frames captured!")
            return

        self.background = np.median(frames, axis=0).astype(np.uint8)

        print("Background captured successfully")

    def get(self):
        return self.background