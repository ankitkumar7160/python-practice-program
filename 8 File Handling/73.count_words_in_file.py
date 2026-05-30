# Function to count words in file

def count_word():

    # File ko read mode me open karo
    with open("Note.txt", "r") as file:

        # File ka sara content read karo
        content = file.read()

    # Content ko words me divide karo
    words = content.split()

    # Total words return karo
    return len(words)

# Total words print karo
print("Total words:", count_word())