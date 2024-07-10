# Day 2: 30 days of Python Programming

# Excercise 1 - Assigning Variables
first_name = 'Sean'
last_name = 'Harmond'
full_name = 'Sean Harmond'
country = "United States"
city = 'Pulaski'
age = 29
year = 2024
is_married = 'No'
is_true = "Yes"
is_light_on = 'Yes'
first_name, last_name, full_name = 'Sean', 'Harmond', 'United States'


# Excercise 2 
print(type(first_name)) # Str
print(type(last_name)) # Str
print(type(full_name)) # Str
print(type(country)) # Str
print(type(city)) # Str
print(type(age)) # Int
print(type(year)) # Int
print(type(is_married)) # Str
print(type(is_true)) # Str
print(type(is_light_on)) # Str

print(len(first_name)) # 4
print(len(last_name)) # 7
print(7-4) # Last name 3 characters more than first

num_one = 5
num_two = 4
variable_total = num_one + num_two
print(variable_total) # 9
variable_diff = num_one - num_two
print(variable_diff) # 1
variable_product = num_two * num_one
print(variable_product) # 20
variable_division = num_one / num_two
print(variable_division) # 1.25
variable_remainder = num_two % num_one
print(variable_remainder) # 4
variable_exp = num_one ** num_two
print(variable_exp) # 625
variable_floor_division = num_one // num_two
print(variable_floor_division) # 1

# Radius of this circle is 30 meters
area_of_circle = 3.14 * 30 ** 2
print(area_of_circle) # 2826.0
circumference_of_circle = 2 * 3.14 * 30
print(circumference_of_circle) # 188.4
radius = input('Enter the radius: ') # Asking user input for radius
area = 3.14 * float(radius) ** 2 # Have to convert string radius to float radius
print(area) # 2826.0

first_name = input("Firs Name: ")
last_name = input("Last Name: ")
country = input("Country: ")
age = input("Age: ")