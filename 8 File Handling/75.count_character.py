def count_character():
    
    with open("Note.txt", "r") as file:
        content = content.strip()
        
        return len(file)
    
print(f"Characters in this file: {count_character()}")