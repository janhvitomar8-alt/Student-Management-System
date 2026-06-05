def save_students():
    file = open("students.txt", "w")
    for student in students:
        file.write(
    student["name"] + "," +
    str(student["roll"]) + "," +
    student["branch"] + "\n"
       )
    file.close()
    print("Students saved!")
students = []
def add_student():
    name=input("Enter name: ")
    try:
       roll=int(input("Enter roll no: "))
    except:
        print("Invalid roll no!")
    branch=input("Enter branch: ")
    student={ 
       "name": name,
       "roll": roll,
       "branch": branch
   }
    students.append(student)
    print("Student added successfully")
def view_students():
    for student in students:
        print(
            "Name:", student["name"],
    "| Roll:", student["roll"],
    "| Branch:", student["branch"] 
        )
def search_student():
    name = input("Enter student name: ")

    for student in students:
        if student["name"] == name:
            print(
                "Name:", student["name"],
                "| Roll:", student["roll"],
                "| Branch:", student["branch"]
            )
            return

    print("Student not found")

def delete_student():
    name = input("Enter student name: ")

    for student in students:
        if student["name"] == name:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found")
        
def load_students():
    file = open("students.txt",  "r")
    for line in file:
        data = line.strip().split(",")
        student={
        "name" : data[0],
        "roll" : int(data[1]),
        "branch" : data[2]
    }
        students.append(student)
    file.close()

load_students()
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Save Students")
    print("6. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        save_students()
    elif choice == "6":    
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")