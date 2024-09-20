def add_numbers(num1, num2):
     return num1 + num2


def is_even(num):
     return num % 2 == 0


def reverse_string(text):
     return text[::-1]


def count_vowels(text):
     vowels = "aeiouAEIOU"
     return sum(1 for char in text if char in vowels)


def calculate_factorial(n):
     if n < 0:
          raise ValueError("Input must be a non-negative integer")
     factorial = 1
     for i in range (1, n + 1):
          factorial *= i
     return factorial

def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    decorated_function = decorator_func(func)
    return decorated_function()



def sort_by_age(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])


def merge_dicts(dict1, dict2):
     merged = dict1.copy()
     for key, value in dict2.items():
          if key in merged:
               merged[key] += value
          else:
               merged[key] = value
     return merged


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")
     