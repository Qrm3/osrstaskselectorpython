#!/usr/bin/python3
# Main entry point
# for later : https://tkdocs.com/shipman/index-2.html
import tkinter as tk
from ui.ui import MainWindow

# Create root
root = tk.Tk()
# root.title('OSRS Task Selector')

main_window = MainWindow(root)
main_window.master.title('OSRS Task Selector')

if __name__ == "__main__":
    main_window.mainloop()