from abc import ABC, abstractmethod

# 1. SRP: Клас Book відповідає лише за дані книги
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

# 4. ISP: Інтерфейс для основних методів бібліотеки
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, book_title: str):
        pass
    
    @abstractmethod
    def get_all_books(self):
        pass
    
    @abstractmethod
    def find_book(self, book_title: str):
        pass

# 2. OCP, 3. LSP: Клас Library реалізує інтерфейс і може бути розширений
class Library(LibraryInterface):
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    def remove_book(self, book_title: str):
        self._books = [book for book in self._books if book.title != book_title]

    def find_book(self, book_title: str):
        for book in self._books:
            if book.title == book_title:
                return book
        return None

    def get_all_books(self):
        return self._books
        
# 5. DIP: LibraryManager залежить від абстракції (LibraryInterface)
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str):
        try:
            year_int = int(year)
            book = Book(title, author, year_int)
            self.library.add_book(book)
            print(f"Book '{title}' added.")
        except ValueError:
            print("Invalid year. Please enter a number.")

    def remove_book(self, title: str):
        book_to_remove = self.library.find_book(title)
        if book_to_remove:
            self.library.remove_book(title)
            print(f"Book '{title}' removed.")
        else:
            print(f"Book '{title}' not found.")

    def show_books(self):
        books = self.library.get_all_books()
        if not books:
            print("The library is empty.")
        else:
            print("Current books in the library:")
            for book in books:
                print(f"- '{book.title}' by {book.author} ({book.year})")

def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()