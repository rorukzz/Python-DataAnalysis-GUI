import pandas as pd
import os

# Global DataFrame to store edited data
global_edited_data = None

# Global variable to count edits
total_edits = 0

class DataAnalyzerApp:
    def __init__(self):
        self.data = None
        self.edits_count = 0
        self.selected_column = None

    def load_csv(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.display_data()

    def display_data(self):
        if self.data is not None:
            print("Data Analyzer")
            print("File Selected:", self.file_path)
            print(self.data.head())
        else:
            print("No data to display")

    def apply_edits(self, edited_data):
        global global_edited_data
        global total_edits
        global_edited_data
        global_edited_data = edited_data
        self.edits_count += 1
        total_edits += 1

    def sort_data(self):
        if global_edited_data is None:
            edited_data = self.data.copy()
        else:
            edited_data = global_edited_data.copy()

        if self.selected_column in edited_data.columns:
            edited_data.sort_values(by=self.selected_column, inplace=True)
            print("Data sorted by column:", self.selected_column)
            print(edited_data.head())
            self.apply_edits(edited_data)
        else:
            print("Selected column not found in data")

    def aggregate_data(self):
        if global_edited_data is None:
            edited_data = self.data.copy()
        else:
            edited_data = global_edited_data.copy()

        if self.selected_column in edited_data.columns:
            aggregated_data = edited_data.groupby(self.selected_column).size().reset_index(name='count')
            print("Aggregated data by column:", self.selected_column)
            print(aggregated_data)
            self.apply_edits(edited_data)
        else:
            print("Selected column not found in data")

    def convert_to_datetime(self):
        if global_edited_data is None:
            edited_data = self.data.copy()
        else:
            edited_data = global_edited_data.copy()

        if self.selected_column in edited_data.columns:
            edited_data[self.selected_column] = pd.to_datetime(edited_data[self.selected_column])
            print("Converted column to datetime:", self.selected_column)
            print(edited_data.head())
            self.apply_edits(edited_data)
        else:
            print("Selected column not found in data")

    def remove_nulls(self):
        if global_edited_data is None:
            edited_data = self.data.copy()
        else:
            edited_data = global_edited_data.copy()

        if self.selected_column in edited_data.columns:
            edited_data = edited_data.dropna(subset=[self.selected_column])
            print("Nulls removed from column:", self.selected_column)
            print(edited_data.head())
            self.apply_edits(edited_data)
        else:
            print("Selected column not found in data")

    def save_csv(self):
        if global_edited_data is None:
            print("No edits performed yet.")
            return

        print("Select where to save the CSV file:")
        print("1. Current working directory")
        print("2. Custom path")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            output_file = input("Enter the filename to save in the current working directory: ")
        elif choice == '2':
            output_dir = input("Enter the path to save the CSV file: ")
            output_file = os.path.join(output_dir, input("Enter the filename: "))
        else:
            print("Invalid choice.")
            return

        global_edited_data.to_csv(output_file, index=False)
        print("DataFrame saved to CSV file:", output_file)

if __name__ == "__main__":
    app = DataAnalyzerApp()
    file_path = input("Enter the path to the CSV file: ")
    app.load_csv(file_path)

    while True:
        print("\nSelect an option:")
        print("1. Sort data by column")
        print("2. Aggregate data by column")
        print("3. Convert column to datetime")
        print("4. Remove nulls from column")
        print("5. Save edited DataFrame as CSV")
        print("6. Exit")

        option = input("Enter your choice (1-6): ")

        if option == '1':
            app.selected_column = input("Enter the column to sort by: ")
            app.sort_data()
        elif option == '2':
            app.selected_column = input("Enter the column to aggregate by: ")
            app.aggregate_data()
        elif option == '3':
            app.selected_column = input("Enter the column to convert to datetime: ")
            app.convert_to_datetime()
        elif option == '4':
            app.selected_column = input("Enter the column to remove nulls from: ")
            app.remove_nulls()
        elif option == '5':
            app.save_csv()
        elif option == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 6.")

    print("Total edits performed:", total_edits)
