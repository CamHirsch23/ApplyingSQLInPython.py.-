def add_member(id, name, age):
    try:
        # SQL query to add a new member
        query = "INSERT INTO Members (id, name, age) VALUES (?, ?, ?)"
        cursor.execute(query, (id, name, age))
        connection.commit()
        print("Member added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
