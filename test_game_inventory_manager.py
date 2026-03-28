# Team 181
# Game Inventor Manager

import unittest

from game_inventory_manager import GameItem, GameDatabaseManager

class TestGameItem(unittest.TestCase):
    """Tests for GameItem Object"""

    def setUp(self):
        """Create a sample game object"""
        self.game = GameItem("Test Game", "Test Publish", "Test Platform", "Test MSRP", "Test Price", NEW, 1000)

    def test_game_init(self):
        self.assertEqual(self.game.get_name, "Test Game")
        self.assertEqual(self.game.get_publisher, "Test Publish")
        self.assertEqual(self.game.get_platform, "Test Platform")
        self.assertEqual(self.game.get_msrp, "Test MSRP")
        self.assertEqual(self.game.get_price, "Test Price")
        self.assertEqual(self.game.get_condition, "New")
        self.assertEqual(self.game.get_store_id, 1000)

    def test_game_setters(self):
        self.game.set_name("New Name")
        self.game.set_publisher("New Publish")
        self.game.set_platform("New Platform")
        self.game.set_msrp("New MSRP")
        self.game.set_price("New Price")
        self.game.set_condition(USED)
        self.game.set_store_id(2000)

        self.assertEqual(self.game.get_name, "New Game")
        self.assertEqual(self.game.get_publisher, "New Publish")
        self.assertEqual(self.game.get_platform, "New Platform")
        self.assertEqual(self.game.get_msrp, "New MSRP")
        self.assertEqual(self.game.get_price, "New Price")
        self.assertEqual(self.game.get_condition, "Used")
        self.assertEqual(self.game.get_store_id, 2000)

class TestGameDatabaseManager(unittest.TestCase):
    """Tests for the Game Database Manager"""
    
    def setUp(self):
        """Setup a Game Database"""
        self.data = GameDatabaseManager()
        self.game = GameItem("Test Game", "Test Publish", "Test Platform", "Test MSRP", "Test Price", NEW, 1000)

    def test_game_database_manager_init(self):
        """Test Database Initialization"""
        self.assertEqual(len(self.data.inventory), 0)

    def test_database_create(self):
        """Database should add items to inventory"""
        self.data.add_item(self.game)