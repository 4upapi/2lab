#30.Шеснадцатиричные четные числа, не превышающие 2048в10 и содержащие количество
#цифр равное первой цифре. Вывести числа и их количество. Максимальное число вывести прописью.

import re
slov = {0:'ноль',1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять',\
     'A':'десять','B':'одинадцать','C':'двенадцать','D':'тринадцать','E':'четырнадцать','F':'пятнадцать'}
max = "0"
s_max = ''
kol = 0
file = open("text.txt", "r")
while True:
    a = file.readline().split()
    if not a:
        print('\nКонец файла')
        break
    for j in a:
        res = re.findall(r'[3]{1}[0-9,A-F]{1}[0,2,4,6,8,A,C,E]{1}|[2]{1}[0,2,4,6,8,A,C,E]{1}', j)
        if len(res) == 1:
            if len(j) == len(res[0]) and len(j)>0:
                print(res[0], end=" ")
                kol += 1
                if int(res[0], 16) > int(max, 16):
                    max = res[0]
                    s_max = j
if max == 0:
    print('В файле нет чисел, удовлетворяющих условию')
else:
    print('Количество:', kol)
    print('Максимальное число:', end=' ')
    for j in range(len(max)):
        for l in slov:
            if str(l) == max[j]:
                print(slov[l], end=' ')
                break