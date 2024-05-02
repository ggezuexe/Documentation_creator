szó_1 = input("Adj meg egy szöveget ")
szó_2 = input("Adj meg egy szöveget ")
azonosak = []
for i in szó_1:
    for x in szó_2:
        if i == x:
            if i not in azonosak:
                azonosak.append(i)

if len(azonosak) != 0:
    print("Megtalálható mindkát szóban:", azonosak)
else:
    print("Nincsenek azonos betűk")