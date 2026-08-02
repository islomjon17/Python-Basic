"""
🏠 UYGA VAZIFA — "LISTLAR" (darsda o‘tilgan amallar asosida)
1️⃣ — Indexing bilan ishlash

names ro‘yxatining:

birinchi elementini,

oxirgi elementini,

va 2-4 elementlarini chiqaring.

2️⃣ — append()

cities ro‘yxatiga "Xiva" shahrini qo‘shing.
Natijani ekranga chiqaring.

3️⃣ — insert()

subjects ro‘yxatining boshiga "Huquq" fanini,
oxiriga "Jismoniy tarbiya" fanini qo‘shing.
So‘ng ro‘yxatni chop eting.

4️⃣ — extend()

jobs ro‘yxatiga quyidagi kasblarni bir vaqtda qo‘shing:
["Dehqon", "Nonvoy", "Quruvchi"]

Natijani ekranga chiqaring.

5️⃣ — remove() va pop()

names ro‘yxatidan "Ali" ismini o‘chiring (remove() bilan).
Keyin oxirgi elementni (pop()) yordamida olib tashlang.
Qolgan ro‘yxatni chop eting.

6️⃣ — del va clear()

numbers ro‘yxatidan 2-5 indeks oralig‘idagi elementlarni o‘chiring (del numbers[2:6]).
Keyin floats ro‘yxatini butunlay tozalang (clear() bilan).
Ikkalasining natijasini chop eting.

7️⃣ — in, index(), count()

fruits ro‘yxatida "Olma" so‘zi bor-yo‘qligini tekshiring (in yordamida).
Agar mavjud bo‘lsa, uning indeksini (index()) va nechta ekanini (count()) chiqaring.

8️⃣ — sort() va reverse()

numbers ro‘yxatini avval o‘sish tartibida (sort()),
so‘ngra kamayish tartibida (sort(reverse=True)) chiqaring.
Shuningdek, fruits.reverse() qilib, teskari tartibni ko‘rsating.

9 — copy()

fruits ro‘yxatining nusxasini oling (copy() bilan)
va new_fruits nomli yangi o‘zgaruvchiga saqlang.
So‘ng fruits ga yangi element qo‘shing va har ikki ro‘yxatni solishtiring.

🔟 — Slicing (kesish)

numbers ro‘yxatidan:

faqat birinchi 5 ta elementni,

faqat oxirgi 5 ta elementni,

va har 2-elementni (numbers[::2]) alohida chiqaring.
"""
# 1️⃣ — Indexing bilan ishlash

# names ro‘yxatining:

# birinchi elementini,

# oxirgi elementini,

# va 2-4 elementlarini chiqaring.

names = ["Islomjon","Ali","Nodir","Komil","Jahongir",]
# print(names[0], names[-1], names[1], names[3], )

# 2️⃣ — append()

# cities ro‘yxatiga "Xiva" shahrini qo‘shing.
# Natijani ekranga chiqaring.

cities = ["toshkent","namangan","andijon","buxoro","surxondaryo","qoqon",]
# cities.append("Xiva")
# print(cities)

# 3️⃣ — insert()

# subjects ro‘yxatining boshiga "Huquq" fanini,
# oxiriga "Jismoniy tarbiya" fanini qo‘shing.
# So‘ng ro‘yxatni chop eting.
subjects = ["ona tili","adabiyot","tarix","biologiya"]
# subjects.insert(0,'huquq')
# subjects.append('Jismoniy tarbiya')
# print(subjects)

# 4️⃣ — extend()

# jobs ro‘yxatiga quyidagi kasblarni bir vaqtda qo‘shing:
# ["Dehqon", "Nonvoy", "Quruvchi"]

# Natijani ekranga chiqaring.
jobs = ["mashenik", "usta", "quruvchi"]
# jobs.extend(["Dehqon", "Nonvoy", "Quruvchi"])
# print(jobs)


# 5️⃣ — remove() va pop()

# names ro‘yxatidan "Ali" ismini o‘chiring (remove() bilan).
# Keyin oxirgi elementni (pop()) yordamida olib tashlang.
# Qolgan ro‘yxatni chop eting.
# names.remove("Ali")
# names.pop()
# print(names)


# 6️⃣ — del va clear()

# numbers ro‘yxatidan 2-5 indeks oralig‘idagi elementlarni o‘chiring (del numbers[2:6]).
# Keyin floats ro‘yxatini butunlay tozalang (clear() bilan).
# Ikkalasining natijasini chop eting.

numbers = [1,2,14,3,4,5,13,6,7,8,15,16,9,10,11,12,17,1,2,14,3,4,5,13,18,19,20]
# del numbers[2:6]
# print(numbers)
# numbers.clear()
# print(numbers)


# 7️⃣ — in, index(), count()

# fruits ro‘yxatida "Olma" so‘zi bor-yo‘qligini tekshiring (in yordamida).
# Agar mavjud bo‘lsa, uning indeksini (index()) va nechta ekanini (count()) chiqaring.


fruits = ["Olma", "Banan", "Uzum", "Olma"]

# print("Olma" in fruits)    
# print(fruits.index("Olma"))
# print(fruits.count("Olma"))


# 8️⃣ — sort() va reverse()

# numbers ro‘yxatini avval o‘sish tartibida (sort()),
# so‘ngra kamayish tartibida (sort(reverse=True)) chiqaring.
# Shuningdek, fruits.reverse() qilib, teskari tartibni ko‘rsating.
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)


# 9 — copy()

# fruits ro‘yxatining nusxasini oling (copy() bilan)
# va new_fruits nomli yangi o‘zgaruvchiga saqlang.
# So‘ng fruits ga yangi element qo‘shing va har ikki ro‘yxatni solishtiring.
# new_fruits = fruits.copy()
# print(new_fruits)

# 🔟 — Slicing (kesish)

# numbers ro‘yxatidan:

# faqat birinchi 5 ta elementni,

# faqat oxirgi 5 ta elementni,

# va har 2-elementni (numbers[::2]) alohida chiqaring.

print("Birinchi 5 ta element:", numbers[:5])
print("Oxirgi 5 ta element:", numbers[-5:])
print("Har 2-element:", numbers[::2])
