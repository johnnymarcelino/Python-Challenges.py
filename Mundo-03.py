# ENCODING: UTF-8

# TUPLAS SÃO IMUTÁVEIS

# lanche = ('hambuger', 'suco', 'pizza', 'pudim', "Batata Frita")
# print(lanche[-2::-1])

'''for count in range(0, len(lanche)):
    print(f"Vou comer {lanche[count]} na posição {count}")
print("Comi pra caramba")
'''
'''for comida in lanche:
    print(f"Vou comer {comida}")
print("Comi pra caramba")
'''

'''for pos, count in enumerate(lanche):
    print(f"Vou comer {count}, na posição {pos}")
print("Comi pra caramba")'''

# print(sorted(lanche))

'''a = (1, 4, 7, 2)
b = (7, 9, 0, 1)
c = a + b
d = sorted(c)'''
# print(sorted(c))

# print(c.count(1))
'''print(d)
print(d[2])
print(f"temos {c.count(7)} número 7")
print(f"A sua primeira posição do 7 é {c.index(7)}")
print(f"A sua segunda posição do 7 é {c.index(7, 2+1)}")'''

'''pessoa = ("Johnny", 27, 1.70, 1,68, "M")
del(pessoa)
print(pessoa)'''

# CHALLENGE 72
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, do zero até vinte.
# Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostrá-lo por extenso

'''numExtenso = ("Zero", "One", "Two", "Tree", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
              "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty")
numeral = int(input("Enter any number between '0' and '20': "))
if(numeral > 20):
    while(numeral > 20):
        numeral = int(input("Enter any number between '0' and '20': "))

print(f"You have choose {numeral} in numeral and this number in extensive is {numExtenso[numeral]}")'''

# CHALLENGE 73

'''times = ("São Paulo", "Vasco", "Botafogo", "Cruzeiro", "Flamengo", "Coritiba", "Juventude", "Arsenal", "Man Unt", "Milan", "Liverpool",
              "Inter Milão", "Real Madrid", "Barcelona", "Bayer Muniq", "Chelsea", "PSG", "Palmeiras", "Corinthians", "Zenit", "Man City")
rank = 0
print(f"These are the rankings of the top 5 on the soccer table:\n{times[0:5]}")
print(f"These are the rankings of the last 4 on the soccer table:\n{times[-4:len(times):1]}")
print(f"This is the list of the club's classification in sort {sorted(times)}")
for pos in times:
    if(pos != "Barcelona"):
        rank += 1
    if(pos == "Barcelona"):
        break
print(f"Barcelona club it is in the position {times.index(pos)}ª of the classification!")'''

# CHALLENGE 74

'''from random import randint

# for tupla in range(random.randint(0, 10), 5):
#     lista = tupla
#     print(lista)
# tupla1 =
# tupla2 =
# tupla3 =
# tupla4 =
# tupla5 =

c = m = n = tupla = 0
e = f = 0
# tupla1 = tupla2 = tupla3 = tupla4 = 0
while(c != 5):
    # a = randint(0, 10)
    # print("numeros do A", a)
    # b = randint(0, 10)
    # print("numeros do B", b)
    # d = randint(0, 10)
    # print("numeros do D", d)
    # e = randint(0, 10)
    # print("numeros do E", e)
    # f = randint(0, 10)
    # print("numeros do F", f)
    # print()
    # tupla = tupla.split()
    # if(c == 0):
    #     m = n = a = b = d = e = f
    a = randint(0, 10)
    print("numeros do A", a)
    b = randint(0, 10)
    print("numeros do B", b)
    d = randint(0, 10)
    print("numeros do D", d)
    e = randint(0, 10)
    print("numeros do E", e)
    f = randint(0, 10)
    print("numeros do F", f)
    if(c == 0):
        m = n = a
    # else:
    if(a > m):
        m = a
    if(b > m):
        m = b
    if(d > m):
        m = d
    if(e > m):
        m = e
    if(f > m):
        m = f
    if(a < n):
        n = a
    if(b < n):
        n = b
    if(d < n):
        n = d
    if(e < n):
        n = e
    if(f < n):
        n = f
    # tupla = tuple(tupla)
    tupla = ((a), (b), (d), (e), (f))
    c = 5
print(f"The drawn numbers was: {tupla}")
print(f"The bigger number was {m}")
print(f"The lower number was {n}")

    # b = str(a)
    # tupla1 = str(a)
    # del(a)
    # d = str(a)
    # tupla2 = b + tupla1
    # del(b)
    # e = str(d)
    # tupla3 = e + tupla1 + tupla2
    # del(d)
    # f = str(e)
    # tupla4 = f + tupla1 + tupla2 + tupla3
    # del(e)
    # g = str(f)
    # tupla5 = g + tupla1 + tupla2 + tupla3 + tupla4
    # del(f)
    # total = list(tupla5)
    # print(d)'''


# CHALLENGE 75

'''total = 0
val1 = int(input("Enter with any number: "))
val2 = int(input("Enter with any number: "))
val3 = int(input("Enter with any number: "))
val4 = int(input("Enter with any number: "))
tupla = ((val1), (val2), (val3), (val4))
print(tuple(tupla))
print(f"The total of times that showed the number off '9' is {tupla.count(9)}")
if(3 not in tupla):
    print(f"The number '3' was not enter any time.")
else:
    print(f"The number '3' is in position {tupla.index(3)+1}ª")
count = 0
for pos, a in enumerate(tupla):
    if(a % 2 == 0):
        count += 1
        if(count == 1):
            total = (a)
            total2 = total
            del(a)
        if(count == 2):
            total1 = a
            total2 = (total, total1)
            # del(a)
        if(count == 3):
            total3 = a
            total2 = (total, total1, total3)
            # del(a)
        if(count == 4):
            total4 = a
            total2 = (total, total1, total3, total4)
            # del(a)
# if(val2 % 2 == 0):
#     count += 1
        print(f"We hava till now {count} even numbers and its positions is {pos+1}")
print(f"The total of even numbers is {count} and they are {total2}")'''

# CHALLENGE 76

'''# price = (1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90)
count = 0
listing = ("Pencil", 1.75, "Eraser", 2.00, "notebook", 15.90, "Pencil Case", 25.00, "Protractor", 4.20, "Compass", 9.99, "Schoolbag", 120.32, "Pens", 22.30, "Books", 34.90)
# print(listing[2], "R$", listing[3])
for products in listing:
    print(products[count], end="..............R$: ")
    count += 1
    print(listing[count])
    # print(price)'''

# CHALLENGE 77

'''lotWords = ("rice", "mouse", "notebook", "chair", "tv", "light", "sofa", "plate", "screem", "aleloui")
for vogal in lotWords:
    if("a" in vogal or "e" in vogal or "i" in vogal or "o" in vogal or "u" in vogal):
        a = vogal.find("a")
        e = vogal.find("e")
        i = vogal.find("i")
        o = vogal.find("o")
        u = vogal.find("u")
        print(f"In phrase {vogal}, we have the vowels {vogal[a]}, {vogal[e]}, {vogal[i]}, {vogal[o]}, {vogal[u]}")
    if ("a" in vogal or "e" in vogal or "i" in vogal or "o" in vogal):
        a = vogal.find("a")
        e = vogal.find("e")
        i = vogal.find("i")
        o = vogal.find("o")
        print(f"In phrase {vogal}, we have the vowels {vogal[a]}, {vogal[e]}, {vogal[i]}, {vogal[o]}")
    if ("a" in vogal or "e" in vogal or "i" in vogal):
        a = vogal.find("a")
        e = vogal.find("e")
        i = vogal.find("i")
        print(f"In phrase {vogal}, we have the vowels {vogal[a]}, {vogal[e]}, {vogal[i]}")
    if ("a" in vogal or "e" in vogal):
        a = vogal.find("a")
        e = vogal.find("e")
        print(f"In phrase {vogal}, we have the vowels {vogal[a]}, {vogal[e]}")
    if ("a" in vogal):
        a = vogal.find("a")
        print(f"In phrase {vogal}, we have the vowels {vogal[a]}")
    if ("e" in vogal):
        e = vogal.find("e")
        print(f"In phrase {vogal}, we have the vowels {vogal[e]}")
    if ("i" in vogal):
        i = vogal.find("i")
        print(f"In phrase {vogal}, we have the vowels {vogal[i]}")
    if ("o" in vogal):
        o = vogal.find("o")
        print(f"In phrase {vogal}, we have the vowels {vogal[o]}")
    if ("u" in vogal):
        u = vogal.find("u")
        print(f"In phrase {vogal}, we have the vowels {vogal[u]}")
    # else:
    #     print("This is not in 'aeiou'")
    # print(vogal)'''