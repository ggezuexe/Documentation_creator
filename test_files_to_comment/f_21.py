# f_21.py

def csillag(szó_1):
    # Function to print an asterisk (*) for each character in the input string szó_1
    for _ in range(len(szó_1)):
        print("*")  # Print asterisk
    return  # End of function

szó = input("Adj meg egy szöveget ")  # Prompt user to enter a text
csillag(szó)  # Call the csillag function with the user input as argument