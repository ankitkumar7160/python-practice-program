# Copy content to another file

def copy_content():

    with open("Note.txt", "r") as file:
        content = file.read()
        
    n_content = content

    with open("Copy_Note.txt","w") as n_file:
        data = n_file.write(n_content)
        
    return "Content copy Successfully."

print(copy_content)