The file named `f_19.py` is a Python script that allows users to check for common characters between two inputted strings. Here's a step-by-step breakdown of what the script does:

1. **Input Collection**: The script prompts the user twice to input strings, storing them in `szó_1` and `szó_2`.

2. **Initialization of List**: A list named `azonosak` is initialized to store characters that are common between the two inputted strings.

3. **Character Comparison**:
    - The script uses nested loops to compare each character in `szó_1` with each character in `szó_2`.
    - If a common character is found and it has not yet been added to the `azonosak` list, it is appended to the list. This ensures that each character appears only once in the `azonosak` list.

4. **Output**:
    - If the `azonosak` list is not empty, the script prints the characters that are found in both strings.
    - If the `azonosak` list remains empty, it means there are no common characters between the two strings, and the script informs the user accordingly.

This script can be useful in various contexts, such as text analysis or games that involve character matching. The implementation ensures that the comparison process avoids duplicate entries in the results list.