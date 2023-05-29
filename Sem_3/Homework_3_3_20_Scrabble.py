# 3.3[20]: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно 
# слово, которое содержит либо только английские, либо только русские буквы и заранее известно какой алфавит надо использовать.

# Примеры/Тесты:
# Input:   ноутбук
# Output:  12

# Input:   notebook
# Output:  14
# (*) Примечание.
# Подумайте о том какие структуры данных здесь наиболее удобно использовать, чтобы просто проверять в какую группу попадает 
# буква, а также просто накапливать сумму очков.

def ScrableRus(word,dic):
  count_rus=0
  for letter in word:
    for key, value in dic.items():
        if letter in key:
            count_rus += value
  return(count_rus)

def ScrableEng(word,dic):
  count_eng=0
  for items in word:
    count_eng += dic.get(items)
  return(count_eng)

dict_ABC = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, 
           "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3,
           "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8,
           "Y": 4, "Z": 10}

dict_Rus = {'АВЕИНОРСТ':1, 'ДКЛМПУ':2, 'БГЁЬЯ':3, 'ЙЫ':4, 'ЖЗХЦЧ':5, 'ШЭЮ':8, 'ФЩЪ':10} # чтоб мозги попарить...

set_ABC=set(dict_ABC)
set_Rus=set(dict_Rus)

set_Rus_1=set()
for i in set_Rus:
    for j in i:
     set_Rus_1.add(j)  #сделаем новое множество по буквам русского алфавита, распакуем множество set_Rus
     
count=0
word_input=input('Введите слово либо на русском либо на аглийском: ').upper()
set_word_input=set(word_input)

if set_word_input.intersection(set_ABC) & set_word_input.intersection(set_Rus):
  print('Ввели и русские и английские слова, введите либо русские буквы либо английские')
  exit()
elif set_word_input.intersection(set_ABC):
  count=ScrableEng(word_input,dict_ABC)
elif set_word_input.intersection(set_Rus_1):
  count=ScrableRus(word_input, dict_Rus)
else: print('Ввели какую-то абракадабру, введите либо русские буквы либо английские')


print("Количество очков в слове: ",count)
