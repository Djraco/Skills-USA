import math
import sys
from tkinter import filedialog as fd

debug = True # Prints each step to console when true

data = {}
lines = list()

def get_file():
    filename = fd.askopenfilename()

    with open(filename, 'r') as file:
        lines.append(file.readlines())
       # print(type(file.readlines()))
        

def sign(x): #sign function. Helps with the creativity^2 rule.
    return (x > 0) - (x < 0)

def error(msg, exit):
    print(f"ERROR: {msg}")
    if exit: sys.exit()

def format_data(data):
    current_candidate = None

    for line in lines[0]:
        line = str(line).strip()  # Remove leading/trailing whitespaces
        
        if debug: print(line)

        if line.startswith('Candidate'):
        # Extract the candidate name from the line
            current_candidate = line.split()[1]
            data[current_candidate] = []
        elif line and current_candidate:
            try: 
                # Split the line into a list of integers and append it to the current candidate's data
                candidate_data = list(map(int, line.split(','))) 
            except:
                error("Expected all scores to be intergers 0-9.", True)
                
            del candidate_data[0]  # Remove the "time" column

            if len(candidate_data) != 4:
                error("Expected four personality traits for each attempt.", True)
            
            for trait in candidate_data:
                if trait<0 or trait>9:
                    error("Expected all scores to be intergers 0-9.", True)       

            # Add the formatted data to the dictionary
            data[current_candidate].append(candidate_data)

    if debug: print(f"Formatted data:\n{data}\n")


# Converts each set of traits for each candidate to the base profile
def process_data(data):
    for candidate in data:
        i = 0
        for traits in data[candidate]:
            personality = traits[0] - 5
            creativity = traits[1] - 5
            detail = traits[2] - 5
            teamWork = traits[3] - 5

            # Convert traits to base profiles and rounded to the second decimal
            base_profiles = round(math.sqrt(abs(
                2 * personality + 
                sign(creativity) * pow(creativity, 2) + 
                2 * detail + 
                (3 * teamWork - creativity)
                )), 2)
            
            # Rewrite the traits as base profiles
            data[candidate][i] = base_profiles
            i += 1
    if debug: print(f"Processed data:\n{data}\n")

# Averages each attempt to get one final base profile number for each candidate
def average_data(data):
    for candidate in data:

        average = 0
        i = 0
        for base_profile in data[candidate]:
            average += base_profile
            i += 1
        try:
            average /= i
        except:
            error(f"Candidate '{candidate}' has no data.", True)
        data[candidate] = round(average, 2)
    if debug: print(f"Averaged data:\n{data}\n")



get_file()

format_data(data)

process_data(data)

average_data(data)

# Sort the data by lowest to highest
data = dict(sorted(data.items(), key=lambda x:x[1]))
if debug: print(f"Sorted data: \n{data}\n")