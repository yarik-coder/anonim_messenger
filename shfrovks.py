import random

aphavit = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюяa"
message = input()

shifr = []
shifr_chisel = []
for i in range(len(aphavit)):
    #print(i)
    for a in message:
        if aphavit[i] == a:
            #for_append = i + 1
            shifr.append(aphavit[i])
            shifr_chisel.append(i)

print(shifr[::-1])


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
        #print(message)


#print(message[::3])
