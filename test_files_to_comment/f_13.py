# Request the user to input a positive integer and store it in `szam_1`
szam_1 = int(input("Adj meg egy pozitív egész számot "))

# Request the user to input another positive integer and store it in `szam_2`
szam_2 = int(input("Adj meg egy pozitív egész számot "))

# Check if the first number is less than the second number
if szam_1 < szam_2:
    # If true, loop through numbers between `szam_1` and `szam_2`
    for i in range(szam_1 + 1, szam_2):
        # Check if the current number is even
        if i % 2 == 0:
            # If it is even, print the number
            print(i)
# Check if the first number is greater than the second number
elif szam_1 > szam_2:
    # If true, loop through numbers between `szam_2` and `szam_1`
    for i in range(szam_2 + 1, szam_1):
        # Check if the current number is even
        if i % 2 == 0:
            # If it is even, print the number
            print(i)
# The case where both numbers are equal
else:
    # Print that the two numbers are equal
    print("A két szám egyenlő")