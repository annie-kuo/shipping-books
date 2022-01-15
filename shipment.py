# Annie Kuo

# Shipping Books
# This program aids in preparing books for shipment from a book depot
# by letting a user choose from a menu of options and executing the option chosen.

# Define functions

def calculate_isbn_checksum_by_digits(d1, d2, d3, d4, d5, d6, d7, d8, d9):
    """ (int, int, int, int, int, int, int, int, int) -> str
    The function takes in 9 one-digit integers, and calculates and returns the checksum as a string.
    >>> calculate_isbn_checksum_by_digits(8, 7, 1, 1, 0, 7, 5, 5, 9)
    '7'
    >>> calculate_isbn_checksum_by_digits(1, 2, 3, 4, 5, 6, 7, 8, 9)
    'X'
    >>> calculate_isbn_checksum_by_digits(3, 5, 1, 3, 0, 1, 6, 2, 1)
    '2'
    """
    # calculate the checksum using the formula provided
    checksum_by_digits= (d1 + 2*d2 + 3*d3 + 4*d4 +5*d5 + 6*d6 + 7*d7 + 8*d8 + 9*d9) % 11
    if checksum_by_digits == 10:
        checksum_by_digits = "X"
    return str(checksum_by_digits)


def calculate_isbn_checksum(isbn):
    """ (int) -> str
    The function takes a 9-digit integer, and calculates and returns the checksum as a string.
    >>> calculate_isbn_checksum(871107559)
    '7'
    >>> calculate_isbn_checksum(123456789)
    'X'
    >>> calculate_isbn_checksum(351301621)
    '2'
    """
    # isolate each digit from the IBSN
    int1 = isbn//(10**8)
    int2 = isbn//(10**7)%10
    int3 = isbn//(10**6)%10
    int4 = isbn//(10**5)%10
    int5 = isbn//(10**4)%10
    int6 = isbn//(10**3)%10
    int7 = isbn//(10**2)%10
    int8 = isbn//(10**1)%10
    int9 = isbn%10
    
    # calculate the checksum
    checksum_from_isbn = calculate_isbn_checksum_by_digits(int1, int2, int3, int4, int5, int6, int7, int8, int9)
    return checksum_from_isbn


def is_isbn(isbn, checksum):
    """ (int, str) -> bool
    The function returns True if the checksum from the ISBN is equal to the checksum on the book, False otherwise.
    >>> is_isbn(871107559, "4")
    False
    >>> is_isbn(123456789, "10")
    False
    >>> is_isbn(123456789, "X")
    True
    >>> is_isbn(351301621, "2")
    True
    """
    # calculate expected checksum
    checksum_from_isbn= calculate_isbn_checksum(isbn)
    # check if the checksum on the book matches the expected checksum
    checksum_is_correct= (checksum_from_isbn == checksum)
    return checksum_is_correct


def book_fits_in_box(box_w, box_d, box_h, book_w, book_d, book_h):
    """ (int, int, int, int, int, int) -> bool
    The function returns True if the book of dimensions book_w x book_d x book_h
    can fit in the box of dimensions box_w x box_d, box_h, False otherwise.
    >>> book_fits_in_box(15, 2, 2, 2, 15, 2)
    True
    >>> book_fits_in_box(20, 12, 10, 2, 34, 10)
    False
    >>> book_fits_in_box(34, 35, 20, 34, 35, 20)
    True
    """
    # check if the book can fit against the three different sides of the box
    # with the book vertically and horizontally
    
    if (book_h <= box_h) and (book_w <= box_w) and (book_d <= box_d):
        return True
    elif (book_h <= box_w) and (book_w <= box_h) and (book_d <= box_d):
        return True
    elif (book_h <= box_d) and (book_w <= box_h) and (book_d <= box_w):
        return True
    elif (book_h <= box_h) and (book_w <= box_d) and (book_d <= box_w):
        return True
    elif (book_h <= box_w) and (book_w <= box_d) and (book_d <= box_h):
        return True
    elif (book_h <= box_d) and (book_w <= box_w) and (book_d <= box_h):
        return True
    else:
        return False
    

def get_smallest_box_for_book(book_w, book_d, book_h):
    """ (int, int, int) -> str
    The function takes as input the dimensions of the book, and returns the smallest box in which the book can fit.
    The function returns an empty string if it fits in neither of the boxes.
    >>> get_smallest_box_for_book(12, 12, 2)
    'medium'
    >>> get_smallest_box_for_book(20, 20, 4)
    'large'
    >>> get_smallest_box_for_book(30, 24, 5)
    ''
    """
    if book_fits_in_box(10,10,2, book_w, book_d, book_h):
        return "small"
    elif book_fits_in_box(15,15,3, book_w, book_d, book_h):
        return "medium"
    elif book_fits_in_box(20,20,4, book_w, book_d, book_h):
        return "large"
    else:
        return ""


def get_num_books_for_box(box_w, box_d, box_h, book_w, book_d, book_h):
    """ (int, int, int, int, int, int) -> int
    The function returns the maximum number of copies of a book that can fit into a box of given integer dimensions
    >>> get_num_books_for_box(10, 5, 5, 5, 5, 2)
    4
    >>> get_num_books_for_box(15, 20, 12, 10, 2, 10)
    10
    >>> get_num_books_for_box(10, 10, 10, 10, 15, 10)
    0
    """
    num_books= (box_w// book_w) * (box_d// book_d) * (box_h// book_h)
    return num_books
    
    
def main():
    """ () -> NoneType
    The function greets the user and displays the menu of options.
    The function then executes the option as chosen by the user's input and displays a result message.
    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN 
    2) Check box/book size 
    3) Get smallest box size for book 
    4) Get num equally-sized books per box
    Enter choice (1-4): 1
    Enter ISBN: 100101011
    Enter checksum: 1
    ISBN is not valid (checksum did not match).
    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN 
    2) Check box/book size 
    3) Get smallest box size for book 
    4) Get num equally-sized books per box
    Enter choice (1-4): 3
    Enter the box's width in cm: 30
    Enter the box's depth in cm: 40
    Enter the box's height in cm: 10
    Package does not fit in any of the boxes.
    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN 
    2) Check box/book size 
    3) Get smallest box size for book 
    4) Get num equally-sized books per box
    Enter choice (1-4): 2
    Enter the box's width in cm: 55
    Enter the box's depth in cm: 45
    Enter the box's height in cm: 35
    Enter the book's width in cm: 35
    Enter the book's depth in cm: 45
    Enter the book's height in cm: 55
    Package fits in box.
    """
    # greet the user and display the menu of options
    print("Welcome to the shipment calculation system.")
    print("1) Check ISBN \n2) Check box/book size \n3) Get smallest box size for book \n4) Get num equally-sized books per box")
    
    # take input from the user
    choice= input("Enter choice (1-4): ")
    
    # call the appropriate function(s) and print out the appropriate result message
    if choice == "1":
        isbn_to_verify = int(input("Enter ISBN: "))
        checksum_to_verify = int(input("Enter checksum: "))
        isbn_validity=  is_isbn(isbn_to_verify, checksum_to_verify)
        # display message
        if isbn_validity:
            print("ISBN is valid (checksum match).")
        else:
            print("ISBN is not valid (checksum did not match).")
    
    elif choice == "2":
        box_W= int(input("Enter the box's width in cm: "))
        box_D= int(input("Enter the box's depth in cm: "))
        box_H= int(input("Enter the box's height in cm: "))
        book_W= int(input("Enter the book's width in cm: "))
        book_D= int(input("Enter the book's depth in cm: "))
        book_H= int(input("Enter the book's height in cm: "))
        book_fit = book_fits_in_box(box_W, box_D, box_H, book_W, book_D, book_H)
        # display message
        if book_fit:
            print("Package fits in box.")
        else:
            print("Package does not fit in box")
    
    elif choice == "3":
        book_W= int(input("Enter the box's width in cm: "))
        book_D= int(input("Enter the box's depth in cm: "))
        book_H= int(input("Enter the box's height in cm: "))
        size= get_smallest_box_for_book(book_W, book_D, book_H)
        # display message
        if size == "":
            print("Package does not fit in any of the boxes.")
        else:
            print("The smallest box for your book is of the following size: " + size + ".")
        
    else:
        box_W= int(input("Enter the box's width in cm: "))
        box_D= int(input("Enter the box's depth in cm: "))
        box_H= int(input("Enter the box's height in cm: "))
        book_W= int(input("Enter the book's width in cm: "))
        book_D= int(input("Enter the book's depth in cm: "))
        book_H= int(input("Enter the book's height in cm: "))       
        num_of_books= get_num_books_for_box(box_W, box_D, box_H, book_W, book_D, book_H)
        # display message
        print(num_of_books, "copies of the book will fit in the box.")
    