"""
Python-da Inkapsulyatsiya (Encapsulation)
Public, Protected, Private atributlar va Getter/Setter
"""

# ======================================================
# 1️⃣ Inkapsulyatsiya turlari
# ======================================================


# Public – hamma tomonidan erkin foydalanish mumkin (default)
class StudentPublic:
    def __init__(self, name: str):
        self.name = name  # public atribut


s_pub = StudentPublic("Ali")
print("Public:", s_pub.name)
s_pub.name = "Vali"
print("Public (o‘zgartirilgan):", s_pub.name)


# Protected – faqat klass va voris klasslarida ishlatilishi mo‘ljallangan (_ oldi bilan)
class StudentProtected:
    def __init__(self, name: str):
        self._name = name  # protected atribut


s_prot = StudentProtected("Ali")
print("Protected:", s_prot._name)
s_prot._name = "Vali"
print("Protected (o‘zgartirilgan):", s_prot._name)


# Private – faqat o‘z klassi ichida ishlatiladi (__ oldi bilan)
class StudentPrivate:
    def __init__(self, name: str):
        self.__name = name  # private atribut

    # getter
    def get_name(self):
        return self.__name

    # setter
    def set_name(self, name: str):
        self.__name = name


s_priv = StudentPrivate("Ali")
print("Private (getter):", s_priv.get_name())
s_priv.set_name("Vali")
print("Private (setter bilan o‘zgartirilgan):", s_priv.get_name())


# ======================================================
# 2️⃣ Property decorator orqali inkapsulyatsiya
# ======================================================


class StudentProperty:
    def __init__(self, name: str):
        self.__name = name  # private atribut

    @property
    def name(self):
        """Getter: atributni olish"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Setter: atributni o‘zgartirish"""
        self.__name = value


s_prop = StudentProperty("Ali")
print("Property (getter):", s_prop.name)

s_prop.name = "Vali"
print("Property (setter bilan o‘zgartirilgan):", s_prop.name)
