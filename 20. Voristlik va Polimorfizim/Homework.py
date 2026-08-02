# UY ISHLARI: Python OOP (Inheritance & Polymorphism)

# 1️⃣ Oddiy vorislik

# Animal klassi: nom atributi va ovoz() metodi.

# Dog va Cat klasslarini Animal dan meros olgan holda yarat.

# 2️⃣ Method Override

# Dog va Cat klasslarida ovoz() metodini o‘ziga xos qilib yoz.

# Ob’ektlarni ro‘yxatda saqlab, for orqali ovoz() chaqiring.

# 3️⃣ super() bilan init

# Employee klassi: name, salary

# Developer(Employee) klassi: lang qo‘shing, super() orqali parent __init__ chaqiring.

# 4️⃣ Method Override + super()

# Developer klassida info() yozing: parent info() chaqiriladi va til chiqariladi.

# 5️⃣ Polimorfizm ro‘yxat orqali

# Vehicle klassi: speed()

# Car va Bike override qilsin.

# Ro‘yxat: [Car(), Bike()], for orqali speed() chaqirish.

# 6️⃣ Duck Typing polimorfizm

# Pdf, Word, Excel klasslari: open() metodi.

# Ro‘yxatga ob’ektlar qo‘shib, for orqali open() chaqirish.

# 7️⃣ ABC va abstract method

# Shape(ABC) abstract klassi: area() abstract method.

# Square va Rectangle klasslari: area() implementatsiya qilinsin.

# 8️⃣ Obyekt atributlarini o‘zgartirish

# Dog ob’ektini yarating, name va age ni keyin yangilang.

# 9️⃣ Class variable va instance variable

# Student klassi: class variable school, instance variable name

# 2 ob’ekt yaratib, class variable va instance variable ni chop eting.

# 🔟 Default parametr bilan vorislik

# Car klassi: brand, year=2020, color='white'

# ElectricCar(Car) klassini yaratib, default parametrlarni test qiling.

# 1️⃣1️⃣ Polimorfizm + ro‘yxat bilan statistik

# Student ob’ektlar ro‘yxati

# Funksiya: max_score(students) eng yuqori ballni qaytarsin.

# 1️⃣2️⃣ Metodlar orasida chaining

# Calculator klassi: add(a,b), sub(a,b)

# Metodlar chaining qilinsin: calc.add(2,3).sub(1,1) (return self).

# 1️⃣3️⃣ Override + parent method chaqirish

# Bird klassi: fly()

# Penguin(Bird) klassi: override fly(), lekin parent methodni ham chaqiring.

# 1️⃣4️⃣ Real misol: Bank

# Account klassi: deposit(), withdraw(), balance

# SavingsAccount(Account) override withdraw(): faqat balance >= amount bo‘lsa chiqaradi.

# 1️⃣5️⃣ Mixins polimorfizm

# SwimmingMixin klassi: swim()

# Duck(SwimmingMixin, Animal) klassi yarating. Ob’ekt yaratib, swim() va ovoz() chaqiring.