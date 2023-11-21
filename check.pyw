
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

def create_file_hash(filepath)-> str:
    sha256sum = hashlib.sha256()
    with open(filepath, 'rb') as file:
        # Read and update hash string value in blocks of 4K
        try:
            for byte_block in iter(lambda: file.read(4096),b""):
                sha256sum.update(byte_block)
        except Exception as e:
            log_error(e)
            exit(1)
    return sha256sum.hexdigest().upper()

def main():
    if len(sys.argv)<2:
        log_error("Program did not get any arguments supplied") # Compare with clipboard then?
        print("Could not find file to create hash from!")
        exit(1)
    path = sys.argv[-1]

    if not os.path.exists(path):
        error = f"Could not find file to create hash from! Path: {path}"
        log_error(error)
        print(error)
        exit(1)

    hash = create_file_hash(path)

    webbrowser.open_new_tab(f"https://www.virustotal.com/gui/search/{hash}")


if __name__ == "__main__":
    main()