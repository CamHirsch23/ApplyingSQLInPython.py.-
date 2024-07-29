def update_member_age(member_id, new_age):
    try:
        # SQL query to update age
        query = "UPDATE Members SET age = ? WHERE id = ?"
        cursor.execute(query, (new_age, member_id))
        connection.commit()
        print("Member age updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
