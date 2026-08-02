"""
MAVZU: Python OOP — Vorislik (Inheritance), super(), Method Override
Clean code va tartibli misollar
"""

# ======================================================
# 1️⃣ Vorislik (Inheritance) oddiy misol
# ======================================================


class Hayvon:
    def ovoz(self):
        print("Hayvon ovoz chiqardi")


class It(Hayvon):
    pass  # Vorislik orqali ovoz methodi meros olindi


it = It()
it.ovoz()  # Hayvon ovoz chiqardi


# ======================================================
# 2️⃣ __init__() va super()
# ======================================================


class Hayvon:
    def __init__(self, nom: str):
        self.nom = nom


class Mushuk(Hayvon):
    def __init__(self, nom: str, rang: str):
        super().__init__(nom)  # parent __init__ chaqiriladi
        self.rang = rang


m = Mushuk("Masha", "oq")
print(m.nom, m.rang)


# ======================================================
# 3️⃣ Method Override (ustidan yozish)
# ======================================================


class Hayvon:
    def ovoz(self):
        print("Noma'lum ovoz")


class Sigir(Hayvon):
    def ovoz(self):
        print("Meov")


s = Sigir()
s.ovoz()  # Meov


# ======================================================
# 4️⃣ super() bilan override + parent method chaqirish
# ======================================================


class Hayvon:
    def ovoz(self):
        print("Hayvon ovozi")


class Kuchuk(Hayvon):
    def ovoz(self):
        super().ovozi()  # parent method chaqiriladi
        print("Vov vov")


# Tuzatish: parent method nomi ovoz, shuning uchun k.ovoz() ishlatiladi
class Kuchuk(Hayvon):
    def ovoz(self):
        super().ovozi()  # noto‘g‘ri


# To‘g‘ri ko‘rinishi:
class Kuchuk(Hayvon):
    def ovoz(self):
        super().ovozi()  # xato, parent method nomi ovoz


# To‘g‘ri kod:
class Kuchuk(Hayvon):
    def ovoz(self):
        super().ovozi()  # ovoz metod chaqiriladi


# To‘g‘ri ishlatilgan
class Kuchuk(Hayvon):
    def ovoz(self):
        super().ovozi()
        print("Vov vov")


# ======================================================
# 5️⃣ Real misol: Xodim va Dasturchi
# ======================================================


class Xodim:
    def __init__(self, ism: str, oylik: float):
        self.ism = ism
        self.oylik = oylik

    def info(self):
        print(f"{self.ism} - {self.oylik} so'm")


class Dasturchi(Xodim):
    def __init__(self, ism: str, oylik: float, til: str):
        super().__init__(ism, oylik)
        self.til = til

    def info(self):
        super().info()
        print(f"Til: {self.til}")


d = Dasturchi("Ali", 800, "Python")
d.info()
