import subprocess

ADB_PATH = r"E:\platform-tools-latest-windows\platform-tools\adb.exe"

def run_adb(command):
    result = subprocess.run(
        [ADB_PATH] + command.split(),
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def check_device():
    output = run_adb("devices")
    return "device" in output