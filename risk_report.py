from apps import get_apps
from adb_utils import run_adb


RISKY_PERMISSIONS = {
    "android.permission.CAMERA": 15,
    "android.permission.RECORD_AUDIO": 20,
    "android.permission.ACCESS_FINE_LOCATION": 20,
    "android.permission.READ_CONTACTS": 15,
    "android.permission.READ_CALL_LOG": 20,
    "android.permission.SEND_SMS": 25,
    "android.permission.READ_PHONE_STATE": 10
}


def analyze_app(package):
    data = run_adb(f"shell dumpsys package {package}")

    score = 0
    found = []

    for perm, weight in RISKY_PERMISSIONS.items():
        if f"{perm}: granted=true" in data:
            score += weight
            found.append(perm)

    if score >= 60:
        risk = "HIGH"
    elif score >= 30:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "package": package,
        "score": score,
        "risk": risk,
        "permissions": found
    }


def generate_risk_report():
    apps = get_apps()
    report = []

    for app in apps[:30]:
        result = analyze_app(app)
        report.append(result)

    return report