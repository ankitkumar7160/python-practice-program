class Book():
    
    def __init__(self,book_id,title,author):
        self.book_ID = book_id
        self.title = title
        self.author = author
        self.status = "Available"
        
    def __str__(self):
        return f"""
    Book ID : {self.book_ID}
    Book Title : {self.title}
    Author : {self.author}
    """
    
