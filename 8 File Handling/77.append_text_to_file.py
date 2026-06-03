# Append Text To File

def append_text(text):
    
    with open("Note.txt", "a") as file:
        content = file.write("\n"+text)
        
    return "Append text is Successfully."

text = input("Enter Data: ")

print(append_text(text))