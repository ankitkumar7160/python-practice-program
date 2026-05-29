# Function to read content from a file

def read_file():
    with open("8 File Handling/Note.txt", "r") as file:
        content = file.read()

    print("File content read successfully.")
    return content

print(read_file())