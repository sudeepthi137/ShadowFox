
# Initial list of Justice League members
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)

# 1. Calculate the number of members
print("Number of members:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to the beginning (leader)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman leader:", justice_league)

# 4. Separate Aquaman and Flash by inserting Superman in between
justice_league.remove("Superman")  # remove Superman first
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Superman")
print("After separating Aquaman and Flash:", justice_league)

# 5. Replace with new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League:", justice_league)

# 6. Sort alphabetically
justice_league.sort()
print("Sorted Justice League:", justice_league)
print("New Leader (0th index):", justice_league[0])



#Bonus Answer:
#After sorting alphabetically, the new leader will be Cyborg because "Cyborg" comes first alphabetically.