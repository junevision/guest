from pymysql import connect,OperationalError

# Database connection details
db_config = {
    'host': '127.0.0.1',  # Replace with your MySQL server host
    'user': 'root',      # Replace with your MySQL username
    'password': '123456',  # Replace with your MySQL password
    'database': 'guest'   # Replace with your database name
}

try:
    # Establishing the connection
    connection = connect(**db_config)
    print("Connected to the MySQL database successfully!")

    cursor = connection.cursor()

    # Create a guest table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS guests (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    )
    """)
    print("Guests table ensured.")

    # Insert a guest record
    insert_query = "INSERT INTO guests (name, email) VALUES (%s, %s)"
    guest_data = ("John Doe", "john.doe@example.com")
    cursor.execute(insert_query, guest_data)
    connection.commit()
    print(f"Inserted guest with ID: {cursor.lastrowid}")

    # Query the created guest
    select_query = "SELECT * FROM guests WHERE id = %s"
    cursor.execute(select_query, (cursor.lastrowid,))
    result = cursor.fetchone()
    print("Queried guest:", result)

except OperationalError as err:
    print(f"Error: {err}")
finally:
    # Closing the connection
    if 'connection' in locals() and connection.open:
        connection.close()
        print("MySQL connection closed.")