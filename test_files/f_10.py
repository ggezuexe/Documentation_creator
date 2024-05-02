szam = int(input("Adj meg egy pozitív egész számot "))
if szam > 0:
    x = 0
    összeg  = 0
    for i in range(szam - 1):
        x = i +1
        összeg = összeg + x
    print("A számok összeg:",összeg)
else:
    print("Ez nem egy pozitív szám")