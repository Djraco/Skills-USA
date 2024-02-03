import sys
import math
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QFileDialog

data = {}  # Your data dictionary
averages = []  # List to store average base profiles

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Data Presentation')
        self.setGeometry(10, 10, 800, 600)

        # Create a QPushButton to load data from a file
        self.loadButton = QPushButton('Load Data', self)
        self.loadButton.setGeometry(50, 20, 100, 30)
        self.loadButton.clicked.connect(self.load_data)

        # Create a QTableWidget to display the data
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 70, 640, 480)

        # Enable sorting when header is clicked
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

        # Set the number of rows and columns in the table
        num_rows = len(data)
        num_columns = 6  # Assuming there are 6 columns in your data (Candidate, Personality, Creativity, Detail, TeamWork, Average)

        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_columns)

        # Set the column headers
        column_headers = ["Candidate", "Personality", "Creativity", "Detail", "TeamWork", "Average"]
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        # Populate the table with data from the dictionary and 'averages' list
        row = 0
        for candidate, values in data.items():
            self.tableWidget.setItem(row, 0, QTableWidgetItem(candidate))
            for col, value in enumerate(values):
                self.tableWidget.setItem(row, col + 1, QTableWidgetItem(str(value)))
            self.tableWidget.setItem(row, num_columns - 1, QTableWidgetItem(str(averages[row])))  # Set the "Average" column
            row += 1

    def load_data(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        # Open a file dialog to select the data file
        file_path, _ = QFileDialog.getOpenFileName(self, "Load Data File", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_path:
            read_and_process_data(file_path)
            self.update_table()

    def update_table(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)  # Clear the table

        # Set the number of rows and columns in the table
        num_rows = len(data)
        num_columns = 6  # Assuming there are 6 columns in your data (Candidate, Personality, Creativity, Detail, TeamWork, Average)

        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_columns)

        # Set the column headers
        column_headers = ["Candidate", "Personality", "Creativity", "Detail", "TeamWork", "Average"]
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        # Populate the table with data from the dictionary and 'averages' list
        row = 0
        for candidate, values in data.items():      
            self.tableWidget.setItem(row, 0, QTableWidgetItem(candidate))
            for col, value in enumerate(values):
                self.tableWidget.setItem(row, col + 1, QTableWidgetItem(str(value)))
            self.tableWidget.setItem(row, num_columns - 1, QTableWidgetItem(str(averages[row])))  # Set the "Average" column
            row += 1

def read_and_process_data(file_path):
    global data
    global averages

    data = {}  # Reset the data dictionary
    averages = []  # Reset the averages list

    with open(file_path, 'r') as file:
        lines = file.readlines()

    def sign(x): #sign function. Helps with the creativity^2 rule.
        return (x > 0) - (x < 0)

    current_candidate = None

    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespaces
        if line.startswith('Candidate'):
            # Extract the candidate name from the line
            current_candidate = line.split()[1]
            data[current_candidate] = []
        elif line and current_candidate:
            # Split the line into a list of integers and append it to the current candidate's data
            candidate_data = list(map(int, line.split(',')))
            del candidate_data[0]  # Remove the "time" column
        
            # Send the data to the processing function)
            data[current_candidate].append(candidate_data)

    # Converts each set of scores for each candidate to the base profile
    for candidate in data:
        base_profiles = []  # Initialize a list to store base profiles for this candidate
        for scores in data[candidate]:
            personality = scores[0] - 5
            creativity = scores[1] - 5
            detail = scores[2] - 5
            teamWork = scores[3] - 5

            base_profile = round(math.sqrt(abs(
                2 * personality + 
                sign(creativity) * pow(creativity, 2) + 
                2 * detail + 
                (3 * teamWork - creativity)
                )), 2)
            
            base_profiles.append(base_profile)  # Append the base_profile to the list
        data[candidate] = base_profiles  # Store the list of base profiles for this candidate

    # Calculate average base profiles and store them in the 'averages' list
    for candidate in data:
        if data[candidate]:  # Check if the list is not empty
            average = sum(data[candidate]) / len(data[candidate])
            averages.append(round(average, 2))
        else:
            averages.append(0.0)  # Set the average to 0.0 if the list is empty

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
