# 🎥 Terminal Screen Recorder (Python CLI + .exe + Installer)

A fully terminal-driven fullscreen screen recorder built using Python, packaged as a `.exe` with a proper Windows installer.  
Perfect for developers, students, and CLI lovers who want a distraction-free recording experience.

---

## 📌 What It Is

Terminal Screen Recorder is a lightweight and open-source screen recording tool that:

- 📺 Records the **entire screen**
- ⌨️ Takes **keyboard input inside the terminal only** (no global hotkeys!)
- 💾 Saves video to your chosen directory in `.mp4` format
- 📦 Comes with a Windows `.exe` and a full **installer with shortcut support**
- 🧠 Works without GUI popups or setup — simple, fast, focused

---

## ❓ Why I Built It

I needed a **simple, distraction-free screen recorder** that:
- Runs entirely inside the terminal
- Doesn't pause when typing `p` in another app (like VS Code or Chrome)
- Can be compiled and shared as a clean `.exe` installer
- Offers the power of CLI + the polish of native apps

So I built this as a real-world project, learned packaging and deployment — and now sharing it open-source!

---

## ⚙️ How It Works

- Captures screenshots frame-by-frame using `pyautogui`
- Encodes video using `OpenCV`
- Controls recording with simple key presses **within terminal window**
- Prompts the user for video name, save location, and frame rate if not provided

---

## 💡 Features

✅ Fullscreen screen recording  
✅ Terminal-only control (safe from accidental key presses in other apps)  
✅ Pause/resume (`p`), stop/save (`q`), show help (`h`)  
✅ Save anywhere — defaults to your `Documents` folder  
✅ Opens folder after recording completes  
✅ Supports CLI arguments for automation  
✅ Comes with Windows installer + desktop shortcut

---

## 🧩 Technologies Used

- Python 3.11
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) for screen capture
- [OpenCV](https://opencv.org/) for video encoding
- [NumPy](https://numpy.org/) for frame handling
- [PyInstaller](https://pyinstaller.org/) for `.exe` generation
- [Inno Setup](https://jrsoftware.org/isinfo.php) for Windows installer

---

## 💻 How to Install

### ✅ Option 1: Using Installer (Recommended)

1. [Download `ScreenRecorderInstaller.exe`](https://your-link-here)
2. Run the installer
3. It will:
   - Install to `C:\Program Files\python Screen Recorder`
   - Create Start Menu and Desktop shortcuts
   - Automatically launch the recorder when done

### ✅ Option 2: Portable `.exe` Only

1. [Download `recorder.exe`](https://your-link-here)
2. Place it anywhere
3. Run from terminal or double-click

---

## 🚀 How to Use
You can use the screen recorder either **interactively** (just run it and it will ask you questions) or by passing **command-line arguments**.

You’ll be prompted in the terminal to enter:

📁 Video file name

📂 Save folder path (default = Documents)

🎞️ FPS (frames per second) (default = 15)

⚙️ All Command-Line Options
Option	Description	Default	Required?
--name	File name (without .mp4 extension)	Prompted if not provided	✅ Yes
--fps	Frames per second for video recording	15	❌ No
--output-path	Folder to save the recorded .mp4 file	Documents folder	❌ No
--help	Show command-line help and exit	—	❌ No

🎮 Terminal-Only Controls
Once recording starts, use the terminal window to control it:

Key	Action
p	⏸️ Pause / ▶️ Resume
q	🛑 Stop and save video
h	📖 Show help commands again

📌 Only works while terminal is focused!



### 📦 CLI (Fast)

```bash
recorder.exe --name tutorial --fps 20 --output-path "D:\Videos"
## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

See the [LICENSE](LICENSE) file for details.