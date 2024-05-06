import openai 
import os
import concurrent.futures
import time

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

def create_summary_documentation(files):
    # Define a list of messages to be used as input for the OpenAI chat completion model
    MSGS = [
        # Initial message from the system, describing the user's role
        {"role": "system", "content": "You are a software engineer, your primary role is to assist users in creating a big summary documentation for their code. "},
    ]

    # Loop through the list of files
    for file in files:
        # Add a message to the MSGS list with the file name
        MSGS.append({"role": "user", "content": "The name of the file: " + file.file_name})
        
        # Add a message to the MSGS list with the file content
        MSGS.append({"role": "user", "content": "The content of the file: " + file.content})
        
    # Add a message to the MSGS list prompting the user for a file description
    MSGS.append({"role": "system", "content": "Make a large summary document of the files below."})

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
    path = file.directory_path + "/" +"summary_documentation.md"

    # Open the file in write mode
    documentation = open(path, "w")

    # Write the response from the OpenAI model to the file
    documentation.write(response.choices[0].message["content"])

    # Close the file
    documentation.close()

def menu_1(files):
    # Initialize an empty list to store futures
    futures = []

    # Create a ThreadPoolExecutor with max_workers equal to the number of files
    # This allows us to process multiple files concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(files)) as executor:
        # Submit a task to create documentation for each file and store the future in the list
        for file in files:
            futures.append(executor.submit(create_documentation, file))
            # Introduce a delay of 2 seconds between submitting tasks to avoid overwhelming the executor (because of the rate limit in the Openai API)
            time.sleep(2)

        for future in futures:
            # Wait for the task to complete
            future.result()

def comment_codes(file):
    MSGS = [
        # Initial message from the system, describing the user's role
        {"role": "system", "content": "You are a software engineer, your primary role is to assist users in creating comments for their code."},
        # Message from the user, providing the file name
        {"role": "user", "content": "The name of the file: " + file.file_name},
        # Message from the user, providing the file content
        {"role": "user", "content": "The content of the file: " + file.content},
        # Follow-up message from the system, asking for a commented version of the file
        {"role": "system", "content": "Please provide a commented version of the file do NOT return anything else."},
        {"role": "system", "content": "Do not add something like this to it: ```python ```"},
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

    #Remove the original file
    file_path = file.directory_path + "/" + file.file_name
    os.remove(file_path)

    # Construct the path for the output documentation file
    path = file.directory_path + "/" + file.file_name

    # Open the file in write mode
    documentation = open(path, "w")

    # Write the response from the OpenAI model to the file
    documentation.write(response.choices[0].message["content"])

    # Close the file
    documentation.close()

def menu_3(files):
    # Initialize an empty list to store futures
    futures = []

    # Create a ThreadPoolExecutor with max_workers equal to the number of files
    # This allows us to process multiple files concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(files)) as executor:
        for file in files:
            futures.append(executor.submit(comment_codes, file))
            # Introduce a delay of 3 seconds between submitting tasks to avoid overwhelming the executor (because of the rate limit in the Openai API)
            time.sleep(3)

        for future in futures:
            future.result()

def main():
    # Prompt the user to enter an OpenAI API token
    token = input("Give me a token: ")

    # Set the OpenAI API key using the provided token
    openai.api_key = token

    # Prompt the user to enter a directory path
    directory_path = input("Give me a directory: ")

    # Read the files in the specified directory using a function called read_files_in_directory
    files = read_files_in_directory(directory_path)

    # Displaying a menu and executing corresponding actions based on user input
    menutext = ""
    while menutext != "4":
        print('Choose a mode:')
        print("1. Create a document for every file")
        print("2. Create a big summary document")
        print("3. Add comments")
        print("4. Exit")
        menutext = input("")
        if menutext == "1":
            menu_1(files)  # Execute function to create a document for each file
        elif menutext == "2":
            create_summary_documentation(files)  # Execute function to create a summary document
        elif menutext == "3":
            menu_3(files) # Execute function to create comments
        elif menutext == "4":
            print("Bye! :)")  # Inform user of exit
        else:
            print("Wrong number")  # Inform user of incorrect input
        print()  # Add a newline for readability after each menu iteration


if __name__ == "__main__":
    main()  # Execute the main function when the script is run directly