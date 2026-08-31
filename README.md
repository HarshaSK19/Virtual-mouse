# 🖱️ Gesture Controlled Virtual Mouse

A real-time computer vision project that allows users to control the mouse using hand gestures through a webcam.

The system uses **MediaPipe** for hand landmark detection, **OpenCV** for real-time video processing, and **PyAutoGUI/Pynput** for system-level mouse control.

---

## 🚀 Features

- 🖐️ Real-time hand detection and tracking
- 🖱️ Gesture-based cursor movement
- 👆 Left click
- 👉 Right click
- ✌️ Double click
- 📜 Scroll control
- 🤏 Drag and drop
- 📸 Screenshot capture
- 🎥 Webcam-based interaction
- 💻 Contactless computer control
- ⚡ Responsive cursor movement

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 👁️ OpenCV | Webcam input and image processing |
| ✋ MediaPipe | Hand landmark detection |
| 🖱️ PyAutoGUI | Cursor and screenshot automation |
| 🖱️ Pynput | Mouse click and drag control |
| 🔢 NumPy | Mathematical calculations |
| 💻 VS Code | Development environment |

---

## 🧠 How It Works

The system follows a real-time computer vision pipeline:

```text
Webcam
   ↓
Capture Video Frame
   ↓
OpenCV Processing
   ↓
MediaPipe Hand Detection
   ↓
21 Hand Landmarks
   ↓
Gesture Analysis
   ↓
Gesture Recognition
   ↓
Mouse / System Action
```

### 🔄 Process

1. The webcam captures the user's hand movement.
2. OpenCV processes each video frame.
3. MediaPipe detects the hand and identifies 21 hand landmarks.
4. Finger positions, angles, and distances are analyzed.
5. The system identifies the corresponding gesture.
6. The recognized gesture is mapped to a computer action.
7. PyAutoGUI or Pynput performs the required system-level action.

---

## ✋ Gesture Controls

| Gesture | Action |
|---|---|
| ☝️ Index finger | Move cursor |
| 👆 Index + bent middle finger | Left click |
| 👉 Middle + bent index finger | Right click |
| ✌️ Two fingers bent | Double click |
| 🖐️ Index + middle fingers extended | Scroll |
| 🤏 Index extended + middle bent + thumb close | Drag |
| 🤌 Both fingers bent + thumb close | Screenshot |

Gesture recognition is based on finger angles and the distance between hand landmarks.

---

## 📁 Project Structure

```text
Virtual-mouse/
│
├── main.py
├── util.py
├── evaluate_accuracy.py
├── requirements.txt
├── README.md
├── FINAL REPORT.pdf
├── final.pptx
├── final ppttt.pptx
├── my_screenshot_128.png
└── .gitignore
```

---

## ⚙️ Requirements

Before running the project, make sure you have:

- Python 3.11
- A working webcam
- Windows, Linux, or macOS
- Internet connection for installing dependencies

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/HarshaSK19/Virtual-mouse.git
```

### 2. Navigate into the project

```bash
cd Virtual-mouse
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Start the virtual mouse using:

```bash
python main.py
```

A webcam window will open and the system will begin detecting hand gestures.

To stop the application, press:

```text
Q
```

---

## 📸 Screenshot Capture

The project includes a gesture-based screenshot feature.

When the screenshot gesture is detected, the program captures the current screen and saves the image as a PNG file.

Example:

```text
my_screenshot_128.png
```

Generated screenshots are ignored by Git using the project's `.gitignore` configuration.

---

## 📊 Accuracy Evaluation

The project includes an evaluation script:

```text
evaluate_accuracy.py
```

The script is designed to calculate:

- Overall accuracy
- True Positives (TP)
- False Positives (FP)
- False Negatives (FN)
- Precision
- Recall

Run the evaluation using:

```bash
python evaluate_accuracy.py
```

The evaluation script expects a CSV file containing predicted and true gesture labels.

Accuracy values are not listed because the project does not currently have a finalized benchmark dataset.

---

## 🔍 Computer Vision Concepts

This project demonstrates practical applications of:

- Hand landmark detection
- Real-time computer vision
- Gesture recognition
- Coordinate mapping
- Distance calculation
- Angle calculation
- Human-computer interaction
- System automation

---

## 🎯 Applications

Gesture-controlled interfaces can be useful for:

- 💻 Touchless computer interaction
- ♿ Assistive technology
- 🎮 Interactive systems
- 🖥️ Contactless interfaces
- 🔗 Human-computer interaction research
- 🏠 Smart environments

---

## 🔮 Future Improvements

Possible future improvements include:

- 🖐️ Support for multiple hands
- 🎯 Improved cursor stabilization
- 🧠 Machine-learning-based gesture classification
- ⚙️ Customizable gestures
- 📈 Real-time performance metrics
- 🖥️ GUI-based configuration
- 🔊 Voice and gesture hybrid control
- 📱 Integration with other smart-device interfaces

---

## 👨‍💻 Author

**Harsha SK**

AI/ML & Data Science Enthusiast | RAG | Python

Interested in building practical solutions using:

- Artificial Intelligence
- Machine Learning
- Data Science
- Computer Vision
- Python
- Retrieval-Augmented Generation (RAG)

---

## ⭐ If You Like This Project

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project was developed for educational and project-development purposes.
