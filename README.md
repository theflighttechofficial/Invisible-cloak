# 🪄 Invisible Cloak using OpenCV

An interactive Computer Vision project that creates a real-time invisibility cloak effect using Python and OpenCV. The application detects a user-selected cloak color and replaces it with the captured background, producing the illusion of invisibility inspired by the famous Harry Potter cloak.

---

## 🚀 Features

- 🎨 Interactive color selection palette
- 🎥 Real-time webcam processing
- 🌈 HSV color detection
- 🧹 Noise removal using morphological operations
- 🪄 Real-time invisibility effect
- ⚡ Lightweight and easy to run
- 💻 Pure Python implementation

---

## 📸 Demo

> Add screenshots or a GIF here.

Example:

```text
screenshots/
├── dashboard.png
├── cloak_effect.png
└── color_selection.png
```

```markdown
![Color Selection](screenshots/color_selection.png)

![Invisible Cloak](screenshots/cloak_effect.png)
```

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Computer Vision | OpenCV |
| Numerical Computing | NumPy |

---

## 📂 Project Structure

```
Invisible-cloak/
│
├── cloak.py
├── screenshots/
│   ├── color_selection.png
│   └── cloak_effect.png
│
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/theflighttechofficial/Invisible-cloak.git
```

```bash
cd Invisible-cloak
```

### Install dependencies

```bash
pip install opencv-python numpy
```

---

## ▶️ Run the Project

```bash
python cloak.py
```

---

## 🧠 How It Works

1. Launch the application.
2. Select the desired cloak color from the color palette.
3. The system captures the background.
4. Wear a cloth of the selected color.
5. The cloak region is detected using HSV color segmentation.
6. The detected region is replaced with the stored background.
7. The cloak appears invisible in real time.

---

## 🔄 Workflow

```
Start
   │
   ▼
Select Cloak Color
   │
   ▼
Capture Background
   │
   ▼
Read Webcam Frames
   │
   ▼
Convert to HSV
   │
   ▼
Detect Selected Color
   │
   ▼
Create Binary Mask
   │
   ▼
Remove Noise
   │
   ▼
Replace Cloak with Background
   │
   ▼
Display Invisible Effect
```

---

## ✨ Core Concepts

- HSV Color Space
- Color Thresholding
- Background Subtraction
- Morphological Transformations
- Bitwise Image Operations
- Real-Time Video Processing

---

## 📌 Applications

- Computer Vision Learning
- Image Processing Demonstrations
- Educational Projects
- Augmented Reality Concepts
- OpenCV Practice

---

## 🔮 Future Improvements

- Multiple cloak color detection
- Automatic color calibration
- Deep Learning segmentation
- Background refresh button
- Video recording support
- CUDA GPU acceleration
- Streamlit GUI
- Mobile camera support

---

## 👨‍💻 Author

**Varun Vaibhav**

Computer Science Engineering (AI & Data Analytics)

GitHub: https://github.com/theflighttechofficial

---

## 📄 License

This project is intended for educational and demonstration purposes.

---

## ⭐ Support

If you found this project interesting, consider giving it a ⭐ on GitHub!
