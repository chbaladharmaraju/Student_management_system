import mysql.connector
from prettytable import PrettyTable

# Connect to MySQL
def connect_to_db():
        return mysql.connector.connect(host="localhost",user="root",
        password="Balu@777",
        database="baludb"
    )

# Add a new student
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    email = input("Enter student email: ")

    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "INSERT INTO students (name, age, grade, email) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, age, grade, email))
        conn.commit()
        print("Student added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        conn.close()

# View all students
def view_students():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        records = cursor.fetchall()

        table = PrettyTable(["ID", "Name", "Age", "Grade", "Email"])
        for record in records:
            table.add_row(record)
        print(table)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        conn.close()

# Update student record
def update_student():
    student_id = int(input("Enter student ID to update: "))
    column = input("Which field do you want to update (name/age/grade/email)? ")
    new_value = input(f"Enter new value for {column}: ")

    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = f"UPDATE students SET {column} = %s WHERE id = %s"
        cursor.execute(query, (new_value, student_id))
        conn.commit()
        print("Student record updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        conn.close()

# Delete student record
def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "DELETE FROM students WHERE id = %s"
        cursor.execute(query, (student_id,))
        conn.commit()
        print("Student record deleted successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        conn.close()

# Main menu
def main():
    while True:
        print("\n--- Student Records Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            update_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
