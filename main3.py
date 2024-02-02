import math

data = {}

with open('data.txt', 'r') as file:
    lines = file.readlines()

def sign(x): #sign function. Helps with the creativity^2 rule.
    return (x > 0) - (x < 0)

def format_data(data):
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
def process_data(data):
    for candidate in data:
        i = 0
        for scores in data[candidate]:
            personality = scores[0] - 5
            creativity = scores[1] - 5
            detail = scores[2] - 5
            teamWork = scores[3] - 5

            base_profiles = round(math.sqrt(abs(
                2 * personality + 
                sign(creativity) * pow(creativity, 2) + 
                2 * detail + 
                (3 * teamWork - creativity)
                )), 2)
            
            data[candidate][i] = base_profiles
            i += 1

def average_base_profiles(data):
    for candidate in data:

        average = 0
        i = 0
        for base_profile in data[candidate]:
            average += base_profile
            i += 1
        average /= i
        data[candidate] = round(average, 2)


#read_file()

format_data(data)

print(f"Formatted data:\n{data}\n")

process_data(data)

print(f"Processed data:\n{data}\n")

average_base_profiles(data)

print(f"Averaged base profiles:\n{data}\n")