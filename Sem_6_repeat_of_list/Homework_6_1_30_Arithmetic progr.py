# 6.1[30]: Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа :

# Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Напишите функцию

# - Аргументы: три указанных параметра
# - Возвращает: список элементов арифмитической прогрессии.

# Примеры/Тесты:

# Ввод: 7 2 5
# Вывод: [7 9 11 13 15]
# Ввод: 2 3 12
# Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension

# (**) Усложнение. Присвоение значений переменным a1,d,n запишите, используя только один input, в одну строку, вам понадобится 
# распаковка и Comprehension или map
from time import perf_counter

# el_first=int(input("Введите значение 1-го элемента прогрессии: "))
# step=int(input("Введите шаг прогресии: "))
# num=int(input("Введите кол-во элементов прогрессии: "))

lst_input=[int(x) for x in input("Введите через пробел параметры прогресcии: первый элемент, шаг, коли-во элементов: ").split()]
el_first, step, num = lst_input 
#x, y = map(int, input().split())

el_last=el_first+(num-1)*step
lst1=[]
lst2=[]
lst3=[]

def Progr_1(start:int,step:int, end:int)->list:
    for i in range(start,end+step,step):
        #var1=el_first+step
        lst1.append(i)
    return lst1

def Progr_Compr(start:int,step:int,end:int)->list:  # получается, что эта функция быстрее Progr_1
    lst2=[el for el in range(start,end+step, step)]
    return lst2

def Prog_from_ideal(start:int,step:int,end:int)->list: # из идеального решения
    for i in range(end):
        lst3.append(start + i * step)
    return lst3

t1=perf_counter()
Progr_1(el_first,step,el_last)
#print(Progr_1(el_first,step,el_last)) 
t2=perf_counter()
print(t2-t1)

t3=perf_counter()
Progr_Compr(el_first,step,el_last)
#print(Progr_Compr(el_first,step,el_last)) 
t4=perf_counter()
print(t4-t3)

t5=perf_counter()
Prog_from_ideal(el_first,step,num)
#print(Prog_from_ideal(el_first,step,num)) 
t6=perf_counter()
print(t6-t5)