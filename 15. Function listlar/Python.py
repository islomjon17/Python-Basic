# =========================================
# 1️⃣ Listga qiymat qo‘shish (append)
# =========================================
def qosh(royxat, qiymat):
    royxat.append(qiymat)
    return royxat


# =========================================
# 2️⃣ Listdan shart asosida o‘chirish
# =========================================
def manfiylarni_ochir(sonlar):
    tozalangan = []
    for son in sonlar:
        if son >= 0:
            tozalangan.append(son)
    return tozalangan


# =========================================
# 3️⃣ List ichidan eng katta va eng kichikni topish
# =========================================
def min_max(sonlar):
    if not sonlar:
        return None
    return min(sonlar), max(sonlar)


# =========================================
# 4️⃣ Listni qayta ishlash (map logikasi)
# =========================================
def kvadratlar(sonlar):
    natija = []
    for son in sonlar:
        natija.append(son**2)
    return natija


# =========================================
# 5️⃣ List bo‘yicha tahlil (filtr + statistika)
# =========================================
def musbat_statistika(sonlar):
    musbatlar = []

    for son in sonlar:
        if son > 0:
            musbatlar.append(son)

    if not musbatlar:
        return "Musbat son yo‘q"

    return {
        "sonlar": musbatlar,
        "jami": sum(musbatlar),
        "o‘rtacha": sum(musbatlar) / len(musbatlar),
    }


# =========================================
# TEST QISMI (namuna ishlatish)
# =========================================
print("1️⃣ Qo‘shish:", qosh([1, 2, 3], 4))

print("2️⃣ Tozalash:", manfiylarni_ochir([-5, 3, -1, 7, 0]))

print("3️⃣ Min–Max:", min_max([10, 2, 8, 4]))

print("4️⃣ Kvadratlar:", kvadratlar([1, 2, 3, 4]))

print("5️⃣ Musbat statistika:", musbat_statistika([-3, 5, 7, -2, 10]))
