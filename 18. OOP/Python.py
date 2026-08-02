"""
MAVZU: Python OOP — __init__ (constructor), self, metodlar va class variable
Quyidagi misollar tartibli, clean code va o‘rganish uchun qulay ko‘rinishda yozilgan.
"""

# ======================================================
# 1️⃣ __init__ — KONSTRUKTOR
# ======================================================


class Car:
    def __init__(self, model: str, year: int):
        self.model = model
        self.year = year


car1 = Car("MERC", 2025)
print(car1.model, car1.year)


"""
self — klassdan yaratilgan joriy ob'ektga (instance) ishora qiladi.
U orqali ob'ektning atributlari va metodlariga murojaat qilinadi.
"""


# ======================================================
# 2️⃣ CLASS ICHIDA METODLAR
# ======================================================


class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b

    def sub(self, a: int, b: int) -> int:
        return a - b


calc = Calculator()
print(calc.add(1, 2))
print(calc.sub(5, 2))


# ======================================================
# 3️⃣ CLASS O‘ZGARUVCHISI (CLASS VARIABLE)
# ======================================================


class Student:
    school = "42-maktab"  # class variable

    def __init__(self, name: str):
        self.name = name  # instance variable


s1 = Student("Ali")
s2 = Student("Vali")

print(s1.school)
print(s2.school)


# ======================================================
# 4️⃣ ODDIY MISOL: PERSON KLASSI
# ======================================================


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Salom, mening ismim {self.name}"


person = Person("Aziz", 22)
print(person.greet())


# ======================================================
# MUHIM ESLATMALAR
# ======================================================

"""
✔ __init__ metodi har doim birinchi parametr sifatida self oladi
✔ __init__ — maxsus (magic / dunder) metod
✔ __init__ return qiymat qaytarmaydi
✔ Agar __init__ yozilmasa, Python standart bo‘sh konstruktordan foydalanadi
"""


# ======================================================
# 5️⃣ DEFAULT QIYMATLI PARAMETRLAR
# ======================================================


class Mashina:
    def __init__(self, model: str, yil: int = 2003, rang: str = "oq"):
        self.model = model
        self.yil = yil
        self.rang = rang


mashina1 = Mashina("Tesla")
mashina2 = Mashina("BMW", 2026, "ko‘k")

print(mashina1.model, mashina1.yil, mashina1.rang)
print(mashina2.model, mashina2.yil, mashina2.rang)
