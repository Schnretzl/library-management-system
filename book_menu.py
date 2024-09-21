from book import Book

def add_book(books):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    genre = input("Enter the genre of the book: ")
    publication_date = input("Enter the publication date of the book: ")
    books.append(Book(title, author, genre, publication_date))
    
def borrow_book(books, users):
    book_title = input("Enter the title of the book you want to borrow: ")
    user_id = input("Enter your user ID: ")
    for book in books:
        if book.title == book_title:
            for user in users:
                if user.id == user_id:
                    if book.borrow():
                        user.borrowed_books.append(book)
                        break
                    else:
                        print("Book is not available.")
                        break
                elif user == users[-1]:
                    print("User not found.")
                    break
            break
        
def return_book(books, users):
    pass

def book_index(books, title):
    #Return the index of the book, or None if the book is not found
    for index in range(len(books)):
        if books[index].title == title:
            return index
    return None