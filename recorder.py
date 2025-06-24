import cv2
import pyautogui
import numpy as np
import argparse
import os
import re
import time
import sys
from win32api import GetSystemMetrics
import subprocess

def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def get_screen_size():
    return GetSystemMetrics(0), GetSystemMetrics(1)

def print_help():
    print("""
🎥 Terminal Screen Recorder - Command List
------------------------------------------
p      → Pause/Resume Recording
q      → Stop and Save Recording
h      → Show Commands Again
------------------------------------------
""")

def record_screen(filename, fps, output_dir):
    width, height = get_screen_size()
    dim = (width, height)

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{sanitize_filename(filename)}.mp4")

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, dim)

    print(f"\n🎬 Recording started: {output_path}")
    print_help()

    paused = False

    try:
        while True:
            if not paused:
                img = pyautogui.screenshot()
                frame = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
                out.write(frame)

            if os.name == 'nt':
                import msvcrt
                if msvcrt.kbhit():
                    key = msvcrt.getwch().lower()
                    if key == 'p':
                        paused = not paused
                        print("⏸️ Paused" if paused else "▶️ Resumed")
                    elif key == 'q':
                        print("🛑 Stopping recording...")
                        break
                    elif key == 'h':
                        print_help()
    except KeyboardInterrupt:
        print("\n⚠️ Interrupted by user.")
    finally:
        out.release()
        print(f"\n✅ Video saved as {output_path}")
        try:
            subprocess.Popen(f'explorer \"{output_dir}\"', shell=True)
        except Exception as e:
            print(f"⚠️ Could not open folder: {e}")

def prompt_if_missing(args):
    if not args.name:
        args.name = input("📁 Enter video file name (without extension): ").strip()
        if not args.name:
            print("❌ Video name is required. Exiting.")
            sys.exit()

    if not args.output_path:
        args.output_path = input("📂 Enter folder to save video (or leave blank for Documents): ").strip()
        if not args.output_path:
            args.output_path = os.path.join(os.path.expanduser("~"), "Documents")
        if not os.path.exists(args.output_path):
            try:
                os.makedirs(args.output_path)
            except:
                print("❌ Could not create the folder. Exiting.")
                sys.exit()

    if args.fps is None:
        try:
            args.fps = int(input("🎞️ Enter FPS (frames per second, default is 15): ").strip() or 15)
        except ValueError:
            print("⚠️ Invalid FPS entered. Using default: 15")
            args.fps = 15

    return args

def main():
    parser = argparse.ArgumentParser(
        description="🎥 Terminal Screen Recorder - CLI & Interactive",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('--name', type=str, help="Output video file name (without extension)")
    parser.add_argument('--fps', type=int, help="Frames per second (default: 15)")
    parser.add_argument('--output-path', type=str, help="Optional path to save the recording")
    args = parser.parse_args()

    args = prompt_if_missing(args)
    record_screen(args.name, args.fps, args.output_path)

if __name__ == "__main__":
    main()
