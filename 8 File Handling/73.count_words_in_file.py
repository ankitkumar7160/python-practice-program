# Function to count words in file

def count_word():

    with open("Note.txt", "r") as file:
        content = file.read()

    words = content.split()

    return len(words)

print("Total words:", count_word())