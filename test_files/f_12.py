szam_1 = int(input("Adj meg egy pozitív egész számot "))
szam_2 = int(input("Adj meg egy pozitív egész számot "))
if szam_1 < szam_2:
    for i in range(szam_1 + 1, szam_2):
        print(i)
else:
    print("Rosszul adtad meg")