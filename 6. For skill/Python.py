# ==========================================================
# 1. Oddiy ro'yxatni aylantirish
# ==========================================================
countries = ["Uzbekistan", "Kazagistan", "Russia", "Korea", "Japan", "Malasia"]

for country in countries:
    print(country)

print("\n========================\n")

# ==========================================================
# 2. Har bir elementdan keyin ajratuvchi qo'yish
# ==========================================================
for country in countries:
    print(country)
    print("-----")

print("\n========================\n")

# ==========================================================
# 3. String (matn) ichidagi harflarni aylantirish
# ==========================================================
language = "Python"

for letter in language:
    print(letter)

print("\n========================\n")

# ==========================================================
# 4. range() — ma'lum oraliqdagi sonlarni aylantirish
# ==========================================================
for i in range(0, 4):  # 0, 1, 2, 3
    print(i)

print("\n========================\n")

# ==========================================================
# 5. break — shart to'g'ri bo'lsa siklni to'xtatadi
# ==========================================================
for country in countries:
    if country == "Russia":
        break
    print(country)

print("\n========================\n")

# ==========================================================
# 6. continue — elementni tashlab o'tadi
# ==========================================================
for country in countries:
    if country == "Russia":
        continue
    print(country)

print("\n========================\n")

# ==========================================================
# 7. Nested loops — ikki sikl ichma-ich
# ==========================================================
for i in [1, 2, 3]:
    for j in ["A", "B"]:
        print(i, j)

print("\n========================\n")

# ==========================================================
# 8. Ko'paytirish jadvali misoli
# ==========================================================
for i in range(1, 4):  # 1, 2, 3
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

print("\n========================\n")

# ==========================================================
# 9. len() yordamida parallel ro'yxatlar bilan yurish
# ==========================================================
countries = ["Uzbekistan", "Kazakhstan", "Russia", "South Korea", "Japan", "Malaysia"]
capitals = ["Tashkent", "Astana", "Moscow", "Seoul", "Tokyo", "Kuala Lumpur"]

for i in range(len(countries)):
    print(countries[i], "-", capitals[i])

print("\n========================\n")

# ==========================================================
# 10. enumerate() — indeks + element
# ==========================================================
mevalar = ["olma", "banan", "anor"]

for i, meva in enumerate(mevalar):
    print(i, meva)

print("\n========================\n")

# ==========================================================
# 11. zip() — ro'yxatlarni juftlab yurish
# ==========================================================
ism = ["Ali", "Vali", "Sardor"]
yosh = [25, 30, 22]

for i, y in zip(ism, yosh):
    print(i, y, "yoshda")

print("\n========================\n")

# ==========================================================
# 12. dict.items() — lug'atni aylantirish
# ==========================================================
talaba = {"ism": "Sarvar", "yosh": 19, "bahosi": 4.8}

for kalit, qiymat in talaba.items():
    print(kalit, "->", qiymat)
