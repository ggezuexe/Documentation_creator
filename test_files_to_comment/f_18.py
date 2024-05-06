# Define a function to calculate the sum of all integers between two given numbers
def összeg(szam1, szam2):
    szam_össz = 0  # Initialize the sum variable to zero
    if szam1 < szam2:  # Check if the first number is less than the second number
        for i in range(szam1, szam2 + 1):  # Loop from the first number to the second number inclusive
            szam_össz = szam_össz + i  # Add each number to the sum
    elif szam1 > szam2:  # Check if the first number is greater than the second number
        for i in range(szam_2, szam_1 + 1):  # Loop from the second number to the first number inclusive
            szam_össz = szam_össz + i  # Add each number to the sum
    return szam_össz  # Return the total sum

# Main program starts here
szam_1 = int(input("Adj meg egy egész számot "))  # Prompt the user to enter the first integer
szam_2 = int(input("Adj meg egy egész számot "))  # Prompt the user to enter the second integer
szamok_összege = összeg(szam_1, szam_2)  # Call the function with the user inputs
print("A számok összege:", szamok_összege)  # Print the sum of the numbers