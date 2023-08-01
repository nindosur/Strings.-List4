    # 1
string = "Lorem 5 ipsum dolor sit 1 amet, consectetur adipiscing elit.. phasellus 2 non sem blandit 4, suscipit ligula non, feugiat odio! mauris et eros."
countZ = 0 # знаки припинания
countValue = 0 # цифры
countV = 0 # знаки восклицания
# print(string.capitalize())
s = []
for i in range(len(string)):
    if string[i].isalnum() == False and string[i] != " ":
        countZ += 1
    if string[i] == "!":
        countV += 1
    elif string[i].isdigit() == True:
        countValue += 1
s = string.split(sep=". ",) # список разделитель
s2 = [] # доп список
for i in s:
    s2.append(i.capitalize())
print(s)
print(s2)
print("Знаки препинания: ", countZ)
print("Цифры: ", countValue)
print("Знаки восклицания: ", countV)

    # 2, 3
s = []
p = 1 # ввод
k = 0 # сравнение
summ = 0 # сумма
n = 0 # счетчик
k = int(input("Введите число для поиска: "))
while (p!=0):
    p = int(input("Введите число: "))
    if p!=0:
        s.append(p)
        summ += p
    if k == p:
        n += 1
print("Кол-во повторов: ", n)
print("Сумма: ", summ)
print("Сред. арифметическое: ", summ/len(s))