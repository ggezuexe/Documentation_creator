# Request user input and store it in the variable 'szöveg'
szöveg = input("Írj valamit")
# Split the entered text into a list of words and store in 'szöveg_lista'
szöveg_lista = szöveg.split()
# Initialize an empty string to build the new string
uj_szöveg = ""

# Iterate over each word in the list
for i in szöveg_lista:
    # Append each word to the 'uj_szöveg' variable
    uj_szöveg = uj_szöveg + i

# Print the concatenated string, which removes any spaces between words
print(uj_szöveg)