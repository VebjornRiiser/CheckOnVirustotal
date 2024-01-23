import os
import sys
import winreg

python_executable = os.path.join(os.path.dirname(sys.executable), "pythonw.exe")
path_to_pyw_file = os.path.abspath(os.path.dirname(__file__)) + r"\check.pyw"

if not os.path.exists(path_to_pyw_file):
    print(f"File {path_to_pyw_file} not found")
    input("Press Enter to exit...")
    exit(1)
if not os.path.exists(python_executable):
    print(f"Pythonw executable not found")
    input("Press Enter to exit...")
    exit(1)

winreg.SetValue(winreg.HKEY_CURRENT_USER,
                r"SOFTWARE\Classes\*\shell\\virustotal_checker", 1,
                "Check file on VirusTotal")

winreg.SetValue(winreg.HKEY_CURRENT_USER,
                r"SOFTWARE\Classes\*\shell\\virustotal_checker\command", 1,
                f"{python_executable} {path_to_pyw_file} \"%1\"")
