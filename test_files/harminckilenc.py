import turtle

def paint(number):
    turtle.resetscreen()
    s = turtle.getscreen()
    t = turtle.Turtle()
    szog = 180 - (((number - 2) * 180)/number)
    for _ in range(number):
        t.left(szog)
        t.forward(100)

while True:
    n = int(input("Milyen szabályos poligont szeretne? "))
    if n >= 3 and 9 >= n:
        paint(n)
    else:
        print("Ilyet nem tudok :c")
        break