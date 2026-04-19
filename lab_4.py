# 1. datetime modulunu import et və cari tarix-vaxtı çap et.
# import datetime

# now1 = datetime.datetime.now()
# print(now1)


# Task-2

# import datetime
# now2 = datetime.datetime.now().date()
# print(now2)


# Task-3

# import datetime
# now3 = datetime.datetime.now().time()
# print(now3)


# Task-4

# import datetime
# now4 = datetime.datetime.now().year
# print(now4)


# Task-5

# import datetime
# now5 = datetime.datetime.now()
# nowMonth5 = now5.month
# nowDay5 = now5.day
# print(nowMonth5)
# print(nowDay5)


# Task-6

# import datetime
# now6 = datetime.datetime(2025,5,10)
# print(now6)


# # Task-7

# import datetime
# now7 = datetime.datetime(2023, 3,12,16)
# print(now7)


# Task-8

# import datetime
# now7 = datetime.datetime(2023, 3,12,16,25,45)
# print(now7)


# Task-9
# import datetime
# now9 = datetime.datetime(2023, 3,12,16,25,45,10)
# print(now9)


# Task-10
# import datetime
# now10 = datetime.datetime(2023, 3,12,16,25,45,10)
# print(type(now10))


# Task-11
# import datetime
# now11 = datetime.datetime.now()
# print(now11.strftime("%d-%m-%y"))


# Task-12
# import datetime
# now12 = datetime.datetime.now()
# print(now12.strftime("%B"))


# Task-13
# import datetime
# now13 = datetime.datetime.now()
# print(now13.strftime("%A"))


# Task-14
# import datetime
# now14 =datetime.datetime.now()
# print(now14.strftime("%I : %M : %S"))


# Task-15
# import datetime
# now15 =datetime.datetime.now()
# print(now15.strftime("%I : %M : %S , %p"))


# Task-16
# import datetime
# now16 ="2024-04-07"
# print(datetime.datetime.strptime(now16,"%Y-%m-%d"))


# Task-17
# import datetime
# now17 = "21 March 2025"
# print(datetime.datetime.strptime(now17,"%d %B %Y"))


# Task-18
# import datetime
# now18 = "21 March 2025 15:02:34"
# print(datetime.datetime.strptime(now18,"%d %B %Y %H:%M:%S"))


# Task-19

# import datetime
# now16 ="2024:04:07"
# print(datetime.datetime.strptime(now16,"%Y-%m-%d"))

# Error: Netice ValueError verir


# Task-20
# import datetime
# now20_one = "21 March 2025"
# now20_two = "2025-03-21"
# now20_three = "2025/03/21"

# print(datetime.datetime.strptime(now20_one,"%d %B %Y"))
# print(datetime.datetime.strptime(now20_two,"%Y-%m-%d"))
# print(datetime.datetime.strptime(now20_three,"%Y/%m/%d"))


# Task-21

# import datetime
# now21 = datetime.datetime.now()
# print(now21 + datetime.timedelta(days=5))


# Task-22

# import datetime
# now22 = datetime.datetime.now()
# print(now22 - datetime.timedelta(days=10))


# Task-23

# import datetime
# now23 = datetime.datetime.now()
# print(now23 + datetime.timedelta(hours=2))


# Task-24

# import datetime
# now24_one = datetime.datetime(2026 , 12 , 24)
# now24_two = datetime.datetime(2026 , 3 , 14)
# print(now24_one - now24_two)


# Task-25

# import datetime
# now25_one = datetime.datetime(2026 , 3 , 24)
# now25_two = datetime.datetime(2026 , 3 , 14)
# print(now25_one - now25_two)


# Task-26

# import datetime
# now26_one = datetime.datetime(2026 , 3 , 24)
# now26_two = datetime.datetime(2026 , 3 , 14)
# print(now26_one > now26_two)
# print(now26_one < now26_two)


# Task-27

# import datetime

# now27_one = datetime.datetime(2026, 10, 3)
# now27_two = datetime.datetime(2026, 11, 14)
# if now27_one > now27_two:
#     print("now27_one tarixi daha yenidir")
# else:
#     print("now27_two tarixi daha yenidir")


# Task-28

# import datetime

# now28_one = datetime.datetime(2026, 10, 3)
# now28_two = datetime.datetime(2026, 11, 14)
# if now28_one == now28_two:
#     print("tarixler beraberdir")
# else:
#     print("tarixler beraber deyil")


# Task-29

# import datetime

# now29_one = datetime.datetime(2018, 10, 3)
# now29_two = datetime.datetime(2035, 11, 14)
# print(now29_one > now29_two)
# print(now29_one < now29_two)
# print(now29_one == now29_two)


# Task-30

# import datetime

# now30_one = datetime.datetime.now()
# now30_two = datetime.datetime(2018, 10, 3)

# if now30_one > now30_two:
#     print("Bu gun tarixden evveldir")
# elif now30_one < now30_two:
#     print("Bu gun tarixden sonradir")
# else:
#     print("Tarxi bu gunki tarixe beraberdir")


# Task-31
# import math


# Task-32
# import math

# print(math.sqrt(49))


# Task-33
# import math

# print(math.ceil(4.67))


# Task-34
# import math

# print(math.floor(4.67))


# Task-35

# import math

# print(math.fabs(-34))


# Task-36

# import math

# print(math.pow(4, 3))


# Task-37

# a = 3**6
# b = 6**9
# print(a > b)
# print(a < b)


# Task-38

# import math

# print(math.log(10))


# Task-39

# import math

# print(math.log10(100))


# Task-40
# import math

# print(math.log2(16))


# Task-41

# import math

# print(math.sin(180))


# Task-42
# import math

# print(math.cos(120))


# Task-43

# import math

# print(math.tan(120))


# Task-44
# import math

# print(math.radians(60))


# Task-45

# import math

# print(math.degrees(math.pi))


# Task-46

# import math

# print(math.pi)


# Task-47

# import math

# print(math.e)


# Task-48

# import math

# r = 10
# s = math.pi * (r**2)
# print(s)


# Task-49
# import math

# print(math.exp(10))


# Task-50
# import math

# print(math.tau)


# task-51
# import math

# print(math.factorial(5))


# Task-52
# import math

# print(math.gcd(10))


# Task-53

# import math

# print(math.isqrt(49))


# Task-54

# import math

# print(math.trunc(10.808))


# Task-55
# import math

# a1 = (1, 2)
# a2 = (3, 4)
# print(math.dist(a1, a2))


# Task-56
# import random

# print(random.random())


# Task-57
# import random

# print(random.randint(1, 10))


# Task-58
# import random

# print(random.choice(["Python", "Java", "SQL", "JavaScript"]))


# Task-59
# import random

# print(random.uniform(1, 10))


# Task-60

# import random
# import math

# r = random.uniform(1, 10)
# s = math.pi * (r**2)
# print(s)
