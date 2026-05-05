from adb_utils import run_adb

def get_battery_info():
    data = run_adb("shell dumpsys battery")
    return data