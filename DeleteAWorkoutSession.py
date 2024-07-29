def delete_workout_session(session_id):
    try:
        # SQL query to delete a session
        query = "DELETE FROM WorkoutSessions WHERE id = ?"
        cursor.execute(query, (session_id,))
        connection.commit()
        print("Workout session deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
