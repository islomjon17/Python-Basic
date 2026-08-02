# UY ISHLARI: *args va **kwargs

# 1️⃣ Yig‘indini hisoblash

# Funksiya yozing: yigindi_args(*sonlar)

# Har qanday sonlarni qabul qilib, ularning yig‘indisini qaytarsin.

# Test: 1, 2, 3, 4 → 10

# 2️⃣ O‘rtacha qiymat

# Funksiya: ortalama(*sonlar)

# Argumentlar soni noma’lum, o‘rtacha qaytaradi.

# 3️⃣ Max va Min topish

# min_max_args(*sonlar)

# Argumentlardan min va max qiymatlarni qaytarsin.

# 4️⃣ *Oddiy parametr + args

# Funksiya: test_args(a, b, *args)

# a, b ni alohida, qolganlarini tuple sifatida chiqaring.

# 5️⃣ Nomlangan argumentlar bilan info chiqarish

# Funksiya: info_kwargs(**malumot)

# Barcha nomlangan argumentlarni kalit => qiymat ko‘rinishida chiqaradi.

# 6️⃣ **Oddiy + kwargs

# Funksiya: test_kwargs(a, **kwargs)

# Oddiy parametr va qolgan nomlangan argumentlarni chiqaring.

# 7️⃣ *args va **kwargs birga ishlatish

# Funksiya: test_all(a, b, *args, **kwargs)

# Test qiling: test_all(1,2,3,4,x=5,y=6)

# 8️⃣ Buyurtmalar tizimi (real)

# Funksiya: buyurtma(nomi, *tovarlar, **malumot)

# Tovarlarni list sifatida, malumotlarni dictionary sifatida chiqaradi.

# 9️⃣ Sonlarni kvadratga oshirish

# Funksiya: kvadrat_args(*sonlar)

# Faqat musbat sonlarni kvadratga oshirsin.

# 🔟 Nomlangan argumentlardan faqat tanlangan kalitlarni olish

# Funksiya: tanla_kwargs(**malumot)

# Masalan, faqat ism va yosh kalitlarini qaytarsin.

# 1️⃣1️⃣ *Oddiy parametr va args bilan yig‘indi

# Funksiya: yigindi_oddiy(a, *sonlar)

# a ni ham hisobga olib barcha sonlarni yig‘indisini qaytarsin.

# 1️⃣2️⃣ Nomlangan argumentlar yordamida hisob-kitob

# Funksiya: hisob(**malumot)

# Masalan: a=5, b=10 bo‘lsa, ularni qo‘shsin.

# 1️⃣3️⃣ *args va **kwargs bilan stringlarni birlashtirish

# Funksiya: birlashtir(*so‘zlar, **malumot)

# Tupledagi so‘zlar va dictionary’dagi qoshimcha kaliti qiymatlarini stringga qo‘shib chiqarish.

# 1️⃣4️⃣ Tovar narxini hisoblash

# Funksiya: narx(*tovarlar, **narxlar)

# Tovarlar ro‘yxati va narxlarini dictionary orqali berib, jami narxni qaytarsin.

# 1️⃣5️⃣ O‘rtacha va jami qiymat *args va **kwargs bilan

# Funksiya: stats(*sonlar, **bonus)

# *argsdagi sonlar va **bonusdagi qo‘shimcha qiymatini qo‘shib, jami va o‘rtachani qaytarsin.