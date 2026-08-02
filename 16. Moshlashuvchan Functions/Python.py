"""
MAVZU: *args va **kwargs (Python Functions)
Quyidagi misollar *args va **kwargs tushunchalarini
clean code va o‘qitish uchun qulay tartibda tushuntiradi.
"""

# ======================================================
# 1️⃣ *args — ISTALGANCHA POZITSION ARGUMENT
# ======================================================


def print_sonlar(*args):
    """Qabul qilingan barcha sonlarni tuple ko‘rinishida chiqaradi"""
    print(args)


print_sonlar(1, 2, 3)  # (1, 2, 3)


# Qachon ishlatiladi:
# - Argumentlar soni oldindan noma’lum bo‘lsa
# - Funksiya universal bo‘lishi kerak bo‘lsa


# ======================================================
# 2️⃣ *args BILAN YIG‘INDI HISOBLASH
# ======================================================


def yigindi(*sonlar):
    """Berilgan barcha sonlarning yig‘indisini qaytaradi"""
    jami = 0
    for son in sonlar:
        jami += son
    return jami


print(yigindi(1))
print(yigindi(1, 2, 3, 4))


# ======================================================
# 3️⃣ ODDIY PARAMETR + *args
# ======================================================


def test_args(a, b, *args):
    print("a:", a)
    print("b:", b)
    print("args:", args)


test_args(1, 2, 3, 4, 5)
# a=1, b=2, args=(3, 4, 5)


# ======================================================
# 4️⃣ **kwargs — NOMLANGAN ARGUMENTLAR
# ======================================================


def print_info(**kwargs):
    """Barcha nomlangan argumentlarni dictionary ko‘rinishida chiqaradi"""
    print(kwargs)


print_info(ism="Ali", yosh=20)


# ======================================================
# 5️⃣ **kwargs BILAN MA’LUMOT CHIQARISH
# ======================================================


def foydalanuvchi(**malumot):
    for kalit, qiymat in malumot.items():
        print(f"{kalit} => {qiymat}")


foydalanuvchi(ism="Ali", yosh=20, shahar="Toshkent")


# ======================================================
# 6️⃣ ODDIY PARAMETR + **kwargs
# ======================================================


def test_kwargs(a, **kwargs):
    print("a:", a)
    print("kwargs:", kwargs)


test_kwargs(10, x=5, y=7)


# ======================================================
# ⚠️ QOIDALAR
# ======================================================
# - **kwargs har doim oxirida bo‘ladi
# - *args **kwargs dan oldin yoziladi
# - Tartib: oddiy -> *args -> **kwargs


# ======================================================
# 7️⃣ *args VA **kwargs BIRGA ISHLATISH
# ======================================================


def test_all(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)


test_all(1, 2, 3, 4, x=10, y=20)


# ======================================================
# 8️⃣ REAL MISOL: BUYURTMA TIZIMI
# ======================================================


def buyurtma(nomi, *tovarlar, **malumot):
    print("Buyurtmachi:", nomi)
    print("Tovarlar:", ", ".join(tovarlar))
    print("Manzil:", malumot.get("manzil"))
    print("Telefon:", malumot.get("telefon"))


buyurtma("Ali", "Olma", "Banan", "Uzum", manzil="Toshkent", telefon="99890...")
