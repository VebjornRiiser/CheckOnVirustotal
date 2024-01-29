from datetime import datetime
import os
import sys
import webbrowser
from main import *

def main():
    if len(sys.argv) < 2:
        log_error("Program did not get any arguments supplied")
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
