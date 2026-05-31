# Count lines from file

def count_lines():

    # File ko read mode me open karo
    with open("Note.txt", "r") as file:

        # File ki sabhi lines read karo
        lines = file.readlines()

    # Total lines return karo
    return len(lines)

# Total lines print karo
print(count_lines())