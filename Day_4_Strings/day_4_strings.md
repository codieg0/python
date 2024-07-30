# Strings
A string is a text data type. Any data under single, double or triple quotes are strings.
```
letter = 'P'
print(letter)
P
```
This would be a **multiline** string example:
```py
>>> multiline_sting = '''This is
... a multiline string
... so we can divide a string
... in multiple lines'''
>>> print(multiline_string)
 this is a \ multiline string nd it can be done \in multiple lines
```

## String contatenation
We can connect string together. See the example below:
```py
first_name = 'Diego'
last_name = 'C'
print(f'{first_name} {last_name})
```
## Escape sequence
In Python and other programming languages \ followed by a character is an escape sequence. The most common escape characters below:
```bash
/n: new line
/t: Tab (8 spaces)
\\: Back slash
\': Single quote
\": Double quote
```
We can see some examples:
```py
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote
```

## String formatting
