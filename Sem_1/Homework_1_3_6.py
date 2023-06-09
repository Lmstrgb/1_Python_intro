#### 1.3[6]. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# 	Примеры/Тесты:
# 	385916 >>> yes
# 	123456 >>> no

# ```(*)``` **Усложнение.** Вывод результат на экран сделайте одной строкой(только один print), для этого используйте тернарный оператор


num = input("Введите номер билета: ")

def Happy(a):
    r1 = range(0, len(num) // 2)
    r2 = range(len(num) // 2, len(num))
    # r1=(0, 4)
    # r2=(4, 6)
    sum1 = 0
    sum2 = 0
    res=''
    if len(num) == 6:
        for i in r1:
            sum1 += int(num[i])
        for j in r2:
            sum2 += int(num[j])
        if sum1 == sum2:
            res = f"Билет под номером {num} - счастливый"
        else:
            res = f"Билет под номером {num} - не счастливый"
    else:
        print("Введенное значение - не шестизначное, введите шесть цифр билета")
    return res

print(Happy(num))