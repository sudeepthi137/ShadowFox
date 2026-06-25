#1)
import random

# Number of rolls
num_rolls = 20

# Counters
count_6 = 0
count_1 = 0
count_two_6s = 0

# Previous roll tracker
previous_roll = None

# Simulate rolling the die
for i in range(num_rolls):
    roll = random.randint(1, 6)  # roll between 1 and 6
    
    # Count 6s and 1s
    if roll == 6:
        count_6 += 1
    if roll == 1:
        count_1 += 1
    
    # Check for two 6s in a row
    if roll == 6 and previous_roll == 6:
        count_two_6s += 1
    
    # Update previous roll
    previous_roll = roll

# Print results
print(f"Total rolls: {num_rolls}")
print(f"Number of times rolled a 6: {count_6}")
print(f"Number of times rolled a 1: {count_1}")
print(f"Number of times rolled two 6s in a row: {count_two_6s}")

#2
completed = 0

while completed < 100:
    print("Do 10 jumping jacks!")
    completed += 10

    tired = input("Are you tired? (yes/no): ").lower()

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()

        if skip == "yes" or skip == "y":
            print("You completed a total of", completed, "jumping jacks.")
            break

    remaining = 100 - completed

    if remaining > 0:
        print(remaining, "jumping jacks remaining.")
    else:
        print("Congratulations! You completed the workout!")