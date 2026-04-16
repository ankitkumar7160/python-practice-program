# Create File Method Fuction
print("Write your note in Notes file.")

def create_file(new_file):
    file = open("File Handling/Note.text", "a")
    file.write("\n" + new_file)
    file.close()
    
    return "Successfully Write in the file."

new_file = input("Enter data: ")
print(create_file(new_file))