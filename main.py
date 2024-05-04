import openai 
import os

class File_to_comment:
  # This class represents a file and its content
  def __init__(self, file_name, content, directory_path):
    # Initialize the object with file name, content and path
    # Store the name of the file
    self.file_name = file_name
    # Store the content of the file
    self.content = content
    # Store the path to the file
    self.directory_path = directory_path

def remove_file_extension(file_name):
    # Split the file name based on the period ('.') character
    parts = file_name.split('.')
    
    # If there are more than one part, remove the last part (which is the extension)
    if len(parts) > 1:
        return '.'.join(parts[:-1])
    else:
        # If there is only one part, return the file name as is
        return file_name

# Function to read all files in a directory
def read_files_in_directory(directory_path):
    #Create a list of files
    files_to_return = []

    # Check if the directory exists
    if not os.path.isdir(directory_path):
        print("Directory does not exist.")
        return
    
    # List all files in the directory
    files = os.listdir(directory_path)
    
    # Iterate through each file
    for file_name in files:
        # Construct the full path to the file
        file_path = os.path.join(directory_path, file_name)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Read the file
            with open(file_path, 'r') as file:
                # Append the file and its contents to the list
                files_to_return.append(File_to_comment(file_name, file.read(), directory_path))
                
    # Return the list of files and their contents
    return files_to_return

def create_documentation(file):
    # Define a list of messages to be used as input for the OpenAI chat completion model
    MSGS = [
        # Initial message from the system, describing the user's role
        {"role": "system", "content": "You are a software engineer, your primary role is to assist users in creating documentation for their code."},
        # Message from the user, providing the file name
        {"role": "user", "content": "The name of the file: " + file.file_name},
        # Message from the user, providing the file content
        {"role": "user", "content": "The content of the file: " + file.content},
        # Follow-up message from the system, asking for a description of the file
        {"role": "system", "content": "Please provide a description of the file"},
    ]

    # Create a chat completion response using the OpenAI API
    response = openai.ChatCompletion.create(
        # Specify the model to use (in this case, gpt-4-turbo)
        model="gpt-4-turbo",
        # Pass in the list of messages as input
        messages=MSGS,
        # Set the maximum number of tokens in the response
        max_tokens=4095,
        # Request a single response (n=1)
        n=1,
    )

    # Construct the path for the output documentation file
    path = file.directory_path + "/" + "documentation_" + remove_file_extension(file.file_name) + ".md"

    # Open the file in write mode
    documentation = open(path, "w")

    # Write the response from the OpenAI model to the file
    documentation.write(response.choices[0].message["content"])

    # Close the file
    documentation.close()

# Prompt the user to enter an OpenAI API token
token = input("Give me a token: ")

# Set the OpenAI API key using the provided token
openai.api_key = token

# Prompt the user to enter a directory path
directory_path = input("Give me a directory: ")

# Read the files in the specified directory using a function called read_files_in_directory
files = read_files_in_directory(directory_path)

# Iterate over the list of files
for file in files:
    # Call the create_documentation function for each file, passing the file object as an argument
    create_documentation(file)