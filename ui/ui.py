#  UI Components
import tkinter as tk
    
class MainWindow(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, width=800, height=600)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # self.grid_columnconfigure(2, weight=1)
        
        self.quit_button = tk.Button(self, text='Quit', command=self.quit)
        self.quit_button.grid(sticky=tk.EW)

        self.current_task_labelframe = tk.LabelFrame(self, padx=2, pady=2, text='Current Task')
        self.current_task_labelframe.grid()

        self.current_task_label = tk.Label(self.current_task_labelframe, text="Placeholder Text", anchor=tk.W, width=50)
        self.current_task_label.pack()
        
        self.task_button_frame = tk.Frame(self, padx=2, pady=2)
        self.task_button_frame.grid(sticky=tk.W)
        
        self.get_task_button = tk.Button(self.task_button_frame, text="Get Task")
        self.get_task_button.grid(column=0, row=0)

        self.skip_task_button = tk.Button(self.task_button_frame, text="Skip Task")
        self.skip_task_button.grid(column=1, row=0)

        self.complete_task_button = tk.Button(self.task_button_frame, text="Complete Task")
        self.complete_task_button.grid(column=2, row=0)
