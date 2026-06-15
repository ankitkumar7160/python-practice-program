class constructor_example:
    
    def __init__(self,name,roll_no,s_class):
        self.name = name
        self.roll_no = roll_no
        self.subject = []
        self.s_class = s_class
        self.marks = None

    def s_marks(self):
        
        subject_count = len(self.subject)
        
        if subject_count == 0:
            return "Enter Subject First"
        
        while True:
            user_input= input(f"Enter each {subject_count} subject Marks, Seperated by space : ")
            new_marks = [ int(x) for x in user_input.split()]
            
            if len(new_marks) == subject_count:
                self.marks = new_marks
                break
            else:
                print("oops try again!")
    
    