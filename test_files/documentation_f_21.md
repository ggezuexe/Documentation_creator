### File Description: f_21.py

`f_21.py` is a Python script that defines and utilizes a function named `csillag` to print asterisks based on the length of a given input string.

#### Function: `csillag`
- **Purpose**: Prints an asterisk "*" for each character in the input string.
- **Parameter**:
  - `szó_1`: A string for which the number of asterisks equal to its length will be printed.
- **Returns**: None. The function primarily has side effects (printing).

#### Usage:
- The script prompts the user to input a string with the message "Adj meg egy szöveget", which translates to "Provide a text."
- It then calls the `csillag` function using the user's input as an argument.

#### Example:
If the user inputs "hello", the output will be:
```
*
*
*
*
*
```
Here, one asterisk is printed for each of the 5 characters in "hello".
This script could be used in scenarios where a simple visualization of string length is needed, such as in beginner programming classes to demonstrate loops and function usage.

#### Additional Suggestions (if applicable):
- Consider adding or modifying the function to provide different or more complex functionalities, such as printing other symbols or including the count of characters printed.
- Enhance user interaction by providing more descriptive prompts or output messages.