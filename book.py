class Book:
    def __init__(self, title, author, book_type, total_pages):
        if type(title) is not str:
            raise TypeError
        
        if title.strip()=="":
            raise ValueError
        
        self.title = title.strip()
        
        if type(author) is not str:
            raise TypeError
        
        if author.strip()=="":
            raise ValueError
        
        self.author = author.strip()
        
        if type(book_type) is not str:
            raise TypeError
        
        if book_type not in ["fiction", "non_fiction"]:
            raise ValueError
        
        self.book_type = book_type
        
        if type(total_pages) is not int:
            raise TypeError
        
        if total_pages<=0:
            raise ValueError
        
        self.total_pages = total_pages
            