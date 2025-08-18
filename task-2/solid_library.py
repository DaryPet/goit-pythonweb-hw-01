from abc import ABC, abstractmethod
from typing import List, Optional
from logger import get_logger

logger = get_logger(__name__)


# 1. SRP: Клас Book відповідає лише за дані книги
class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title: str = title
        self.author: str = author
        self.year: int = year


# 2. ISP: Інтерфейс для основних методів бібліотеки
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, book_title: str) -> bool:
        pass

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass

    @abstractmethod
    def find_book(self, book_title: str) -> Optional[Book]:
        pass


# 3. OCP, 3. LSP: Клас Library реалізує інтерфейс і може бути розширений
class Library(LibraryInterface):
    def __init__(self) -> None:
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, book_title: str) -> bool:
        for i, b in enumerate(self._books):
            if b.title == book_title:
                del self._books[i]
                return True
        return False

    def find_book(self, book_title: str) -> Optional[Book]:
        for book in self._books:
            if book.title == book_title:
                return book
        return None

    def get_all_books(self) -> List[Book]:
        return list(self._books)


# 5. DIP: LibraryManager залежить від абстракції (LibraryInterface)
class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library: LibraryInterface = library

    def add_book(self, title: str, author: str, year: str) -> None:
        try:
            year_int: int = int(year)
        except ValueError:
            logger.info("Invalid year. Please enter a number.")
            return
        self.library.add_book(Book(title, author, year_int))
        logger.info(f"Book '{title}' added.")

    def remove_book(self, title: str) -> None:
        if self.library.remove_book(title):
            logger.info(f"Book '{title}' removed.")
        else:
            logger.info(f"Book '{title}' not found.")

    def show_books(self) -> None:
        books: List[Book] = self.library.get_all_books()
        if not books:
            logger.info("The library is empty.")
            return
        logger.info("Current books in the library:")
        for book in books:
            logger.info(f"- '{book.title}' by {book.author} ({book.year})")


def main() -> None:
    library: LibraryInterface = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title: str = input("Enter book title: ").strip()
                author: str = input("Enter book author: ").strip()
                year: str = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title: str = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
