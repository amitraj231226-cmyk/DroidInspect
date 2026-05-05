from adb_utils import run_adb

def get_storage():
    return run_adb("shell df /storage/emulated")