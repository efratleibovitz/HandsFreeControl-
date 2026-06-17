# ✋ AirCommand

> Control your computer without touching it — using just your hand and your voice.

AirCommand uses your **webcam** and **microphone** as smart sensors to control music, volume, and screen scrolling in real time.

---

## 🎯 What It Does

| Input | Gesture / Word | Action |
|-------|---------------|--------|
| ✋ Camera | Open hand — fingers spread | Control volume by distance |
| ✊ Camera | Fist | Play / Pause |
| 📷 Camera | Wrist in top third of frame | Scroll up |
| 📷 Camera | Wrist in bottom third of frame | Scroll down |
| 🎙️ Microphone | "תגביה" | Volume up |
| 🎙️ Microphone | "תנמיך" | Volume down |
| 🎙️ Microphone | "תעצור" | Pause |
| 🎙️ Microphone | "תמשיך" | Continue |
| 🎙️ Microphone | "גלול כלפי מעלה" | Scroll up |
| 🎙️ Microphone | "גלול כלפי מטה" | Scroll down |

---

## 📁 Project Structure

```
AirCommand/
├── main.py                      ← Entry point, connects everything
│
├── camera/
│   ├── hand_data.py             ← Hand calculations (distance, fist, wrist)
│   ├── hand_service.py          ← Camera → MediaPipe processing
│   └── gesture_controller.py   ← Gesture → Action logic
│
├── microphone/
│   ├── voice_data.py            ← Maps recognized words to commands
│   ├── voice_service.py         ← Listens in background thread
│   └── voice_controller.py     ← Command → Action logic
│
├── actions/
│   └── action_executor.py      ← All OS commands (shared by camera & mic)
│
└── hand_landmarker.task         ← Pre-trained MediaPipe hand model
```

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install opencv-python mediapipe pyautogui SpeechRecognition pyaudio
```

### 2. Make sure `hand_landmarker.task` is in the root folder

If it's missing, download it from:
```
https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task
```

### 3. Run

```bash
python main.py
```

Press **Q** to quit.

---

## 🛠️ Technologies Used

| Library | Purpose |
|---------|---------|
| [OpenCV](https://opencv.org/) | Camera feed capture and display |
| [MediaPipe](https://mediapipe.dev/) | Hand landmark detection |
| [PyAutoGUI](https://pyautogui.readthedocs.io/) | Keyboard & scroll simulation |
| [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) | Hebrew voice command recognition |

---

## ⚙️ Configuration

| Setting | File | Default |
|---------|------|---------|
| Scroll speed | `actions/action_executor.py` | `15` |
| Scroll interval (frames) | `camera/gesture_controller.py` | `5` |
| Voice language | `microphone/voice_service.py` | `he-IL` |

---

## 💡 How It Works

- The **camera loop** runs in the main thread — captures frames, detects hand landmarks, and triggers gestures.
- The **microphone** runs in a **background thread** — so it never blocks the camera.
- Both share the same `ActionExecutor` to perform OS-level actions.

---

*Built with ❤️ as a graduation project.*
