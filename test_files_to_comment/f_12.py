# Request the user to enter a positive integer and store it in szam_1
szam_1 = int(input("Adj meg egy pozitív egész számot "))  
# Request the user to enter another positive integer and store it in szam_2
szam_2 = int(input("Adj meg egy pozitív egész számot "))  
# Compare the two numbers to determine the order
if szam_1 < szam_2:  
    # If szam_1 is less than szam_2, loop through the numbers between them
    for i in range(szam_1 + 1, szam_2):  
        # Print each number in the range
        print(i)  
else:
    # If the first number is not less than the second, output an error message
    print("Rosszul adtad meg")  