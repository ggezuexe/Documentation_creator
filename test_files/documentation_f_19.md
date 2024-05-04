The Python script `f_19.py` is designed to identify common characters between two textual inputs given by the user. Here's a breakdown of how the script operates:

1. **Input Collection**: The script prompts the user twice to enter a string of text. These inputs are stored in the variables `szó_1` and `szó_2`.

2. **Initialization of List**: An empty list `azonosak` is created to store characters that are found in both input strings.

3. **Nested Loops for Comparison**:
    - The script uses nested `for` loops to compare each character in `szó_1` with every character in `szó_2`.
    - If a matching character is found (i.e., a character present in both strings) and that character is not already in the list `azonosak`, it is added to the list.
  
4. **Output**:
    - After the comparison is complete, the script checks if the list `azonosak` contains any characters. 
    - If the list is not empty, it prints the characters that were found in both strings.
    - If the list is empty, it prints a message indicating that no common characters were found.

Overall, this script is useful for identifying overlapping characters between two text inputs, which can be applied in various scenarios such as finding commonalities in word-based games or in basic cryptographic analyses.