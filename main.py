import tkinter as tk
from tkinter import filedialog
import pandas as pd

class DataAnalyzerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data Analyzer")
        self.geometry("600x400")

        self.data = None

        self.create_widgets()

    def create_widgets(self):
        self.file_label = tk.Label(self, text="No file selected")
        self.file_label.pack(pady=10)

        self.load_button = tk.Button(self, text="Select CSV File", command=self.load_csv)
        self.load_button.pack(pady=5)

        self.data_listbox = tk.Listbox(self, width=100)
        self.data_listbox.pack(pady=10)

        self.sort_button = tk.Button(self, text="Sort by Column", command=self.sort_data)
        self.sort_button.pack(pady=5)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.file_label.config(text=file_path)
            self.data = pd.read_csv(file_path)
            self.display_data()

    def display_data(self):
        self.data_listbox.delete(0, tk.END)
        for row in self.data.values:
            self.data_listbox.insert(tk.END, " | ".join(str(cell) for cell in row))

    def sort_data(self):
        if self.data is not None:
            selected_index = self.data_listbox.curselection()
            if selected_index:
                column_index = selected_index[0]
                column_name = self.data.columns[column_index]
                self.data.sort_values(by=column_name, inplace=True)
                self.display_data()

if __name__ == "__main__":
    app = DataAnalyzerApp()
    app.mainloop()
