"""
Asosiy uchta turi mavjud


    int - butun sonlar 123, 2323
    float - ma'nfiy sonlar 2.2, 556.78, 99.18
    complex - murakkab sonlar 3j, 6l

"""

##################################################################################################################
"""  
type() funsksiyasi consolega ma'lumot turini chiqaradi

"""
# a = 2323
# b = 556.12
# c = 3j
# print(type(a))
# print(type(b))
# print(type(c))
##################################################################################################################
"""  intga misollar """
# a = 9
# b = 10
# c = -10
# print(a,b,c)  ## 9 10 -10
##################################################################################################################
"""  floatga misollar """
# a = 9.10
# b = 12.98
# c = -93.30
# print(a,b,c) ## 9.1 12.98 -93.3
##################################################################################################################
"""  floatdan 10 xonali sonni belgilash uchun e dan foydalanilsa ham bo'ladi. """
##################################################################################################################
# a = 9e10
# b = 12E8
# c = -93.3e2
# print(a,b,c) ## 90000000000.0 1200000000.0 -9330.0
##################################################################################################################
"""   Murakkab sonlar"""
# Kompleks son yaratish
z = 3 + 4j
print(z)              # (3+4j)
print(z.real)         # 3.0 (haqiqiy qism)
print(z.imag)         # 4.0 (xayoliy qism)
print(abs(z))         # 5.0 (modul: sqrt(3^2 + 4^2))

# Arifmetik amallar
z2 = 1 + 2j
print(z + z2)         # (4+6j)
print(z * z2)         # (-5+10j)
print(z / z2)         # (2.2+0.4j)

# Konjugat
print(z.conjugate())  # (3-4j)

