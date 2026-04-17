def read_file():
    
    with open("File Handking/Note.text", "r") as file:
        
        content = file.read()
        
    file.close()
    
    print("File content read Successfully.")
    
    return