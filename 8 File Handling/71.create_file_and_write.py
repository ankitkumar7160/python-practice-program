# Create File Method Function

print("Write your note in Notes file.")

def create_file(new_file):
    file = open("Note.txt", "a")   # File open in append mode
    file.write("\n" + new_file)
    file.close()

    return "Successfully written in the file."

new_file = input("Enter data: ")
print(create_file(new_file))