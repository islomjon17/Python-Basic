# ═══════════════════════════════════════════════════════════
#      PYTHONDA XATOLIKLARDAN QO‘RQMAYDI!
#      Try / Except — Darsligi (Super Qiziqarli Versiya) ✨
# ═══════════════════════════════════════════════════════════

# ⭐ 1. Try–Except nima qiladi? (Oddiy misol)
print("1. Try-Except asoslari 💡")
try:
    x = 10 / 0  # Bu yerda xato bo‘ladi!
except:
    print("Xato yuz berdi! Dastur to‘xtab qolmadi")  # Ishlaydi!

print("Dastur davom etyapti...\n")


# ⭐ 2. Aniq xato turini tutish (Professional usul!)
print("2. Aniq xato turlarini tutamiz 🛡️")
try:
    son = int("abc")  # ValueError chiqadi
except ValueError:
    print("Faqat son kiriting! Bu matn emas!\n")

# Eng muhim xato turlari (yodlab oling!)
xato_jadvali = """
┌────────────────────┬─────────────────────────────────┐
│     Xato turi      │          Qachon chiqadi?        │
├────────────────────┼─────────────────────────────────┤
│
│ ValueError         │ Noto‘g‘ri turga o‘tkazganda     │
│ ZeroDivisionError  │ 0 ga bo‘lishda                  │
│ TypeError          │ Noto‘g‘ri amal (masalan: 5 + "a")│
│ IndexError         │ Ro‘yxatdan tashqariga chiqishda  │
│ KeyError           │ Lug‘atda yo‘q kalitga murojaat   │
│ FileNotFoundError  │ Fayl topilmasa                  │
│ NameError          │ O‘zgaruvchi nomi xato bo‘lsa     │
└────────────────────┴─────────────────────────────────┘
"""
print(xato_jadvali)


# ⭐ 3. Bir nechta except bloklari
print("3. Bir nechta except")
try:
    raqam = int("salom")
except ValueError:
    print("ValueError: Bu son emas!")
except TypeError:
    print("TypeError: Turi mos emas!\n")


# ⭐ 4. Bitta except’da bir nechta xato turi
print("4. Bir except’da ko‘p xato")
try:
    # x = "salom" + 5
    pass
except (ValueError, TypeError) as e:
    print(f"Xatolik turi: {type(e).__name__} → {e}\n")


# ⭐ 5. Xato haqida batafsil ma’lumot olish
print("5. Xato haqida to‘liq ma’lumot")
try:
    son = int("xyz123")
except Exception as e:  # Barcha xatolarni ushlaydi
    print(f"Xato turi: {type(e).__name__}")
    print(f"Xato xabari: {e}\n")


# ⭐ 6. else — faqat xato BO‘LMASA ishlaydi
print("6. else bloki")
try:
    son = int("2025")
except ValueError:
    print("Xato kiritdingiz!")
else:
    print(f"Zo‘r! Son muvaffaqiyatli o‘qildi: {son}\n")


# ⭐ 7. finally — HAR DOIM ishlaydi (hatto return bo‘lsa ham!)
print("7. finally bloki")
try:
    print("Hisoblayapmiz...")
    natija = 100 / 4
except ZeroDivisionError:
    print("0 ga bo‘lib bo‘lmaydi!")
else:
    print(f"Natija: {natija}")
finally:
    print("Finally: Men har doim ishlayman! Tugadi!\n")


# ⭐ 8. Finally hatto return bo‘lsa ham ishlaydi!
print("8. Return bo‘lsa ham finally ishlaydi")


def test_return():
    try:
        return "Muvaffaqiyatli natija"
    except:
        return "Xato"
    finally:
        print("Finally: Men oxirgi so‘zni aytaman!\n")


print(test_return())


# ⭐ 9. Real hayotda eng ko‘p ishlatiladigan joylar
print("9. Real misollar")

# 1. Foydalanuvchi kiritgan ma’lumotni tekshirish
print("→ Foydalanuvchi kiritishi")
# try:
#     yosh = int(input("Yoshingizni kiriting: "))
#     print(f"Siz {yosh} yoshdasiz")
# except ValueError:
#     print("Iltimos, faqat son kiriting!")

# 2.Fayl ochish
print("→ Fayl ochish")
try:
    f = open("mavjud_emas.txt")
except FileNotFoundError:
    print("Fayl topilmadi! Yangi yaratamiz...")
    open("mavjud_emas.txt", "w").close()

# 3.Lug‘atdan kalit olish
print("→ Lug‘atdan xavfsiz olish")
talaba = {"ism": "Sarvar", "yosh": 20}
try:
    print(talaba["bahosi"])
except KeyError:
    print("Bunday kalit yo‘q. Standart qiymat beramiz → 0")
    talaba["bahosi"] = 0


# ⭐ 10. O‘zingiz xato yaratish (raise)
print("\n10. O‘zimiz xato uloqtiramiz (raise)")


def yoshni_tekshir(yosh):
    if yosh < 0 or yosh > 150:
        raise ValueError("Yosh real bo‘lishi kerak (0-150)!")
    return f"Yoshingiz {yosh} — zo‘r!"


try:
    print(yoshni_tekshir(-5))
except ValueError as e:
    print(f"Xato: {e}")


# ⭐ 11. Ro‘yxat ichidagi faqat sonlarni olish
print("\n11. Faqat sonlarni ajratib olish")
raqamlar = ["10", "salom", "25", "-5", "hello", "100"]

for r in raqamlar:
    try:
        print(f"{r} → {int(r)} (son)")
    except ValueError:
        print(f"{r} → bu son emas")


# ⭐ 12. To‘g‘ri son kiritmaguncha so‘raydigan funksiya
print("\n12. To‘g‘ri son kiritmaguncha so‘raymiz")


def son_kirit():
    while True:
        try:
            return int(input("Iltimos, to‘g‘ri son kiriting: "))
        except ValueError:
            print("Xato! Faqat son kiriting!")


# son = son_kirit()
# print(f"Rahmat! Siz kiritgan son: {son}")


# ⭐ 13. Eng professional yozilish shakli (muhim!)
print("\n13. Professional Try-Except struktura")
try:
    # Xavfli kod joylashadi
    foydalanuvchi_soni = int(input("Son kiriting: "))
    natija = 100 / foydalanuvchi_soni
except ValueError:
    print("Iltimos, faqat son kiriting!")
except ZeroDivisionError:
    print("0 ga bo‘lish mumkin emas!")
except Exception as e:
    print(f"Kutilmagan xato: {e}")
else:
    print(f"Hisoblash muvaffaqiyatli: 100 / {foydalanuvchi_soni} = {natija}")
finally:
    print("Dastur yakunlandi. Rahmat!\n")

print("Try-Except darsi tugadi! Endi siz xatolardan qo‘rqmaysiz!")
