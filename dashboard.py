from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(Fore.CYAN + """
========================================
         D R O I D  I N S P E C T
========================================
    Android Device Diagnostic Toolkit
""")

def menu():
    print(Fore.GREEN + "\nChoose an option:")
    print("1. Device Info")
    print("2. Battery Info")
    print("3. Storage Info")
    print("4. Installed Apps")
    print("5. Capture Screenshot")
    print("6. Export Report")
    print("7. Search App")
    print("8. Battery Monitor")
    print("9. Export PDF")
    print("10. Exit")