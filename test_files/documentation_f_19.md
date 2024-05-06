The `f_19.py` file contains a Python script designed to identify and display the common characters between two strings input by the user. Here is a detailed breakdown of its functionality:

1. **Input Collection**:
   - The script begins by prompting the user twice to input text. These texts are stored in two variables, `szó_1` and `szó_2`.

2. **Initialization**:
   - An empty list named `azonosak` is initialized to store the unique common characters between `szó_1` and `szó_2`.

3. **Character Comparison**:
   - The script uses nested loops to compare each character in `szó_1` with each character in `szó_2`. If a common character is found and it is not already included in the `azonosak` list, it is appended to this list.

4. **Result Display**:
   - After all characters have been compared, the script checks if the `azonosak` list is not empty. If it contains characters, it prints them out with a message stating that these characters are found in both words. If the list is empty, a message is printed stating that there are no common characters.

This script is useful for determining overlapping characters between two pieces of textual input, potentially assisting in tasks like analyzing common typing errors or finding patterns in user inputs.