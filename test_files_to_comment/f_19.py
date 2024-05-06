# f_19.py - This script finds common letters between two input words and prints them.

# Request an input string from the user and store it in szó_1
szó_1 = input("Adj meg egy szöveget ")
# Request another input string from the user and store it in szó_2
szó_2 = input("Adj meg egy szöveget ")

# Initialize an empty list to store letters common to both input strings
azonosak = []

# Iterate over each character in the first input string
for i in szó_1:
    # For each character in the first string, iterate through each character in the second string
    for x in szó_2:
        # Check if the current character of the first string matches any character of the second string
        if i == x:
            # Ensure the character has not already been recorded as a common character
            if i not in azonosak:
                # Add the character to the list of common characters
                azonosak.append(i)

# Check if the list of common characters is not empty
if len(azonosak) != 0:
    # If common characters exist, print them
    print("Megtalálható mindkát szóban:", azonosak)
else:
    # If there are no common characters, inform the user
    print("Nincsenek azonos betűk")