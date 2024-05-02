szöveg = input("Írj valamit te cigány")
szöveg_lista = szöveg.split()
uj_szöveg = ""

for i in szöveg_lista:
    uj_szöveg = uj_szöveg + i

print(uj_szöveg)