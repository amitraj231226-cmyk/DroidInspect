import time
from adb_utils import run_adb


def monitor_battery():
    while True:
        battery = run_adb("shell dumpsys battery | findstr level")
        print(f"Battery Status: {battery}")
        time.sleep(5)