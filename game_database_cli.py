from game_inventory_manager import GameItem, GameDatabaseManager, Condition

choice = 0

# Banner
print("~~~ Welcome ~~~")
print("Game Inventory Manager")
print()

# Main Menu
print("Main Menu")
print("~~~~~~~~~~~~")
print("1. Store Inventory Check")
print("2. Item Search")
print("3. Item Manager")

choice = int(input())

match choice:

    case 1:
        print("Store Inventory Check")
        print("~~~~~~~~~~~~")
        print("Please, enter the StoreID to view current inventory.")

    case 2:
        print("Item Search")
        print("~~~~~~~~~~~~")
        print("Please, enter the item's exact name, condition, and StoreID. (Condition can be: (New, Good, Used, Damaged))")

    case 3:
        pick = 0

        # Item Manager
        print("Item Manager")
        print("~~~~~~~~~~~~")
        print("1. New Item")
        print("2. View Item")
        print("3. Edit Item")
        print("4. Remove Item")

        pick = int(input())

        match pick:
            case 1:
                print("New Item")
                print("~~~~~~~~~~~~")
                print("Title:")
                title = input()
                print("Publisher:")
                publisher = input()
                print("Platform:")
                platform = input()
                print("MSRP:")
                msrp = input()
                print("Price:")
                price = input()
                print("Condition:")
                condition = input()
                print("StoreID:")
                store_id = input()

                y = "n"
                print("Add Item: {condition} {title} to Store {store_id}?")
                y = input().lower()

                if y == "y":
                    GameDatabaseManager.add_item(title, publisher, platform, msrp, price, condition, store_id)

            case 2:
                print("View Item")
                print("~~~~~~~~~~~~")
                print("Title:")
                title = input()
                print("Condition:")
                condition = input()
                print("StoreID:")
                store_id = input()

                y = "n"
                print("View Item: {condition} {title} at Store {store_id}?")
                y = input().lower()

                if y == "y":
                    item = GameDatabaseManager.find_item(title, condition, store_id)
                    print(f"{item.get_title}, {item.get_publisher}, {item.get_platform}, {item.get_msrp}, {item.get_price}, {item.get_condition}, {item.get_store_id}")

            case 3:
                print("Edit Item")
                print("~~~~~~~~~~~~")
                print("Title:")
                title = input()
                print("Condition:")
                condition = input()
                print("StoreID:")
                store_id = input()

                y = "n"
                print("View Item: {condition} {title} at Store {store_id}?")
                y = input().lower()

                if y == "y":
                    item = GameDatabaseManager.find_item(title, condition, store_id)
                    print(f"{item.get_title}, {item.get_publisher}, {item.get_platform}, {item.get_msrp}, {item.get_price}, {item.get_condition}, {item.get_store_id}")

                quit = False

                var = 0

                print("Edit Item - {item.get_title}")
                print("~~~~~~~~~~~~")
                print("1. Title")
                print("2. Publisher")
                print("3. Platform")
                print("4. MSRP")
                print("5. Price")
                print("6. StoreID")
                
                var = int(input())

                match var:

                    case 1:
                        new = str(input())
                        item.set_
                    case 1:
                    case 1:
                    case 1:
                    case 1:
                    case 1:

            case 4:
                print("Remove Item")
                print("~~~~~~~~~~~~")

