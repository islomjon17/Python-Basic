

""" 
Topshiriqlar haqida qisqacha izoh:

1. To‘liq ism formatlash: Foydalanuvchidan ma’lumot olib, f-string yordamida to‘liq ismni shakllantirish.
2. Katta harfga aylantirish: Matnni .upper() yordamida katta harfga o‘zgartirish.
3. Matn uzunligi: len() funksiyasi yordamida matn uzunligini aniqlash.
4. So‘zlar sonini aniqlash: split() yordamida matnni so‘zlarga ajratib, ularni sanash.
5. Teskari matn: Slicing ([::-1]) yordamida matnni teskari chiqarish.
6. So'z almashtirish: replace() funksiyasi yordamida matndagi So'zlarni almashtirish.
7. So‘zlarni ro‘yxat sifatida chiqarish: split() bilan so‘zlarni alohida qatorlarda chiqarish.
8. Faqat raqamlarni ajratish: List comprehension yordamida matndan raqamlarni olish.
"""
# # 1
# ism = input(str("Ismingizni kiriting: "))
# familiya = input(str("Familyangizni kiriting: "))
# print(f"Sizning to'liq ismingiz {ism.title()}, {familiya.title()}")
# 2
# matn = input(str("Istalgan matnni kiriting: "))
# print(f"Siz kiritgan matn {matn.upper()}")
# 3
# matn = input(str("Istalgan matnni kiriting: "))
# print(f"Siz kiritgan matnning uzunligi {len(matn)}")
# 4
# matn = input("Istalgan matnni kiriting: ")
# print(f"Siz kiritgan matnda {len(matn.split())} ta so'z bor")
# 5
# matn = input("Istalgan matnni kiriting: ")
# print(f"Siz kiritgan matnning teskari yozilishi: {matn[::-1]}")
# 6
# matn = "Salom dunyo, dunyo salom"
# print(matn.replace("dunyo", "yer"))
# 7
# matn = input("Istalgan matnni kiriting: ")
# print('\n'.join(matn.split()))
# 8
# matn = input("Matn kiriting: ")
# raqamlar = "".join(filter(str.isdigit, matn))
# print(raqamlar)

