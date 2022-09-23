'''
    This program asks the user for a number.
    Whether is odd or even.
'''

num = int(input("Please enter a integer: "))

# num = num / 2

if (num % 2) == 0:
    print("That's an even number")
else:
    print("That's an odd number")