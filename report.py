import json

def export_report(device_info, battery, storage, apps):
    report = {
        "device_info": device_info,
        "battery": battery,
        "storage": storage,
        "installed_apps": apps
    }

    with open("report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    return "Report exported to report.json"