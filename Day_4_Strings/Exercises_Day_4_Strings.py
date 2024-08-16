# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string_one = 'Thirty'
string_two = 'Days'
string_three = 'Of'
string_four = 'Python'
print(f'{string_one} {string_two} {string_three} {string_four}!')

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string_uno = 'Coding'
string_dos = 'For'
string_tres = 'All'
print(f'{string_uno} {string_dos} {string_tres}')

# Declare a variable named company and assign it to an initial value "Coding For All".
full_sentence = string_uno + ' ' + string_dos + ' ' + string_tres
print(full_sentence)

# Print the length of the company string using len() method and print().
print(len(full_sentence))

# Change all the characters to uppercase letters using upper() method.
new_upper_sentence = full_sentence.upper()
print(new_upper_sentence)

# Change all the characters to lowercase letters using lower() method.
low_full_sentence = new_upper_sentence.lower()
print(low_full_sentence)

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
capital_sentence = full_sentence.capitalize()
print(capital_sentence)

title_sentence = full_sentence.title() # This will set capital the first character of all the words
print(title_sentence)

swap_test = full_sentence.swapcase()
print(swap_test)

# Cut(slice) out the first word of Coding For All string.
sliced_sentence = slice(6)
print(full_sentence[sliced_sentence])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
another_sentence = ['Coding', 'For', 'All']
check_word_coding = another_sentence.index('Coding')
print(check_word_coding)

# Replace the word coding in the string 'Coding For All' to Python.
another_sentence[0]  = 'Python'
print(another_sentence)

# Change Python for Everyone to Python for All using the replace method or other methods.

string = 'Python for Everyone'
new_string = string.replace('Everyone', 'All')
print(new_string)

# Split the string 'Coding For All' using space as the separator (split()) .
split_string = new_string.split()
print(split_string)
 
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
fang_list = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'

# What is the character at index 0 in the string Coding For All.
coding_string = 'Coding'
print(coding_string[0])

 # What character is at index 10 in "Coding For All" string.
print(split_string[-1])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
string_python = 'Python'
string_for = 'For'
string_everyone = 'Everyone'
print(string_python[0])
print(string_for[0])
print(string_everyone[0])

# Use index to determine the position of the first occurrence of C in Coding For All.
string_coding = 'Coding For All'
print(string_coding.index('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.
print(string_coding.index('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
string_code_people = 'Coding For All People'
print(string_code_people.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

word_because = 'You cannot end a sentence with because because because is a conjunction'
print(word_because.find('because'))
print(word_because.index('because'))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(word_because.rindex('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(word_because[31:54])
# print(word_because.index('h'))
# print(word_because.index('is'))

# Does ''Coding For All' start with a substring Coding?
print(string_coding[0:6] == 'Coding')
'''
I was confusing with == and is

The “is” keyword is used to compare the variables and string whether they are pointing to the same object or not. If both the variables (var1 and var2) refer to the same object, they will have the same ID. 

The “==” operator will compare both the variables whether their values refer to the same object or not.
'''

# Does 'Coding For All' end with a substring coding?
print(string_coding[-1] == 'g')

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
str_coding_spaces = '   Coding For All      ' 
print(str_coding_spaces)
print(str_coding_spaces.strip(' '))

# Which one of the following variables return True when we use the method isidentifier():
st_one = '30DaysOfPython'
st_two = 'thirty_days_of_python'

print(st_one.isidentifier())
print(st_two.isidentifier())

# Use the new line escape sequence to separate the following sentences.

ex_one = 'I am enjoying this challenge'
ex_two= 'I just wonder what is next.'