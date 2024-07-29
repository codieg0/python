'''
Declare your age as integer variable
Declare your height as a float variable
Declare a variable that store a complex number
'''
# age = 30
# height_in_cm = 1.60
# complex_var = 3 + 7j
'''
Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
'''
# base = int(input("Please enter the base: "))
# height_triangle = float(input("Please enter area: "))
# area_triangle = 0.5 * base * height_triangle
# print(f'The area is {area_triangle}.')
'''
Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
'''
# side_a = int(input("Please enter side a: "))
# side_b = int(input("Please enter side b: "))
# side_c = int(input("Please enter side c: "))
# perimeter_triangle = side_a + side_b + side_c
# print(f'The perimeter of the triangle is {perimeter_triangle}.')
# '''
# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
# '''
# length = int(input("Please enter length: "))
# width = int(input("Please enter width: "))
# area = length * width
# print(f'The new are is {area}.')
# perimeter = 2 * (length + width)
'''
Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
'''
# pi = 3.14
# radius = int(input("Please enter the radius: "))
# area_cirle = pi * (radius ** 2)
# print(f'The are of the circle is {area_cirle}')
# circumference_circle = 2 * pi * radius
# print(f"This is the circumference of the circle - {circumference_circle}")
'''
Calculate the slope, x-intercept and y-intercept of y = 2x -2
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
Compare the slopes in tasks 8 and 9.
'''
# x1 = 2
# x2 = 2
# y1 = 6
# y2 = 10
# y = y2 - y1
# x = x2 - x1
# slope_is = y / x
# if x == 0:
#     print("Not possible to divide by 0.")
# else:
#     print(f'The slope value is {slope_is}')
'''
Find the length of 'python' and 'dragon' and make a falsy comparison statement.
'''
# string_one = 'python'
# string_two = 'dragon'
# length_string_one = len(string_one)
# length_string_two = len(string_two)
# print(f'The length of the first string is {length_string_one}. The lenght of the second string is {length_string_two}')
# if length_string_two == length_string_one:
#     print(f"Does the length have the same value? {True}")
# else:
#     print(f'Does the length have the same value? {False}')
'''
Use and operator to check if 'on' is found in both 'python' and 'dragon'
'''
# if 'on' in (string_one and string_two) :
#     print(f"'on' is in both strings {True}")
# elif 'on' in (string_one or string_two):
#     print(f"'on' was found in either string")
# else:
#     print(f"'on' is not in either strings {False}")
'''
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
'''
# variable_text = 'I hope this course is not full of jargon'
# if 'jargon' in variable_text:
#     print("'jargon' is in the string.")
# else:
#     print("'jargon' is NOT in the string.")
'''
Find the length of the text python and convert the value to float and convert it to string
'''
# another_var = 'python'
# get_length = float(len(another_var))
# print(f'The length of the string is {get_length}')
# convert_str = str(get_length)
# print(type(convert_str))
'''
Check if type of '10' is equal to type of 10
'''
# var_number = '10'
# value_number = 10
# if type(var_number) == type(value_number):
#     print("They are the same type.")
# else:
#     print("They are not the same type.")
'''
Check if int('9.8') is equal to 10
'''
# int_test = 9.8
# print(int(int_test))
'''
Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
'''
# hours_working = float(input("How many hours have you worked? "))
# hourly_rate = float(input("What's your hourly rate? "))
# weekly_earning = hourly_rate * hours_working
# print(f'You have earned £{weekly_earning}')
# yearly_salary = 52 * weekly_earning
# print(f'This year you might be earning £{yearly_salary} gross')
'''
Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
'''
# age_total = int(input("How old are you? "))
# month_seconds = 2628288
# year_seconds = 12 * month_seconds
# totals_seconds_lived = age_total * year_seconds
# print(f'You have lived {totals_seconds_lived} seconds')
'''
Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''
number_table = [1, 2 ,3, 4, 5]
range_number = [0, 1, 2, 3]
for number_table in range_number :
    number_table[0] ** range_number[0]
    print(f"{number_table}")

    # Need to finish it later