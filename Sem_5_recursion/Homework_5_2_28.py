# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических 
# операций допускаются только +1 и -1. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3

def sum_a_b(a,b):
    if b<0:return 0
    return a+sum_a_b(1,b-1)

def sum(a, b):  # из чат GPT для исследования
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a+1, b-1)

def exp_func(a):  # экспериментальная 
    if a<1: return 0
    return 1+exp_func(a-1)

print(sum(4,4))
#print(exp_func(7))