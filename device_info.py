from adb_utils import run_adb

def get_device_info():
    return {
        "Model": run_adb("shell getprop ro.product.model"),
        "Brand": run_adb("shell getprop ro.product.brand"),
        "Android Version": run_adb("shell getprop ro.build.version.release"),
        "Device": run_adb("shell getprop ro.product.device"),
        "Manufacturer": run_adb("shell getprop ro.product.manufacturer")
    }