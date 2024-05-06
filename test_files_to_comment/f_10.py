# Request the user to input a positive integer and store it in 'szam'
szam = int(input("Adj meg egy pozitív egész számot "))

# Check if the input number is greater than 0
if szam > 0:
    # Initialize variables x and összeg to 0
    x = 0
    összeg  = 0
    
    # Loop from 0 to szam-1
    for i in range(szam - 1):
        # Increase x by 1 in each iteration
        x = i + 1
        # Add the current value of x to összeg
        összeg = összeg + x
        
    # Display the sum of numbers from 1 to szam-1
    print("A számok összeg:",összeg)
else:
    # Print error message if the input is not a positive number
    print("Ez nem egy pozitív szám")