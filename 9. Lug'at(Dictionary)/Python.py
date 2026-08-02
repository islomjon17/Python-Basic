# ============================
# Oddiy Dictionary
# ============================

brends = {
    "Chevrolet": "Camaro",
    "Tesla": "Model Y",
    "Merc": "G63",
    "BMW": "i5",
}

print(brends)
print(brends["Tesla"])
print(len(brends))


# ============================
# Dictionary ichida boshqa turlar
# ============================

brends2 = {
    "Chevrolet": ["Cobalt", "Camaro", "Spark"],
    "Tesla": False,
    "Merc": True,
    "BMW": "i5",
}


# ============================
# dict() konstruktori
# ============================

lugat1 = dict(name="Islomjon", age=25, country="UZB")
print(lugat1)


# ======================================================
# Python – Dictionary elementlariga murojaat qilish
# ======================================================

# 1. Kalit orqali qiymatni olish
person = {
    "name": "Islomjon",
    "age": 22,
    "country": "Uzbekistan",
}

print(person["name"])
print(person["age"])
print(person["country"])

# 2. get() metodi orqali kirish
print(person.get("age"))

# 3. Dictionary ichidagi barcha kalitlarni olish
print(person.keys())

# 4. Barcha qiymatlarni olish
print(person.values())

# 5. Kalit-qiymat juftliklarini olish
print(person.items())


# ======================================================
# Python – Dictionary elementlarini o‘zgartirish
# ======================================================

person = {
    "name": "Islomjon",
    "age": 6,
    "country": "Norway",
    "Uylangan": "yoq",
    "city": "",
}

# 1. Kalit orqali qiymatni almashtirish
person["age"] = 27
print(person)

person["Uylangan"] = "Ha, Uylangan"
print(person)

# 2. update() metodi yordamida o‘zgartirish
person.update({"country": "Sweden"})
person.update({"name": "Islomjon Bek", "age": 28})
print(person)

# 3. Kalit bo‘lmasa update() yangi element qo‘shadi
person.update({"city": "Ferghana"})
print(person)


# ======================================================
# Python – Dictionary elementlarini qo‘shish
# ======================================================

person = {
    "name": "Islomjon",
    "age": 6,
    "country": "Norway",
}

# 1. Oddiy usul bilan yangi element qo‘shish
person["nomer"] = "998999999999"
print(person)

# 2. update() orqali element qo‘shish
person.update({"school": "12-maktab"})
print(person)
