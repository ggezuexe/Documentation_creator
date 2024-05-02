szam_1 = int(input("Adj meg egy pozitív egész számot "))
szam_2 = int(input("Adj meg egy pozitív egész számot "))
if szam_1 < szam_2:
    for i in range(szam_1 + 1, szam_2):
        if i%2==0:
            print(i)
elif szam_1 > szam_2:
    for i in range(szam_2 + 1, szam_1):
        if i%2==0:
            print(i)
else:
    print("A két szám egyenlő")