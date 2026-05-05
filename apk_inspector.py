from adb_utils import run_adb


def inspect_app(package):
    data = run_adb(f"shell dumpsys package {package}")
    return data