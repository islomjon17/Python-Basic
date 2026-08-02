"""
Nested loop — bir sikl ichida yana boshqa sikl bo‘lishi.
Ichki sikl tashqi siklning har bir aylanishida to‘liq ishlaydi.
"""

i = 1
while i <= 3:
    j = i
    while j <= 2:
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1
i = 1
# while + for nested loop
while i <= 3:
    for j in range(1, 4):
        print(i, j)
    i += 1
# Ko‘paytirish jadvali (nested loop)


i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print(f"{i} x {j} = {i * j}")
        j += 1
    print("------")
    i += 1


# break nested loop ichida
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        if j == 3:
            break
        print(i, j)
        j += 1
    i += 1

# continue nested loop ichida
i = 0
while i < 3:
    i += 1
    j = 0
    while j < 5:
        j += 1
        if j == 2:
            continue
        print(i, j)


"""
Nested for — bir for sikl ichida yana boshqa for sikl bo‘lishi.
Ichki for tashqi forning har bir aylanishida to‘liq ishlaydi.
"""
# Oddiy nested for
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i = {i}, j = {j}")


# 2D jadval (matritsa ko‘rinishi)
for row in range(3):
    for col in range(3):
        print(row, col, end="  ")
    print()


# Ko‘paytirish jadvali (1 dan 9 gacha)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print("------")


# break nested for ichida
for i in range(1, 6):
    for j in range(1, 6):
        if j == 3:
            break
        print(i, j)


# continue nested for ichida
for i in range(1, 4):
    for j in range(1, 6):
        if j == 2:
            continue
        print(i, j)
