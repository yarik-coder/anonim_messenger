import random

aphavit = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
message = input()

shifr = []
shifr_chisel = []
for a in message:
    for i in range(len(aphavit)):
        if aphavit[i] == a:
            for_append = i + 1
            if for_append == 59:
                for_append = for_append - 59
            shifr.append(aphavit[for_append])
            shifr_chisel.append(i)
message = shifr
#print(shifr)
n = ""
for i in shifr:
    n = n + i
print(n)
message = n

a = 2
poln_scet = 0
i = 0
#print(len(message))
while i < len(message):
    i = i + 1
    a += 1
    poln_scet += 1
    #print(i)
    if a == 3:
        b = random.randint(0, 59)
        b1 = random.randint(0, 59)
        dopp_bukva = aphavit[b1]
        dop_bukva = aphavit[b]
        #print(message[poln_scet])
        message = message[0: poln_scet] + dop_bukva + dopp_bukva + message[poln_scet:]
        a = 0
print(message)

#дешифровка↓
message = message[::3]
print(message)
shifr1 = []
shifr_chisel1 = []
for a in message:
    for i in range(len(aphavit)):
        if aphavit[i] == a:
            for_append = i - 1
            shifr1.append(aphavit[for_append])
            shifr_chisel1.append(i)

#print(shifr1)

n1 = ""
for i in shifr1:
    n1 = n1 + i
print(n1)
message = n1