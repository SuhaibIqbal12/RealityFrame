# Vision-Reality – AI-Powered Augmented Reality & Invisibility System

Vision Reality is an advanced real-time Computer Vision and Augmented Reality platform built using Python, OpenCV, MediaPipe, and YOLOv8. The system combines gesture recognition, AI-powered object detection, background reconstruction, selective invisibility, and AR overlays into a single interactive experience.

The project demonstrates the integration of multiple AI and Computer Vision technologies working together in real time on live webcam feeds.

---

## Key Features

### AI Object Detection

* Real-time object detection using YOLOv8
* GPU-accelerated inference
* Object confidence visualization
* Multiple object tracking and recognition

### Smart Invisibility System

* Full-body invisibility mode using AI segmentation
* Portal-based selective invisibility
* Dynamic background reconstruction
* Adaptive lighting correction for realistic blending

### Gesture-Based Control

* Hand tracking using MediaPipe
* Pinch gesture mode switching
* Touchless interaction system
* Real-time gesture recognition

### Augmented Reality Engine

* Marker-based AR tracking
* Dynamic AR overlays
* Perspective-correct rendering
* Real-time target locking

### Performance Monitoring

* Live FPS monitoring
* GPU status monitoring
* Optimized detection pipeline
* Reduced-latency object detection

### Interactive Focus Mode

* Custom focus area selection
* Mouse-driven region targeting
* Background isolation effects

---

## Technologies Used

* Python
* OpenCV
* MediaPipe
* YOLOv8
* PyTorch
* NumPy
* Computer Vision
* Augmented Reality
* Real-Time Image Processing
* GPU Acceleration (CUDA)

---

## System Architecture

RealityFrame/
│
├── ar/
│   ├── ar_renderer.py
│   ├── overlay_factory.py
│   └── target_tracker.py
│
├── core/
│   └── background.py
│
├── graphics/
│   └── renderer.py
│
├── vision/
│   ├── gesture.py
│   ├── hand_tracker.py
│   ├── portal_detector.py
│   └── yolo_detector.py
│
├── assets/
│
├── tools/
│
├── main.py
└── requirements.txt

---

## Controls

| Key | Function                 |
| --- | ------------------------ |
| Q   | Quit Application         |
| B   | Rebuild Background Model |
| F   | Toggle Focus Mode        |
| R   | Reset Focus Area         |
| A   | Toggle AR Mode           |
| V   | Toggle AR Tracking Frame |

---

## Real-World Applications

### Smart Privacy Systems

Hide sensitive areas during video calls while maintaining a natural appearance.

### AI Surveillance & Monitoring

Detect and track objects in real time using deep learning.

### Interactive AR Experiences

Create immersive augmented reality interactions using marker tracking.

### Content Creation

Generate visual effects and selective invisibility without requiring a green screen.

### Educational Computer Vision Platform

Demonstrates practical applications of:

* Deep Learning
* Object Detection
* Gesture Recognition
* Image Segmentation
* Augmented Reality
* Human-Computer Interaction

---

## Performance Enhancements

* YOLOv8 GPU acceleration
* Real-time FPS monitoring
* Optimized detection scheduling
* Low-latency rendering pipeline
* Adaptive background reconstruction

---

## Installation

git clone https://github.com/SuhaibIqbal12/RealityFrame.git

cd RealityFrame

pip install -r requirements.txt

---

## Run

python main.py

---

## Future Roadmap

* Voice-controlled commands
* Custom-trained object detection models
* Multi-person tracking
* Face recognition integration
* AI scene understanding
* Spatial AR object placement
* Gesture-controlled UI system

---

## Author

Mohammed Suhaib Iqbal

B.Tech CSE (AI & ML)

Computer Vision • Artificial Intelligence • Augmented Reality • Deep Learning
