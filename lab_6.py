# FILE HANDLING

# 1.  Open a file in read mode using open() and print its content
# f = open("metn.txt", "r", encoding="utf-8")
# content = f.read()
# print(content)
# f.close()


# 2. Open a file in write mode ("w") and show that previous content is overwritten.
# f = open("metn.txt", "w", encoding="utf-8")
# f.write("Bu yeni məzmundur\n")
# f.write("Əvvəlki hər şey silindi!")
# f.close()


# 3. Open a file in append mode ("a") and add a new line at the end.
# f=open("metn.txt","a",encoding="utf-8")
# f.write("\nBu sətir əlavə edildi.")
# f.close()


# 4. Use read() to read the entire file content.
# with open("metn.txt", "r", encoding="utf-8") as f:
#     content = f.read()
# print(content)


# 5. Use readline() to read only the first line.
# with open("metn.txt", "r", encoding="utf-8") as f:
#     birinci_setir = f.readline()
# print(birinci_setir)


# 6.  Use readlines() to get all lines as a list.
# with open("metn.txt", "r", encoding="utf-8") as f:
#     setirler = f.readlines()
# print(setirler)


# 7. Use a for loop to print each line in a file.
# with open("metn.txt", "r", encoding="utf-8") as f:
#     for setir in f:
#         print(setir.strip())


# 8.  Close a file using close() and explain why it is important.
# f = open("metn.txt", "r", encoding="utf-8")
# content = f.read()
# print(content)
# f.close()


# 9. Use with open() to open a file with automatic closing.
# with open("metn.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     print(content)


# 10. Count how many lines are in a file using a loop
# say = 0
# with open("metn.txt", "r", encoding="utf-8") as f:
#     for setir in f:
#         say += 1
# print(f"Cəmi sətir sayı: {say}")


# 11.  Check if a specific word exists in a file.
# axtarilan = "python"
# with open("metn.txt", "r", encoding="utf-8") as f:
#     content = f.read().lower()
# if axtarilan in content:
#     print(f"'{axtarilan}' sözü tapıldı!")
# else:
#     print(f"'{axtarilan}' sözü tapılmadı.")


# 12. Count the total number of words in a file.
# with open("metn.txt", "r", encoding="utf-8") as f:
#     content = f.read()
# sozler = content.split()
# print(f"Cəmi söz sayı: {len(sozler)}")


# 13. Count the number of characters in a file.
# with open("metn.txt", "r", encoding="utf-8") as f:
#     content = f.read()
# print(f"Simvol sayı: {len(content)}")


# 14.  Filter and print empty lines from a file.
# with open("metn.txt", "r", encoding="utf-8") as f:
#     for setir in f:
#         if setir.strip() == "":
#             print("[boş sətir tapıldı]")


# 15.  Print only lines that start with a specific letter.
# herf = "P"
# with open("metn.txt", "r", encoding="utf-8") as f:
#     for setir in f:
#         if setir.startswith(herf):
#             print(setir.strip())


# 16. Create a new file and write multiple lines into it.
# with open("yeni_fayl.txt", "w", encoding="utf-8") as f:
#     f.write("Birinci sətir\n")
#     f.write("İkinci sətir\n")
#     f.write("Üçüncü sətir\n")
# print("Fayl yaradıldı!")


# 17. Write elements of a list into a file (each on a new line).
# meyveler = ["alma", "armud", "üzüm", "gilas"]
# with open("meyveler.txt", "w", encoding="utf-8") as f:
#     for meyve in meyveler:
#         f.write(meyve + "\n")


# 18. Copy content from one file to another.
# with open("metn.txt", "r", encoding="utf-8") as oxu:
#     content = oxu.read()

# with open("kopya.txt", "w", encoding="utf-8") as yaz:
#     yaz.write(content)
# print("Kopya yaradıldı!")


# 19.  Convert all file content to uppercase and rewrite it.
# with open("metn.txt", "r", encoding="utf-8") as f:
#     content = f.read()

# with open("metn.txt", "w", encoding="utf-8") as f:
#     f.write(content.upper())

# print("Mətn böyük hərflərə çevrildi!")


# 20. Replace all "a" characters with "@" in a file.

# with open("metn.txt", "r", encoding="utf-8") as f:
#     content = f.read()
# yeni_content = content.replace("a", "@")

# with open("metn.txt", "w", encoding="utf-8") as f:
#     f.write(yeni_content)
# print("Əvəzetmə tamamlandı!")


# 21. Check if a file exists using the os module
# import os

# fayl_adi = "metn.txt"
# if os.path.exists(fayl_adi):
#     print(f"'{fayl_adi}' mövcuddur.")
# else:
#     print(f"'{fayl_adi}' tapılmadı.")


# 22. Try opening a non-existing file and handle the error.
# try:
#     with open("yoxdur.txt", "r") as f:
#         content = f.read()
# except FileNotFoundError:
#     print("Xəta: Fayl tapılmadı!")


# 23.  Use try-except to handle errors when reading a file.
# try:
#     with open("metn.txt", "r", encoding="utf-8") as f:
#         content = f.read()
#     print(content)
# except FileNotFoundError:
#     print("Fayl tapılmadı!")
# except PermissionError:
#     print("Bu faylı oxumağa icazəniz yoxdur!")
# except Exception as e:
#     print(f"Gözlənilməz xəta: {e}")


# 24. Use finally to ensure the file is closed.
# f = None
# try:
#     f = open("metn.txt", "r", encoding="utf-8")
#     content = f.read()
#     print(content)
# except FileNotFoundError:
#     print("Fayl tapılmadı!")
# finally:
#     if f:
#         f.close()
#         print("Fayl bağlandı.")


# 25. Use encoding="utf-8" when opening a file and explain why
# with open("metn.txt", "r", encoding="utf-8") as f:
#     content = f.read()
# print(content)


# 26. Print file lines in reverse order.
# with open("metn.txt", "r", encoding="utf-8") as f:
#     setirler = f.readlines()

# for setir in reversed(setirler):
#     print(setir.strip())


# 27. Find the longest line in a file.

# with open("metn.txt", "r", encoding="utf-8") as f:
#     setirler = f.readlines()

# en_uzun = max(setirler, key=len)
# print(f"Ən uzun sətir: {en_uzun.strip()}")
# print(f"Uzunluğu: {len(en_uzun.strip())} simvol")


# 28. Find the shortest line in a file.
# with open("metn.txt", "r", encoding="utf-8") as f:
#     setirler = [s.strip() for s in f if s.strip()]

# en_qisa = min(setirler, key=len)
# print(f"Ən qısa sətir: {en_qisa}")
# print(f"Uzunluğu: {len(en_qisa)} simvol")


# 29. Extract unique words from a file using a set.
# with open("metn.txt", "r", encoding="utf-8") as f:
#     content = f.read().lower()

# sozler = content.split()
# unikal = set(sozler)
# print(f"Unikal söz sayı: {len(unikal)}")
# print(unikal)


# 30. Count word frequency in a file using a dictionary.
# with open("metn.txt", "r", encoding="utf-8") as f:
#     content = f.read().lower()

# sozler = content.split()
# tezlik = {}
# for soz in sozler:
#     tezlik[soz] = tezlik.get(soz, 0) + 1

# sorted_tezlik = sorted(tezlik.items(), key=lambda x: x[1], reverse=True)
# for soz, say in sorted_tezlik[:5]:
#     print(f"{soz}: {say} dəfə")


# 31. Extract only numbers from a file and store them in a list.
# reqemler = []
# with open("metn.txt", "r", encoding="utf-8") as f:
#     for setir in f:
#         for soz in setir.split():
#             if soz.isdigit():
#                 reqemler.append(int(soz))
# print(f"Tapılan rəqəmlər: {reqemler}")


# 32. Sort file lines alphabetically and write to a new file.
# with open("metn.txt", "r", encoding="utf-8") as f:
#     setirler = f.readlines()

# setirler.sort()

# with open("sirali.txt", "w", encoding="utf-8") as f:
#     f.writelines(setirler)

# print("Sıralı fayl yaradıldı!")


# 33.  Read file content using list comprehension.
# with open("metn.txt", "r", encoding="utf-8") as f:
#     setirler = [setir.strip() for setir in f]

# print(setirler)


# 34.  Strip whitespace from each line in a file.
# with open("metn.txt", "r", encoding="utf-8") as f:
#     for setir in f:
#         temiz = setir.strip()
#         print(temiz)


# 35. Calculate the sum of all numbers in a file.
# cem = 0
# with open("metn.txt", "r", encoding="utf-8") as f:
#     for setir in f:
#         for soz in setir.split():
#             if soz.isdigit():
#                 cem += int(soz)
# print(f"Bütün rəqəmlərin cəmi: {cem}")


# 36. Open a file in binary mode ("rb") and read it
# with open("metn.txt", "rb") as f:
#     data = f.read()
# print(data)
# print(type(data))


# 37. Write data to a file in binary mode ("wb").
# metn = "Salam, dünya!"
# data = metn.encode("utf-8")  # string → bytes

# with open("binary_fayl.bin", "wb") as f:
#     f.write(data)

# print("Binary fayl yazıldı!")


# 38. Use tell() to get the current file pointer position.
# with open("metn.txt", "r", encoding="utf-8") as f:
#     print(f"Başlanğıc: {f.tell()}")  # 0
#     f.read(5)
#     print(f"5 simvol sonra: {f.tell()}")
#     f.readline()
#     print(f"Bir sətir sonra: {f.tell()}")


# 39. Use seek() to move to a specific position in a file.
# with open("metn.txt", "rb") as f:
#     f.seek(10)
#     content = f.read()
#     print(content)

#     f.seek(0)
#     print(f.read(5))


# 40.  Read only the first 10 characters of a file
# with open("metn.txt", "r", encoding="utf-8") as f:
#     ilk_10 = f.read(10)
# print(ilk_10)

