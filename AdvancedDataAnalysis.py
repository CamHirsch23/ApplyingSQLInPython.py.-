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
