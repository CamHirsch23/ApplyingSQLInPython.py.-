import mysql.connector

# Task 1: Add Member
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

# Task 2: Add Workout Session
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

# Task 3: Update Member Age
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

# Task 4: Delete Workout Session
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

# Task 5: Advanced Data Analysis
def analyze_workout_data():
    try:
        conn = mysql.connector.connect(
            host='your_host',
            user='your_user',
            password='your_password',
            database='your_database'
        )
        cursor = conn.cursor()
        query = """
        SELECT member_id, COUNT(*) AS session_count, SUM(duration_minutes) AS total_duration, SUM(calories_burned) AS total_calories
        FROM WorkoutSessions
        GROUP BY member_id
        """
        cursor.execute(query)
        results = cursor.fetchall()
        print("Workout Data Analysis:")
        for row in results:
            print(f"Member ID: {row[0]}, Sessions: {row[1]}, Total Duration: {row[2]} minutes, Total Calories Burned: {row[3]}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Main Menu
def main():
    print("Welcome to the Gym Management System!")
    print("Please choose an operation:")
    print("1. Add Member")
    print("2. Add Workout Session")
    print("3. Update Member Age")
    print("4. Delete Workout Session")
    print("5. Analyze Workout Data")
    print("6. Quit")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            id = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            age = input("Enter Member Age: ")
            add_member(id, name, age)
        elif choice == "2":
            member_id = input("Enter Member ID: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            duration_minutes = input("Enter Duration (minutes): ")
            calories_burned = input("Enter Calories Burned: ")
            add_workout_session(member_id, date, duration_minutes, calories_burned)
        elif choice == "3":
            member_id = input("Enter Member ID: ")
            new_age = input("Enter New Age: ")
            update_member_age(member_id, new_age)
        elif choice == "4":
            session_id = input("Enter Session ID: ")
            delete_workout_session(session_id)
        elif choice == "5":
            analyze_workout_data()
        elif choice == "6":
            print("Thank you for using the Gym Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
