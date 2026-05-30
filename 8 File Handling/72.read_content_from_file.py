# Function to read content from a file

def read_file():

    # File ko read mode me open karo
    with open("Note.txt", "r") as file:

        # File ka sara content read karo
        content = file.read()

    # Success message print karo
    print("File content read successfully.")

    # File ka content return karo
    return content

# Function call karke content print karo
print(read_file())