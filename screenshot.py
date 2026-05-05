from adb_utils import run_adb
import os

def capture_screenshot():
    run_adb("shell screencap -p /sdcard/screen.png")
    os.system("adb pull /sdcard/screen.png")
    run_adb("shell rm /sdcard/screen.png")
    return "Screenshot saved"