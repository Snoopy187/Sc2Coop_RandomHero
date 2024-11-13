import random
import datetime
from collections import Counter

# Define the mapping from numbers to Starcraft 2 Co-op Commanders
# Missing commanders: Tychus, Mengsk, Stratman, Alarak, Han & Horner & Dehaka due to not being max lvl or not purchased
characters = {
    1: "Jim Raynor",
    2: "Kerrigan",
    3: "Artanis",
    4: "Swann",
    5: "Zagara",
    6: "Vorazun",
    7: "Karax",
    8: "Abathur",
    9: "Nova",
    10: "Stukov",
    11: "Fenix"
}

# Function to find the most common number and map it to a string if needed
def find_most_common_number(num_range, count, mapping=None):
    while True:
        # Generate and store the random numbers in a list
        random_numbers = [random.randint(1, num_range) for _ in range(count)]
        print('A set of random numbers:', random_numbers)

        # Use Counter to count the occurrences of each number
        number_counts = Counter(random_numbers)
        # print('Number and the counts:', number_counts)

        # Find the most common numbers and their counts
        most_common = number_counts.most_common()
        # print('Most common number & how many times it occurred:', most_common)

        # Get the highest count
        most_common_count = most_common[0][1]

        # Find all numbers with the most common count
        most_common_numbers = [num for num, cnt in most_common if cnt == most_common_count]
        # print('Most common numbers:', most_common_numbers, 'and count:', most_common_count)

        # If there's only one most common number, break the loop
        if len(most_common_numbers) == 1:
            most_common_number = most_common_numbers[0]
            # Map the most common number to its corresponding string if a mapping is provided
            mapped_value = mapping.get(most_common_number, str(most_common_number)) if mapping else str(most_common_number)
            return mapped_value, most_common_count

# Parameters for the first set
num_range1 = 11 # Number of Heros

while True:
    try:
        count1 = int(input("How many numbers do you want to generate? "))
        if count1 > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

most_common_number1 = find_most_common_number(num_range1, count1, mapping=characters)

# Print the most common number and its count for the first set
print(f"The commander you have been selected is {most_common_number1}.\n")

# Parameters for the second set
num_range2 = 3 # Prestige Levels
count2 = 3 # Generating 3 numbers
most_common_number2 = find_most_common_number(num_range2, count2)

# Print the most common number and its count for the second set
print(f"The prestige talent is the {most_common_number2} option.")