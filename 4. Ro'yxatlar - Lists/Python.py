"""
=====================================
          📘 LISTS (RO‘YXATLAR)
=====================================

List — bu Python’da bir nechta qiymatlarni bitta o‘zgaruvchida saqlash uchun ishlatiladigan ma’lumot turi.
Masalan: ismlar, shaharlar, raqamlar va hokazo.
"""

# 🔹 1. Oddiy ro‘yxatlar
names = ["Ali", "Vali", "Sardor", "Malika", "Dilnoza"]
cities = ["Toshkent", "Samarqand", "Buxoro", "Namangan", "Andijon"]
subjects = ["Matematika", "Fizika", "Informatika", "Kimyo", "Tarix"]
jobs = ["Dasturchi", "Shifokor", "O‘qituvchi", "Muhandis", "Dizayner"]

# 🔹 Sonlar bilan ishlovchi ro‘yxatlar
numbers = list(range(1, 21))  # 1 dan 20 gacha sonlar
floats = [3.14, 0.99, 2.71, 10.5, 1.618]



"""
=====================================
     🎯 ELEMENTLARGA MUROJAAT QILISH
=====================================
"""

# print(names[0])       # Birinchi elementni chiqaradi → "Ali"
# print(cities[-1])     # Oxirgi elementni chiqaradi → "Andijon"
# print(subjects[1:4])  # 1–3 indeks oralig‘idagi elementlar
# print(numbers[::3])   # Har 3-elementni chiqaradi



"""
=====================================
     ➕ ELEMENT QO‘SHISH USULLARI
=====================================
"""

# append() → oxiriga element qo‘shadi
# names.append("Toxir")
# jobs.append("Santexnik")
# print(names, jobs)

# insert() → indeks bo‘yicha element qo‘shadi
# subjects.insert(0, "Huquq")
# numbers.insert(0, -1)
# print(subjects, numbers)

# extend() → bir nechta elementlarni birdan qo‘shish
# floats.extend([1.5, 5.6, 7.4, 23.17])
# jobs.extend(["Quruvchi", "Dehqon", "Nonvoy", "Asalarichi"])
# print(floats, jobs)



"""
=====================================
      ❌ ELEMENTLARNI O‘CHIRISH
=====================================
"""

# remove() → qiymat bo‘yicha o‘chirish
# names.remove("Ali")
# print(names)

# pop() → oxirgi elementni o‘chiradi
# jobs.pop()
# print(jobs)

# pop(index) → indeks bo‘yicha o‘chiradi
# subjects.pop(3)
# print(subjects)

# del → indeks yoki interval bo‘yicha o‘chirish
# del numbers[1:3]
# print(numbers)

# clear() → ro‘yxatni to‘liq tozalaydi
# floats.clear()
# print(floats)



"""
=====================================
       🔍 QIDIRISH VA TEKSHIRISH
=====================================
"""

fruits = ["Olma", "Banan", "Uzum", "Olma"]

# print("Olma" in fruits)     # True — mavjudligini tekshirish
# print(fruits.index("Uzum")) # "Uzum" elementining indeksini topish
# print(fruits.count("Olma")) # "Olma" necha marta qatnashganini sanash



"""
=====================================
       📊 TARTIBLASH (SORTING)
=====================================
"""

numbers = [5, 6, 7, 14, 3, 4, 8, 9, 10, 1, 2, 11, 12, 13, 16, 15, 17, 18, 19, 20]

# numbers.sort()                # O‘sish tartibida saralash
# print(numbers)

# numbers.sort(reverse=True)    # Kamayish tartibida saralash
# print(numbers)

# fruits.reverse()              # Tartibni teskari qilish
# print(fruits)



"""
=====================================
         📋 NUSXA OLISH
=====================================
"""

new_fruits = fruits.copy()  # Asl ro‘yxatni o‘zgartirmasdan nusxa olish
print(new_fruits)
