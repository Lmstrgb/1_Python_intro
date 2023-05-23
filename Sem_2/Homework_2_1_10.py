#### 2.1[10]: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число 
#монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество 
#монет, которые нужно перевернуть. Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.

    # Примеры/Тесты:
    # Введите кол-во монет>? 5
    # Положение монеты 0: 0 или 1>? 1
    # ...
    # 1 0 1 1 0
    # Кол-во монет, чтобы перевернуть: 2

quant = input ('Введите количество монет: ')

def StrInput(a):
    strstate=''
    while int(a)>0:
      state = input ('Введите число, соответствующее положению монеты: ')
      strstate+=state
      a=int(a)-1
    return (strstate)

def Count(a):
  count1=''
  count0=''
  res_count=''
  for i in range(len(a)):
    if a[i]=='1': 
      count1+=str(i) 
    else: 
      count0+=str(i)
  res_count=len(count0) if len(count1)>=len(count0) else len(count1)
  return(res_count)

def Split(a):
  str_split=''
  for i in a:
    str_split+=' '+i
  return(str_split)


strInput=StrInput(quant)
count=Count(strInput)
strInput=Split(strInput)

print(f'{strInput} -> перевернуть {count}')   