import winreg

winreg.DeleteKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\Classes\*\shell\\virustotal_checker\command") # must delete in two steps
winreg.DeleteKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\Classes\*\shell\\virustotal_checker")
