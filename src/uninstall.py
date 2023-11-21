import winreg

winreg.DeleteKey(winreg.HKEY_CURRENT_USER,  # must delete in two steps
                 r"SOFTWARE\Classes\*\shell\\virustotal_checker\command")
winreg.DeleteKey(winreg.HKEY_CURRENT_USER,
                 r"SOFTWARE\Classes\*\shell\\virustotal_checker")
