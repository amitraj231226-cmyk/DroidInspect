from adb_utils import run_adb


def get_health_score():
    battery_data = run_adb("shell dumpsys battery")
    storage_data = run_adb("shell df /storage/emulated")

    score = 100

    if "level: " in battery_data:
        battery_level = int(
            battery_data.split("level: ")[1].split("\n")[0]
        )

        if battery_level < 20:
            score -= 25
        elif battery_level < 50:
            score -= 10

    if "100%" in storage_data:
        score -= 30

    if score >= 80:
        status = "Healthy"
    elif score >= 50:
        status = "Moderate"
    else:
        status = "Critical"

    return score, status