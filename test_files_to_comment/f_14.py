# This file defines and uses a function to print a rectangle made of asterisks.

def teglalap(n, m):
    """
    Prints a rectangle of asterisks with n width and m height.
    
    Parameters:
    n (int): The number of asterisks in a row.
    m (int): The number of rows in the rectangle.
    """
    for _ in range(m):  # Loop over the number of rows
        for _ in range(n):  # Loop over the number of asterisks in a row
            print("*", end="")  # Print an asterisk without moving to a new line
        print("")  # Move to the next line after finishing a row
    return

# Main section of the script
n = int(input("Adj meg egy egész számot "))  # Prompt user to input the width of the rectangle
m = int(input("Adj meg egy egész számot "))  # Prompt user to input the height of the rectangle
teglalap(n, m)  # Call the function with user inputs to print the rectangle