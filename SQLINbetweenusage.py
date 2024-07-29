def get_members_in_age_range(start_age, end_age):
    try:
        # SQL query using BETWEEN
        query = "SELECT * FROM Members WHERE age BETWEEN ? AND ?"
        cursor.execute(query, (start_age, end_age))
        members = cursor.fetchall()
        return members
    except Exception as e:
        print(f"An error occurred: {e}")
