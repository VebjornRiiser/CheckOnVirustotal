
from datetime import datetime
import os, sys, hashlib, webbrowser
def log_error(error_msg):
    with open("logfile_virustotalchecker.txt", "a+") as logfile:
        logfile.write(f"{datetime.now()}: {error_msg}\n")
    show_popup("Error", error_msg)

def show_popup(title, message):
    import tkinter as tk
    from tkinter import messagebox

    root = tk.Tk()
    root.withdraw()  # Hides the main window

    messagebox.showinfo(title, message)
    root.quit()


if len(sys.argv)<2:
    log_error("Program did not get any arguments supplied") # Compare with clipboard then?
    print("Could not find file to create hash from!")
    exit(1)


if not os.path.exists(sys.argv[-1]):
    error = f"Could not find file to create hash from! Path: {sys.argv[-1]}"
    log_error(error)
    print(error)
    exit(1)


sha256sum = hashlib.sha256()

with open(sys.argv[-1], 'rb') as file:
    # Read and update hash string value in blocks of 4K
    try:
        for byte_block in iter(lambda: file.read(4096),b""):
            sha256sum.update(byte_block)
    except Exception as e:
        log_error(e)
        exit(1)
webbrowser.open_new_tab(f"https://www.virustotal.com/gui/search/{sha256sum.hexdigest().upper()}")
