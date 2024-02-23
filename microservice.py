import csv
import random

def readNames(filename):
    names = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            names.append((row['nameFirst'], row['nameLast']))
    return names

def generate_random_name(names):
    first_name, last_name = random.choice(names)
    return f"{first_name} {last_name}"

if __name__ == "__main__":
    filename = "people.csv"
    names = readNames(filename)
    if names:
        random_name = generate_random_name(names)
        print("Randomly generated name:", random_name)
    else:
        print("No names found in the CSV file.")
