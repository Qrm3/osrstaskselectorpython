#  UI Components
import tkinter as tk
import tkinter.ttk as ttk
   
class MainWindow(tk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master, width=800, height=600)
        self.grid(sticky=tk.EW)
        self.create_widgets()
        # set master and self to have '0' columns.
        if self.master:
            self.master.grid_columnconfigure(0, weight=1)
        
        self.grid_columnconfigure(0, weight=1)

    def create_widgets(self):        
        ## Notebook
        self.notebook = ttk.Notebook(self)
        
        # tabs
        self.current_task_tab = ttk.Frame(self.notebook)
        self.current_task_tab.grid_columnconfigure(0, weight=1)
        
        self.create_task_tab = ttk.Frame(self.notebook)
        self.create_task_tab.grid_columnconfigure(1, weight=1)
        
        self.completed_task_tab = ttk.Frame(self.notebook)
        
        # add tabs
        self.notebook.add(self.current_task_tab, text="Current Task")
        self.notebook.add(self.create_task_tab, text="Create Task")
        self.notebook.add(self.completed_task_tab, text="Completed Tasks")
        
        self.notebook.grid(sticky=tk.NSEW)
        
        ## Current Task
        # label frame
        self.current_task_labelframe = ttk.LabelFrame(self.current_task_tab, text="Current Task")
        self.current_task_labelframe.grid(sticky=tk.EW)
        
        # label        
        self.current_task_label = ttk.Label(self.current_task_labelframe, text="Test Placeholder Text")
        self.current_task_label.grid(sticky=tk.EW)
        
        # button frame
        self.current_task_button_frame = ttk.Frame(self.current_task_tab)
        self.current_task_button_frame.grid(sticky=tk.E)
        
        # buttons
        self.get_task_button = ttk.Button(self.current_task_button_frame, text="Get Task")
        self.get_task_button.grid(column=0, row=0)
        
        self.skip_task_button = ttk.Button(self.current_task_button_frame, text="Skip Task")
        self.skip_task_button.grid(column=1, row=0)
        
        self.complete_task_button = ttk.Button(self.current_task_button_frame, text="Complete Task")
        self.complete_task_button.grid(column=2, row=0)
        
        ## Create Task
        # labels
        self.create_task_name_label = ttk.Label(self.create_task_tab, text="Name:")
        self.create_task_name_label.grid(column=0, row=0, sticky=tk.W)
        
        self.create_task_description_label = ttk.Label(self.create_task_tab, text="Description:")
        self.create_task_description_label.grid(column=0, row=1, sticky=tk.W)
        
        # entries
        self.create_task_name_textbox = ttk.Entry(self.create_task_tab)
        self.create_task_name_textbox.grid(column=1, row=0, sticky=tk.EW)
        
        self.create_task_description_textbox = ttk.Entry(self.create_task_tab)
        self.create_task_description_textbox.grid(column=1, row=1, sticky=tk.EW)
        
        
        
        ## Completed Task
        
        # ### New Task
        # self.new_task_labelframe = tk.LabelFrame(self, padx=2, pady=2, text="New Task")
        # self.new_task_labelframe.columnconfigure(1, weight=1)
        # self.new_task_labelframe.grid(sticky=tk.EW)
        # # Task Name
        # self.new_task_name_label = tk.Label(self.new_task_labelframe, text="Name:")
        # self.new_task_name_label.grid(column=0, row=0, sticky=tk.W)

        # self.new_task_name_text = tk.Text(self.new_task_labelframe, height=1, padx=2, pady=2, takefocus=0)
        # self.new_task_name_text.grid(column=1, row=0, sticky=tk.EW)
        # # Task Description 
        # self.new_task_description_label = tk.Label(self.new_task_labelframe, text="Description:")
        # self.new_task_description_label.grid(column=0, row=1, sticky=tk.W)
        
        # self.new_task_description_text = tk.Text(self.new_task_labelframe, height=1, padx=2, pady=2, takefocus=0)
        # self.new_task_description_text.grid(column=1, row=1, sticky=tk.EW)
        # ### New Task buttons
        # self.new_task_button_frame = tk.Frame(self.new_task_labelframe, padx=2, pady=2)
        # self.new_task_button_frame.grid(sticky=tk.E)
        # # Create Task
        # self.create_task_button = tk.Button(self, text="Create Task")
        # self.create_task_button.grid(sticky=tk.E)
        # ### Completed Tasks
        # self.completed_task_labelframe = tk.LabelFrame(self, padx=2, pady=2, text="Completed Tasks")
        # self.completed_task_labelframe.grid(sticky=tk.EW)
        # # Completed Task
        # self.completed_task_yscrollbar = tk.Scrollbar(self.completed_task_labelframe, orient=tk.VERTICAL)
        # self.completed_task_yscrollbar.grid(column=1, row=0, sticky=tk.NS)
        
        # self.completed_task_listbox = tk.Listbox(self.completed_task_labelframe, activestyle="none", yscrollcommand=self.completed_task_yscrollbar)
        # self.completed_task_listbox.grid(column=0, row=0)
        