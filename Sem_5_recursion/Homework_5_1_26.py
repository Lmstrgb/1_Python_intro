# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию умножения. 
# Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

def degree(a,b):
    if b<1: return 1
    b=b-1
    return a*degree(a,b)

def power(a, b): # это из чат GPT пока вообще не пойму как работает
    if b == 0:
        return 1
    elif b % 2 == 0:
        temp = power(a, b//2)
        return temp * temp
    else:
        temp = power(a, (b-1)//2)
        return a * temp * temp


print(degree(2,3))