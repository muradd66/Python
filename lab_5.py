# 1.  Write a function called square(n) that takes a number and returns its square.
# def square(n):
#     value = n**2
#     return value


# number = float(input("ededi daxil edin: "))

# print(square(number))


# 2. Write a function called greet(name) that returns the string 'Hello, !'
# def greet(name):
#     str = "'Hello',"
#     str = str + " "+ name + "!"
#     return str

# print(greet("Murad"))


# 3. Write a function called is_even(n) that returns True if n is even, False otherwise.
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False


# print(is_even(5))


# 4. Write a function called list_sum(lst) that returns the sum of all numbers in a list. Do NOT use the built-in sum()


# def list_sum(lst):
#     cem = 0
#     for i in lst:
#         cem += i
#     return cem


# print(list_sum([1, 2, 3, 4]))


# 5. Write a function called reverse_string(s) that returns the string in reverse order


# def reverse_string(s):
#     lst = list(s)
#     lst.reverse()
#     new_str = ("").join(lst)
#     return new_str


# print(reverse_string("Hello"))


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


# 7. Write a function called find_max(lst) that returns the largest number in a list. Do NOT use the built-in max().


# def find_max(lst):
#     max = lst[0]
#     for i in lst:
#         if i > max:
#             max = i
#     return max
# print(find_max([3, 1, 7, 2]))


# 8. Write a function called celsius_to_fahrenheit(c) that converts Celsius to Fahrenheit. Formula: F = C * 9/5 + 32
