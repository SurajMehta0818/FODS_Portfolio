import os

class User:
    def __init__(self, username, full_name, role):
        self.username = username
        self.full_name = full_name
        self.role = role


def authenticate(username, password,role):
    """
    Authenticate the user by checking the credentials in passwords.txt.
    Returns the role (admin or student) if valid, otherwise None.
    """
    try:
        with open("data/passwords.txt", "r") as file:  # Use forward slashes for compatibility
            for line in file:
                stored_username, stored_password, stored_role = line.strip().split(",")
                if username == stored_username and password == stored_password and stored_role==role:
                    return stored_role  # Return the role (admin or student)
    except FileNotFoundError:
        print("Error: passwords.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None


def get_user_details(username):
    """
    Fetch user details from users.txt based on the username.
    Returns a User object if found, otherwise None.
    """
    try:
        with open("data/users.txt", "r") as file:  # Use forward slashes for compatibility
            for line in file:
                stored_username, full_name, role = line.strip().split(",")
                if username == stored_username:
                    return User(username, full_name, role)
    except FileNotFoundError:
        print("Error: users.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None


def add_user(username, full_name, password, role):
    """
    Add a new user to users.txt and passwords.txt.
    """
    try:
        # Check if the username already exists
        with open("data/users.txt", "r") as file:
            for line in file:
                stored_username, _, _ = line.strip().split(",")
                if username == stored_username:
                    return False  # Username already exists

        # Add the user to users.txt
        with open("data/users.txt", "a") as file:
            file.write(f"{username},{full_name},{role}\n")

        # Add the user to passwords.txt
        with open("data/passwords.txt", "a") as file:
            file.write(f"{username},{password},{role}\n")

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def delete_user(username):
    """
    Delete a user from users.txt and passwords.txt.
    """
    try:
        # Remove the user from users.txt
        with open("data/users.txt", "r") as file:
            lines = file.readlines()
        with open("data/users.txt", "w") as file:
            for line in lines:
                if not line.startswith(username + ","):
                    file.write(line)

        # Remove the user from passwords.txt
        with open("data/passwords.txt", "r") as file:
            lines = file.readlines()
        with open("data/passwords.txt", "w") as file:
            for line in lines:
                if not line.startswith(username + ","):
                    file.write(line)

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def update_grades(username, new_grades_list):
    """
    Update or add grades data for a student in grades.txt
    Format: student1,85,90,78,88,92
    """
    try:
        filepath = "data/grades.txt"
        updated = False
        lines = []

        if os.path.exists(filepath):
            with open(filepath, "r") as file:
                lines = file.readlines()

        with open(filepath, "w") as file:
            for line in lines:
                if line.strip().startswith(username + ","):
                    file.write(username + "," + ",".join(map(str, new_grades_list)) + "\n")
                    updated = True
                else:
                    file.write(line)
            if not updated:
                file.write(username + "," + ",".join(map(str, new_grades_list)) + "\n")
        return True
    except Exception as e:
        print(f"Error updating grades: {e}")
        return False

def update_eca(username, new_eca_list):
    """
    Update or add ECA data for a student in eca.txt
    Format: student1,Football,Debate Club
    """
    try:
        filepath = "data/eca.txt"
        updated = False
        lines = []

        if os.path.exists(filepath):
            with open(filepath, "r") as file:
                lines = file.readlines()

        with open(filepath, "w") as file:
            for line in lines:
                if line.strip().startswith(username + ","):
                    file.write(username + "," + ",".join(new_eca_list) + "\n")
                    updated = True
                else:
                    file.write(line)
            if not updated:
                file.write(username + "," + ",".join(new_eca_list) + "\n")
        return True
    except Exception as e:
        print(f"Error updating ECA: {e}")
        return False


def get_student_grades(username):
    """
    Fetch grades for a student from grades.txt.
    Returns a dictionary of subjects and grades if found, otherwise None.
    """
    try:
        with open("data/grades.txt", "r") as file:
            for line in file:
                stored_username, *grades = line.strip().split(",")
                if username == stored_username:
                    return grades  # Return the grades as a list
    except FileNotFoundError:
        print("Error: grades.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None


def get_student_eca(username):
    """
    Fetch extracurricular activities for a student from eca.txt.
    Returns a list of activities if found, otherwise None.
    """
    try:
        with open("data/eca.txt", "r") as file:
            for line in file:
                stored_username, *activities = line.strip().split(",")
                if username == stored_username:
                    return activities  # Return the activities as a list
    except FileNotFoundError:
        print("Error: eca.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None


def update_student_profile(username, full_name):
    """
    Update the student's profile information in users.txt.
    """
    try:
        updated = False
        with open("data/users.txt", "r") as file:
            lines = file.readlines()
        with open("data/users.txt", "w") as file:
            for line in lines:
                stored_username, _, role = line.strip().split(",")
                if username == stored_username:
                    file.write(f"{username},{full_name},{role}\n")
                    updated = True
                else:
                    file.write(line)
        return updated
    except Exception as e:
        print(f"Error: {e}")
        return False


def read_grades_from_file(username):
    grades = []
    try:
        with open("data/grades.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if parts[0] == username:
                    grades = list(map(int, parts[1:]))
                    break
    except FileNotFoundError:
        print("grades.txt not found.")
    return grades

