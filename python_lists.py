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

myList = ["Python", "C", "C++", "HTML", "JS", "CSS"]
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
