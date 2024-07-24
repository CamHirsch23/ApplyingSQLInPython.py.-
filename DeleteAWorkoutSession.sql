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
