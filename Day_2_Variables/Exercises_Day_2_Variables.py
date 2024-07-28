'''
Exercises: Level 1

Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
Write a python comment saying 'Day 2: 30 Days of python programming'

- Declare a first name variable and assign a value to it
- Declare a last name variable and assign a value to it
- Declare a full name variable and assign a value to it
- Declare a country variable and assign a value to it
- Declare a city variable and assign a value to it
- Declare an age variable and assign a value to it
- Declare a year variable and assign a value to it
- Declare a variable is_married and assign a value to it
- Declare a variable is_true and assign a value to it
- Declare a variable is_light_on and assign a value to it
- Declare multiple variable on one line
'''
first_name = 'Diego'
last_name = 'Costra'
full_name = first_name + last_name
country = 'Ireland'
city = 'Cork'
age = 25
year = 2024
is_married = True
is_true = True
is_light_on = False
Diego_wife_name, Diego_wife_height_in_cm = 'Evush',  1.60

'''
Exercises: Level 2

- Check the data type of all your variables using type() built-in function
- Using the len() built-in function, find the length of your first name
- Compare the length of your first name and your last name
- Declare 5 as num_one and 4 as num_two
        * Add num_one and num_two and assign the value to a variable total
        * Subtract num_two from num_one and assign the value to a variable diff
        * Multiply num_two and num_one and assign the value to a variable product
        * Divide num_one by num_two and assign the value to a variable division
        * Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
        * Calculate num_one to the power of num_two and assign the value to a variable exp
        * Find floor division of num_one by num_two and assign the value to a variable floor_division
 -The radius of a circle is 30 meters.
        * Calculate the area of a circle and assign the value to a variable name of area_of_circle
        * Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
        * Take radius as user input and calculate the area.
- Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
- Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
'''
# Printing type
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(Diego_wife_name))
print(type(Diego_wife_height_in_cm))

# Printing length
print(len(first_name))
print(len(last_name))
print(len(full_name))
print(len(country))
print(len(city))
# print(len(age)) -> no len for int
# print(len(year))
#print(len(is_married)) -> no len for boll
#print(len(is_true))
#print(len(is_light_on))
print(len(Diego_wife_name))
#print(len(Diego_wife_height_in_cm))

# Comparing length of first_name and last_name
print(len(first_name))
print(len(last_name))

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

sum_nums = sum(int((num_one, num_two)))
sub_nums = num_two - num_one
multiply_nums = num_one * num_two
divide_nums = num_one / num_two
modulus_nums = num_two % num_one
power_nums = num_one ** num_two
floor_div_nums = num_one // num_two

# Radius of a circle is 30 meters. Calculate area and circumference
radius = 30
pi = 3.14
area_circle = pi * (radius)**2
print(area_circle)

circumference_circle = 2 * pi * radius
print(circumference_circle)

# Now the same but we ask the user
new_radius = input("Please enter an integer: ")
area_circle = pi  *  int((new_radius))**2
print(f"The new area is : {new_radius}")
new_circumference_circle = 2 * pi * float(new_radius)
print(f"The new circumference is {new_circumference_circle}")

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

name = input("What's your name: ")
last_name = input("What's your last name: ")
country = input("What's your country: ")
age = input("What's your age: ")
list_user = [name, last_name, country, age]

print (list_user)