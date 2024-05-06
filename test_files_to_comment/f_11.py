# Request an integer input from the user and store it in 'szam'
szam = int(input("Adj meg egy pozitív egész számot "))

# Check if the input number is greater than 0
if szam > 0:
    # Iterate through a range from 0 to the entered number
    for i in range(szam):
        # Check if the current number 'i' is even
        if i%2 == 0:
            print("0")
        else:
            # Print '1' if 'i' is odd
            print("1")
else:
    # Output an error message if the entered number is non-positive
    print("Ez nem egy pozitív szám")