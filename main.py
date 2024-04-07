#!/usr/bin/python3
# Main entry point
# for later : https://docs.python.org/3/library/tkinter.html
import tkinter as tk
from ui.ui import MainWindow

# Create root top level window
root = tk.Tk()


# Create an instance of MainWindow 
main_window = MainWindow(root)
main_window.master.title('OSRS Task Selector')
main_window.master.minsize(800, 600)

if __name__ == "__main__":
    main_window.mainloop()
