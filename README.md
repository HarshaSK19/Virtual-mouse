# 🖱️ Gesture Controlled Virtual Mouse

A real-time gesture-controlled virtual mouse system that allows users to interact with a computer using hand gestures instead of a traditional physical mouse.

## 📌 About the Project

This project uses a standard webcam to detect and track hand movements in real time. Hand gestures are recognized and mapped to different mouse operations, providing a convenient and contactless method of computer interaction.

The system is developed using Python, OpenCV, MediaPipe, and PyAutoGUI. MediaPipe is used for hand landmark detection, OpenCV handles real-time camera input and image processing, and PyAutoGUI and Pynput perform system-level mouse actions.

## ✨ Features

- 🖐️ Real-time hand detection and tracking
- 🖱️ Cursor movement using finger gestures
- 👆 Left click
- 👉 Right click
- ✌️ Double click
- 📜 Scrolling
- 🖱️ Dragging
- 📸 Screenshot capture
- 🎥 Webcam-based interaction
- 💻 Contactless computer control

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- Pynput
- Visual Studio Code

## ⚙️ How It Works

1. The webcam captures the user's hand movements.
2. OpenCV processes the camera frames.
3. MediaPipe detects the hand and identifies its landmarks.
4. Finger positions and gestures are analyzed.
5. Recognized gestures are mapped to mouse operations.
6. PyAutoGUI/Pynput sends the corresponding commands to the operating system.

## 📋 Requirements

- Python 3.x
- Webcam
- Windows/Linux/macOS computer
- Required Python libraries

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/HarshaSK19/Virtual-mouse.git
