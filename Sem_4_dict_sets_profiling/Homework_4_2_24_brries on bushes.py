# 4.2[24]: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по 
# окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Собирающий модуль за один заход, 
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед 
# некоторым кустом. На входе задано количество ягод на каждом кусте. Не обязательно вводить их с клавиатуры, можно задать 
# непосредственно в коде программы

# Примеры/Тесты:
# Input1: 1, 2, 3, 4, 5, 6, 7, 8
# Output1: Макс. кол-во ягод 21, собрано для куста 7

# Input1: 11, 92, 1, 42, 15, 12, 11, 81
# Output1: Макс. кол-во ягод 184, собрано для куста 1

lst_1=[1, 2, 3, 4, 5, 6, 7, 8]  # 11, 92, 1, 42, 15, 12, 11, 81   1, 2, 3, 4, 5, 6, 7, 8
list_count=list()
list_exp=[]
for i in range(len(lst_1)-1):
    list_count.append(lst_1[i-1]+lst_1[i]+lst_1[i+1])
list_count.append(lst_1[-2]+lst_1[-1]+lst_1[0])
index = [index+1 for index, val in enumerate(list_count) if val == max(list_count)]
print(*index)
