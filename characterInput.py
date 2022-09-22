'''
    The program asks the user for their first name and age.
    Print a message addressed to them that tells them the year they will turn 100 yo
'''
name = input(str("What's your name?  "))
age = int(input("What's your age? "))

# Here we print the year the user will be 100 years old.
# We create a new variable and equal it to the current year - the age so that will take us to
# the year they were born and, finally, we add 100 years to obtain the year
year = 2022 - age + 100
print(f"You will be 100 years old on in {year}")

# Here we just know how many years they will need to "wait" to get 100 years old
# We just need to rest 100 years minus the current years old the user is
age = 100 - age
print(f"You would need to wait just {age} years mister/ma'an!")