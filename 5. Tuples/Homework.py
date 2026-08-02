# ### **1-mashq**

# 5 ta hayvon nomidan iborat tuple yarating. Uning 3- va 5-elementlarini ekranga chiqaring.

# ---

# ### **2-mashq**

# Quyidagi tuple berilgan:

# ```python
# numbers = (10, 20, 30, 40, 50, 60)
# ```

# Ushbu tuple uzunligini toping.

# ---

# ### **3-mashq**

# Quyidagi qiymatning haqiqatan ham tuple yoki tuple emasligini type() yordamida aniqlang:

# ```python
# value = ("Python")
# ```

# ---

# ### **4-mashq**

# Quyidagi tuplega `"banana"` elementini qo‘shing (listga aylantirib):

# ```python
# fruits = ("apple", "cherry")
# ```

# ---

# ### **5-mashq**

# Tupledan `"cherry"` elementini o‘chirib tashlang (list orqali o‘chirib, yana tuplega aylantiring):

# ```python
# data = ("cherry", "mango", "grape")
# ```

# ---

# ### **6-mashq**

# Quyidagi ikki tuple’ni qo‘shing:

# ```python
# t1 = (1, 2, 3)
# t2 = (4, 5)
# ```

# ---

# ### **7-mashq**

# Quyidagidagi tupleni 3 ta o‘zgaruvchiga unpack qiling va ularni chop eting:

# ```python
# colors = ("red", "green", "blue")
# ```

# ---

# ### **8-mashq**

# Quyidagi tuple’da * ishlatib unpacking qiling:

# ```python
# nums = (5, 10, 15, 20, 25)
# ```

# 1-o‘zgaruvchi = 5
# 2-o‘zgaruvchi = 10
# qolgan barcha = *middle

# ---

# ### **9-mashq**

# Quyidagi tuple berilgan:

# ```python
# food = ("Osh", "Lagmon", "Shashlik", "Somsa")
# ```

# Tuple ichidagi `"Somsa"` ning indeksini toping.

# ---

# ### **10-mashq**

# Quyidagi tupleni o‘chirib tashlang:

# ```python
# cities = ("Toshkent", "Samarqand", "Buxoro")
# ```

# Keyin uni chop etishga harakat qiling (xatolik bo‘lishi kerak).

# ---

# Agar yana **yana 10 ta** yoki **yanada qiyinroq mashqlar** istasangiz — darhol yozib beraman!

##################################
########### Javoblar #############
##################################

# ### **1-mashq**

# 5 ta hayvon nomidan iborat tuple yarating. Uning 3- va 5-elementlarini ekranga chiqaring.

hayvonlar = ("ilon", "burgut", "she'r", "bori", "karkidon", "akula")
# print(hayvonlar[3], hayvonlar[5])


# ### **2-mashq**

# # Quyidagi tuple berilgan:

# # ```python
# numbers = (10, 20, 30, 40, 50, 60)
# # ```

# # Ushbu tuple uzunligini toping.

# print(len(numbers))

# ### **3-mashq**

# Quyidagi qiymatning haqiqatan ham tuple yoki tuple emasligini type() yordamida aniqlang:

# ```python

# value = ("Python")
# print(type(value))

# ### **4-mashq**

# Quyidagi tuplega `"banana"` elementini qo‘shing (listga aylantirib):

# ```python
# fruits = ("apple", "cherry")
# ```

# fruits = ("apple", "cherry")
# list1 = list(fruits)
# list1.append("banana")
# fruits2 = tuple(list1)
# print(fruits2, type(fruits2))

# ---

# ### **5-mashq**

# Tupledan `"cherry"` elementini o‘chirib tashlang (list orqali o‘chirib, yana tuplega aylantiring):

# ```python
# data = ("cherry", "mango", "grape")
# ```

# ---

# data = ("cherry", "mango", "grape")
# data_list = list(data)
# data_list.remove("cherry")
# data_tuple = tuple(data_list)
# print(data_tuple, type(data_tuple))


# ### **6-mashq**

# Quyidagi ikki tuple’ni qo‘shing:

# ```python
# t1 = (1, 2, 3)
# t2 = (4, 5)
# ```

# t1 = (1, 2, 3)
# t2 = (4, 5)
# t3 = t1 + t2
# print(t3)


# ---

# ### **7-mashq**

# Quyidagidagi tupleni 3 ta o‘zgaruvchiga unpack qiling va ularni chop eting:

# ```python
# colors = ("red", "green", "blue")
# ```

# ---

# colors = ("red", "green", "blue")
# (red1, blue2, green2 )= colors
# print(blue2)
# print(red1)
# print(green2)


# ### **8-mashq**

# Quyidagi tuple’da * ishlatib unpacking qiling:

# ```python
# nums = (5, 10, 15, 20, 25)
# ```

# 1-o‘zgaruvchi = 5
# 2-o‘zgaruvchi = 10
# qolgan barcha = *middle
# nums = (5, 10, 15, 20, 25)
# (n1, n2, *middle) = nums
# print(n1)
# print(n2)
# print(middle)

# ---

# ### **9-mashq**

# Quyidagi tuple berilgan:

# ```python
# food = ("Osh", "Lagmon", "Shashlik", "Somsa")
# ```

# Tuple ichidagi `"Somsa"` ning indeksini toping.
# food = ("Osh", "Lagmon", "Shashlik", "Somsa")
# print(food.index("Somsa"))

# ---

# ### **10-mashq**

# Quyidagi tupleni o‘chirib tashlang:

# ```python
# cities = ("Toshkent", "Samarqand", "Buxoro")
# ```

# Keyin uni chop etishga harakat qiling (xatolik bo‘lishi kerak).

# ---

cities = ("Toshkent", "Samarqand", "Buxoro")
del cities
print(cities)  ## Xatolik beradi, chunki cities ochib ketgan.
