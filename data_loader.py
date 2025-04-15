def load_grades():
    try:
        grades_data = {}
        with open("data/grades.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                student = parts[0]
                grades = list(map(int, parts[1:]))  # Convert grade strings to integers
                grades_data[student] = grades
        return grades_data
    except FileNotFoundError:
        print("grades.txt not found")
        return {}
    except Exception as e:
        print("Error loading grades:", e)
        return {}
        

def load_eca_data():
    try:
        eca_data = {}
        with open("data/eca.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                student = parts[0]
                activities = parts[1:]  # Keep as strings
                eca_data[student] = activities
        return eca_data
    except FileNotFoundError:
        print("eca.txt not found")
        return {}
    except Exception as e:
        print("Error loading ECA data:", e)
        return {}

