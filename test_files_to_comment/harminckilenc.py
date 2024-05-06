import turtle

# Importing the turtle module to use its drawing capabilities

def paint(number):
    # Function to draw a regular polygon. 'number' refers to the number of sides.
    turtle.resetscreen()  # Clears the screen and resets turtle position and settings
    s = turtle.getscreen()  # Gets the turtle screen
    t = turtle.Turtle()  # Creates a new turtle object
    szog = 180 - (((number - 2) * 180)/number)  # Calculates the internal angle for the polygon
    for _ in range(number):  # Loops through the number of sides
        t.left(szog)  # Turns the turtle left by 'szog' degrees
        t.forward(100)  # Moves the turtle forward by 100 units

while True:
    n = int(input("Milyen szabályos poligont szeretne? "))  # Asks the user for a number of sides
    if n >= 3 and 9 >= n:  # Checks if the input is within the valid range (3 to 9)
        paint(n)  # Calls the paint function to draw the polygon
    else:
        print("Ilyet nem tudok :c")  # Prints an error message if the input is out of range
        break  # Exits the loop and ends the program