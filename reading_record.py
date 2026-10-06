from datetime import date
from book import Book

class ReadingRecord:
    def __init__(
        self,
        book: Book
        ):
        if not isinstance(book, Book):
            raise TypeError
        self.book = book
        self.status = "TBR"
        self.current_page = None
        self.start_date = None
        self.finish_date = None
        
    def start_reading(self):
        if self.status == "TBR":
            self.status="Currently Reading"
            self.current_page=0
            self.start_date=date.today()
        elif self.status == "Currently Reading":
            raise RuntimeError("Book already being read")
        elif self.status=="Finished":
            raise RuntimeError("You have already finished this book")
        else:
            raise RuntimeError("Unknown reading status")
        
    def update_progress(self, new_page: int):
        if self.status!="Currently Reading":
            raise RuntimeError("Book should be in Currently Reading")
        if type(new_page) is not int:
            raise TypeError("Enter a valid page number")
        if new_page<0 or new_page>self.book.total_pages:
            raise ValueError("Page number must be between 0 and total pages")
        self.current_page=new_page
        if self.current_page==self.book.total_pages:
            self.status="Finished"
            self.finish_date=date.today()
            
    def mark_finished(self, finish_date: date | None = None):
        if self.status not in ["Currently Reading", "TBR"]:
            raise RuntimeError("Book should be either in TBR or Currently Reading")
        if finish_date is None:
            self.finish_date=date.today()
        else:
            if not isinstance(finish_date, date):
                raise TypeError("The date should be numeric")
            if self.start_date is not None:
                if finish_date<self.start_date:
                        raise ValueError("Finish date cannot be ahead of start date")
            self.finish_date=finish_date   
        self.status="Finished"
        
    def mark_dnf(self):
        if self.status!="Currently Reading":
            raise RuntimeError("Book should be in Currently Reading")
        self.status = "DNF"
        
        