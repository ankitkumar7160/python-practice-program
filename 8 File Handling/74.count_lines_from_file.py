def count_lines():
    
    with open ("Note.txt", "r") as file:
        lines = file.readlines()
        
        file.close()
        
        return len(lines)

print(count_lines())