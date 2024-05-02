def összeg(szam1, szam2):
    szam_össz = 0
    if szam1 < szam2:
        for i in range(szam1, szam2 + 1):
            szam_össz = szam_össz + i
    elif szam1 > szam2:
        for i in range(szam_2, szam_1 + 1):
            szam_össz = szam_össz + i
    return szam_össz

szam_1 = int(input("Adj meg egy egész számot "))
szam_2 = int(input("Adj meg egy egész számot "))
szamok_összege = összeg(szam_1, szam_2)
print("A számok összege:", szamok_összege)