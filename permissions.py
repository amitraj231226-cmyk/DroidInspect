from adb_utils import run_adb


IMPORTANT_PERMISSIONS = {
    "android.permission.CAMERA": "Camera",
    "android.permission.RECORD_AUDIO": "Microphone",
    "android.permission.ACCESS_FINE_LOCATION": "Precise Location",
    "android.permission.ACCESS_COARSE_LOCATION": "Approx Location",
    "android.permission.READ_CONTACTS": "Contacts",
    "android.permission.READ_CALL_LOG": "Call Logs",
    "android.permission.READ_EXTERNAL_STORAGE": "Storage",
    "android.permission.READ_PHONE_STATE": "Phone State",
    "android.permission.SEND_SMS": "Send SMS"
}


def scan_permissions(package):
    data = run_adb(f"shell dumpsys package {package}")

    results = {}

    for perm, label in IMPORTANT_PERMISSIONS.items():
        if perm in data:
            if f"{perm}: granted=true" in data:
                results[label] = "Allowed"
            elif f"{perm}: granted=false" in data:
                results[label] = "Denied"
            else:
                results[label] = "Requested"

    return results