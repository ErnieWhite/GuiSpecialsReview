import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog as fd
import csv


class FileControls(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.cs_label = ttk.Label(self, text="Customer Special File")
        self.cs_label.grid(row=0, column=0, sticky=(tk.W,))
        self.cs_entry = ttk.Entry(self)
        self.cs_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
        self.cs_button = ttk.Button(self, text="Load", command=lambda: self.button_clicked(self.cs_label['text']))
        self.cs_button.grid(row=0, column=2, sticky=(tk.E,))

        self.bs_label = ttk.Label(self, text="Branch Special File")
        self.bs_label.grid(row=1, column=0, sticky=(tk.W,))
        self.bs_entry = ttk.Entry(self)
        self.bs_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))
        self.bs_button = ttk.Button(self, text="Load", command=lambda: self.button_clicked(self.bs_label['text']))
        self.bs_button.grid(row=1, column=2, sticky=(tk.E,))

        self.rc_label = ttk.Label(self, text="Rate Card File")
        self.rc_label.grid(row=2, column=0, sticky=(tk.W,))
        self.rc_entry = ttk.Entry(self)
        self.rc_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))
        self.rc_button = ttk.Button(self, text="Load", command=lambda: self.button_clicked(self.rc_label['text']))
        self.rc_button.grid(row=2, column=2, sticky=(tk.E,))

    def button_clicked(self, which):
        print(f"{which}  button clicked")
        file_path = fd.askopenfilename()
        if file_path != '':
            if which == 'Customer Special File':
                print('Customer Specials loaded')
                app.cs_text.delete('1.0', app.cs_text.index('end'))
                with open(file_path, 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    for row in reader:
                        app.cs_text.insert(app.cs_text.index('end'), str(row)+'\n')
            elif which == 'Branch Special File':
                print('Branch Specials loaded')
                app.bs_text.delete('1.0', app.bs_text.index('end'))
                with open(file_path, 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    for row in reader:
                        app.bs_text.insert(app.bs_text.index('end'), str(row) + '\n')
            elif which == 'Rate Card File':
                print('Rate Cards loaded')
                app.rc_text.delete('1.0', app.rc_text.index('end'))
                with open(file_path, 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    for row in reader:
                        app.rc_text.insert(app.rc_text.index('end'), str(row) + '\n')
            else:
                raise ValueError('I do not know what button was cliked')


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.file_controls = FileControls(self)
        self.file_controls.grid(row=0, column=0, sticky=(tk.W,))
####################################################################################################

        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1, column=0, sticky=(tk.W, tk.S, tk.E))

        self.cs_frame = ttk.Frame(self.notebook, width=400, height=200)
        self.bs_frame = ttk.Frame(self.notebook, width=400, height=200)
        self.rc_frame = ttk.Frame(self.notebook, width=400, height=200)

        self.cs_text = tk.Text(self.cs_frame, wrap='none')
        self.cs_text.pack()
        self.bs_text = tk.Text(self.bs_frame)
        self.bs_text.pack()
        self.rc_text = tk.Text(self.rc_frame)
        self.rc_text.pack()

        self.cs_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.bs_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.rc_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))

        self.notebook.add(self.cs_frame, text="Customer Specials")
        self.notebook.add(self.bs_frame, text="Branch Specials")
        self.notebook.add(self.rc_frame, text="Rate Card Entries")
        self.columnconfigure(index=0, weight=1)


if __name__ == "__main__":
    app = App()
    app.mainloop()
