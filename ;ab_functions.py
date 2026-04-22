# Functions Lab             ---------------------------------------------------------------------------------


# 1.  Write a function called square(n) that takes a number and returns its square.
# def square(n):
#     value = n**2
#     return value
# number = float(input("ededi daxil edin: "))
# print(square(number))
# ---------------------------------------------------------------------------------


# 2. Write a function called greet(name) that returns the string 'Hello, !'
# def greet(name):
#     str = "'Hello',"
#     str = str + " "+ name + "!"
#     return str
# print(greet("Murad"))
# ---------------------------------------------------------------------------------


# 3. Write a function called is_even(n) that returns True if n is even, False otherwise.
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(5))
# ---------------------------------------------------------------------------------


# 4. Write a function called list_sum(lst) that returns the sum of all numbers in a list. Do NOT use the built-in sum()
# def list_sum(lst):
#     cem = 0
#     for i in lst:
#         cem += i
#     return cem
# print(list_sum([1, 2, 3, 4]))
# ---------------------------------------------------------------------------------


# 5. Write a function called reverse_string(s) that returns the string in reverse order
# def reverse_string(s):
#     lst = list(s)
#     lst.reverse()
#     new_str = ("").join(lst)
#     return new_str
# print(reverse_string("Hello"))
# ---------------------------------------------------------------------------------


# 6. Write a function called count_vowels(s) that counts and returns the number of vowels (a, e, i, o, u) in a string. It should be case-insensitive.
# def count_vowels(s):
#     count = 0
#     s = s.lower()
#     vowels = "aıoueəiöü"
#     for i in s:
#         if i in vowels:
#             count += 1
#     return count
# print(count_vowels("Hello"))
# ---------------------------------------------------------------------------------


# 7. Write a function called find_max(lst) that returns the largest number in a list. Do NOT use the built-in max().
# def find_max(lst):
#     max = lst[0]
#     for i in lst:
#         if i > max:
#             max = i
#     return max
# print(find_max([3, 1, 7, 2]))
# ---------------------------------------------------------------------------------


# 8. Write a function called celsius_to_fahrenheit(c) that converts Celsius to Fahrenheit. Formula: F = C * 9/5 + 32
# def celsius_to_fahranheit(c):
#     f = c * (9 / 5) + 32
#     return f
# print(celsius_to_fahranheit(100))
# ---------------------------------------------------------------------------------


# 9. Write a function called is_palindrome(s) that returns True if the string reads the same forwards and backwards (case-insensitive), False otherwise.
# def is_palindrome(s):
#     s = s.lower()
#     lst = list(s)
#     lst.reverse()
#     new_str=("").join(lst)
#     if s==new_str:
#         return True
#     else:
#         return False
# print(is_palindrome("Racecar"))
# ---------------------------------------------------------------------------------


# 10. Write a function called fizzbuzz(n) that returns 'Fizz' if n is divisible by 3, 'Buzz' if divisible by 5, 'FizzBuzz' if both, otherwise returns n as a string
# def fizzbuzz(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return "FizzBuzz"
#     elif n % 3 == 0:
#         return "Fizz"
#     elif n % 5 == 0:
#         return "Buzz"
#     else:
#         return str(n)
# print(fizzbuzz(8))
# ---------------------------------------------------------------------------------


# 11. Write a recursive function called factorial(n) that returns n factorial. Assume n >= 0.
# def factorial(n):
#     if n == 0:
#         return 1
#     h = n * factorial(n - 1)
#     return h
# print(factorial(6))
# ---------------------------------------------------------------------------------


# 12. Write a function called flatten(lst) that takes a list with one level of nesting and returns a flat list.
# def flatten(lst):
#     new_lst = []
#     for i in lst:
#         if type(i) == list:
#             for j in i:
#                 new_lst.append(j)
#         else:
#             new_lst.append(i)
#     return new_lst
# print(flatten([1, [2, 3][4, 5], 6]))
# ---------------------------------------------------------------------------------


# 13. Write a function called word_freq(text) that returns a dictionary where each key is a word and its value is how many times it appears (case-insensitive).
# def word_freq(text):
#     count = {}
#     lst = text.lower().split(" ")
#     for i in lst:
#         if i in count:
#             count[i] += 1
#         else:
#             count[i] = 1
#     return count
# print(word_freq("hi hi hello"))
# ---------------------------------------------------------------------------------


# 14. Write a function called binary_search(lst, target) that returns the index of target in a sorted list, or -1 if not found.
# def binary_search(lst, target):
#     for i in lst:
#         if i == target:
#             return lst.index(target)
#         else:
#             return -1
# print(binary_search([1, 3, 5, 7, 9], 5))
# ---------------------------------------------------------------------------------


# 15. Write a function called caesar(text, shift) that encodes a string by shifting each letter by shift positions. Non-letter characters must stay unchanged.
# def caesar(text, shift):
#     upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     lower = "abcdefghijklmnopqrstuvwxyz"
#     result = ""
#     for char in text:
#         if char in upper:
#             index = upper.index(char)
#             result += upper[(index + shift) % 26]
#         elif char in lower:
#             index = lower.index(char)
#             result += lower[(index + shift) % 26]
#         else:
#             result += char
#     return result
# print(caesar("Hello, World!", 3))
# ---------------------------------------------------------------------------------


# 16. Write a function called make_counter(start=0) that returns a function. Every time the returned function is called, it increments by 1 and returns the new count.
# def make_counter(start=0):
#     count = start
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter
# c1 = make_counter()
# print(c1())
# print(c1())
# ---------------------------------------------------------------------------------


# 17. Write a function called fib(n) that returns the n-th Fibonacci number using memoization for efficiency
# def fib(n):
#     sum = 0
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     a = 0
#     b = 1
#     for i in range(2, n + 1):
#         sum = a + b
#         a = b
#         b = sum
#     return b
# print(fib(10))
# ---------------------------------------------------------------------------------


# 18. Write a function called group_by(lst, key_func) that groups the items of lst into a dictionary based on the result of key_func applied to each item.
# def group_by(lst, key_func):
#     result = {}
#     for item in lst:
#         key = key_func(item)
#         if key in result:
#             result[key].append(item)
#         else:
#             result[key] = [item]
#     return result
# print(group_by([1,2,3,4,5,6], lambda x: x % 2))
# ---------------------------------------------------------------------------------


# 19. Write a decorator called timer that measures and prints how long a function takes to run in seconds, then returns the result.
# import time

# def timer(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f"Elapsed: {end - start}s")
#     return wrapper

# @timer
# def slow():
#     time.sleep(1)

# slow()
# ---------------------------------------------------------------------------------


# 20. Write a function called digit_sum(n) using recursion that returns the sum of all digits of a non-negative integer
# def digit_sum(n):
#     sum = 0
#     while n > 0:
#         sum += n % 10
#         n = n // 10
#     return sum


# print(digit_sum(1234))
# print(digit_sum(999))
# print(digit_sum(5))
# ---------------------------------------------------------------------------------


# 21. Write a function called pipeline(*funcs) that returns a new function. The returned function passes its argument through each function in funcs one by one, left to right.
# def pipeline(*funcs):
#     def apply(x):
#         for func in funcs:
#             x = func(x)
#         return x
#     return apply
# p = pipeline(lambda x: x+1, lambda x: x*2, lambda x: x-3)
# print(p(5))
# ---------------------------------------------------------------------------------


# 22. Write a function called deep_flatten(lst) that recursively flattens a list nested to any depth.
# def deep_flatten(lst):
#     new_lst = []
#     for i in lst:
#         if type(i) == list:
#             for j in deep_flatten(i):
#                 new_lst.append(j)
#         else:
#             new_lst.append(i)
#     return new_lst
# print(deep_flatten([1, [2, [3, 4]], [5, 6], 7]))
# ---------------------------------------------------------------------------------


# 23. Write a general-purpose memoize decorator that caches the results of any function based on its arguments.
# def memoize(func):
#     cache = {}
#     def wrapper(*args):
#         if args not in cache:
#             cache[args] = func(*args)
#         return cache[args]
#     return wrapper

# def fib(n):
#     return n if n <= 1 else fib(n-1) + fib(n-2)
# fib=memoize(fib)
# print(fib(35))
# ---------------------------------------------------------------------------------


# 24. Write a function called curry(func) that converts a two-argument function into a curried version: calling it with one argument returns a function that accepts the second.
# def curry(func):
#     def first(a):
#         def second(b):
#             return func(a, b)
#         return second
#     return first
# def add(a, b):
#     return a + b

# curried_add = curry(add)
# print(curried_add(3)(5))
# ---------------------------------------------------------------------------------


# 25.   Write a function called compose(*funcs) that returns a new function applying the given functions from right to left (mathematical function composition).
# def compose(*funcs):
#     def apply(x):
#         for func in reversed(funcs):
#             x = func(x)
#         return x
#     return apply
# c = compose(lambda x: x-3, lambda x: x*2, lambda x: x+1)
# print(c(5))
# ---------------------------------------------------------------------------------