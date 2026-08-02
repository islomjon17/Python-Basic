# Tuple yaratish

numbers = (1, 2, 3, 4)
food = ("Mastava", "Shovla", "Makron", "Chuchvara")
# print(numbers)

# Tupleda indexlar joylashuvi listlar bilan bir xil, Lekin Tupleni oʻzgartirib boʻlmaydi

# print(numbers[1]) # 2
# print(numbers[0]) # 1

# Tuple turlari

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)
# print(
#     tuple1,
#     tuple2,
#     tuple3,
# )


# len() uzunlikni aniqlash

# print(len(numbers))

# Turini aniqlash
# thistuple = ("apple",)
# print(type(thistuple))

# # Tuple emas
# thistuple = "apple"
# print(type(thistuple))

######
### Tuple qiymatini o'zgartirish
######

# Element qo'shish
# numbers = (1, 2, 3, 4)
# food = ("Mastava", "Shovla", "Makron", "Chuchvara")

# a = list(food)
# a.append("Osh")
# b = tuple(a)
# print(tuple(b), type(b))

# +=

# ovqat = ("Lag'mon",) ###
# b += ovqat
# print(b)


# Elementni olib tashlash
# a = list(food)
# a.remove("Shovla")
# b = tuple(a)
# print(tuple(b), type(b))


# Ochiiish

# del food
# print(food) # Xatolik bo'ladi, sababi food o'chirib tashlandi


######
### Tuple qiymatini o'chish
######


# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# Yulduzchadan foydalanish*


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
