import os, winreg
# os.system("dir")

python_executable = os.path.join(os.__file__.split("lib\\")[0],"pythonw.exe")
path_to_pyw_file = os.path.abspath(os.path.dirname(__file__)) + "\check.pyw"

winreg.SetValue(winreg.HKEY_CURRENT_USER, "SOFTWARE\Classes\*\shell\\virustotal_checker", 1, "Check file on VirusTotal")
winreg.SetValue(winreg.HKEY_CURRENT_USER, "SOFTWARE\Classes\*\shell\\virustotal_checker\command", 1, f"{python_executable} {path_to_pyw_file} \"%1\"")
