#  UI Components
import tkinter as tk
    
class MainWindow(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, width=800, height=600)
        self.grid(sticky=tk.EW)
        self.create_widgets()
        # set master and self to have '0' columns.
        if self.master:
            self.master.grid_columnconfigure(0, weight=1)
        
        self.grid_columnconfigure(0, weight=1)

    def create_widgets(self):        
        # Current Task
        self.current_task_labelframe = tk.LabelFrame(self, padx=2, pady=2, text='Current Task')
        self.current_task_labelframe.grid_columnconfigure(0, weight=1)
        self.current_task_labelframe.grid(sticky=tk.EW)

        self.current_task_label = tk.Label(self.current_task_labelframe, text="Placeholder Text", anchor=tk.W, width=50, border='1')
        self.current_task_label.grid(sticky=tk.EW)
        
        # Task Buttons        
        self.task_button_frame = tk.Frame(self, padx=2, pady=2)
        self.task_button_frame.grid(sticky=tk.E)
        
        self.get_task_button = tk.Button(self.task_button_frame, text="Get Task")
        self.get_task_button.grid(column=0, row=0)

        self.skip_task_button = tk.Button(self.task_button_frame, text="Skip Task")
        self.skip_task_button.grid(column=1, row=0)

        self.complete_task_button = tk.Button(self.task_button_frame, text="Complete Task")
        self.complete_task_button.grid(column=2, row=0)

        # New Task
        self.new_task_labelframe = tk.LabelFrame(self, padx=2, pady=2, text="New Task")
        self.new_task_labelframe.columnconfigure(1, weight=1)
        self.new_task_labelframe.grid(sticky=tk.EW)
        
        # Task Name Field
        self.new_task_name_label = tk.Label(self.new_task_labelframe, text="Name:")
        self.new_task_name_label.grid(column=0, row=0, sticky=tk.W)

        self.new_task_name_text = tk.Text(self.new_task_labelframe, height=1, padx=2, pady=2, takefocus=0)
        self.new_task_name_text.grid(column=1, row=0, sticky=tk.EW)

        # Task Description field
        self.new_task_description_label = tk.Label(self.new_task_labelframe, text="Description:")
        self.new_task_description_label.grid(column=0, row=1, sticky=tk.W)
        
        self.new_task_description_text = tk.Text(self.new_task_labelframe, height=1, padx=2, pady=2, takefocus=0)
        self.new_task_description_text.grid(column=1, row=1, sticky=tk.EW)
        
        # New Task buttons
        self.new_task_button_frame = tk.Frame(self.new_task_labelframe, padx=2, pady=2)
        self.new_task_button_frame.grid(sticky=tk.E)
        
        self.create_task_button = tk.Button(self, text="Create Task")
        self.create_task_button.grid(sticky=tk.E)
        