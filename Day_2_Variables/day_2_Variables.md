# Built-in functions
For all bult-in functions click [**here**](https://docs.python.org/3.9/library/functions.html)

There are a few bult-in functions in Python.
- print()
    ```py
    name = 'Diego'
    print(name)
    ```
- len() -> this will print the number of characters of a string
    ```py
    >>> name
    'Diego'
    >>> print(len(name))
    5
    ```
- int() -> returns an integer
    ```py
    >>> number = 3.14 
    >>> print(int(number))
    3
    ```
- float() -> returns a float
    ```py
    >>> number = 4
    >>> print(float(number))
    4.0
    ```
- str() -> returns a string
    ```py
    >>> test = 45
    >>> type(test)
    <class 'int'>
    >>> type(str(test))
    <class 'str'>
    ```
- input() -> allows user input
    ```py
    >>> name = input('What\'s your name: ')
    What's your name: Eva
    >>> print(name)
    Eva
    ```
 - list() -> returns a list
    ```py
    >>> text = 'Diego'
    >>> list_text = list(text)
    >>> print(list_text)
    ['D', 'i', 'e', 'g', 'o']
    ```
- dict() -> returns a dictionary
    ```py
    >>> dict_list = dict(name = 'Commander Evush', age = 42, isEvaDelicious = True, heightInCms = 1.60)
    >>> print(dict_list)
    {'name': 'Commander Evush', 'age': 42, 'isEvaDelicious': True, 'heightInCms': 1.6}
    ```
- min() -> this will return the minimum number
    ```py
    >>> number1 = 4
    >>> number2 = 3.5645
    >>> number3 = 10
    >>> number4 = 519.42
    >>> min(number1, number2, number3, number4)
    3.5645
    ```
- max() -> returns the max number
    ```py
    >>> number1 = 4
    >>> number2 = 3.5645
    >>> number3 = 10
    >>> number4 = 519.42
    >>> max(number1, number2, number3, number4)
    519.42
    ```
- sum() -> returns the sum of all the numbers
    ```py
    >>> number1 = 4
    >>> number2 = 3.5645
    >>> number3 = 10
    >>> number4 = 519.42
    >>> list_numbers = [number1, number2, number3, number4]
    >>> sum(list_numbers)
    536.9844999999999
    ```
- sorted() -> it is a method to sort all the elements in ascending order
```py
    >>> number1 = 4
    >>> number2 = 3.5645
    >>> number3 = 10
    >>> number4 = 519.42
    >>> list_numbers = [number1, number2, number3, number4]
    >>> sorted(list_numbers)
    [3.5645, 4, 10, 519.42]
```
- help() -> shows the info of a funtion
    ```py
    >>> help(list)
    Help on class list in module builtins:

    class list(object)
    |  list(iterable=(), /)
    |
    |  Built-in mutable sequence.
    |
    |  If no argument is given, the constructor creates a new empty list.
    |  The argument must be an iterable if specified.
    ```

# Variables
A variable refers to a memory address in which data is stored. <br>
These are some rules for the name of variables:
- A variable name must start with a letter or the underscore character _
- A variable name cannot start with a number
- A variable can only contain alpha-numeric characters and undescores (A-z, 0-9, and _ )
- Variable names are case-sensitive (first_name, Firstname, FirstName, FIRSTNAME)