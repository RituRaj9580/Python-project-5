def main():
    # 1. Create a dictionary where student names are keys and marks are values
    student_marks = {
        "Alice": 85,
        "Bob": 78,
        "Charlie": 92,
        "David": 65,
        "Eve": 88
    }

    # 2. Ask the user to input a student's name
    # Using .strip() to remove accidental leading/trailing spaces
    name = input("Enter the student's name: ").strip()

    # 3. Retrieve and display the corresponding marks
    if name in student_marks:
        print(f"{name}'s marks: {student_marks[name]}")
    
    # 4. If the student's name is not found, display an appropriate message
    else:
        print("Student not found.")

if __name__ == "__main__":
    main()
