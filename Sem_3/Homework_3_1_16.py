# 3.1[16]: Дан список целых чисел. Требуется вычислить, сколько раз встречается некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.

# Примеры/Тесты:
# Input:   [1#0, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 3
# Output:  2

# Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 20
# Output:  -1
# Напишите алгоритм подсчета самостоятельно или воспользуйтесь методами списка.

# (*) Усложнение. При выводе результата на экран воспользуйтесь тернарным оператором.

def CountDigit(a):
    count=0
    for i in list_nums:
        count=count+1 if i==num_x else count+0
    
    return (count)


list_nums=[]
print('Вводите числа, а для выхода из режима ввода нажмите \'q\'')
num=''
while num!='q':
    num=input('Введите число: ')
    if num=='q': 
        print("Ввод чисел прекращен")
        break
    list_nums.append(int(num))

num_x=int(input('Введите число, которое будем искать: '))
count_out=CountDigit(num_x)
print(f"Output: {count_out}") if count_out>0 else print(f"Output: -1")