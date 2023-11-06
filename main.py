import mysql.connector

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Suyash@0411mysql",
    database="inventory"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Create the inventory table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        quantity INT NOT NULL,
        price DECIMAL(10, 2) NOT NULL
    )
''')


# Function to add a new product to the inventory
def add_product(name, quantity, price):
    query = "INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s)"
    data = (name, quantity, price)
    cursor.execute(query, data)
    db.commit()
    print("Product added to inventory.")


# Function to update the quantity of a product
def update_quantity(product_id, new_quantity):
    query = "UPDATE products SET quantity = %s WHERE id = %s"
    data = (new_quantity, product_id)
    cursor.execute(query, data)
    db.commit()
    print("Quantity updated.")


# Function to display the current inventory
def view_inventory():
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()

    if not results:
        print("Inventory is empty.")
    else:
        print("Inventory:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Quantity: {row[2]}, Price: {row[3]}")


# Main program loop
while True:
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. View Inventory")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        add_product(name, quantity, price)
    elif choice == '2':
        view_inventory()
        product_id = int(input("Enter the ID of the product to update: "))
        new_quantity = int(input("Enter the new quantity: "))
        update_quantity(product_id, new_quantity)
    elif choice == '3':
        view_inventory()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

# Close the cursor and database connection when done
cursor.close()
db.close()
