import csv

with open('skillsusa_problem1_candidate_data.txt', newline='') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)
        
