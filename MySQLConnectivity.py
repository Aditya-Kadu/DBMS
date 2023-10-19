import mysql.connector

# Function to connect to MySQL database
def connect_to_mysql():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        return db_connection
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None

# Function to add a record
def add_record(connection, cursor):
    name = input("Enter name: ")
    age = input("Enter age: ")
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name, age))
    connection.commit()
    print("Record added successfully!")

# Function to delete a record
def delete_record(connection, cursor):
    id_to_delete = input("Enter the ID to delete: ")
    cursor.execute("DELETE FROM students WHERE id = %s", (id_to_delete,))
    connection.commit()
    print("Record deleted successfully!")

# Function to edit a record
def edit_record(connection, cursor):
    id_to_edit = input("Enter the ID to edit: ")
    new_name = input("Enter new name: ")
    new_age = input("Enter new age: ")
    cursor.execute("UPDATE students SET name = %s, age = %s WHERE id = %s", (new_name, new_age, id_to_edit))
    connection.commit()
    print("Record edited successfully!")

# Function to list all records
def list_records(cursor):
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    for record in records:
        print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}")

# Main menu
def main_menu():
    connection = connect_to_mysql()
    if connection is None:
        return

    cursor = connection.cursor(buffered=True)
    
    while True:
        print("\nMenu:")
        print("1. Add Record")
        print("2. Delete Record")
        print("3. Edit Record")
        print("4. List Records")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_record(connection, cursor)
        elif choice == "2":
            delete_record(connection, cursor)
        elif choice == "3":
            edit_record(connection, cursor)
        elif choice == "4":
            list_records(cursor)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            connection.close()
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
