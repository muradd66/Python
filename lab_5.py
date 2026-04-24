# Set & Dictionary Lab      ---------------------------------------------------------------------------------


# 1. Create an empty set and print its type.
# mySet = {1, 2, 3, 4, 5}
# print(type(mySet))
# ---------------------------------------------------------------------------------


# 2. Create a set with mixed numbers and strings.
# mySet = {1, "salam", 7.5,0,"python"}
# print(mySet)
# ---------------------------------------------------------------------------------


# 3. Show how duplicates are removed in a set.
# mySet = {1, 2, 2, 3, 4, 4, 5, 6, 7, 7}
# print(mySet)
# ---------------------------------------------------------------------------------


# 4. Find the length of a set using len().
# mySet = {1, "salam", 7.5,0,"python"}
# print(len(mySet))
# ---------------------------------------------------------------------------------


# 5. Is a set mutable? Show with code.
# mySet = {1, "salam", 7.5, 0, "python"}
# mySet.add(2)
# mySet.remove(0)
# print(mySet)
# ---------------------------------------------------------------------------------


# 6. Check if an element exists in a set (using in).
# mySet = {1, "salam", 7.5, 0, "python"}
# print(0 in mySet)
# ---------------------------------------------------------------------------------


# 7. Can you access a set element by index? Explain.
# mySet = {1, "salam", 7.5, 0, "python"}
# print(mySet[0])

# Elementlərin yeri sabit deyil!!!
# ---------------------------------------------------------------------------------


# 8. Print all elements of a set using a for loop.
# mySet = {"Python", "C", "C++", "HTML", "JS", "CSS"}
# for i in mySet:
#     print(i)
# ---------------------------------------------------------------------------------


# 9.  Use set comprehension to create even numbers from 1 to 10.
# mySet = {i for i in range(1, 11) if i % 2 == 0}
# print(mySet)
# ---------------------------------------------------------------------------------


# 10. Use set comprehension to create squares of numbers
# mySet = {i**2 for i in range(1, 11)}
# print(sorted(mySet))
# ---------------------------------------------------------------------------------


# 11. Add a new element using add()
# mySet = {1, 2, 3, 4, 5}
# mySet.add(6)
# print(mySet)
# ---------------------------------------------------------------------------------


# 12. Add elements from another set using update().
# set1 = {1, 2, 3, 4}
# set2 = {5, 6, 7, 8}
# set1.update(set2)
# print(set1)
# ---------------------------------------------------------------------------------


# 13. Add elements from a list and tuple using update().
# mySet = {1, 2, 3, 4, 5}
# myTuple = ("murad", 0, 7, 9)
# myList = ["cavidan", 6, 8]
# mySet.update(myTuple, myList)
# print(mySet)
# ---------------------------------------------------------------------------------


# 14. Remove an existing element using remove().
# mySet = {1, 2, 3, 4, 5}
# mySet.remove(2)
# print(mySet)
# ---------------------------------------------------------------------------------


# 15.  Try to remove a non-existing element using discard() and check behavior.
# mySet = {1, 2, 3, 4, 5}
# mySet.discard(0)
# print(mySet)
# ---------------------------------------------------------------------------------


# 16. Find the intersection of two sets.
# set1 = {2, 3, 4, 5, 6, 8, 9}
# set2 = {3, 4, 5, 9, 10, 12}
# set3 = set1.intersection(set2)
# print(set3)
# ---------------------------------------------------------------------------------


# 17. Find the union of two sets
# set1 = {1, 3, 5, 7, 9}
# set2 = {0, 2, 4, 6, 8}
# set3 = set1.union(set2)
# print(set3)
# ---------------------------------------------------------------------------------


# 18. Find the difference between two sets.
# set1 = {1, 2, 3, 4, 7, 9, "salam", 5}
# set2 = {0, 2, 4, 6, 8, "hello"}
# print(set1.difference(set2))
# ---------------------------------------------------------------------------------


# 19. Use symmetric difference to show unique elements.
# set1 = {1, 2, 3, 4, 7, "salam"}
# set2 = {0, 2, 4, 6, 7, "hello"}
# print(set1.symmetric_difference(set2))
# ---------------------------------------------------------------------------------


# 20.  Demonstrate issubset() and issuperset().
# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# ---------------------------------------------------------------------------------


# 21. Create a set from a list with duplicates to get unique elements.
# myList = [1, 1, 2, 2, 3, 3, 4, 5, 6, 4, 5, 6, 7, 7]
# mySet=set(myList)
# print(mySet)
# ---------------------------------------------------------------------------------


# 22. Print only unique elements from a list using set.
# myList = [1, 1, 2, 2, 3, 3, 4, 5, 6, 4, 5, 6, 7, 7]
# mySet=set(myList)
# for i in mySet:
#     print(i)
# ---------------------------------------------------------------------------------


# 23. Check if two sets are disjoint.
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# set3 = {3, 4, 5}
# print(set1.isdisjoint(set2))
# print(set1.isdisjoint(set3))
# ---------------------------------------------------------------------------------


# 24. Convert set to frozenset and check type()
# mySet = {"Python", "C", "C++", "HTML", "JS", "CSS"}
# frznSet=frozenset(mySet)
# print(type(frznSet))
# ---------------------------------------------------------------------------------

# 25. Is frozenset mutable? Show with code
# mySet = {"Python", "C", "C++", "HTML", "JS", "CSS"}
# frznSet = frozenset(mySet)
# frznSet.add("React")
# print(frznSet)
# Xeyr Frozenset dəyişdirilə bilməz!!!


# 26. Create an empty dictionary and check its type.
# myDict = {}
# print(type(myDict))
# ---------------------------------------------------------------------------------


# 27.  Add 3 key-value pairs to a dictionary.
# myDict = {}
# myDict["name"] = "Murad"
# myDict["age"] = 20
# myDict["email"] = "mammadzada2006@gmail.com"
# print(myDict)
# ---------------------------------------------------------------------------------


# 28. Try to add a duplicate key — what happens?
# myDict = {}
# myDict["name"] = "Murad"
# myDict["age"] = 20
# myDict["email"] = "mammadzada2006@gmail.com"
# myDict["age"] = 19
# print(myDict)
# mövcud dəyəri yeniləyir.
# ---------------------------------------------------------------------------------


# 29. Find length of a dictionary using len().
# myDict = {}
# myDict["name"] = "Murad"
# myDict["age"] = 20
# myDict["email"] = "mammadzada2006@gmail.com"
# lenDict = len(myDict)
# print(lenDict)
# ---------------------------------------------------------------------------------


# 30. Is a dictionary mutable? Show with code
# myDict = {"name": "Murad", "age": 20}
# myDict["surname"] = "Mammadzada"
# print(myDict)
# Yes dictionary is mutable.
# ---------------------------------------------------------------------------------


# 31. Print value using an existing key.
# myDict = {
#     "name": "Murad",
#     "surname": "Mammadzada",
#     "age": 20,
#     "email": "mammadzada2006@gmail.com",
# }
# print(myDict["name"])
# print(myDict["age"])
# ---------------------------------------------------------------------------------


# 32. Use get() with a default value
# myDict = {"name": "Murad", "age": 20, "email": "mammadzada2006@gmail.com"}
# name = myDict.get("name", "Naməlum")
# print({name})
# city = myDict.get("city", "Şəhər qeyd olunmayıb")
# print({city})
# ---------------------------------------------------------------------------------


# 33. Print all keys and values using keys() and values().
# myDict = {
#     "name": "Murad",
#     "surname": "Mammadzada",
#     "age": 20,
#     "email": "mammadzada2006@gmail.com",
# }
# allKeys = myDict.keys()
# allValues = myDict.values()
# print(allKeys)
# print(allValues)
# ---------------------------------------------------------------------------------


# 34. Print key-value pairs using items().
# myDict = {
#     "name": "Murad",
#     "surname": "Mammadzada",
#     "age": 20,
#     "email": "mammadzada2006@gmail.com",
# }
# allItems=myDict.items()
# print(allItems)
# ---------------------------------------------------------------------------------


# 35. Check if a key exists using in operator
# myDict = {
#     "name": "Murad",
#     "surname": "Mammadzada",
#     "age": 20,
#     "email": "mammadzada2006@gmail.com",
# }
# print("name" in myDict)
# print("city" in myDict)
# ---------------------------------------------------------------------------------


# 36. Update dictionary with another dictionary
# myDict = {
#     "name": "Murad",
#     "surname": "Mammadzada",
#     "age": 20,
#     "email": "mammadzada2006@gmail.com",
# }
# brotherDict = {
#     "name": "Yusif",
#     "surname": "Mammadzada",
#     "age": 14,
# }
# myDict.update(brotherDict)
# print(myDict)
# ---------------------------------------------------------------------------------


# 37. Remove a key using pop() and return value.
# myDict = {
#     "name": "Murad",
#     "surname": "Mammadzada",
#     "age": 20,
#     "email": "mammadzada2006@gmail.com",
# }
# delKey=myDict.pop("email")
# print(myDict)
# print(delKey)
# ---------------------------------------------------------------------------------


# 38.  Remove last inserted key-value using popitem().
# myDict = {
#     "name": "Murad",
#     "surname": "Mammadzada",
#     "age": 20,
#     "email": "mammadzada2006@gmail.com",
# }
# print(myDict.popitem())
# ---------------------------------------------------------------------------------


# 39. Use setdefault() to add a value if key doesn’t exist.
# myDict = {"name": "Murad"}
# myDict.setdefault("age", 20)
# print(myDict)
# ---------------------------------------------------------------------------------


# 40. Clear all items using clear().
# myDict = {
#     "name": "Murad",
#     "surname": "Mammadzada",
#     "age": 20,
#     "email": "mammadzada2006@gmail.com",
# }
# myDict.clear()
# print(myDict)
# ---------------------------------------------------------------------------------


# 41. Create a nested dictionary (two-level).
# students = {
#     "student_1": {
#         "name": "Murad",
#         "university": "ADNSU",
#         "major": "Computer Engineering",
#     },
#     "student_2": {
#         "name": "Yusif",
#         "university": "TBD",
#         "major": "School",
#     },
# }
# print(students)
# print(f"Birinci tələbənin universiteti: {students['student_1']['university']}")
# ---------------------------------------------------------------------------------


# 42. Access a value from nested dictionary.
# students = {
#     "student_1": {
#         "name": "Murad",
#         "university": "ADNSU",
#         "major": "Computer Engineering",
#     },
#     "student_2": {
#         "name": "Yusif",
#         "university": "TBD",
#         "major": "School",
#     },
# }
# print(students["student_1"]["name"])
# ---------------------------------------------------------------------------------


# 43. Create square pairs using dictionary comprehension (1-5)
# myDict={x: x**2 for x in range(1,6)}
# print(myDict)
# ---------------------------------------------------------------------------------


# 44. Include only even keys using comprehension
# myDict = {x: x for x in range(1, 11) if x % 2 == 0}
# print(myDict)
# ---------------------------------------------------------------------------------


# 45.  Find max and min values in dictionary
# scores = {"Murad": 89, "Yusif": 95, "Cavidan": 78, "Adas": 92}
# max_score = max(scores.values())
# min_score = min(scores.values())

# print(max_score)
# print(min_score)
# ---------------------------------------------------------------------------------


# 46. Convert dictionary keys to a set
# myDict = {
#     "name": "Murad",
#     "surname": "Mammadzada",
#     "age": 20,
#     "email": "mammadzada2006@gmail.com",
# }
# myDict_keys=myDict.keys()
# new_set=set(myDict_keys)
# print(new_set)
# ---------------------------------------------------------------------------------


# 47. Find unique values as a set.
# myDict = {
#     "name": "Murad",
#     "surname": "Mammadzada",
#     "age": 20,
#     "email": "mammadzada2006@gmail.com",
# }
# myDict_values = myDict.values()
# unique_values = set(myDict_values)
# print(unique_values)
# ---------------------------------------------------------------------------------


# 48. Create a new dict with selected keys.
# myDict = {
#     "name": "Murad",
#     "surname": "Mammadzada",
#     "age": 20,
#     "email": "mammadzada2006@gmail.com",
# }
# selected_keys =["name", "age"]

# new_dict={k: myDict[k] for k in selected_keys if k in myDict}
# print(new_dict)
# ---------------------------------------------------------------------------------


# 49. Merge two dictionaries (update or ** operator).
# dict_1 = {
#     "name": "Murad",
#     "surname": "Mammadzada",
#     "age": 20,
#     "email": "mammadzada2006@gmail.com",
# }
# dict_2 = {"status": "student", "experience": "no"}
# merged_dict = {**dict_1, **dict_2}
# print(merged_dict)
# ---------------------------------------------------------------------------------


# 50. Check if key exists, add if missing.
# myDict = {
#     "name": "Murad",
#     "surname": "Mammadzada",
#     "age": 20,
#     "email": "mammadzada2006@gmail.com",
# }
# if "status" not in myDict:
#     myDict["status"] = "student"
# print(myDict)
# ---------------------------------------------------------------------------------


# 51. Print keys and values using a for loop.
# myDict = {
#     "name": "Murad",
#     "surname": "Mammadzada",
#     "age": 20,
#     "email": "mammadzada2006@gmail.com",
# }
# for key, value in myDict.items():
#     print(key, ":", value)
# ---------------------------------------------------------------------------------


# 52. Multiply all values by 10 using comprehension.
# myDict = {x: x * 10 for x in range(1, 10)}
# print(myDict)
# ---------------------------------------------------------------------------------


# 53. Create a set from dictionary keys using comprehension
# myDict = {
#     "name": "Murad",
#     "surname": "Mammadzada",
#     "age": 20,
#     "email": "mammadzada2006@gmail.com",
# }
# mySet={i for i in myDict.keys()}
# print(mySet)
# ---------------------------------------------------------------------------------


# 54. Filter values using loop and condition.
# scores = {
#     "Murad": 79,
#     "Yusif": 55,
#     "Cavidan": 78,
#     "Adas": 92,
#     "Rustam": 63,
#     "Omar": 72,
# }
# for key, value in scores.items():
#     if value > 70:
#         print(key, ":", value)
# ---------------------------------------------------------------------------------


# 55. Print nested dictionary elements using nested loops
# students = {
#     "student_1": {
#         "name": "Murad",
#         "university": "ADNSU",
#         "major": "Computer Engineering",
#     },
#     "student_2": {
#         "name": "Yusif",
#         "university": "TBD",
#         "major": "School",
#     },
# }
# for key, value in students.items():
#     print(key)
#     for k, v in value.items():
#         print(k, ":", v)
# ---------------------------------------------------------------------------------


# 56. Remove duplicates from a list using set and dictionary.
# myList = [1, 2, 3, 4, 4, 3, 5, 3, 2, 2, 1, 7, 9, 19, 7]
# mySet = set(myList)
# myDict=dict.fromkeys(myList)
# print(mySet)
# print(myDict)
# ---------------------------------------------------------------------------------


# 57. Increment a dictionary value for an existing key (default 0)
# scores = {
#     "Murad": 79,
#     "Yusif": 95,
#     "Cavidan": 78,
#     "Adas": 92,
# }
# scores["Murad"] += 12
# scores["Cavidan"]+=3
# print(scores)
# ---------------------------------------------------------------------------------


# 58. Check value in dict, add if missing (get + if)
# myDict = {
#     "name": "Murad",
#     "surname": "Mammadzada",
#     "age": 20,
#     "email": "mammadzada2006@gmail.com",
# }
# if "status" not in myDict:
#     myDict["status"] = "student"
# print(myDict)
# ---------------------------------------------------------------------------------


# 59. Create filtered nested dict using comprehension.
# students = {
#     "Murad": {"age": 20, "grade": 85},
#     "Yusif": {"age": 22, "grade": 55},
#     "Cavidan": {"age": 21, "grade": 71},
#     "Adas": {"age": 19, "grade": 48},
# }
# filtered={k: v for k,v in students.items() if v["grade"]>71}
# print(filtered)
# ---------------------------------------------------------------------------------


# 60. Create a frequency counter using set and dictionary
# fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# unique_fruits = set(fruits) 
# frequency = {fruit: fruits.count(fruit) for fruit in unique_fruits}
# print(frequency)
# ---------------------------------------------------------------------------------
