def without_i(string):
    "Преобразует вхдную строку в список, исключая ' и '"
    str_list = string.split()
    new_list = []
    for i in str_list:
        if i != "и":
            new_list.append(i)
    return new_list


def str_to_num():
    "1.Задаем словарь. 2.меняем строки в списке на числа поразрядно. 3.суму разрядов выводим на печать"
    a = without_i(l)
    th_index = -1
    sum = 0
    dict = {
        "ноль": 0, "один": 1, "одна": 1, "два": 2, "две": 2, "три": 3, "четыре": 4, "пять": 5, "шесть": 6, "семь": 7,
        "восемь": 8, "девять": 9,
        "десять": 10, "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,
        "шестьнадцать": 16, "семьнадцать": 17, "восемнадцать": 18, "девятнадцать": 19,
        "двадцать": 20, "тридцать": 30, "сорок": 40, "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70,
        "восемьдесят": 80, "девяносто": 90,
        "сто": 100, "двести": 200, "триста": 300, "четыреста": 400, "пятьсот": 500, "шестьсот": 600, "семьсот": 700,
        "восемьсот": 800, "девятьсот": 900
    }
    for i in range(len(a)):
        if a[i] in ("тысячи", "тысяч", "тысяча"):
            th_index = i
    for i in range(0, th_index):
        a[i] = dict[a[i]] * 1000
        sum += a[i]
    if th_index == 0:
        sum = 1000
    for i in range(th_index + 1, len(a)):
        a[i] = dict[a[i]]
        sum += a[i]
    print(sum)


l = input("Enter a number from 0 to 1 million in text format in Russian:")
try:  # проверка на ошибки
    if l in ("миллион", "один миллион"):
        print(1000000)
    else:
        without_i(l)
        str_to_num()
except:
    print("You entered the wrong data format\nHave a nice day!")
