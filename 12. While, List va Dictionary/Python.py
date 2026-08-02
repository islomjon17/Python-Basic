"""
MAVZU: Python-da while tsikli, List va Dictionary bilan ishlash
Ushbu faylda while tsikli yordamida ro'yxatlar va lug'atlar bilan ishlash
bo‘yicha tartibli va clean code misollar keltirilgan.
"""

# ======================================================
# 1-QISM: WHILE TSIKLI VA RO'YXATLAR (LIST)
# ======================================================

print("=== 1-Misol: Foydalanuvchilarni tasdiqlash ===")

tasdiqlanmaganlar = ["ali", "vali", "hasan", "husan"]
tasdiqlanganlar = []

while tasdiqlanmaganlar:
    foydalanuvchi = tasdiqlanmaganlar.pop()
    print(f"Tasdiqlanmoqda: {foydalanuvchi.title()}")
    tasdiqlanganlar.append(foydalanuvchi)

print("\nTasdiqlangan foydalanuvchilar:")
for foydalanuvchi in tasdiqlanganlar:
    print(foydalanuvchi.title())


# ======================================================
# 2-Misol: Ro'yxatdan ma'lum qiymatni to'liq o‘chirish
# ======================================================

print("\n=== 2-Misol: Ro'yxatdan 'it' ni o‘chirish ===")

uy_hayvonlari = ["it", "mushuk", "quyon", "it", "baliq", "it"]
print("Boshlang‘ich ro‘yxat:", uy_hayvonlari)

while "it" in uy_hayvonlari:
    uy_hayvonlari.remove("it")

print("Yangilangan ro‘yxat:", uy_hayvonlari)


# ======================================================
# 2-QISM: WHILE TSIKLI VA LUG'ATLAR (DICTIONARY)
# ======================================================

print("\n=== 3-Misol: Do‘stlar lug‘atini to‘ldirish ===")

dostlar = {}
davom_etadi = True

while davom_etadi:
    ism = input("\nDo‘stingizning ismini kiriting: ")
    yosh = int(input(f"{ism.title()}ning yoshini kiriting: "))

    dostlar[ism] = yosh

    javob = input("Yana qo‘shasizmi? (ha/yo‘q): ").lower()
    if javob == "yo‘q":
        davom_etadi = False

print("\nDo‘stlar ro‘yxati:")
for ism, yosh in dostlar.items():
    print(f"{ism.title()} — {yosh} yosh")


# ======================================================
# 3-QISM: LIST + DICTIONARY (BUYURTMALAR TIZIMI)
# ======================================================

print("\n=== 4-Misol: Buyurtmalar tizimi ===")

buyurtmalar = {}
print("Buyurtma qabul qilish boshlandi.")

while True:
    mahsulot = input("\nMahsulot nomi: ")
    narx = float(input(f"{mahsulot.title()} narxi (so‘m): "))

    buyurtmalar[mahsulot] = narx

    davom = input("Yana buyurtma berasizmi? (ha/yo‘q): ").lower()
    if davom != "ha":
        break

print("\nSizning buyurtmalaringiz:")
jami = 0

for mahsulot, narx in buyurtmalar.items():
    print(f"{mahsulot.title()}: {narx} so‘m")
    jami += narx

print(f"\nJami summa: {jami} so‘m")
