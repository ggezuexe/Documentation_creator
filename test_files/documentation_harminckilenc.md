The Python script named `harminckilenc.py` uses the `turtle` module to draw regular polygons based on user input. Here’s a breakdown of its functionality:

1. **Importing Module:** It starts by importing the `turtle` module, which is a popular way to introduce programming to kids. It provides a drawing board called turtle graphics where commands for movement and drawing can be executed.

2. **Function Definition (`paint`):** 
   - The `paint` function takes a single parameter, `number`, representing the number of sides of the polygon to draw.
   - Within the function, `turtle.resetscreen()` is called to clear the screen and reset the turtle’s state.
   - The turtle screen is obtained through `turtle.getscreen()`, and a new turtle object for drawing is created.
   - The angle `szog` (Hungarian for angle) is calculated using the formula for the interior angle of a regular polygon: `180 - (((number - 2) * 180) / number)`.
   - A for loop runs `number` times to draw each side of the polygon: the turtle turns left by the `szog` and moves forward by 100 units.

3. **Main Loop:** 
   - The script continuously prompts the user for input with the message "Milyen szabályos poligont szeretne?" which translates to "What kind of regular polygon would you like?"
   - If the input number of sides, `n`, is between 3 and 9 (inclusive), the `paint` function is invoked to draw the polygon.
   - If the number is not within the specified range, it prints the message "Ilyet nem tudok :c" ("I can't do this :c" in English) and breaks out of the loop, thus terminating the program.

This program is interactive and visual, making it particularly engaging for users who are learning programming concepts or who enjoy graphical demonstrations through coding. It demonstrates the use of loops, conditional statements, user input, and basic geometry in programming.