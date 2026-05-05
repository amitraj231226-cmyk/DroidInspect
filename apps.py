from adb_utils import run_adb


def get_apps():
    apps = run_adb("shell pm list packages")
    return [app.replace("package:", "") for app in apps.splitlines()]


def search_app(keyword):
    apps = get_apps()
    return [app for app in apps if keyword.lower() in app.lower()]