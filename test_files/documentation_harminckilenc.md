The `harminckilenc.py` script is a Python program that uses the `turtle` graphics module to draw regular polygons based on user input. Here's a detailed breakdown of its functionality:

1. **Importing Modules:**
   - The script imports the `turtle` module, which is used for drawing shapes and graphics.

2. **Defining the `paint` Function:**
   - `paint(number)`: This function takes a single argument, `number`, which specifies the number of sides of the polygon to be drawn.
   - Inside the function, the turtle's screen is reset using `turtle.resetscreen()`.
   - A new turtle object `t` is created.
   - The angle `szog` of each turn the turtle makes is calculated based on the formula for interior angles of a regular polygon (`180 - (((number - 2) * 180)/number`).
   - The turtle then iterates through a loop `number` times, each time turning left by `szog` degrees and moving forward by a fixed length (100 units).

3. **Main Loop:**
   - The script runs an infinite loop where it prompts the user to input the desired number of sides for the polygon with the message: "Milyen szabályos poligont szeretne?" (Which regular polygon would you like to draw?).
   - The user's input is captured and converted into an integer (`n`).
   - It checks whether the input `n` is between 3 and 9 (inclusive). If true, the `paint(n)` function is called to draw the corresponding polygon.
   - If the input is outside the accepted range, the script prints "Ilyet nem tudok :c" (I cannot do that :c) and breaks out of the loop, effectively ending the program.

This straightforward program combines user interaction with graphical output, demonstrating basic usage of Python’s turtle module for educational and visual fun by drawing different regular polygons based on user-driven parameters.