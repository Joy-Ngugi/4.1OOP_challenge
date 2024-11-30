class Book:
    def __init__(self, title, author, book_no):
        self.title=title
        self.author = author
        self.book_no = book_no
        self.is_borrowed = False
        
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False
    
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False
    
    def __str__(self):
        return f"Book[Title:{self.title}, author: {self.author}, Book No: {self.book_no}, Borrowed: {self.is_borrowed}]"
    
    
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_boooks = []
        
    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_boooks.append(book)
            return True
        return False
    
    def return_book(self, book):
        if book in self.borrowed_boooks:
            if book.return_book():
                self.borrowed_boooks.remove(book)
                return True
            return False
        
    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_boooks]
        return f"Member[Name: {self.name}, ID: {self.member_id}, Borrowed Books: {borrowed_titles}]"
    
class Library:
        def __init__(self):
            self.books = []
            self.members = []
            
        def add_book(self, book):
            self.books.append(book)
            
        def register_member(self, member):
            self.members.append(member)
            
        def find_book(self, book_no):
            for book in self.books:
                if book.book_no == book_no:
                    return book
            return None
        
        def find_member(self, member_id):
            for member in self.members:
                if member.member_id == member_id:
                    return member
            return None
        
        def borrow_book(self, member_id, book_no):
            member = self.find_member(member_id)
            book = self.find_book(book_no)
            if member and book:
                if member.borrow_book(book):
                    return f"{member.name} successfuly borrowed {book.title}"
                else:
                    return f"{book.title} is already borrowed."
            return "Member or book not found"
        
        def return_book(self, member_id, book_no):
            member = self.find_member(member_id)
            book = self.find_book(book_no)
            if member and book:
                if member.return_book(book):
                    return f"{member.name} returned {book.title}."
                else:
                    return f"{member.name} does not have {book.title}"
            return "Member or book not found"
        
        def __str__(self):
            books_state = "\n".join(str(book) for book in self.books)
            members_state= "\n".join(str(member) for member in self.members)
            return f"Library state:\nBooks:\n{books_state}\n\nMembers:\n{members_state}"
        
def main():
    library = Library()
    
    library.add_book(Book("Weep Not, Child", "Ngugi Wa Thiong'o", 1))
    library.add_book(Book("A Grain of Wheat", "Ngugi Wa Thiong'o", 2))
    library.add_book(Book("Untouchable", "Mulk Raj Anand", 3))
    library.add_book(Book("Animal Farm", "George Orwel", 4))
    
    
    library.register_member(Member("Joy", 101))
    library.register_member(Member("Martin", 102))
    
    
    print(library)

   
    print("\nBorrowing books:")
    print(library.borrow_book(101, 1))  
    print(library.borrow_book(102, 1)) 
    print(library.borrow_book(102, 2))  

   
    print("\nAfter borrowing:")
    print(library)

    
    print("\nReturning books:")
    print(library.return_book(101, 1)) 
    print(library.return_book(102, 3))  

    
    print("\nFinal state of library:")
    print(library)


if __name__ == "__main__":
    main()