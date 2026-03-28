import csv
from abc import ABC, abstractmethod
from datetime import date, timedelta
from enum import Enum
from typing import Optional

# ============================================================================
# CUSTOM EXCEPTIONS
# ============================================================================

class Condition(Enum): 
    NEW = "New"
    GOOD = "Good"
    USED = "Used"
    DAMAGED = "Damaged"


class GameItem:
    """
    Class for all game items.
    
    Attributes:
        title: Name of the Title
        publisher: Publisher of the game
        platform: Platform game is for
        msrp: Manufacturer price for game
        price: Price point of game
        condition: Current condition of game
        store_id: ID of store game is at
    """
    
    def __init__(self, title: str, publisher: str, platform: str, msrp: float, price: float, condition: Condition, store_id: int) -> None:
        """
        Initialize a new library item.
        
        Args:
            title: Name of the Title
            publisher: Publisher of the game
            platform: Platform game is for
            msrp: Manufacturer price for game
            price: Price point of game
            condition: Current condition of game
            store_id: ID of store game is at
        """

        self._title = title
        self._publisher = publisher
        self._platform = platform
        self._msrp = msrp
        self._price = price
        self._condition = condition
        self._store_id = store_id

    # Properties for encapsulation
    
    
    def get_title(self) -> str:
        """Get the item title."""
        return self._title
<<<<<<< HEAD

    def set_title(self, title):
=======
    def set_title(self, title:str):
>>>>>>> 9c05654d822e8ea056bf504942158b45d67a8653
        self._title = title
    
    def get_publisher(self) -> str:
        """Get the item publisher."""
        return self._publisher
<<<<<<< HEAD
    
    def set_publisher(self, publisher):
=======
    def set_publisher(self, publisher:str):
>>>>>>> 9c05654d822e8ea056bf504942158b45d67a8653
        self._publisher = publisher

    def get_platform(self) -> str:
        """Get the item platform."""
        return self._platform
<<<<<<< HEAD
    
    def set_platform(self, platform):
=======
    def set_platform(self, platform:str):
>>>>>>> 9c05654d822e8ea056bf504942158b45d67a8653
        self._platform = platform

    def get_msrp(self) -> float:
        """Get the item MSRP."""
        return self._msrp
<<<<<<< HEAD
    
    def set_msrp(self, msrp):
=======
    def set_msrp(self, msrp:float):
>>>>>>> 9c05654d822e8ea056bf504942158b45d67a8653
        self._msrp = msrp

    def get_price(self) -> str:
        """Get the item price."""
        return self._price
<<<<<<< HEAD
    
    def set_price(self, price):
=======
    def set_price(self, price:int):
>>>>>>> 9c05654d822e8ea056bf504942158b45d67a8653
        self._price = price

    def get_store_id(self) -> str:
        """Get the item store ID."""
        return self._store_id
<<<<<<< HEAD

    def set_store_id(self, store_id):
=======
    def set_store_id(self, store_id:int):
>>>>>>> 9c05654d822e8ea056bf504942158b45d67a8653
        self._store_id = store_id
    

class GameDatabaseManager:
    
    """
    The database manager for all games in all stores.
    
    Attributes:
        inventory: All available games in inventory
    """
    
    def __init__(self) -> None:
        """
        Initialize a new library.
        
        Args:
            name: The library's name
        """
        self._inventory = self.pullFromFile()

    
    @property
    def inventory(self) -> str:
        """Get the inventory."""
        return self._inventory
    
    def add_item(self, item: GameItem) -> None:
        """
        Add an item to the inventory.
        
        Args:
            item: The item to add
        """
        self._inventory.append(item)
    
    def remove_item(self, title:str, condition: Condition, store_id: int) -> GameItem:
        """
        Remove an item from the inventory.
        
        Args:
            item_id: ID of the item to remove
            
        Returns:
            The removed item
            
        Raises:
            ItemNotFoundError: If item doesn't exist
            ItemNotAvailableError: If item is checked out
        """
        not_found = True
        

        for i in self._inventory:
            if i.title == title and i.condition == condition and i.store_id == store_id:
                if not i._is_checked_out:
                    self._items.remove(i)
                    not_found = False
                    return i

        if not_found:
            raise ItemNotFoundError
    
    def pullFromFile(self):
        pass

    def addItemToFile(self, item: GameItem):
        pass