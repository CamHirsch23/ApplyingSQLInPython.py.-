# Question 1 
# Task 1 

# Gym Database Management with Python (Without SQL)

# Data structures to store members and workout sessions
members = []
workout_sessions = []

# Task 1: Add a Member
def add_member(member_id, name, age):
    """Add a new member to the Members list."""
    for member in members:
        if member['id'] == member_id:
            print(f"Failed to add member: Duplicate ID {member_id}")
            return
    new_member = {'id': member_id, 'name': name, 'age': age}
    members.append(new_member)
    print("Member added successfully")

# Task 2: Add a Workout Session
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    """Add a new workout session to the WorkoutSessions list."""
    if any(member['id'] == member_id for member in members):
        new_session = {
            'member_id': member_id,
            'date': date,
            'duration_minutes': duration_minutes,
            'calories_burned': calories_burned
        }
        workout_sessions.append(new_session)
        print("Workout session added successfully")
    else:
        print(f"Failed to add workout session: Invalid member ID {member_id}")

# Task 3: Updating Member Information
def update_member_age(member_id, new_age):
    """Update the age of a member."""
    for member in members:
        if member['id'] == member_id:
            member['age'] = new_age
            print("Member age updated successfully")
            return
    print(f"Member not found: ID {member_id}")

# Task 4: Delete a Workout Session
def delete_workout_session(session_index):
    """Delete a workout session based on its index."""
    if 0 <= session_index < len(workout_sessions):
        del workout_sessions[session_index]
        print("Workout session deleted successfully")
    else:
        print(f"Workout session not found: Index {session_index}")

# Example usage:
add_member('001', 'John Doe', 30)
add_workout_session('001', '2024-07-24', 60, 500)
update_member_age('001', 31)
delete_workout_session(0)  # Assuming the first session is to be deleted

# Question 2 
# Task 1 

# Assuming we have a list of members loaded into Python
members = [
    {'id': '001', 'name': 'John Doe', 'age': 28},
    {'id': '002', 'name': 'Jane Smith', 'age': 24},
    {'id': '003', 'name': 'Emily Johnson', 'age': 35},
    # ... more members
]

def get_members_in_age_range(start_age, end_age):
    """Retrieve the details of members whose ages fall between start_age and end_age."""
    # Filter members using list comprehension
    members_in_range = [member for member in members if start_age <= member['age'] <= end_age]
    
    for member in members_in_range:
        print(f"Member ID: {member['id']}, Name: {member['name']}, Age: {member['age']}")

# Example usage:
get_members_in_age_range(25, 30)
