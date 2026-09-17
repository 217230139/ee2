##Import the necessary module
import json

## This function should load the library data from a JSON file and return it as a suitable Python data structure.
def load_library(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found:", filename)
        return None
    except json.JSONDecodeError:
        print("Invalid JSON in file:", filename)
        return None



## This function should save the library data to a JSON file.
## This function does not need to return anything, but it should ensure that the data is saved correctly to the specified file.
def save_library(data, filename):
     with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    



## This function should find a book by its title, author, or ID.
## If the book is found, it should return the book ID.
## If the book is not found, it should return None.
def find_book(books, search_text):
      target = search_text.strip().lower()
      for book_id in books:
        if book_id.lower() == target:
            return book_id
        book = books[book_id]
        if book["title"].lower() == target:
            return book_id
        if book["author"].lower() == target:
            return book_id
      return None



## This function should display the list of books in a user-friendly format.
## It should show the book ID, title, category, and availability status (available or on loan).
## If the book is available, it should display "AVAILABLE", and if it is on loan, it should display "ON LOAN".
## The function should not return anything, but it should print the information to the console.
## The heading for this display should be "BOOK CATALOGUE".
def display_books(books):
     print("\nBOOK CATALOGUE")
     print("-" * 60)
     for book_id in books:
        book = books[book_id]
        if book["available"]:
            status = "AVAILABLE"
        else:
            status = "ON LOAN"
        print(book_id + " | " + book["title"] + " | " + book["category"] + " | " + status)

## This function should display the list of current loans in a user-friendly format.
## It should show the book ID, title, and the name of the borrower.
## The heading for this display should be "CURRENT LOANS".
## The function should not return anything, but it should print the information to the console.
def display_loans(loans, books):
    print("\nCURRENT LOANS")
    print("-" * 60)
    for loan in loans:
        book_id = loan["book_id"]
        borrower = loan["borrower"]
        if book_id in books:
            title = books[book_id]["title"]
        else:
            title = "Unknown"
        print(book_id + " | " + title + " | Borrower: " + borrower)

## This function should calculate and return the library statistics
## The statsitics should include the total number of books, the number of available books, and the number of borrowed books.
## The function should return these three values in the order: total, available, borrowed. Use a suitable data structure to return these values, such as a tuple or a dictionary.

def library_statistics(books):
     total = len(books)
     available = 0
     for book in books.values():
        if book["available"]:
            available += 1
     borrowed = total - available
     return (total, available, borrowed)


## This function should display the library statistics in a user-friendly format.
## It should first load the library data from a JSON file, 
## Then calculate the statistics, and finally print the information to the console.
## The heading for this display should be "LIBRARY STATISTICS".
## It should print the total number of books, the number of available books, and the number of borrowed books.
## The function should not return anything, but it should print the information to the console.
def main():
    data = load_library("library.json")
    if data is None:
        return

    library = data["library"]
    categories = data["categories"]
    books = data["books"]
    loans = data["loans"]

    print("LIBRARY ADMINISTRATION")
    print("=" * 60)
    print("Library: " + library["name"])
    print("Branch: " + library["branch"])
    print("Year: " + str(library["year"]))
    print("Categories: " + ", ".join(categories))

    display_books(books)
    display_loans(loans, books)

    total, available, borrowed = library_statistics(books)

    print("\nSTATISTICS")
    print("-" * 60)
    print("Total books: " + str(total))
    print("Available: " + str(available))
    print("Borrowed: " + str(borrowed))

if __name__ == "__main__":
    main()

## Following is how the Admin interface should look like when the program is run. 
# The actual output may vary based on the library data and the current state of loans.

""" 
LIBRARY ADMINISTRATION
============================================================
Library: 
Branch: 
Year: 
Categories: 

BOOK CATALOGUE
------------------------------------------------------------
ID1 | Title1 | Category | Availability
ID2 | Title2 | Category | Availability
...
...
...
IDN | TitleN | Category | Availability


CURRENT LOANS
------------------------------------------------------------
ID1 | Title1 | Borrower: Borrower1
ID2 | Title2 | Borrower: Borrower2
...
...
...
IDN | TitleN | Borrower: BorrowerN

STATISTICS
------------------------------------------------------------
Total books: XX
Available: XX
Borrowed: XX
"""