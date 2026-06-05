import datetime

def write_log(level, message):
    
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%M-%D  %H:%M:%S")
    
    log_entry = f"[{timestamp}] {level.upper()} {message}"
    
    with open("Programing_history" , "a") as log_file:
        log_file.write(log_entry)
