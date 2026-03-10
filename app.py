# btn = int(input("Düyməni daxil edin: "))
# balance = 1000
# if btn >= 0 and btn <= 3:
#     while btn != 0:
#         if btn == 1:
#             print("Sizin balansınız:", balance)
#             break
#         elif btn == 2:
#             print("Siz balans çıxarma əməliyyatı yerinə yetirirsiniz")

#             m = int(input("çekme Məbləğini daxil edin: "))
#             if m <= balance:
#                 balance = balance - m
#                 print("sizin balansınız", balance, "qeder qaldı.")
#                 break
#             else:
#                 print("kifayət qədər məbləğ yoxdur!")
#                 break

#         elif btn == 3:
#             n = int(input("ödəmə Məbləğini daxil edin: "))
#             balance = balance + n
#             print("sizin balansınız", balance, "qeder oldu.")
#             break
#     else:
#         print("Siz çıxış etdiniz!")

# else:
#     print("Düyməni düzgün daxil edin!")


# colors=['red','green','blue']
# print(colors[0])
# colors[1]="yellow"
# print(colors)
# colors.append("purple")
# print(colors)
# colors.remove("red")
# print(colors)

# Tasklarrrrrrrrrrrrrrrr (1-50)


# # Task 1
# print("Hello World")

# # Task 2
# name = input("adinizi daxil edin")
# print("Hello", name)


# # Task 3
# year = int(input("Doqum ilinizi qeyd edin"))
# age = 2026 - year
# print("yasiniz: ]", age)

# # Task 4

# name = input("adinizi daxil edin: ")
# age = int(input("yasinizi daxil edin: "))
# height = float(input("cekinizi daxil edin: "))
# is_student = True
# print(type(name))
# print(type(age))
# print(type(height))
# print(type(is_student))


# # Task 5


# num = input("reqemi daxil edin")
# int_num = int(num)
# float_num = float(num)
# print(num, int_num, float_num)
# print(type(num))
# print(type(int_num))
# print(type(float_num))

# # Task 6

# a = float(input())
# b = float(input())
# c = float(input())
# cem = a + b + c

# print(cem.__round__(2))


# # Task 7

# lenght = float(input())
# width = float(input())
# area = lenght * width
# print(area)

# # Task 8

# celsium = float(input())
# Fahrenheit = (celsium * (9 / 5)) + 32
# print(Fahrenheit)

# # Task 9

# x = input()
# y = input()
# print(x, y)
# x = x + " " + y
# x = x.split(" ")
# y = x[0]
# x = x[1]

# print(x, y)


# # Task 10

# weight = float(input())
# height = float(input())
# bmi = weight / height**2
# print(bmi)


# # Task 11

# num = int(input())
# if num % 2 == 0:
#     print("cutdur")
# else:
#     print("tekdir")


# #  Task 12

# score = int(input())
# if score >= 60:
#     print("You passed")
# else:
#     print("you failed")

# # Task 13

# score = float(input())
# if score > 90:
#     print("grade: A", score)
# elif score > 80:
#     print("grade: B", score)
# elif score > 70:
#     print("grade: C", score)
# elif score > 60:
#     print("grade: D", score)
# else:
#     print("grade: F", score)


# # Task 14

# num = float(input())
# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")


# # Task 15

# age = int(input())
# if age >= 18:
#     print("you can vote")
# else:
#     print("Too young to vote")

# #  Task 16

# a = int(input())
# b = int(input())
# c = int(input())
# if a >= b and a >= c:
#     print(a, "is max")
# elif b >= a and b >= c:
#     print(c, "is max")
# else:
#     print(c, "is max")


# # Task 17

# num = int(input())
# if num > 0 and num < 13:
#     if num == 1 or num == 2 or num == 12:
#         print("winter")
#     elif num == 3 or num == 4 or num == 5:
#         print("spring")
#     elif num == 6 or num == 7 or num == 8:
#         print("summer")
#     else:
#         print("Fall")
# else:
#     print("ededi duzgun daxil edin")

#     # Task 18
# age = int(input("yasinizi daxil edin: "))
# if age >= 18:
#     print("you are an adult, price: $15")
# elif age >= 13 and age <= 17:
#     print("you are a teen, price: $10")
# else:
#     print("you are a child, price: $7")

#     # Task 19

# username = "murad"
# password = "murad321"

# log_user = input("istifadeci aadini daxil edin: ")
# log_passwd = input("passwordu daxil edin: ")

# if log_user == username:
#     if log_passwd == password:
#         print("Access Granted")
#     else:
#         print("Access Denied")
# else:
#     print("Access Denied")

#     # Task 20

# a = float(input())
# b = float(input())
# c = float(input())

# if a + b > c and a + c > b and c + b > a:
#     print("correct triangle")
# else:
#     print("valid triangle")

#     # Task 21

# year = int(input("ili daxil edin"))
# if year % 400 == 0:
#     print("esrdir")
# elif year % 4 == 0:
#     print("il 4-e bolunur")
# else:
#     print("il 4-e bolunmur")

#     # Task 22

# weight = float(input("BMI daxil edin: "))
# if weight < 18.5:
#     print("UnderWeight")
# elif weight < 25:
#     print("Normal")
# elif weight < 29.9:
#     print("overweight")
# else:
#     print("obese")

#     # Task 23

# income = float(input())
# credit = float(input())
# if income > 50000 and credit > 700:
#     print("approved")
# else:
#     print("denied")

#     # Task 24

# temp = float(input())
# if temp > 30:
#     print("Suggest")
# elif temp < 30:
#     print("Comfortable")
# else:
#     print("Suggest heater")

#     # Task 25

#     age = int(input())
#     height = float(input("sm-ile"))
#     if height < 120:
#         print("boyunuz el vermir")
#     elif age < 18:
#         print("must parent")

#     # Task 26

#     age = int(input())
#     experience = int(input())
#     degree = input()
#     if (age > 22 and age < 45) and (degree == "CS" or experience >= 5):
#         print("siz is telebine uyqunsuz")
#     else:
#         print("siz uyqun deyilsiz")

#     # Task 27

#     price = float(input())
#     member = input("siz sirkete uzvsuz? he/yox")
#     if price > 100:
#         print("emek haqqi pulsuz")
#     elif price > 100 and member == "he":
#         print("emek haqqi 3$")
#     else:
#         print("emek haqqi 7$")

#     # Task 28:

#     player1 = input()
#     player2 = input()
#     if player1 == "rock" and player2 == "scissors":
#         print("Winner:", player1)
#     elif player1 == "rock" and player2 == "paper":
#         print("Winner:", player2)
#     elif player1 == "rock" and player2 == "rock":
#         print("no Winner")
#     elif player1 == "scissors" and player2 == "rock":
#         print("Winner:", player2)
#     elif player1 == "paper" and player2 == "rock":
#         print("Winner:", player1)
#     elif player1 == "paper" and player2 == "paper":
#         print("no Winner")
#     elif player1 == "scissors" and player2 == "rock":
#         print("no Winner")

# Task 29

# n = int(input())
# for i in range(1, n):
#     print(i)

# Task 30

# n=int(input())
# k=1
# for i in range(1,11):
#     print(n,"x",i,"=",i*n)

# Task 31

# n=int(input())
# sum=0
# for i in range(1,n):
#     sum=sum+i
# print(sum)

# Task 32

# n=int(input())
# for i in range(n):
#     print(n)
#     n=n-1

# Task 33

# n=int(input())
# star=""
# for i in range(n+1):
#     star=i*"*"
#     print(star)

# Task 34

# for i in range(1,51):
#     if i%3==0:
#         print(str(i).replace(str(i),"Fizz"))
#     elif i%5==0:
#         print(str(i).replace(str(i),"Buzz"))
#     elif i%3==0 and i%5==0:
#         print(str(i).replace(str(i),"FizzBuzz"))
#     else:
#         print(i)

# Task 35

# n=int(input())
# h=1
# for i in range(1,n+1):
#     h=h*i
# print(h)

# Task 36


# n=input("ededi daxil edin: ")
# cem=0
# for i in (n):
#     cem=cem+int(i)

# print(cem)

# Task 37

# n=int(input())
# t=0
# for i in range(2,n//2):
#     if n%i==0:
#         t=1
# if t==1:
#     print("murekkeb")
# else:
#     print("sade")


# Task 38 ---------------------------------------------------------------

# n=int(input(" tek ededi daaxil et "))
# for i in range(1,n):

# Task 39

# i=1
# while i<=10:
#     print(i)
#     i=i+1

# Task 40

# attemt = 3
# username = "Murad"
# password = "murad2006"
# i = 1
# while i <= 3:
#     user_log = input("username-ni daxil edin: ")
#     passwdlog = input(" passwordu daxil edin: ")
#     if user_log == "Murad" and passwdlog == "murad2006":
#         print("Giris edildi")
#         break
#     else:
#         print("birdaha cehd edin")
# else:
#     print("cehd sayi qutardi ")


# Task 41

# import random

# k = random.randint(1, 100)
# print(k)
# n = int(input("texmini daxil edin"))
# while n != k:
#     n = int(input("birdaha daxil eddin"))
#     if n > k:
#         print("Lower")
#     else:
#         print("Higher")
# else:
#     print("tebrikler")

# Task 42

# cem = 0
# while True:
#     n = int(input())
#     if n == 0:
#         print("Stop")
#         break
#     cem = cem + n
# print(cem)

# Task 43

# balance = 1000
# action = input("emeliyyat novunu yazin: ")
# if action == "deposit":
#     amount = float(input("daxil edeceyiniz mebllegi daxiledin: "))
#     balance = balance + amount
#     print(f"son balance {balance}")
# elif action == "withdraw":
#     price = float(input("cixaraciqiniz meblegi daxil edin: "))
#     if price > balance:
#         print("kifayet qeder balans yoxdur")
#     else:
#         balance = balance - price
#         print(f"son balans {balance}")
# elif action == "check balance":
#     print(f"sizin balansiiniz {balance}")
# elif action == "quit":
#     print("cixis edildi")

# Task 44

# n = int(input())

# while n != 1:
#     if n % 2 == 0:
#         n = n / 2
#         print(n)
#     else:
#         n = 3 * n + 1
#         print(n)

# Task 45

# n = int(input("ededi daxil edin:"))
# i = 0
# k = 1
# x = 0
# c = 0
# while i < n:
#     print(x)
#     c = x
#     x = k
#     k = c + k
#     i = i + 1

# Task 46

# password = input("sifreni daxil edin")
# if len(password) >= 8:
#     for i in password:
#         if (
#             (i == "1")
#             or (i == "2")
#             or (i == "3")
#             or (i == "4")
#             or (i == "5")
#             or (i == "6")
#             or (i == "7")
#             or (i == "8")
#             or (i == "9")
#         ):
#             if any(char.isupper() for char in password):
#                 print("sifre qebul edildi ")
#             else:
#                 print("sifre duz deyil")
#         else:
#             print("sifre duz deyil")
# else:
#     print("uzunluq azdir")


# Task 47
# print("1. Kalkulyator")
# print("2. Konverter")
# print("3. Viktorina")
# print("4. cıxıs")


# while True:
#     options = input("secim edin (1-4): ")

#     if options == "1":
#         print("Kalkulyator bolmesine xos geldiniz.")
#     elif options == "2":
#         print("Konverter bolmesine xos geldiniz.")
#     elif options == "3":
#         print("Viktorina baslayir")
#     elif options == "4":
#         print("Proqramdan cıxılır")
#         break
#     else:
#         print(" Yeniden yoxlayin")

# Task 48

# a = int(input("Birinci ededi daxil edin: "))
# b = int(input("İkinci ededi daxil edin: "))

# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a

# print(f"ƏBOB: {a}")

# Task 49

# neticeler = ""

# for i in range(5):
#     name = input("Ad daxil edin: ")
#     score = int(input("Bal daxil edin: "))

#     if score >= 50:
#         status = "Keçdi"
#     else:
#         status = "Kəsildi"
#     neticeler = neticeler + name + " - " + str(score) + " - " + status + "\n"

# print(neticeler)

# Task 50

score = 0

# Sual 1
cavab1 = input("1. Dünyada ən çox qonşusu olan ölkə hansıdır? ")
if cavab1 == "çin":
    print("Düzdür!")
    score = score + 1
else:
    print("Səhvdir. Düzgün cavab: Çin")

# Sual 2
cavab2 = input("2. Suyun kimyəvi formulu nədir? ")
if cavab2 == "h2o":
    print("Düzdür!")
    score = score + 1
else:
    print("Səhvdir. Düzgün cavab: H2O")

# Sual 3
cavab3 = input("3. Hansı planet 'Qırmızı Planet' kimi tanınır? ")
if cavab3 == "mars":
    print("Düzdür!")
    score = score + 1
else:
    print("Səhvdir. Düzgün cavab: Mars")

# Sual 4
cavab4 = input("4. Kompüterin 'beyni' sayılan hissə hansıdır? (Qısaltma) ")
if cavab4 == "cpu":
    print("Düzdür!")
    score = score + 1
else:
    print("Səhvdir. Düzgün cavab: CPU")

# Sual 5
cavab5 = input("5. İşığın sürəti saniyədə təxminən neçə min km-dir? ")
if cavab5 == "300":
    print("Düzdür!")
    score = score + 1
else:
    print("Səhvdir. Düzgün cavab: 300")

print("Sənin yekun xalın:", score, "/ 5")
