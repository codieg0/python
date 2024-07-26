#!/bin/usr/env python

'''
Exercise: Level 1

1. Check the python version you are using
$ python3 --version
Python 3.12.3
'''
'''
2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
    - addition(+)
    - subtraction(-)
    - multiplication(*)
    - modulus(%)
    - division(/)
    - exponential(**)
    - floor division operator(//)
'''
print(2+3)
print(3-1)
print(3*2)
print(5%2)
print(5/2)
print(2**6)
print(6//2)

'''
3. Write strings on the python interactive shell. The strings are the following:
    - Your name
    - Your family name
    - Your country
    - I am enjoying 30 days of python
'''
name = 'Diego'
familyName = 'Castro Osorio'
country = 'Ireland'
Enjoying30DaysofPython = True
print(name, familyName, country, Enjoying30DaysofPython)

'''
4. Check the data types of the following data:
    - 10
    - 9.8
    - 3.14
    - 4 - 4j
    - ['Asabeneh', 'Python', 'Finland']
    - Your name
    - Your family name
    - Your country
'''
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 -4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(name))
print(type(familyName))
print(type(country))

'''
Exercise: Level 2

Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.

Done in the previous exercise
'''
'''
Exercise: Level 3

Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
Find an Euclidian distance between (2, 3) and (10, 8)
'''
text = 'My name is Diego'
age = 28
isDiegoMarried = True
DiegoSkills = ['Git', 'Github', 'SMTP', 'Log analysis', 'Linux']
time100Completion = 6.7

# Find an Euclidian distance between (2, 3) and (10, 8)
# Formula -> distance = ((x1-x2)+(y1-y2)) **(1/2)
x1 = 2
y1 = 3
x2 = 10
y2 = 8

distance = ((x1-x2)**2+(y1-y2)**2) **(1/2)
print(distance)