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

