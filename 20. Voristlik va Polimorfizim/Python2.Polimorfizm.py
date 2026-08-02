"""
MAVZU: Python OOP — Polimorfizm (Polymorphism)
Clean code va tartibli misollar
"""

# ======================================================
# 1️⃣ Polimorfizm tushunchasi
# ======================================================

"""
Polimorfizm — bitta nomdagi metod turli obyektlarda turlicha ishlaydi.
Ma’nosi: “bitta interfeys — turli xatti-harakat”
"""


# ======================================================
# 2️⃣ Vorislik orqali polimorfizm
# ======================================================


class Hayvon:
    def ovoz(self):
        print("Hayvon ovozi")


class It(Hayvon):
    def ovoz(self):
        print("Vov")


class Mushuk(Hayvon):
    def ovoz(self):
        print("Miyov")


hayvonlar = [It(), Mushuk()]

for h in hayvonlar:
    h.ovoz()
# Natija: Vov, Miyov


# ======================================================
# 3️⃣ Bir xil method — turli klasslar (duck typing)
# ======================================================


class Pdf:
    def och(self):
        print("PDF ochildi")


class Word:
    def och(self):
        print("Word ochildi")


class Excel:
    def och(self):
        print("Excel ochildi")


fayllar = [Pdf(), Word(), Excel()]

for f in fayllar:
    f.och()
# Natija: PDF ochildi, Word ochildi, Excel ochildi


# ======================================================
# 4️⃣ Method Override + Polimorfizm
# ======================================================


class Transport:
    def tezlik(self):
        print("O'rtacha tezlik")


class Mashina(Transport):
    def tezlik(self):
        print("120 km/soat")


class Velosiped(Transport):
    def tezlik(self):
        print("25 km/soat")


transportlar = [Mashina(), Velosiped()]

for t in transportlar:
    t.tezlik()
# Natija: 120 km/soat, 25 km/soat


# ======================================================
# 5️⃣ ABC bilan haqiqiy polimorfizm (Advanced)
# ======================================================

from abc import ABC, abstractmethod


class Shakl(ABC):
    @abstractmethod
    def yuza(self):
        """Har bir shakl uchun yuza metodini aniqlash majburiy"""
        pass


class Kvadrat(Shakl):
    def __init__(self, a: float):
        self.a = a

    def yuza(self) -> float:
        return self.a * self.a


class TogriTortburchak(Shakl):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def yuza(self) -> float:
        return self.a * self.b


shakllar = [Kvadrat(4), TogriTortburchak(3, 5)]

for s in shakllar:
    print(s.yuza())
# Natija: 16, 15
