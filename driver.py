from game_inventory_manager import GameDatabaseManager, GameItem, Condition

game = GameItem("Test Game", "Test Publish", "Test Platform", "Test MSRP", "Test Price", Condition.NEW, 1000)


choice = 0


print("1 - Database Files")

match choice:

    case 1:
        data = GameDatabaseManager()
        self.data.add_item(game)

        data.pullFromFile()