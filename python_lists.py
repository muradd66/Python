# 1. Üç fərqli data tipindən (string, int, bool) ibarət list yarat və çap et.
# mylist = [666, "Azerbaycan", True]
# print(mylist)
# ---------------------------------------------------------------------------------

# 2. Bir listin type()-ini yoxla — nəticəsi nə olur?
# mylist = [666, "Azerbaycan", True]
# print(type(mylist))
# ---------------------------------------------------------------------------------

# 3. len() funksiyası ilə listin uzunluğunu tap.
# mylist = [666, "Azerbaycan", True]
# print(len(mylist))
# ---------------------------------------------------------------------------------

# 4. List dəyişməzdir (immutable) yoxsa dəyişkən (mutable)? Bunu kodla sübut et.
# mylist = [666, "Azerbaycan", True]
# mylist.append(False)
# print(mylist)
# print("dəyişkəndir (is mutable)")
# ---------------------------------------------------------------------------------

# 5. İçindəki elementlər eyni olan iki list yarat, == ilə müqayisə et.
# first_list = [1, 2, 3, 4, 5]
# second_list = [1, 2, 3, 4, 5]
# print(first_list == second_list)
# ---------------------------------------------------------------------------------

# 6. Listdəki ikinci elementə indeks ilə müraciət et.
# mylist = [666, "Azerbaycan", True]
# print(mylist[1])
# ---------------------------------------------------------------------------------

# 7. Mənfi indeks istifadə edərək sondan ikinci elementi götür.
# mylist = [666, "Azerbaycan", True, "salam", "sağol"]
# print(mylist[-2])
# ---------------------------------------------------------------------------------

# 8. Slice ilə listdəki 2-ci-dən 4-cü elementə qədər olan hissəni götür.
# mylist = [666, "Azerbaycan", True, "salam", "sağol"]
# print(mylist[2:4])
# ---------------------------------------------------------------------------------

# 9. Slice-da başlanğıc və son indeksi boş buraxaraq listin əvvəlindən/sonundan götür.
# mylist = [666, "Azerbaycan", True, "salam", "sağol"]
# print(mylist[::])
# ---------------------------------------------------------------------------------

# 10. in operatoru ilə bir elementin listdə olub-olmadığını yoxla.
# mylist = [666, "Azerbaycan", True, "salam", "sağol"]
# print(666 in mylist)
# ---------------------------------------------------------------------------------

# 11. Listin birinci elementini başqa bir dəyərlə əvəz et.
# mylist = [666, "Azerbaycan", True, "salam", "sağol"]
# mylist[0] = "reqem"
# print(mylist)
# ---------------------------------------------------------------------------------

# 12. Slice assignment ilə listin 2-5-ci elementlərini eyni anda dəyiş.
# mylist = [666, "Azerbaycan", True, "salam", "sağol", "necesen"]
# mylist[2:5] = False, "Hello", "Bye"
# print(mylist)
# ---------------------------------------------------------------------------------

# 13. Slice assignment ilə 2 elementi 3 yeni dəyərlə əvəz et (uzunluq dəyişsin).
# mylist = [666, "Azerbaycan", True, "salam", "sağol", "necesen"]
# print(len(mylist))
# mylist[1:3] = "a", "b", "c"
# print(mylist)
# print(len(mylist))
# ---------------------------------------------------------------------------------

# 14. Slice assignment ilə listin əvvəlinə yeni elementlər əlavə et (heç nə silmə).
# mylist = [666, "Azerbaycan", True, "salam", "sağol", "necesen"]
# mylist[0:0] = 550, 444
# print(mylist)
# ---------------------------------------------------------------------------------

# 15. Listin son iki elementini slice assignment ilə sil.
# mylist = [666, "Azerbaycan", True, "salam", "sağol", "necesen"]
# mylist[-2:] = []
# print(mylist)
# ---------------------------------------------------------------------------------

# 16. append() ilə listə yeni bir element əlavə et.
# mylist = [666, "Azerbaycan", True, "salam", "sağol", "necesen"]
# mylist.append("Yaxşı")
# print(mylist)
# ---------------------------------------------------------------------------------

# 17. insert() ilə listin ortasına (indeks 2-yə) bir element daxil et.
# mylist = [666, "Azerbaycan", True, "salam", "sağol", "necesen"]
# mylist.insert(2, False)
# print(mylist)
# ---------------------------------------------------------------------------------

# 18. extend() ilə bir listi digər listin sonuna birləşdir.
# myList = ["Python", "C", "C++"]
# yourList = ["HTML", "JS", "CSS"]
# myList.extend(yourList)
# print(myList)
# ---------------------------------------------------------------------------------

# 19. extend() ilə bir tuple-ın elementlərini listə əlavə et.
# myList = ["Python", "C", "C++"]
# yourtuple = ("HTML", "JS", "CSS")
# myList.extend(yourtuple)
# print(myList)
# ---------------------------------------------------------------------------------

# 20. + operatoru ilə iki listi birləşdir (yeni list yarat).
# myList = ["Python", "C", "C++"]
# yourList = ["HTML", "JS", "CSS"]
# newList = myList + yourList
# print(newList)
# ---------------------------------------------------------------------------------

# 21. remove() ilə listdən müəyyən bir dəyəri sil.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# myList.remove("C++")
# print(myList)
# ---------------------------------------------------------------------------------

# 22. pop() ilə sonuncu elementi listdən çıxar.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# myList.pop()
# print(myList)
# ---------------------------------------------------------------------------------

# 23. pop(1) ilə ikinci elementi listdən çıxar.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# myList.pop(1)
# print(myList)
# ---------------------------------------------------------------------------------

# 24. del açar sözü ilə listin ilk elementini sil.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# del myList[0]
# print(myList)
# ---------------------------------------------------------------------------------

# 25. clear() ilə listin bütün elementlərini sil (list özü qalsın).
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# myList.clear()
# print(myList)
# ---------------------------------------------------------------------------------

# 26. for dövrüsü ilə listin hər elementini çap et.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# for i in myList:
#     print(i)
# ---------------------------------------------------------------------------------

# 27. range(len()) istifadə edərək indeks nömrəsi ilə listə daxil ol.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# for i in range(len(myList)):
#     print(myList[i])
# ---------------------------------------------------------------------------------

# 28. while dövrüsü ilə listin elementlərini gəz.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# i = 0
# k = len(myList)
# while i < k:
#     print(myList[i])
#     i = i + 1
# ---------------------------------------------------------------------------------

# 29. enumerate() ilə hər elementin indeksini və dəyərini birlikdə çap et.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# for index, value in enumerate(myList):
#     print(f"index: {index}, value: {value}")
# ---------------------------------------------------------------------------------

# 30. Listdəki yalnız cüt indeksdəki elementləri çap et (loop + şərt ilə).
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# for index, value in enumerate(myList):
#     if index % 2 == 0:
#         print(value)
# ---------------------------------------------------------------------------------

# 31. List comprehension ilə 1-dən 20-yə kimi olan bütün ədədlər listini yarat.
# numbers = [i for i in range(1, 20)]
# print(numbers)
# ---------------------------------------------------------------------------------

# 32. Comprehension ilə listdən yalnız 'a' hərfini ehtiva edən sözləri fil­tr et.
# mylist = ["Python", "Azerbaycan", "salam", "sağol", "necesen"]
# new_list = [i for i in mylist if "a" in i]
# print(new_list)
# ---------------------------------------------------------------------------------

# 33. Comprehension ilə hər ədədin kubunu hesabla.
# numbers = [i**3 for i in range(1, 20)]
# print(numbers)
# ---------------------------------------------------------------------------------

# 34. Şərtli (if-else) ifadəni comprehension içinə daxil edərək mənfini 0-a çevir.
# mylist = [1, 4, 6, -5, -8, -43, 7, 0, 66]
# new_numbers = [0 if i < 0 else i for i in mylist]
# print(new_numbers)
# ---------------------------------------------------------------------------------

# 35. Nested list comprehension ilə çarpma cədvəli (5x5) yarat.
# for i in range(1, 11):
#     print(f"5 x {i} = {5 * i}")

# Digər alternativ
# [print(f"5 x {i} = {5 * i}") for i in range(1, 11)]
# ---------------------------------------------------------------------------------

# 36. sort() ilə rəqəmlər listini artan sırada sırala.
# reqemler = [3, 6, 8, 0, 2, 25, 53, 77, 13, 44, 100]
# reqemler.sort()
# print(reqemler)
# ---------------------------------------------------------------------------------

# 37. sort(reverse=True) ilə sözlər listini azalan əlifba sırasında sırala.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# myList.sort(reverse=True)
# print(myList)
# ---------------------------------------------------------------------------------

# 38. sort(key=len) ilə sözlər listini uzunluğuna görə sırala
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# myList.sort(key=len)
# print(myList)
# ---------------------------------------------------------------------------------

# 39. sorted() ilə orijinal listi dəyişmədən sıralanmış yeni list qaytar.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# print(f"Evvelki List: {myList}")
# print(f"Sıralanmış: {sorted(myList)}")
# ---------------------------------------------------------------------------------

# 40. reverse() ilə listin elementlərinin sırasını tərsinə çevir.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# myList.reverse()
# print(myList)
# ---------------------------------------------------------------------------------

# 41. copy() metodu ilə listin surətini çıxar, orijinalı dəyiş, surətin dəyişmədiyini gör.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# newList = myList.copy()
# myList.sort()
# print(myList)
# print(newList)
# ---------------------------------------------------------------------------------

# 42. list() konstruktoru ilə listin kopyasını yarat.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# newList = list(myList)
# print(newList)
# ---------------------------------------------------------------------------------

# 43. Slice [:] ilə tam listin kopyasını çıxar.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# newList = myList[:]
# print(newList)
# ---------------------------------------------------------------------------------

# 44. Sadə mənimsətmə (=) ilə surət çıxarmağı sına — fərqi sübut et.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# newList = myList
# myList.pop()
# print(newList)
# ---------------------------------------------------------------------------------

# 45. import copy; deepcopy() ilə nested listin tam müstəqil kopyasını yarat.
# import copy

# myList = ["Python", "C", "C++", ["Numbers", "Strings", "Boolian"], "HTML", "JS", "CSS"]
# newList = copy.deepcopy(myList)
# print(newList)
# ---------------------------------------------------------------------------------

# 46. + operatoru ilə iki listi birləşdir.
# firstList = ["salam", "necesen?"]
# secondList = ["yaxşı", "sağol"]
# totalList = firstList + secondList
# print(totalList)
# ---------------------------------------------------------------------------------

# 47. extend() metodu ilə birinci listə ikinci listin elementlərini əlavə et.
# firstList = ["salam", "necesen?"]
# secondList = ["yaxşı", "sağol"]
# firstList.extend(secondList)
# print(firstList)
# ---------------------------------------------------------------------------------

# 48. for loop ilə ikinci listin elementlərini birinciyə append et.
# firstList = ["Python", "C", "C++"]
# secondList = ["HTML", "CSS", "JS"]
# for i in secondList:
#     firstList.append(i)
# print(firstList)
# ---------------------------------------------------------------------------------

# 49. * operatoru ilə listi üç dəfə təkrar et.
# myList = ["A", "B", "C"]
# repeatList = myList * 3
# print(repeatList)
# ---------------------------------------------------------------------------------

# 50. + ilə birləşdirmə və extend() arasındakı fərqi göstər (in-place vs yeni list).
# firstList = ["salam", "necesen?"]
# secondList = ["yaxşı", "sağol"]
# totalList = firstList + secondList
# print(totalList)
# + operatoru ilə yeni list yaradırıq

# firstList.extend(secondList)
# print(firstList)
# extend() operatoru ilə bir listi genişlədirik
# ---------------------------------------------------------------------------------

# 51. append() — listə sondan element əlavə et.
# myList = ["A", "B", "C"]
# myList.append("D")
# print(myList)
# ---------------------------------------------------------------------------------

# 52. clear() — listin bütün elementlərini sil.
# myList = ["Python", "C", "C++", ["Numbers", "Strings", "Boolian"], "HTML", "JS", "CSS"]
# myList.clear()
# print(myList)
# ---------------------------------------------------------------------------------

# 53. copy() — listin sığ kopyasını qaytar.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# newList = myList.copy()
# print(newList)
# ---------------------------------------------------------------------------------

# 54. count() — listdə müəyyən dəyərin neçə dəfə göründüyünü tap.
# numbers = [5, 0, -5, 7, 5, 3, 8, 5, 55, 99]
# print(numbers.count(5))
# ---------------------------------------------------------------------------------

# 55. extend() — listi başqa iterable ilə genişləndir.
# family = ["mother", "father", "son", "doughter"]
# family.extend(["grandmother", "grandfather"])
# print(family)
# ---------------------------------------------------------------------------------

# 56. index() — müəyyən dəyərin ilk göründüyü indeksi qaytar.
# numbers = [0, -5, 7, 5, 3, 8, 5, 55, 99]
# print(numbers.index(5))
# ---------------------------------------------------------------------------------

# 57. insert() — müəyyən mövqeyə element daxil et.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# myList.insert(3, "React")
# print(myList)
# ---------------------------------------------------------------------------------

# 58. pop() — müəyyən indeksdəki elementi çıxar (default: sonuncu).
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# myList.pop()
# print(myList)
# ---------------------------------------------------------------------------------

# 59. remove() — ilk tapılan müəyyən dəyəri sil.
# numbers = [0, -5, 7, 5, 3, 8, 5, 55, 99]
# numbers.remove(5)
# print(numbers)
# ---------------------------------------------------------------------------------

# 60. reverse() — listin elementlərini tərsinə çevir.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# myList.reverse()
# print(myList)
# ---------------------------------------------------------------------------------

# 61. sort() — listi sırala (default: artan)
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# myList.sort()
# print(myList)
# ---------------------------------------------------------------------------------

# 62. Dörd elementdən ibarət tuple yarat və çap et.
# myTuple = ("Python", "C", "C++", "HTML")
# print(myTuple)
# ---------------------------------------------------------------------------------

# 63. Tuplenin type()-ini yoxla.
# myTuple = ("Python", "C", "C++", "HTML")
# print(type(myTuple))
# ---------------------------------------------------------------------------------

# 64. Yalnız bir elementli tuple yarat — vergülün niyə vacib olduğunu göstər.
# myTuple = ("Python",)
# print(type(myTuple))
# fakeTuple = "Python"
# print(type(fakeTuple))
# ---------------------------------------------------------------------------------

# 65. len() ilə tuplenin uzunluğunu tap.
# myTuple = ("Python", "C", "C++", "HTML")
# print(len(myTuple))
# ---------------------------------------------------------------------------------

# 66. Tuple müxtəlif data tipli elementlər ehtiva edə bilər — bunu nümunə ilə göstər.
# myTuple = ("Python", "C", False, "C++", True, 5, 0, -6, "HTML", 76.4)
# print(myTuple)
# ---------------------------------------------------------------------------------

# 67. Tuple elementinə müsbət indeks ilə müraciət et.
# myTuple = ("Python", "C", "C++", "HTML")
# print(myTuple[2])
# ---------------------------------------------------------------------------------

# 68. Mənfi indeks istifadə edərək tuplenin sonuncu elementini götür.
# myTuple = ("Python", "C", "C++", "HTML")
# print(myTuple[-1])
# ---------------------------------------------------------------------------------

# 69. Slice ilə tuplenin ortasındakı bir hissəni götür.
# myTuple = ("Python", "C", False, "C++", True, 5, 0, -6, "HTML", 76.4)
# partTuple = myTuple[2:6]
# print(partTuple)
# ---------------------------------------------------------------------------------

# 70. in operatoru ilə bir dəyərin tuple-da olub-olmadığını yoxla.
# myTuple = ("Python", "C", "C++", "HTML")
# if "Python" in myTuple:
#     print("Var")
# else:
#     print("Yoxdur")
# ---------------------------------------------------------------------------------

# 71. Tuple-ı listə çevir, element əlavə et, yenidən tuple-a çevir.
# myTuple = ("Python", "C", "C++", "HTML")
# myTuple = list(myTuple)
# myTuple.append("React")
# myTuple = tuple(myTuple)
# print(myTuple)
# print(type(myTuple))
# ---------------------------------------------------------------------------------

# 72. + ilə iki tuple-ı birləşdir (yeni tuple yarat).
# firstTuple = ("Python", "C", "C++")
# secondTuple = ("HTML", "CSS", "JS", "React")
# newTuple = firstTuple + secondTuple
# print(newTuple)
# ---------------------------------------------------------------------------------

# 73. Tuple-a element əlavə etməyə birbaşa cəhd et — xətanı izah et.
# myTuple = ("Python", "C", "C++", "HTML")
# newTuple = myTuple + "CSS"
# print(newTuple)
# Tuple dəyişdirilə bilməz!!!
# ---------------------------------------------------------------------------------

# 74. del açar sözü ilə tuple-ın özünü tamamilə sil.
# myTuple = ("Python", "C", "C++", "HTML")
# print(myTuple)
# del myTuple
# ---------------------------------------------------------------------------------

# 75. Tuple-ı dəyişənlərə unpack et (eyni sayda dəyişən).
# myTuple = ("Python", "C", "C++", "HTML")
# (P, C, CP, H) = myTuple
# print(P)
# print(C)
# print(CP)
# print(H)
# ---------------------------------------------------------------------------------

# 76. * operatoru ilə artıq qalan dəyərləri bir dəyişənə topla.
# myTuple = ("Python", "C", "C++", "HTML", "CSS", "JS")
# (P, C, CP, H, *all) = myTuple
# print(P)
# print(all)
# ---------------------------------------------------------------------------------

# 77. Funksiyanın qaytardığı tuple-ı unpack edərək ayrı dəyişənlərə mənimsət.
# def info():
#     name = "Murad"
#     surname = "Mammadzada"
#     age = 20
#     degree = "student"
#     return name, surname, age, degree

# student_name, student_surname, student_age, student_degree = info()
# ---------------------------------------------------------------------------------


# print(student_name)
# print(student_surname)
# print(student_age)
# print(student_degree)
# ---------------------------------------------------------------------------------

# 78. İki dəyişənin dəyərini tuple unpacking ilə yerlərini dəyiş (swap).
# myTuple = ("Python", "C", "C++", "HTML")
# (P, C, CP, H) = myTuple
# P, C = C, P
# print(P)
# print(C)
# ---------------------------------------------------------------------------------

# 79. for dövrüsü ilə tuple-ın hər elementini çap et.
# myTuple = ("Python", "C", "C++", "HTML", "CSS", "JS", "React")
# for i in myTuple:
#     print(i)
# ---------------------------------------------------------------------------------

# 80. range(len()) ilə tuple-ı indeks nömrəsi ilə gəz.
# myTuple = ("Python", "C", "C++", "HTML", "CSS", "JS", "React")
# for i in range(0, len(myTuple)):
#     print(myTuple[i])
# ---------------------------------------------------------------------------------

# 81. while dövrüsü ilə tuple elementlərini çap et.
# myTuple = ("Python", "C", "C++", "HTML", "CSS", "JS", "React")
# i = 0
# while i < len(myTuple):
#     print(myTuple[i])
#     i = i + 1
# ---------------------------------------------------------------------------------

# 82. + ilə iki tuple-ı birləşdir.
# firstTuple = ("Python", "C", "C++")
# secondTuple = ("HTML", "CSS", "JS", "React")
# total = firstTuple + secondTuple
# print(total)
# ---------------------------------------------------------------------------------

# 83. * ilə tuple-ı üç dəfə təkrar et.
# myTuple = ("A", "B", "C")
# print(myTuple * 3)
# ---------------------------------------------------------------------------------

# 84. tuple() ilə listdən yeni tuple yarat.
# myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
# myTuple = tuple(myList)
# print(myTuple)
# ---------------------------------------------------------------------------------

# 85. count() — tuple-da müəyyən dəyərin neçə dəfə göründüyünü tap.
# myTuple = ("A", "B", "C", "A", "M", "B", "M", "A", "C")
# print(myTuple.count("A"))
# ---------------------------------------------------------------------------------

# 86. index() — tuple-da dəyərin ilk göründüyü yeri qaytar.
# myTuple = ("A", "B", "C", "A", "M", "B", "M", "A", "C")
# print(myTuple.index("M"))
# ---------------------------------------------------------------------------------

# 87. Tuple-ın niyə yalnız 2 metodu var? List ilə müqayisəli izah et.
# myTuple = ("A", "B", "C")
# myTuple.append("D")
# Error, çünki tuple-lar dəyişməzdir. Üzərində heçbir əməliyyat aparmaq olmaz!
# print(myTuple.index("C"))
# Bu işləyəcək, çünki index() və count() methodlari tuple üzərində heçbir əməliyyat etmir sadəcə tuple-ı oxuyurlar.
# ---------------------------------------------------------------------------------
