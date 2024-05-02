szam = int(input("Adj meg egy pozitív egész számot "))
if szam > 0:
    for i in range(szam):
        if i%2 == 0:
            print("0")
        else:
            print("1")
else:
    print("Ez nem egy pozitív szám")