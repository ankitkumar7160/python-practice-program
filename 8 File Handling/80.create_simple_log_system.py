import datetime

def write_log(level, message):
    
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%M-%D  %H:%M:%S")
    
    log_entry = f"[{timestamp}] {level.upper()} {message}"
    
    with open("Programing_history" , "a") as log_file:
        log_file.write(log_entry)

def replace_word_with_loggin(old_word, new_word):
    try:
        with open("Note.txt", "r") as file:
            content = file.read()
        
        if old_word in content:
            new_content = content.replace(old_word, new_word)
            with open("Note.txt", "w") as file:
                file.write(new_content)
            
            write_log("INFO", f"Replace {old_word} with {new_word}")
            return "successfull"
        
        else:
            write_log("WARNING", f"Failed to replace {old_word} not found.")
            return "Word not found."
        
    except Exception as e:
        write_log("ERROR", f"System Crash {str(e)}")
        return "An error eccurred."
    
print(replace_word_with_loggin("Python", "Java"))