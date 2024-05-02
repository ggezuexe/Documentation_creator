def teglalap(n, m):
    for _ in range(m):
        for _ in range(n):
            print("*", end = "")
        print("")
    return

n = int(input("Adj meg egy egész számot "))
m = int(input("Adj meg egy egész számot "))
teglalap(n, m)