import math

# Define a dictionary to store data for each candidate
base_profiles = {}

def sign(x): #sign function. Helps with the creativity^2 rule.
    return (x > 0) - (x < 0)

# Define a function to process each line of data
def process_line(name, data):
    personality = data[0] - 5
    creativity = data[1] - 5
    detail = data[2] - 5
    teamWork = data[3] - 5

    base_profile = round(math.sqrt(abs(
        2 * personality + 
        sign(creativity) * pow(creativity, 2) + 
        2 * detail + 
        (3 * teamWork - creativity)
        )), 2)
    
    base_profiles[name].append(base_profile)
   # print(f"Processing data for {name}: {data}. Base Profile: {base_profile}")

# Open the text file for reading
with open('data.txt', 'r') as file:
    lines = file.readlines()

# Initialize a variable to keep track of the current candidate
current_candidate = None

# Iterate through each line in the file
for line in lines:
    line = line.strip()  # Remove leading/trailing whitespaces
    if line.startswith('Candidate'):
        # Extract the candidate name from the line
        current_candidate = line.split()[1]
        base_profiles[current_candidate] = []
    elif line and current_candidate:
        # Split the line into a list of integers and append it to the current candidate's data
        data = list(map(int, line.split(',')))
        del data[0]  # Remove the "time" column
        
        # Send the data to the processing function
        process_line(current_candidate, data)

print(base_profiles[str(list(base_profiles)[0])])

average = 0
for v in base_profiles[str(list(base_profiles)[0])]:
    average += v
average /= len(base_profiles[str(list(base_profiles)[0])])

print(average)