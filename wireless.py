from adb_utils import run_adb
import os


def enable_wireless(port=5555):
    result = run_adb(f"tcpip {port}")
    return result


def connect_wireless(ip, port=5555):
    os.system(f"adb connect {ip}:{port}")
    return f"Connecting to {ip}:{port}"


def disconnect_wireless(ip, port=5555):
    os.system(f"adb disconnect {ip}:{port}")
    return "Disconnected"