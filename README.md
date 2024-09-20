This repository contains a collection of Python functions and a class that demonstrate basic programming concepts such as functions, decorators, sequences, sets, dictionaries, and object-oriented programming. Each function is designed to perform specific tasks, while the class encapsulates data and behavior related to a car.
Table of Contents
Functions
add_numbers
is_even
reverse_string
count_vowels
calculate_factorial
apply_decorator
sort_by_age
merge_dicts
Object-Oriented Programming
Car Class
Usage Examples
License
Functions
add_numbers(num1, num2)
Returns the sum of two numbers.
Parameters:
num1: First number (int or float).
num2: Second number (int or float).
Returns:
The sum of num1 and num2.
is_even(number)
Checks if a number is even.
Parameters:
number: An integer to check.
Returns:
True if the number is even, otherwise False.
reverse_string(text)
Reverses a given string.
Parameters:
text: The string to reverse.
Returns:
The reversed string.
count_vowels(text)
Counts the number of vowels in a string.
Parameters:
text: The string to analyze.
Returns:
The count of vowels (a, e, i, o, u) in the string (case insensitive).
calculate_factorial(n)
Calculates the factorial of a non-negative integer.
Parameters:
n: A non-negative integer.
Returns:
The factorial of n.
apply_decorator(func)
Applies a simple decorator that prints a message before executing the function.
Parameters:
func: The function to decorate.
Returns:
The result of the decorated function call.
sort_by_age(tuples_list)
Sorts a list of tuples by age in ascending order.
Parameters:
tuples_list: A list of tuples where each tuple contains a name and an age.
Returns:
A sorted list of tuples by age.
merge_dicts(dict1, dict2)
Merges two dictionaries, summing values for common keys.
Parameters:
dict1: The first dictionary.
dict2: The second dictionary.
Returns:
A merged dictionary with summed values for common keys.
Object-Oriented Programming
Car Class
Class Definition
python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")

Attributes:
make: The manufacturer of the car.
model: The model name of the car.
year: The year the car was manufactured.
Methods:
display_info(): Prints out the car's information.