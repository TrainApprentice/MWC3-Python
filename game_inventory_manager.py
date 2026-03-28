import csv
from abc import ABC, abstractmethod
from datetime import date, timedelta
from enum import Enum
from typing import Optional

# ============================================================================
# CUSTOM EXCEPTIONS
# ============================================================================

class FileNotFoundError(Exception):
    """Raised when a readable csv file can't be found."""
    pass

class FileReadError(Exception):
    """Raised when a csv file fails to parse."""
    pass

class ItemNotFoundError(Exception):
    """Raised when an item cannot be found."""
    pass


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
    
    def __init__(self, title: str, publisher: str, platform: str, msrp: float, price: float, condition: str, store_id: int) -> None:
        """
        Initialize a new game item.
        
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
    def set_title(self, title:str):
        self._title = title
    
    def get_publisher(self) -> str:
        """Get the item publisher."""
        return self._publisher
    def set_publisher(self, publisher:str):
        self._publisher = publisher

    def get_platform(self) -> str:
        """Get the item platform."""
        return self._platform
    def set_platform(self, platform:str):
        self._platform = platform

    def get_msrp(self) -> float:
        """Get the item MSRP."""
        return self._msrp
    def set_msrp(self, msrp:float):
        self._msrp = msrp

    def get_price(self) -> str:
        """Get the item price."""
        return self._price
    def set_price(self, price:int):
        self._price = price

    def get_condition(self) -> str:
        """Get the item condition."""
        return self._condition
    def set_condition(self, condition:str):
        self._condition = condition

    def get_store_id(self) -> str:
        """Get the item store ID."""
        return self._store_id
    def set_store_id(self, store_id:int):
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
        self.pullFromFile()

    
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
        
    
    def remove_item(self, title:str, condition: str, store_id: int) -> GameItem:
        """
        Remove an item from the inventory.
        
        Args:
            title: Title of item to remove
            condition: Condition of item to remove
            store_id: Store ID of item to remove
            
        Returns:
            The removed item
             
        Raises:
            ItemNotFoundError: If item doesn't exist
        """
        not_found = True
        

        for i in self._inventory:
            if i.get_title() == title and i.get_condition() == condition and i.get_store_id() == store_id:
                self._inventory.remove(i)
                not_found = False
                return i

        if not_found:
            raise ItemNotFoundError
    
    def find_item(self, title:str, condition: str, store_id: int) -> GameItem:
        
        foundItem:GameItem = None
        for i in self._inventory:
            if i.get_title() == title and i.get_condition() == condition and i.get_store_id() == store_id:
                foundItem = i
        
        if foundItem is not None:
            return i
        else:
            raise ItemNotFoundError

    
    def pullFromFile(self):
        self._inventory = []
        with open("database/game_database_data.csv", newline="") as csvfile:
            fileReader = csv.DictReader(csvfile)
            for row in fileReader:
                setItem = GameItem(str(row['Title']), str(row['Publisher']), str(row['Platform']), float(row['MSRP']), float(row['PurchasePrice']), str(row['Condition']), int(row['StoreID']))
                self.add_item(setItem)
                

    def addItemToInventory(self, item: GameItem):
        with open("database/game_database_data.csv", 'w', newline="") as csvfile:
            fieldNames = ['Title', 'Publisher', 'Platform', 'MSRP', 'PurchasePrice', 'Condition', 'StoreID']
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
            writer.writeheader()
            for i in self.inventory:
                prevItem = {
                    'Title': i.get_title(),
                    'Publisher': i.get_publisher(),
                    'Platform': i.get_platform(),
                    'MSRP': i.get_msrp(),
                    'PurchasePrice': i.get_price(),
                    'Condition': i.get_condition(),
                    'StoreID': i.get_store_id()
                }
                writer.writerow(prevItem)
            newItem = {
                'Title': item.get_title(),
                'Publisher': item.get_publisher(),
                'Platform': item.get_platform(),
                'MSRP': item.get_msrp(),
                'PurchasePrice': item.get_price(),
                'Condition': item.get_condition(),
                'StoreID': item.get_store_id()
            }
            writer.writerow(newItem)
        self.add_item(item)
    
    def rewriteInventoryFile(self):
        with open("database/game_database_data.csv", 'w', newline="") as csvfile:
            fieldNames = ['Title', 'Publisher', 'Platform', 'MSRP', 'PurchasePrice', 'Condition', 'StoreID']
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
            writer.writeheader()
            for i in self.inventory:
                prevItem = {
                    'Title': i.get_title(),
                    'Publisher': i.get_publisher(),
                    'Platform': i.get_platform(),
                    'MSRP': i.get_msrp(),
                    'PurchasePrice': i.get_price(),
                    'Condition': i.get_condition(),
                    'StoreID': i.get_store_id()
                }
                writer.writerow(prevItem)
