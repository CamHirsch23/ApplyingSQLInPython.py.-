# Task1 

import mysql.connector

def add_member(id, name, age):
    try:
        conn = mysql.connector.connect(
            host='your_host',
            user='your_user',
            password='your_password',
            database='your_database'
        )
        cursor = conn.cursor()
        query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
        cursor.execute(query, (id, name, age))
        conn.commit()
        print("Member added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Task 2 

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        conn = mysql.connector.connect(
            host='your_host',
            user='your_user',
            password='your_password',
            database='your_database'
        )
        cursor = conn.cursor()
        query = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (member_id, date, duration_minutes, calories_burned))
        conn.commit()
        print("Workout session added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Task 3 

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

# Task 4 

def delete_workout_session(session_id):
    try:
        conn = mysql.connector.connect(
            host='your_host',
            user='your_user',
            password='your_password',
            database='your_database'
        )
        cursor = conn.cursor()
        delete_query = "DELETE FROM WorkoutSessions WHERE id = %s"
        cursor.execute(delete_query, (session_id,))
        if cursor.rowcount == 0:
            print("Session ID does not exist.")
        else:
            conn.commit()
            print("Workout session deleted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()
