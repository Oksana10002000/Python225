# Задача №1 Выведите все элементы списка с чеиными индексами.

# a = [int(input('-> ')) for i in range(int(input("n = ")))]
#
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end="")


# Задача № 2 Выведите все элементы списка, которые больше предыдущего элемента.

# a = [int(input('-> ')) for i in range(int(input("n = ")))]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#
#         print(a[i], end=" ")

# Задача № 3 Треугольник из звездочек

# a = int(input("Введите высоту треугольника: "))
# b = int(input("Введите ширину треугольника: "))
# for i in range(a):
#     for j in range(b):
#         if i > j:
#             print("*", end="")
#     print()

# Задача № 4 Треугольник из звездочек перевернутый

# a = int(input("Введите высоту треугольника: "))
# b = int(input("Введите ширину треугольника: "))
# for i in range(a):
#     for j in range(b):
#         if i < j:
#             print("*", end="")
#     print()

# Задача № 5 Шахматная доска

# size = int(input("Введите размер поля: "))
# simb = int(input("Введите кол-во символов: "))
# for i in range(size):
#     for j in range(simb):
#         for k in range(size):
#             for m in range(simb):
#                 if (i + k) % 2 == 0:
#                     print("*", end="")
#                 else:
#                     print(" ", end="")
#         print()
