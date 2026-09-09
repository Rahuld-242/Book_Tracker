from datetime import date
from book import Book

class ReadingRecord:
    def __init__(
        self,
        book: Book, 
        status: str, 
        current_page: int = 0, 
        start_date: date | None = None, 
        finish_date: date | None = None
        ):
        self.book = book
        self.status = status
        self.current_page = current_page
        self.start_date = start_date
        self.finish_date = finish_date
        
        
        
        