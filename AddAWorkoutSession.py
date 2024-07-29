def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        # SQL query to add a new workout session
        query = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (member_id, date, duration_minutes, calories_burned))
        connection.commit()
        print("Workout session added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
