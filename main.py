import pandas as pd

class DataAnalyzerApp:
    def __init__(self):
        self.data = None
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

    def sort_data(self):
        if self.data is not None:
            if self.selected_column in self.data.columns:
                self.data.sort_values(by=self.selected_column, inplace=True)
                print("Data sorted by column:", self.selected_column)
                print(self.data.head())
            else:
                print("Selected column not found in data")

    def aggregate_data(self):
        if self.data is not None:
            if self.selected_column in self.data.columns:
                aggregated_data = self.data.groupby(self.selected_column).size().reset_index(name='count')
                print("Aggregated data by column:", self.selected_column)
                print(aggregated_data)
            else:
                print("Selected column not found in data")

    def convert_to_datetime(self):
        if self.data is not None:
            if self.selected_column in self.data.columns:
                self.data[self.selected_column] = pd.to_datetime(self.data[self.selected_column])
                print("Converted column to datetime:", self.selected_column)
                print(self.data.head())
            else:
                print("Selected column not found in data")

if __name__ == "__main__":
    app = DataAnalyzerApp()
    file_path = input("Enter the path to the CSV file: ")
    app.load_csv(file_path)

    while True:
        print("\nSelect an option:")
        print("1. Sort data by column")
        print("2. Aggregate data by column")
        print("3. Convert column to datetime")
        print("4. Exit")

        option = input("Enter your choice (1-4): ")

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
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.")
