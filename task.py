from typing import Dict


class Author:
    def __init__(self, author_id: int, name: str):
        self.author_id = author_id
        self.name = name


class Book:
    def __init__(self, book_id: int, title: str, author_id=None, num_pages=None):
        self.book_id = book_id
        self.title = title
        self.author_id = author_id
        self.num_pages = int(num_pages) if num_pages else None


class Library:
    def __init__(self):
        self.authors: Dict[int, Author] = {
            1: Author(1, "Jane Austen"),
            2: Author(2, "F. Scott Fitzgerald"),
            3: Author(3, "William Shakespeare")
        }
        self.books: Dict[int, Book] = {
            1: Book(1, "Pride and Prejudice", author_id=1, num_pages=266),
            2: Book(2, "The Great Gatsby", author_id=2, num_pages=192),
            3: Book(3, "Romeo and Juliet", author_id=3, num_pages=128)
        }
        self.next_book_id = 4
        self.next_author_id = 4

    def display_books(self):
        if self.books:
            print("All Books:")
            for book_id, book in self.books.items():
                print(f"ID: {book.book_id}")
                print(f"Title: {book.title}")
                if book.author_id in self.authors:
                    print(f"Author: {self.authors[book.author_id].name}")
                if book.num_pages:
                    print(f"Number of Pages: {book.num_pages}")
                print()
        else:
            print("No books available.")

    def add_new_book(self, book_name: str):
        author_name = input("Who is the author of the book? ").title()
        num_pages = input("How many pages does the book have? ")
        author_id = None

        for id_, author in self.authors.items():
            if author.name == author_name:
                author_id = id_
                break
        if author_id is None:
            author_id = self.next_author_id
            self.authors[author_id] = Author(author_id, author_name)
            self.next_author_id += 1

        new_book = Book(self.next_book_id, book_name, author_id, num_pages)
        self.books[self.next_book_id] = new_book
        self.next_book_id += 1
        print(f"Added '{new_book.title}' to the library.")

    def display_authors(self):
        if self.authors:
            print("All Authors:")
            for author_id, author in self.authors.items():
                print(f"- ID: {author_id}, Name: {self.authors[author_id].name}")
            author_id = input("Enter the author ID to display their books-> ")
            if author_id:
                try:
                    author_id = int(author_id)
                    if author_id in self.authors:
                        author = self.authors[author_id]
                        author_books = [book for book in self.books.values() if book.author_id == author_id]
                        if author_books:
                            print(f"\nBooks by Author {author.name}")
                            for book in author_books:
                                print(f"Title: {book.title}")
                                print(f"Pages Numbers: {book.num_pages}")
                        else:
                            print("No books available for this author.")
                    else:
                        print("Invalid author ID.")
                except ValueError:
                    print("Invalid input. Please enter a valid author ID.")
        else:
            print("No authors available")

    def add_new_author(self, author_name: str):
        author_id = self.next_author_id
        self.authors[author_id] = Author(author_id, author_name)
        self.next_author_id += 1
        print(f"Added '{author_name}' to the library.")


def display_menu():
    print('''
Welcome to our library, what can I help with:
1-> Show all books
2-> Add new book
3-> Show all authors
4-> Add new author
5-> Exit''')


def main():
    library = Library()
    display_menu()

    while True:
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            book_name = input("What is your new book? ").title()
            library.add_new_book(book_name)
        elif choice == "3":
            library.display_authors()
        elif choice == "4":
            author_name = input("Who is the new author? ").title()
            library.add_new_author(author_name)
        elif choice == "5":
            print("Exiting the program. Bye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

        option = input("Enter '1' to go Back to the main menu or '2' to Exit-> ")
        if option == '1':
            display_menu()
        elif option == '2':
            print("Exiting the program. Bye!")
            break


if __name__ == "__main__":
    main()
