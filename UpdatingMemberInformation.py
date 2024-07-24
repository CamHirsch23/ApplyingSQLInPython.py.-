def update_member_age(member_id, new_age):
    try:
        conn = mysql.connector.connect(
            host='your_host',
            user='your_user',
            password='your_password',
            database='your_database'
        )
        cursor = conn.cursor()
        check_query = "SELECT * FROM Members WHERE id = %s"
        cursor.execute(check_query, (member_id,))
        if cursor.fetchone() is None:
            print("Member does not exist.")
            return
        update_query = "UPDATE Members SET age = %s WHERE id = %s"
        cursor.execute(update_query, (new_age, member_id))
        conn.commit()
        print("Member age updated successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()
