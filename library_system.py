"""
Library Management System - Starter Code
CIS 226: Introduction to Object-Oriented Programming

Complete the implementation of all classes according to the assignment specifications.
Do not modify the class names, method names, or method signatures.

Author: Lee Kusowski
Date: 01/15/2025
"""

from abc import ABC, abstractmethod
from datetime import date, timedelta
from typing import Optional


# ============================================================================
# CUSTOM EXCEPTIONS
# ============================================================================

class LibraryException(Exception):
    """Base exception for library operations."""
    pass


class ItemNotAvailableError(LibraryException):
    """Raised when attempting to checkout an unavailable item."""
    pass


class ItemNotFoundError(LibraryException):
    """Raised when an item cannot be found."""
    pass


class PatronNotFoundError(LibraryException):
    """Raised when a patron cannot be found."""
    pass


class BorrowingLimitError(LibraryException):
    """Raised when patron cannot borrow more items."""
    print("Borrowing limit met. Please return items or pay fines to continue use.")


# ============================================================================
# PART 1: LIBRARY ITEMS
# ============================================================================

class LibraryItem(ABC):
    """
    Abstract base class for all library items.
    
    Attributes:
        item_id: Unique identifier for the item
        title: The title of the item
        is_checked_out: Whether the item is currently borrowed
        due_date: The date the item is due back (None if not checked out)
    """
    
    def __init__(self, item_id: str, title: str) -> None:
        """
        Initialize a new library item.
        
        Args:
            item_id: Unique identifier for the item
            title: The title of the item
        """

        self._item_id = item_id
        self._title = title

        self._is_checked_out = False
        self._due_date = None

    # Properties for encapsulation
    @property
    def item_id(self) -> str:
        """Get the item ID."""
        return self._item_id
    
    @property
    def title(self) -> str:
        """Get the item title."""
        return self._title
    
    @property
    def is_checked_out(self) -> bool:
        """Check if the item is currently checked out."""
        return self._is_checked_out

        
    
    @property
    def due_date(self) -> Optional[date]:
        """Get the due date for the item."""

        if self._due_date:
            return self._due_date
        else:
            return None


    
    @abstractmethod
    def get_checkout_duration(self) -> int:
        """
        Get the number of days this item can be borrowed.
        
        Returns:
            Number of days for checkout period
        """
        return self._get_checkout_duration
    
    @abstractmethod
    def calculate_late_fee(self, days_overdue: int) -> float:
        """
        Calculate the late fee for overdue items.
        
        Args:
            days_overdue: Number of days the item is overdue
            
        Returns:
            The late fee amount in dollars
        """
        return days_overdue * self.LATE_FEE_PER_DAY
    
    @abstractmethod
    def get_item_type(self) -> str:
        """
        Get a string describing the type of item.
        
        Returns:
            String name of the item type (e.g., "Book", "DVD")
        """
        return self.__class__.__name__

    
    def check_out(self, due_date: date) -> None:
        """
        Mark the item as checked out.
        
        Args:
            due_date: The date the item is due back
        """
        self._due_date = due_date
        self._is_checked_out = True
    
    def check_in(self) -> None:
        """Mark the item as returned."""
        self._due_date = None
        self._is_checked_out = False
    
    def __str__(self) -> str:
        """Return a formatted string representation of the item."""
        # TODO: Implement
        # Format: "[Type] Title (ID: item_id) - Status"
        # Status should be "Available" or "Due: YYYY-MM-DD"
        pass


class Book(LibraryItem):
    """
    A book in the library collection.
    
    Additional Attributes:
        author: The book's author
        isbn: The ISBN number
        page_count: Number of pages
    """
    
    CHECKOUT_DURATION = 21  # days
    LATE_FEE_PER_DAY = 0.25  # dollars
    
    def __init__(self, item_id: str, title: str, author: str, 
                 isbn: str, page_count: int) -> None:
        """
        Initialize a new book.
        
        Args:
            item_id: Unique identifier
            title: Book title
            author: Book author
            isbn: ISBN number
            page_count: Number of pages
        """
        super().__init__(item_id, title)

        self._author = author
        self._isbn = isbn
        self._page_count = page_count
    
    @property
    def author(self) -> str:
        """Get the book's author."""
        return self._author
    
    @property
    def isbn(self) -> str:
        """Get the book's ISBN."""
        return self._isbn
    
    @property
    def page_count(self) -> int:
        """Get the page count."""
        return self._page_count
    
    def get_checkout_duration(self) -> int:
        return self.CHECKOUT_DURATION
    
    def calculate_late_fee(self, days_overdue: int) -> float:
        return super().calculate_late_fee(days_overdue)
        
    
    def get_item_type(self) -> str:
        return self.__class__.__name__


class DVD(LibraryItem):
    """
    A DVD in the library collection.
    
    Additional Attributes:
        director: The DVD's director
        runtime_minutes: Length in minutes
        rating: Content rating (e.g., "PG", "R")
    """
    
    CHECKOUT_DURATION = 7  # days
    LATE_FEE_PER_DAY = 1.00  # dollars
    
    def __init__(self, item_id: str, title: str, director: str,
                 runtime_minutes: int, rating: str) -> None:
        """
        Initialize a new DVD.
        
        Args:
            item_id: Unique identifier
            title: DVD title
            director: Director's name
            runtime_minutes: Runtime in minutes
            rating: Content rating
        """
        super().__init__(item_id, title)

        self._director = director
        self._runtime_minutes = runtime_minutes
        self._rating = rating
    
    @property
    def director(self) -> str:
        """Get the DVD's director."""
        return self._director
    
    @property
    def runtime_minutes(self) -> int:
        """Get the runtime in minutes."""
        return self._runtime_minutes
    
    @property
    def rating(self) -> str:
        """Get the content rating."""
        return self._rating
    
    def get_checkout_duration(self) -> int:
        return self.CHECKOUT_DURATION

    
    def calculate_late_fee(self, days_overdue: int) -> float:
        return super().calculate_late_fee(days_overdue)
    
    def get_item_type(self) -> str:
        return self.__class__.__name__


class Magazine(LibraryItem):
    """
    A magazine in the library collection.
    
    Additional Attributes:
        issue_number: The issue number
        publication_date: When the issue was published
    """
    
    CHECKOUT_DURATION = 7  # days
    LATE_FEE_PER_DAY = 0.10  # dollars
    
    def __init__(self, item_id: str, title: str, 
                 issue_number: int, publication_date: date) -> None:
        """
        Initialize a new magazine.
        
        Args:
            item_id: Unique identifier
            title: Magazine title
            issue_number: Issue number
            publication_date: Publication date
        """

        super().__init__(item_id, title)

        self._issue_number = issue_number
        self._publication_date = publication_date
    
    @property
    def issue_number(self) -> int:
        """Get the issue number."""
        return self._issue_number
    
    @property
    def publication_date(self) -> date:
        """Get the publication date."""
        return self._publication_date
    
    def get_checkout_duration(self) -> int:
        return self.CHECKOUT_DURATION
    
    def calculate_late_fee(self, days_overdue: int) -> float:
        return super().calculate_late_fee(days_overdue)
    
    def get_item_type(self) -> str:
        return self.__class__.__name__


# ============================================================================
# PART 2: PATRON
# ============================================================================

class Patron:
    """
    A library patron who can borrow items.
    
    Attributes:
        patron_id: Unique identifier
        name: Patron's full name
        email: Contact email
        checked_out_items: List of currently borrowed items
        fine_balance: Outstanding fines owed
    """
    
    MAX_ITEMS = 5
    MAX_FINE_FOR_BORROWING = 10.00
    
    def __init__(self, patron_id: str, name: str, email: str) -> None:
        """
        Initialize a new patron.
        
        Args:
            patron_id: Unique identifier
            name: Patron's full name
            email: Contact email
        """
        self._patron_id = patron_id
        self._name = name
        self._email = email

        self._can_borrow = True
        self._checked_out_items = []
        self._fine_balance = 0
    
    @property
    def patron_id(self) -> str:
        """Get the patron ID."""
        return self._patron_id
    
    @property
    def name(self) -> str:
        """Get the patron's name."""
        return self._name
    
    @property
    def email(self) -> str:
        """Get the patron's email."""
        return self._email
    
    @property
    def fine_balance(self) -> float:
        """Get the current fine balance."""
        return self._fine_balance
    
    @property
    def checked_out_items(self) -> list:
        """Get list of checked out items (return a copy for encapsulation)."""
        copy = list(self._checked_out_items)

        return copy
    
    def borrow_item(self, item: LibraryItem) -> None:
        """
        Add an item to the patron's checked out items.
        
        Args:
            item: The library item to borrow
            
        Raises:
            BorrowingLimitError: If patron cannot borrow more items
        """
        if self.can_borrow() == True:
            self._checked_out_items.append(item)
        else:
            raise BorrowingLimitError
        
        return self._checked_out_items
    
    def return_item(self, item: LibraryItem) -> None:
        """
        Remove an item from the patron's checked out items.
        
        Args:
            item: The library item to return
        """
        if item in self._checked_out_items:
            self._checked_out_items.remove(item)
        return self._checked_out_items
    
    def add_fine(self, amount: float) -> None:
        """
        Add to the patron's fine balance.
        
        Args:
            amount: Amount to add to fines
        """
        self._fine_balance += amount
        return self._fine_balance
    
    def pay_fine(self, amount: float) -> None:
        """
        Pay towards the patron's fine balance.
        
        Args:
            amount: Amount to pay (balance cannot go negative)
        """

        self._fine_balance = abs(amount - self._fine_balance)
        return self._fine_balance
    
    def get_checked_out_count(self) -> int:
        """
        Get the number of items currently checked out.
        
        Returns:
            Number of checked out items
        """
        return self._checked_out_items.__len__()
    
    def can_borrow(self) -> bool:
        """
        Check if the patron can borrow more items.
        
        Returns:
            True if patron has < 5 items and fines < $10
        """
        if len(self._checked_out_items) < self.MAX_ITEMS and self._fine_balance < self.MAX_FINE_FOR_BORROWING:
            self._can_borrow = True
        else:
            self._can_borrow = False

        return self._can_borrow
    
    def __str__(self) -> str:
        """Return a string representation of the patron."""
        return self._patron_id


# ============================================================================
# PART 3: TRANSACTION
# ============================================================================

class Transaction:
    """
    A record of a checkout/return transaction.
    
    Uses composition to link Patron and LibraryItem objects.
    
    Attributes:
        transaction_id: Unique identifier
        patron: The patron who borrowed the item
        item: The borrowed item
        checkout_date: When the item was checked out
        due_date: When the item is due
        return_date: When the item was returned (None if not yet returned)
        late_fee: Any late fee charged
    """
    
    def __init__(self, transaction_id: str, patron: Patron,
                 item: LibraryItem, checkout_date: date, due_date: date) -> None:
        """
        Initialize a new transaction.
        
        Args:
            transaction_id: Unique identifier
            patron: The borrowing patron
            item: The borrowed item
            checkout_date: Date of checkout
            due_date: Due date for return
        """
        self._transaction_id = transaction_id
        self._patron = patron
        self._item = item
        self._checkout_date = checkout_date
        self._due_date = due_date

        self._is_complete = False
        self._return_date = None
        self._late_fee = 0
    
    @property
    def transaction_id(self) -> str:
        """Get the transaction ID."""
        return self._transaction_id
    
    @property
    def patron(self) -> Patron:
        """Get the patron."""
        return self._patron
    
    @property
    def item(self) -> LibraryItem:
        """Get the item."""
        return self._item
    
    @property
    def checkout_date(self) -> date:
        """Get the checkout date."""
        return self._checkout_date
    
    @property
    def due_date(self) -> date:
        """Get the due date."""
        return self._due_date
    
    @property
    def return_date(self) -> Optional[date]:
        """Get the return date."""
        return self._return_date
    
    @property
    def late_fee(self) -> float:
        """Get the late fee charged."""
        return self._late_fee
    
    def complete_return(self, return_date: date, late_fee: float) -> None:
        """
        Mark the transaction as complete.
        
        Args:
            return_date: The date the item was returned
            late_fee: The late fee charged (if any)
        """
        
        self._return_date = return_date

        self._late_fee = late_fee

        self._is_complete = True
    
    def is_complete(self) -> bool:
        """
        Check if the transaction is complete.
        
        Returns:
            True if the item has been returned
        """
        return self._is_complete
    
    def calculate_days_overdue(self, return_date: date) -> int:
        """
        Calculate how many days overdue the item is/was.
        
        Args:
            return_date: The date to check against
            
        Returns:
            Number of days overdue (0 if not overdue)
        """
        diff = (return_date - self.due_date).days

        if diff > 0:
            return diff
        else:
            return 0

    def __str__(self) -> str:
        """Return a string representation of the transaction."""
        # TODO: Implement
        pass


# ============================================================================
# PART 4: LIBRARY
# ============================================================================

class Library:
    """
    The main library system that manages items, patrons, and transactions.
    
    Attributes:
        name: The library's name
        items: Dictionary mapping item_id to LibraryItem
        patrons: Dictionary mapping patron_id to Patron
        transactions: List of all transactions
    """
    
    def __init__(self, name: str) -> None:
        """
        Initialize a new library.
        
        Args:
            name: The library's name
        """
        self._name = name
        self._items = []
        self._patrons = []
        self._transactions = []
    
    @property
    def name(self) -> str:
        """Get the library name."""
        return self._name
    
    def add_item(self, item: LibraryItem) -> None:
        """
        Add an item to the library collection.
        
        Args:
            item: The item to add
        """
        self._items.append(item)
    
    def remove_item(self, item_id: str) -> LibraryItem:
        """
        Remove an item from the library.
        
        Args:
            item_id: ID of the item to remove
            
        Returns:
            The removed item
            
        Raises:
            ItemNotFoundError: If item doesn't exist
            ItemNotAvailableError: If item is checked out
        """
        not_found = True
        not_available = False

        for i in self._items:
            if i.item_id == item_id:
                if not i._is_checked_out:
                    self._items.remove(i)
                    not_found = False
                    return i
                else:
                    not_available = True


        if not_available:
            raise ItemNotAvailableError
        if not_found:
            raise ItemNotFoundError

    
    def register_patron(self, patron: Patron) -> None:
        """
        Register a new patron with the library.
        
        Args:
            patron: The patron to register
        """
        self._patrons.append(patron)

    
    def find_item(self, item_id: str) -> Optional[LibraryItem]:
        """
        Find an item by ID.
        
        Args:
            item_id: The item ID to search for
            
        Returns:
            The item if found, None otherwise
        """
        for i in self._items:
            if i.item_id == item_id:
                return i
    
    def find_patron(self, patron_id: str) -> Optional[Patron]:
        """
        Find a patron by ID.
        
        Args:
            patron_id: The patron ID to search for
            
        Returns:
            The patron if found, None otherwise
        """
        for p in self._patrons:
            if p.patron_id == patron_id:
                return p
    
    def checkout_item(self, patron_id: str, item_id: str, 
                      checkout_date: date) -> Transaction:
        """
        Process a checkout transaction.
        
        Args:
            patron_id: ID of the patron checking out
            item_id: ID of the item to checkout
            checkout_date: The date of checkout
            
        Returns:
            The created Transaction object
            
        Raises:
            PatronNotFoundError: If patron doesn't exist
            ItemNotFoundError: If item doesn't exist
            ItemNotAvailableError: If item is already checked out
            BorrowingLimitError: If patron cannot borrow more items
        """

        p = self.find_patron(patron_id)
        if p == None:
            raise PatronNotFoundError    
            
        if p.can_borrow():

            i = self.find_item(item_id)
            if i == None:
                raise ItemNotFoundError
            
            if not i._is_checked_out:

#
                transaction_id = patron_id + str(checkout_date.fromtimestamp)

                due_date = checkout_date + timedelta(int(i.get_checkout_duration()))

                p.borrow_item(i)
                i.check_out(due_date)

                return Transaction(transaction_id, p, i, checkout_date, due_date)
#

            else:
                raise ItemNotAvailableError
        else:
            raise BorrowingLimitError

    def return_item(self, patron_id: str, item_id: str,
                    return_date: date) -> Transaction:
        """
        Process a return transaction.
        
        Args:
            patron_id: ID of the returning patron
            item_id: ID of the item being returned
            return_date: The date of return
            
        Returns:
            The completed Transaction object
            
        Raises:
            PatronNotFoundError: If patron doesn't exist
            ItemNotFoundError: If item doesn't exist
        """
        # Errors
        p = self.find_patron(patron_id)
        if p == None:
            raise PatronNotFoundError  
        
        i = self.find_item(item_id)
        if i == None:
            raise ItemNotFoundError
        
        # Create Transaction ID (patron_id and timestamp)
        transaction_id = patron_id + str(return_date.fromtimestamp)

        txn = Transaction(transaction_id, p, i, return_date, i._due_date)

        # Calc Late Fee
        late_fee = i.calculate_late_fee(txn.calculate_days_overdue(return_date))

        # Add Late Fee to Patron Balance
        p.add_fine(late_fee)

        # Return Item Methods
        p.return_item(i)
        i.check_in()

        txn.complete_return(return_date, late_fee)
        self._transactions.append(txn)

        return txn
#       
    
    def get_available_items(self) -> list:
        """
        Get all items that are not checked out.
        
        Returns:
            List of available LibraryItem objects
        """

        copy = []

        for i in self._items:
            if not i.is_checked_out:
                copy.append(i)
        return copy
    
    def get_overdue_items(self, current_date: date) -> list:
        """
        Get all items that are overdue.
        
        Args:
            current_date: The date to check against
            
        Returns:
            List of overdue LibraryItem objects
        """

        copy = []

        for i in self._items:
            if i.due_date != None:
                if i.due_date < current_date:
                    copy.append(i)

        return copy
    
    def get_patron_transactions(self, patron_id: str) -> list:
        """
        Get all transactions for a specific patron.
        
        Args:
            patron_id: The patron's ID
            
        Returns:
            List of Transaction objects for this patron
        """
        # TODO: Implement
        pass
    
    def __str__(self) -> str:
        """Return a string representation of the library."""
        # TODO: Implement
        pass


# ============================================================================
# MAIN (for testing)
# ============================================================================

if __name__ == "__main__":
    # You can add your own test code here
    print("Library Management System")
