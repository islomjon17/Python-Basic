"""
MAVZU: Python OOP — Class metodlari, obyekt atributlarini o‘zgartirish
Clean code va tartibli misollar
"""

# ======================================================
# 1️⃣ Oddiy Student klassi
# ======================================================


class Student:
    def __init__(self, name: str, age: int, grade: int):
        self.name = name
        self.age = age
        self.grade = grade


s1 = Student("Ali", 15, 9)
s2 = Student("Vali", 14, 8)

print(s1.name, s1.grade)
print(s2.name, s2.grade)


# ======================================================
# 2️⃣ Class ichida metod (passed)
# ======================================================


class StudentWithScore:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def passed(self) -> bool:
        """Studentning balli 60 dan yuqori bo‘lsa True qaytaradi"""
        return self.score >= 60


student = StudentWithScore("Aziz", 75)
print(student.passed())  # True


# ======================================================
# 3️⃣ Obyekt ichidagi qiymatni o‘zgartirish (add_money)
# ======================================================


class Account:
    def __init__(self, balance: float):
        self.balance = balance

    def add_money(self, amount: float):
        """Hisob balansiga pul qo‘shish"""
        self.balance += amount


account = Account(100)
account.add_money(50)
print(account.balance)  # 150


# ======================================================
# 4️⃣ Book klassi va info metodi
# ======================================================


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def info(self):
        """Kitob haqida ma’lumot chiqarish"""
        print(f"{self.title} - {self.author}")


book1 = Book("Info1", "Uxla Tur")
book1.info()
