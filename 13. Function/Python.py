"""
MAVZU: Python funksiyalari (Functions)
Ushbu faylda funksiyalar bo‘yicha eng muhim tushunchalar
"""

# ======================================================
# 1. ODDIY FUNKSIYA
# ======================================================


def salom():
    print("Hello")


salom()


# ======================================================
# 2. ARGUMENT (PARAMETRLI FUNKSIYA)
# ======================================================


def salom_ber(ism):
    print(f"Salom {ism}")


salom_ber("Nodir")


# ======================================================
# 3. BIR NECHTA PARAMETR
# ======================================================


def yigindi(a, b):
    print(a + b)


yigindi(1, 2)


# ======================================================
# 4. RETURN (QIYMAT QAYTARISH)
# ======================================================


def kvadrat(x):
    return x * x


natija = kvadrat(5)
print(natija)


# ======================================================
# 5. DEFAULT (STANDART) QIYMAT
# ======================================================


def salom_default(ism="Mehmon"):
    print(f"Salom {ism}")


salom_default()
salom_default("Ali")


# ======================================================
# 6. LAMBDA FUNKSIYA (KICHIK FUNKSIYA)
# ======================================================

kvadrat_lambda = lambda x: x * x
print(kvadrat_lambda(6))


# ======================================================
# 7. GLOBAL VA LOCAL O‘ZGARUVCHI
# ======================================================

x = 10  # global


def local_test():
    x = 5  # local
    print("Local x:", x)


def global_test():
    global x
    x = 5


local_test()
global_test()
print("Global x:", x)


# ======================================================
# 8. DOCSTRING (FUNKTsiYA IZOHI)
# ======================================================


def qosh(a, b):
    """Ikki sonni qo‘shib, natijani qaytaradi"""
    return a + b


print(qosh(3, 4))


# ======================================================
# 9. FUNKSIYANI PARAMETR SIFATIDA UZATISH
# ======================================================


def salom_f():
    print("Salom!")


def chaqir(funksiya):
    funksiya()


chaqir(salom_f)


# ======================================================
# 10. REKURSIYA (FUNKSiyaning o‘zini chaqirishi)
# ======================================================


def faktorial(n):
    if n == 1:
        return 1
    return n * faktorial(n - 1)


print(faktorial(5))


# ======================================================
# 11. *args (ISTALGANCHA ARGUMENT)
# ======================================================


def yigindi_args(*sonlar):
    return sum(sonlar)


print(yigindi_args(1, 2, 3, 4))


# ======================================================
# 12. **kwargs (NOMLANGAN ARGUMENTLAR)
# ======================================================


def info(**malumot):
    for kalit, qiymat in malumot.items():
        print(f"{kalit}: {qiymat}")


info(ism="Ali", yosh=20, shahar="Toshkent")
