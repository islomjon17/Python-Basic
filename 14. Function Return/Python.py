"""
MAVZU: return bilan ishlash (shartli baholash, xatolik, validatsiya, statistika)
Quyidagi misollar clean code va o‘qitish uchun qulay tartibda yozilgan.
"""

# ======================================================
# 1️⃣ SHARTLI BAHOLASH VA RETURN
# ======================================================


def baho_hisobla(ball: int, kechikdi: bool) -> int | str:
    if not 0 <= ball <= 100:
        return "Noto‘g‘ri ball"

    if kechikdi:
        ball -= 10

    if ball >= 86:
        return 5
    if ball >= 71:
        return 4
    if ball >= 56:
        return 3
    return 2


# ======================================================
# 2️⃣ XATOLIKNI RETURN ORQALI QAYTARISH
# ======================================================


def bolish(a: float, b: float):
    if b == 0:
        return None, "0 ga bo‘lish mumkin emas"
    return a / b, "Hisoblandi"


# ======================================================
# 3️⃣ RO‘YXATDAN QIDIRISH (ERTA RETURN)
# ======================================================


def top(sonlar: list, qidirilayotgan: int) -> bool:
    for son in sonlar:
        if son == qidirilayotgan:
            return True
    return False


# ======================================================
# 4️⃣ MA’LUMOT TEKSHIRISH (VALIDATSIYA)
# ======================================================


def foydalanuvchi_tekshir(username: str, password: str):
    if len(username) < 5:
        return False, "Login juda qisqa"

    if len(password) < 8:
        return False, "Parol kuchsiz"

    if password.isdigit():
        return False, "Parolda kamida bitta harf bo‘lishi kerak"

    return True, "Ruxsat berildi"


# ======================================================
# 5️⃣ STATISTIK MA’LUMOTLARNI RETURN QILISH
# ======================================================


def statistika(sonlar: list):
    if not sonlar:
        return None

    jami = sum(sonlar)
    orta = jami / len(sonlar)

    return {
        "jami": jami,
        "o‘rtacha": orta,
        "maksimum": max(sonlar),
        "minimum": min(sonlar),
    }


# ======================================================
# TEST QISMI (NAMUNA ISHLATISH)
# ======================================================

print("1️⃣ Baho:", baho_hisobla(82, True))

natija, xabar = bolish(10, 2)
print("2️⃣ Bo‘lish:", natija, "-", xabar)

print("3️⃣ Qidiruv:", top([3, 6, 9, 12], 9))

holat, xabar = foydalanuvchi_tekshir("admin01", "pass1234")
print("4️⃣ Login:", holat, "-", xabar)

print("5️⃣ Statistika:", statistika([10, 20, 30, 40]))
