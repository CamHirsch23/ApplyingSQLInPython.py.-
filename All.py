import sqlite3

# Establish a connection to your database
connection = sqlite3.connect('gym_database.db')
cursor = connection.cursor()

def add_member(id, name, age):
    try:
        query = "INSERT INTO Members (id, name, age) VALUES (?, ?, ?)"
        cursor.execute(query, (id, name, age))
        connection.commit()
        print("Member added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        query = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (member_id, date, duration_minutes, calories_burned))
        connection.commit()
        print("Workout session added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def update_member_age(member_id, new_age):
    try:
        query = "UPDATE Members SET age = ? WHERE id = ?"
        cursor.execute(query, (new_age, member_id))
        connection.commit()
        print("Member age updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_workout_session(session_id):
    try:
        query = "DELETE FROM WorkoutSessions WHERE id = ?"
        cursor.execute(query, (session_id,))
        connection.commit()
        print("Workout session deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_members_in_age_range(start_age, end_age):
    try:
        query = "SELECT * FROM Members WHERE age BETWEEN ? AND ?"
        cursor.execute(query, (start_age, end_age))
        members = cursor.fetchall()
        return members
    except Exception as e:
        print(f"An error occurred: {e}")

# Don't forget to close the connection when you're done
connection.close()
