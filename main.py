from adb_utils import check_device
from device_info import get_device_info
from battery import get_battery_info
from storage import get_storage
from apps import get_apps
from screenshot import capture_screenshot
from report import export_report
from dashboard import banner, menu
from pdf_report import export_pdf
from apps import search_app
from monitor import monitor_battery
from wireless import enable_wireless, connect_wireless, disconnect_wireless
from health import get_health_score
from apk_inspector import inspect_app
from permissions import scan_permissions
from risk_report import generate_risk_report


def main():
    if not check_device():
        print("No device connected")
        return

    while True:
        banner()
        menu()

        choice = input("\nEnter choice: ")

        if choice == "1":
            info = get_device_info()
            for k, v in info.items():
                print(f"{k}: {v}")

        elif choice == "2":
            print(get_battery_info())

        elif choice == "3":
            print(get_storage())

        elif choice == "4":
            apps = get_apps()
            print(f"\nInstalled Apps: {len(apps)}")
            for app in apps[:30]:
                print(app)

        elif choice == "5":
            print(capture_screenshot())

        elif choice == "6":
            export_report(
                get_device_info(),
                get_battery_info(),
                get_storage(),
                get_apps()
            )
            print("Report Exported")

        elif choice == "7":
            keyword = input("Enter app keyword: ")
            results = search_app(keyword)
            for app in results:
                print(app)

        elif choice == "8":
            monitor_battery()

        elif choice == "9":
            print(export_pdf(
            get_device_info(),
            get_battery_info(),
            get_storage()
        ))

        elif choice == "10":
            print(enable_wireless())

        elif choice == "11":
            ip = input("Enter device IP: ")
            print(connect_wireless(ip))

        elif choice == "12":
            ip = input("Enter device IP: ")
            print(disconnect_wireless(ip))

        elif choice == "13":
            score, status = get_health_score()
            print(f"\nHealth Score: {score}/100")
            print(f"Status: {status}")
        
        elif choice == "14":
            package = input("Enter package name: ")
            print(inspect_app(package))

        elif choice == "15":
            package = input("Enter package name: ")
            perms = scan_permissions(package)

            print("\n===== PERMISSION AUDIT =====")

            for perm, status in perms.items():
                print(f"{perm}: {status}")
        
        elif choice == "16":
            report = generate_risk_report()

            print("\n===== PERMISSION RISK REPORT =====\n")

            for app in report:
                print(f"{app['package']}")
                print(f"Risk: {app['risk']}")
                print(f"Score: {app['score']}")
                print("-" * 30)

        elif choice == "17":
            break

        else:
            print("Invalid option")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()