# ==========================================================
# 1. Oddiy if
# ==========================================================
age = 20
if age >= 20:
    print("18 dan kattasiz")

print("\n---------------------------\n")


# ==========================================================
# 2. If + else
# ==========================================================
age = 10
if age < 18:
    print("Kirish mumkin emas")
else:
    print("Kirish mumkin")

print("\n---------------------------\n")


# ==========================================================
# 3. If + elif + else
# ==========================================================
ball = 85

if ball >= 90:
    print("A")
elif ball >= 80:
    print("B")
elif ball >= 70:
    print("C")
else:
    print("Yomon natija")

print("\n---------------------------\n")


# ==========================================================
# 4. AND operatori
# ==========================================================
age = 10
has_passport = True

if age >= 18 and has_passport:
    print("Safarga chiqishingiz mumkin")

print("\n---------------------------\n")


# ==========================================================
# 5. OR operatori
# ==========================================================
day = "Shanba"

if day == "Yakshanva" or day == "Shanba":
    print("Bugun dam olish kuni")

print("\n---------------------------\n")


# ==========================================================
# 6. NOT operatori
# ==========================================================
logged_in = False

if not logged_in:
    print("Avvazl tizimga kiring")

print("\n---------------------------\n")


# ==========================================================
# 7. Solishtirish operatorlari
# ==========================================================
a = 10
b = 5

if a > b:
    print("a katta")

print("\n---------------------------\n")


# ==========================================================
# 8. Nested (ichma-ich) if
# ==========================================================
age = 20
country = "Uzbekistan"

if age >= 20:
    if country == "Uzbekistan":
        print("Ovoz berishingiz mumkin")

print("\n---------------------------\n")


# ==========================================================
# 9. Bir qatordagi if (short if)
# ==========================================================
age = 20
print("Voyaga yetgan") if age >= 18 else print("Voyaga yetmagan")

print("\n---------------------------\n")


# ==========================================================
# 10. Ro'yxatda bor-yo'qligini tekshirish
# ==========================================================
countries = ["Uzbekistan", "Japan", "Korea"]

if "Japan" in countries:
    print("Japan ro'yxatda bor")

print("\n---------------------------\n")


# ==========================================================
# 11. Bo'sh qiymatni tekshirish
# ==========================================================
user_input = ""

if not user_input:
    print("Maydon bo'sh!")

print("\n---------------------------\n")


# ==========================================================
# 12. Tipni tekshirish
# ==========================================================
x = 5

if type(x) == int:
    print("Bu integer")

print("\n---------------------------\n")


# ==========================================================
# 13. Bir nechta shartni bir qatorda tekshirish
# ==========================================================
x = 10

if 0 < x < 20:
    print("x 0 va 20 orasida")

print("\n---------------------------\n")


# ==========================================================
# 14. Murakkab shartlar
# ==========================================================
ism = "Ali"
yosh = 20
ball = 85

if (ism == "Ali" and yosh > 18) or ball > 80:
    print("Qabul qilindingiz!")

print("\n---------------------------\n")


# ==========================================================
# 15. Boolean tekshirish
# ==========================================================
is_active = True

if is_active:
    print("Foydalanuvchi faol")

print("\n---------------------------\n")


# ==========================================================
# 16. Lug‘at (dictionary) bilan if
# ==========================================================
talaba = {"ism": "Sardor", "yosh": 17}

if talaba["yosh"] >= 18:
    print("Ro'yxatdan o'tdi")
else:
    print("Hali 18 yoshga to'lmagan")

print("\n---------------------------\n")


# ==========================================================
# 17. try/except + if
# ==========================================================
x = "5"

try:
    son = int(x)
    if son > 0:
        print("Musbat son")
except:
    print("Son kiritilmadi")

print("\n---------------------------\n")


# ==========================================================
# 18. If funksiyada ishlatilishi
# ==========================================================
def tekshir(yosh):
    if yosh >= 18:
        return "Kirish mumkin"
    else:
        return "Kirish mumkin emas"


print(tekshir(17))

print("\n---------------------------\n")


# ==========================================================
# 19. Menyu misoli
# ==========================================================
tanlov = 2

if tanlov == 1:
    print("O'yin boshlandi")
elif tanlov == 2:
    print("Davom ettirildi")
elif tanlov == 3:
    print("Tugatildi")

print("\n---------------------------\n")


# ==========================================================
# 20. If har qanday musbat sonni True deb hisoblaydi
# ==========================================================
if 10:
    print("True bo‘ladi, chunki har qanday >0 son True")

