# 1. Oddiy try/except
# 10 ni 0 ga bo‘lishga urinib ko‘ring va xatoni ushlang, "Xato yuz berdi!" deb chiqaring.

# 2. Aniq xato turi
# Foydalanuvchi kiritgan matnni integerga aylantiring. Agar ValueError chiqsa "Faqat son kiriting!" deb chiqsin.

# 3. Bir nechta except bloklari
# Biror matn va sonni qo‘shish (masalan "5" + 5) orqali ValueError va TypeError xatolarini alohida except bloklarda tuting.

# 4. Bir except’da bir nechta xato
# int("abc") va "salom" + 5 kodlarini bitta except (ValueError, TypeError) yordamida tuting va xato turini chiqaradigan kod yozing.

# 5. Xato haqida batafsil ma’lumot
# Foydalanuvchi kiritgan matnni integerga aylantirishga urinib, xato turini va xabarini chiqaring.

# 6. else bloki ishlatish
# Foydalanuvchi 2025 sonini integerga aylantiradi. Agar xato bo‘lmasa "Son muvaffaqiyatli o‘qildi" deb else blokda chiqaring.

# 7. finally bloki
# 100 ni 4 ga bo‘ling, natijani else blokda chiqaring va finally blokda "Har doim ishlayman" deb yozing.

# 8. finally + return
# Funksiya ichida return bo‘lsa ham finally blok ishlashini tekshiring.

# 9. Fayl ochish
# Mavjud bo‘lmagan faylni oching, FileNotFoundError xatosini tuting va yangi fayl yarating.

# 10. Lug‘atdagi kalitni tekshirish
# Lug‘atda mavjud bo‘lmagan "bahosi" kalitini olishga urinib, KeyError xatosini tuting va standart qiymat bering.

# 11. O‘zimiz xato raise qilish
# Funksiya yozing: agar yosh < 0 yoki > 150 bo‘lsa ValueError chiqarilsin.

# 12. Ro‘yxatdagi sonlarni ajratish
# Ro‘yxatdagi elementlarni integerga aylantirishga urinib, faqat sonlarni chiqaradigan kod yozing, xatolarni ushlab.

# 13. Foydalanuvchidan son so‘rash
# Foydalanuvchi to‘g‘ri son kiritmaguncha input so‘rash funksiyasini yozing.

# 14. Professional try/except
# Foydalanuvchi son kiritadi, 100 ni unga bo‘ling, ValueError, ZeroDivisionError va boshqa xatolarni alohida except blokda tuting. Natijani else blokda, yakunini finally blokda chiqaring.

# 15. Mashq kombinatsiyasi
# Ro‘yxatdagi elementlarni integerga aylantiring. Agar ValueError bo‘lsa "Bu son emas", else bo‘lsa "Son muvaffaqiyatli o‘qildi", finally bo‘lsa "Element tekshirildi" deb chiqaring.