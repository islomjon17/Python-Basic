"""
NESTED LOOP (ichma-ich sikllar)
— Bir sikl ichida yana boshqa sikl ishlatiladi
— Ichki sikl tashqi siklning har bir aylanishida to‘liq bajariladi
"""

# ======================================================
# 1. WHILE + WHILE (oddiy nested loop)
# ======================================================

i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1


# ======================================================
# 2. WHILE + FOR (aralash nested loop)
# ======================================================

i = 1
while i <= 3:
    for j in range(1, 4):
        print(i, j)
    i += 1


# ======================================================
# 3. KO‘PAYTIRISH JADVALI (1–9, while orqali)
# ======================================================

i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print(f"{i} x {j} = {i * j}")
        j += 1
    print("------")
    i += 1


# ======================================================
# 4. BREAK (nested while ichida)
# ======================================================

i = 1
while i <= 5:
    j = 1
    while j <= 5:
        if j == 3:
            break
        print(i, j)
        j += 1
    i += 1


# ======================================================
# 5. CONTINUE (nested while ichida)
# ======================================================

i = 1
while i <= 3:
    j = 1
    while j <= 5:
        if j == 2:
            j += 1
            continue
        print(i, j)
        j += 1
    i += 1


# ======================================================
# NESTED FOR LOOP
# ======================================================

"""
Nested for — for ichida yana for
"""

# ======================================================
# 6. Oddiy nested for
# ======================================================

for i in range(1, 4):
    for j in range(1, 3):
        print(f"i = {i}, j = {j}")


# ======================================================
# 7. 2D jadval (matritsa)
# ======================================================

for row in range(3):
    for col in range(3):
        print(row, col, end="  ")
    print()


# ======================================================
# 8. KO‘PAYTIRISH JADVALI (for orqali)
# ======================================================

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print("------")


# ======================================================
# 9. BREAK (nested for ichida)
# ======================================================

for i in range(1, 6):
    for j in range(1, 6):
        if j == 3:
            break
        print(i, j)


# ======================================================
# 10. CONTINUE (nested for ichida)
# ======================================================

for i in range(1, 4):
    for j in range(1, 6):
        if j == 2:
            continue
        print(i, j)
