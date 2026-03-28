from game_inventory_manager import GameDatabaseManager, GameItem

game = GameItem("Test Game", "Test Publish", "Test Platform", 1.00, 1.00, "New", 1000)


choice = 0


print("1 - Database Files")
print("2 - Add Item")
print("3 - Remove Game")

choice = int(input())

match choice:

    case 1:
        data = GameDatabaseManager()

        #data.pullFromFile()
    case 2:
        data = GameDatabaseManager()
        testItem = GameItem("Kirby Air Riders", "Nintendo", "Gamecube", 49.99, 39.99, "Good", 3)
        data.addItemToInventory(testItem)
        data.addItemToInventory(game)

        print(data.inventory)
    case 3:
        data = GameDatabaseManager()
        data.remove_item("Kirby Air Riders", "Good", 3)

        print(data.inventory)
