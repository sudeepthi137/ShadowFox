#1)
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

# Calculate BMI
BMI = weight / (height ** 2)

# Determine BMI Category
if BMI >= 30:
    category = "Obesity"
elif BMI >= 25:
    category = "Overweight"
elif BMI >= 18.5:
    category = "Normal"
else:
    category = "Underweight"

# Display result
print(category)


#2)
# Lists of cities per country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Ask the user to enter a city name
city = input("Enter a city name: ")

# Check which country the city belongs to
if city in Australia:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print(f"Sorry, {city} is not in the list.")



#3)
# Lists of cities per country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Ask the user to enter two cities
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Function to find the country of a city
def find_country(city):
    if city in Australia:
        return "Australia"
    elif city in UAE:
        return "UAE"
    elif city in India:
        return "India"
    else:
        return None

# Get countries for both cities
country1 = find_country(city1)
country2 = find_country(city2)

# Compare and print result
if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the list.")




