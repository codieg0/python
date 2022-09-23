# The goal of this game is using a different sentence every time the script is executed.
# The Mad Lib will have 1 noun, 1 verb, and 1 adjective
# the full sentence will show after the user input the noun, verb, and adjective.

import time
from time import sleep

# Asking for the name
userName = input(str("What is your name: "))

# Greetings
print("Getting your name... Please, bear with me!")
print("...")
sleep(1)
print("...")
sleep(1)

print(f"Welcome to Mad Libs, {userName}!. Hope you have fun!")

print("The goal of the game is to get a verb, a noun/s, and a adjective to get crazy sentences.")

# Asking the user whether they want to play or not
ready = input(str("Ready to play? [Y/n]: "))

# Conditional: either yes or no
if ready.lower() in ("y", "yes"):
    adj = input(str("Enter an adjective: "))
    noun = input(str("Enter a noun: "))
    verb = input(str("Enter a verb: "))

    # Here below are the answers to the inputs

    print(f"The first five days after the weekend are the {adj}est.")

    print(f"Whenever you are right, noone {verb}s. When you are wrong, noone forgets")

    print(f"My {noun} made me join a bridge group. I {verb} off next Tuesday")

else:
    print("Okay then, see you next time...")
    print("Closing in 3...")
    sleep(1)
    print("Closing in 2...")
    sleep(1)
    print("Closing in 1...")
    sleep(1)

    print("\u1f595") # That is the code for the middle finger. Not sure why it does not work

    exit()