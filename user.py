## This module contains the user interface for the library system. 
# It allows users to search for books, borrow books, and return books.

## Import the necessary functions from the admin module. 
# Replace "function_name1" with the actual function names you want to import.

from admin import (
    load_library,
    save_library,
    find_book
)



## Search books by category.
## This function should return book IDs that match the given category.
def books_in_category(
    books,
    category
):
    target = category.strip().lower()
    result = []
    for book_id in books:
        if books[book_id]["category"].lower() == target:
            result.append(book_id)
    return result
    


## Search books by full or partial title.
## This function should return book IDs that match the given title or part of the title.
def search_by_title(
    books,
    search_text
):
     target = search_text.strip().lower()
     result = []
     for book_id in books:
        if target in books[book_id]["title"].lower():
            result.append(book_id)
     return result



## Create logic to let users borrow books.
## The function should check if the book is available or on loan, or if the borrower name is provided.
## If the book is not found, then return "BOOK_NOT_FOUND"
## If the borrower name is empty, then return "EMPTY_NAME"
## If the book is not available, then return "NOT_AVAILABLE"
## If the book is successfully borrowed, then return "OK"
def borrow_book(
    books,
    loans,
    search_text,
    borrower
):
    name = borrower.strip()
    if name == "":
        return "EMPTY_NAME"
    
    book_id = find_book(books, search_text)
    if book_id is None:
        return "BOOK_NOT_FOUND"
    
    if books[book_id]["available"] is False:
        return "NOT_AVAILABLE"
    
    books[book_id]["available"] = False
    loans.append({"book_id": book_id, "borrower": name})
    return "OK"


    


## Create logic to let users return books.
## The function should check if the book is on loan, or if the borrower name is provided
## If the book is not found, then return "BOOK_NOT_FOUND"
## If the borrower name is empty, then return "EMPTY_NAME"
## If the book is not on loan, then return "NOT_ON_LOAN"
## If the book is successfully returned, then return "OK"

def return_book(
    books,
    loans,
    book_title,
    borrower
):
    name = borrower.strip()
    if name == "":
        return "EMPTY_NAME"
    
    book_id = find_book(books, book_title)
    if book_id is None:
        return "BOOK_NOT_FOUND"
    
    if books[book_id]["available"] is True:
        return "NOT_ON_LOAN"
   
    found_index = -1
    for i in range(len(loans)):
        if loans[i]["book_id"] == book_id:
            found_index = i
            break
    
    if found_index == -1:
        return "NOT_ON_LOAN"
    
    loans.pop(found_index)
    books[book_id]["available"] = True
    return "OK"

    



## The main function that runs the user interface for the library system.
## The function must first load the library data from a JSON file, then display a menu for the user to select options.
## The options include searching for books by title or category, borrowing a book, returning a book, and exiting the program.
## When the user selects an option, the corresponding function is called to perform the action.
## The program continues to display the menu until the user chooses to exit, at which point the library data is saved back to the JSON file.
## The main function should also handle invalid selections by displaying an error message and prompting the user to select again.
def main():
    data = load_library("library.json")
    if data is None:
        return

    books = data["books"]
    loans = data["loans"]

    print("LIBRARY USER SYSTEM")
    print("=" * 60)

    while True:
        print("\n1. Search by title")
        print("2. Search by category")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            text = input("Enter title to search: ")
            results = search_by_title(books, text)
            if len(results) == 0:
                print("No books found.")
            else:
                for book_id in results:
                    print(book_id + " | " + books[book_id]["title"])

        elif choice == "2":
            cat = input("Enter category to search: ")
            results = books_in_category(books, cat)
            if len(results) == 0:
                print("No books found.")
            else:
                for book_id in results:
                    print(book_id + " | " + books[book_id]["title"])

        elif choice == "3":
            text = input("Enter book ID or title: ")
            name = input("Enter borrower name: ")
            result = borrow_book(books, loans, text, name)
            print(result)

        elif choice == "4":
            text = input("Enter book ID or title: ")
            name = input("Enter borrower name: ")
            result = return_book(books, loans, text, name)
            print(result)

        elif choice == "5":
            save_library(data, "library.json")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()