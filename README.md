# 🔊 Audio Control Using Hand Gestures

## Project Overview

Audio Control Using Hand Gestures is a real-time computer vision application that allows users to control their system volume using hand movements detected through a webcam. The system tracks hand landmarks and measures the distance between the thumb and index finger to adjust the audio volume without requiring any physical interaction.

Built using Python, OpenCV, MediaPipe, and Pycaw, this project demonstrates the practical implementation of gesture recognition and human-computer interaction technologies to create a touchless and intuitive audio control experience.

---

## Features

* Real-Time Hand Detection
* Gesture-Based Volume Control
* Live Webcam Tracking
* Finger Landmark Detection
* Smooth Volume Adjustment
* Contactless User Interaction
* Fast and Lightweight Performance
* Real-Time Visual Feedback
* AI-Based Hand Tracking
* Touch-Free Audio Management

---

## Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy
* Pycaw
* comtypes

---

## Project Structure

Audio-Control-Using-Hand-Gestures/

├── main.py

├── hand_tracker.py

├── gesture_control.py

├── volume_controller.py

├── requirements.txt

├── .gitignore

└── README.md

---

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/audio-control-using-hand-gestures.git

cd audio-control-using-hand-gestures
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python main.py
```

### 6. Allow Webcam Access

The application will automatically access your webcam and begin tracking hand movements.

---

## System Workflow

### Hand Detection

* Capture live webcam feed.
* Detect hand landmarks using MediaPipe.
* Track thumb and index finger positions.
* Process hand movement in real time.

### Gesture Recognition

* Calculate the distance between fingertips.
* Convert distance into volume values.
* Detect volume increase and decrease gestures.
* Provide instant visual feedback.

### Audio Control

* Increase system volume with wider finger spacing.
* Decrease system volume with closer finger spacing.
* Update system audio levels in real time.
* Enable touchless media interaction.

---

## Core Modules

### Hand Tracking Module

* Webcam Access
* Hand Detection
* Landmark Tracking
* Motion Analysis

### Gesture Recognition Module

* Finger Distance Calculation
* Gesture Detection
* Real-Time Processing
* Gesture Mapping

### Audio Control Module

* System Volume Access
* Volume Adjustment
* Audio Synchronization
* Real-Time Control

### User Interface Module

* Webcam Display
* Visual Indicators
* Gesture Feedback
* Performance Monitoring

---

## Requirements

```text
OpenCV-Python
MediaPipe
NumPy
Pycaw
comtypes
```

Install all requirements using:

```bash
pip install -r requirements.txt
```

---

## Future Enhancements

* Brightness Control Using Gestures
* Media Player Control
* Multi-Hand Gesture Support
* Custom Gesture Configuration
* Voice Command Integration
* Cross-Platform Compatibility
* Desktop GUI Application
* Smart Home Device Control

---

## Author

Developed by: Barnali Bhowmik

---

## License

This project is created for educational and learning purposes. Feel free to modify and improve it as needed.

⭐ If you find this project useful, please give it a star.
