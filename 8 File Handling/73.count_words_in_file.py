def count_word():
    
    with open("File Handling/Note.txt", "r") as file:
        content = file.read()
    
    words = content.split()
    
    return len(words)

print(count_word())