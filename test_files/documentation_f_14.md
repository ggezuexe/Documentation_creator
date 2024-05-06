The file `f_14.py` contains a Python script designed to print a rectangle composed of asterisks (`*`). The dimensions of the rectangle, specifically the width (`n`) and height (`m`), are determined by user input. Here's a breakdown of the script:

### Function: `teglalap(n, m)`
- **Parameters**:
  - `n`: integer representing the width of the rectangle (number of asterisks in each row).
  - `m`: integer representing the height of the rectangle (number of rows).
- **Behavior**: This function uses two nested loops:
  - The outer loop runs `m` times, each time representing a row.
  - The inner loop runs `n` times, adding an asterisk for each iteration to construct a single row.
  - At the end of each row (each iteration of the outer loop), a newline character is printed to move to the next line.
- **Output**: Prints a `m` by `n` rectangle made up of asterisks.

### Main Program:
- The script prompts the user twice to input integers:
  - The first prompt asks the user for an integer `n`, representing the width of the rectangle.
  - The second prompt asks for an integer `m`, representing the height.
- These values are then passed to the `teglalap` function to print the desired rectangle.

### Execution Example:
If the user inputs `4` for `n` and `3` for `m`, the output will be:
```
****
****
****
```
This rectangle consists of 3 rows of 4 asterisks each. 

This script is a simple example of user input handling and nested loops in Python, and it offers a practical demonstration of basic programming concepts such as functions, loops, and input/output operations.