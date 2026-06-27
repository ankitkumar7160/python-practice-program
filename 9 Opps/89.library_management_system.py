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
    
class Member:
    
    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name
        self.issued_book = []
        
    def __str__(self):
        return f"""
    Member Name : {self.name}
    Member ID : {self.member_id}
    Books : {[b.title for b in self.issued_book]}
    """
    
class Library:
    
    def __init__(self):
        self.books = {}
        self.members = {}
        
    def add_books(self,book_id,title,author):
        new_book = Book(book_id,title,author)
        self.books[book_id] = new_book
        return 'book added.'
    
    def add_member(self,member_id,name):
        new_member = Member(member_id,name)
        self.members[member_id] = new_member
        return "Member Add Successfully."
    
    def issued_book(self,m_id,b_id):
        if b_id in self.book and m_id in self.members:
            book = self.books[b_id]
            member = self.members[m_id]
            
            if book.status == "Available":
                book.status = "Issued"
                member.issued_book.append(book)
                return f"Success: {book.title} issued to {member.name}"
            
            else:
                return "Error Book is already issued."
        else:
            return "Error: Invalid User ID or Book ID."
    
    
                