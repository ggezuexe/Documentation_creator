import openai 
from os import listdir
from os.path import isfile, join

token  = input("Give me a token: ")
openai.api_key = token

directory  = input("Give me the directory: ")
onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]

for i in onlyfiles:
    print(i.read())