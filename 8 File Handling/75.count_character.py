# Count Character in file

def count_character():

    # File ko read mode me open karo
    with open("Note.txt", "r") as file:

        # File ka sara content read karo
        content = file.read()

        # Extra spaces remove karo
        content = content.strip()

    # Total characters return karo
    return len(content)

# Total characters print karo
print(f"Characters in this file: {count_character()}")