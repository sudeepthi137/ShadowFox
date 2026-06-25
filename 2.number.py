
#1
def format_number(number, format_type):
    formatted_value = format(number, format_type)
    return formatted_value
result = format_number(145, 'o')
print("Formatted value:", result)
#The format specifier 'o' converts the decimal number 145 into its octal (base 8) representation.
#2
radius = 84
pi = 3.14
water_per_square_meter = 1.4
area = pi * radius * radius
total_water = area * water_per_square_meter
print("Area of the pond:", area)
print("Total water in the pond:", int(total_water))
#3
distance = 490  
time_in_minutes = 7
time_in_seconds = time_in_minutes * 60
speed = distance / time_in_seconds
print("Speed:", int(speed), "m/s")
