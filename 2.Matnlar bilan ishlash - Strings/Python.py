# ===============================
# STRINGLAR BILAN ISHLASH
# O'zbek tilida to'liq ismni shakllantirish va string usullari
# ===============================
print("=== 1-Bo'lim: To'liq ismni shakllantirish ===")

# O'zgaruvchilarni aniqlash
ism = "Ali"
familya = "Sobirov"
otasi = "Hoshim"
ogil = "o'g'li"
qiz = "qizi"

# To'liq ismni f-string yordamida shakllantirish (o'g'il)
toliq_ism = f"{ism} {familya} {otasi} {ogil}"
print("To'liq ism (o'g'il):", toliq_ism)

# Boshqa misol: qiz uchun to'liq ism
ism = "Zilola"
familya = "Qodirova"
otasi = "Jamshid"
toliq_ism = f"{ism} {familya} {otasi} {qiz}"
print("To'liq ism (qiz):", toliq_ism)

# ===============================
print("\n=== 2-Bo'lim: Matn elementlarini chiqarish ===")

# Ma'lum bir elementni indeks orqali chiqarish
ism = "Zilola"
print(f"Ism: {ism}")
for i in range(len(ism)):
    print(f"Indeks {i}: {ism[i]}")

# ===============================
print("\n=== 3-Bo'lim: String usullari ===")

# 1. Matn uzunligini aniqlash
print("\nMatn uzunligi:")
matn = "Zilola"
print(f"'{matn}' uzunligi: {len(matn)}")

# 2. Boshqa ma'lumot turlarini stringga o'tkazish
print("\nRaqamni stringga o'tkazish:")
raqam = 123  # int turi
matn = str(raqam)
print(f"Raqam: {matn}, turi: {type(matn)}")

# 3. Barcha harflarni katta harfga aylantirish
print("\nKatta harfga aylantirish:")
matn = "salom"
print(f"Asl matn: {matn}")
print(f"Katta harf: {matn.upper()}")

# 4. Barcha harflarni kichik harfga aylantirish
print("\nKichik harfga aylantirish:")
matn = "SALOM"
print(f"Asl matn: {matn}")
print(f"Kichik harf: {matn.lower()}")

# 5. Har bir so'zning birinchi harfini katta harfga aylantirish
print("\nSo'zlarning birinchi harfini katta qilish:")
matn = "salom dunyo"
print(f"Asl matn: {matn}")
print(f"Title usuli: {matn.title()}")

# 6. Faqat birinchi harfni katta qilish
print("\nFaqat birinchi harfni katta qilish:")
matn = "dunyoni alishmasman boshqa jahonga"
print(f"Asl matn: {matn}")
print(f"Capitalize usuli: {matn.capitalize()}")

# 7. Matnning boshida va oxiridagi bo'shliqlarni olib tashlash
print("\nBo'shliqlarni olib tashlash (strip):")
matn = "   o'zbekiston tengur o'zbekistonga   "
print(f"Asl matn: '{matn}'")
print(f"Strip usuli: '{matn.strip()}'")

# 8. Faqat boshidagi bo'shliqlarni olib tashlash
print("\nFaqat boshidagi bo'shliqlarni olib tashlash (lstrip):")
matn = "   salom   "
print(f"Asl matn: '{matn}'")
print(f"Lstrip usuli: '{matn.lstrip()}'")

# 9. Faqat oxiridagi bo'shliqlarni olib tashlash
print("\nFaqat oxiridagi bo'shliqlarni olib tashlash (rstrip):")
matn = "   salom   "
print(f"Asl matn: '{matn}'")
print(f"Rstrip usuli: '{matn.rstrip()}'")

# 10. Matndagi belgi yoki so'zni almashtirish
print("\nSo'zni almashtirish (replace):")
matn = "Salom, dunyo!"
yangi = matn.replace("dunyo", "olam")
print(f"Asl matn: {matn}")
print(f"Almashtirilgan: {yangi}")

# 11. Matnni so'zlarga ajratish
print("\nMatnni so'zlarga ajratish (split):")
matn = "salom dunyo olam"
sozlar = matn.split()
print(f"Asl matn: {matn}")
print(f"So'zlar ro'yxati: {sozlar}")
