import pymongo


client = pymongo.MongoClient("mongodb://10.10.13.76:27017")
database = client["te31234db"]
collection = database["items"]


def add_item():
    name = input("Enter the item name: ")
    description = input("Enter the item description: ")
    item = {"name": name, "description": description}
    collection.insert_one(item)
    print("Item added successfully!")


def edit_item():
    name = input("Enter the item name you want to edit: ")
    item = collection.find_one({"name": name})
    if item:
        new_name = input("Enter the new name: ")
        new_description = input("Enter the new description: ")
        collection.update_one({"_id": item["_id"]}, {"$set": {"name": new_name, "description": new_description}})
        print("Item edited successfully!")
    else:
        print("Item not found.")


def delete_item():
    name = input("Enter the item name you want to delete: ")
    item = collection.find_one({"name": name})
    if item:
        collection.delete_one({"_id": item["_id"]})
        print("Item deleted successfully!")
    else:
        print("Item not found.")

def list_items():
    items = collection.find()
    print("All Items:")
    for item in items:
        print(f"Name: {item['name']}, Description: {item['description']}")


while True:
    print("\nMenu:")
    print("1. Add Item")
    print("2. Edit Item")
    print("3. Delete Item")
    print("4. List Items")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        edit_item()
    elif choice == "3":
        delete_item()
    elif choice == "4":
        list_items()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
