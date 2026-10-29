
import csv

# Student records
students = [
    {"RollNo": 1, "Name": "Priya", "Department": "CSE", "Mark": 95},
    {"RollNo": 2, "Name": "Anu", "Department": "IT", "Mark": 90},
    {"RollNo": 3, "Name": "Ravi", "Department": "ECE", "Mark": 88}
]
#Tuple example:fixed courses
course=("Python",4)
print("Course Tuple:",course)

# Write text file
with open("students.txt", "w") as file:
    for student in students:
        file.write(str(student) + "\n")

print("Student records written to text file successfully!")

# Write CSV file
with open("students.csv", "w", newline="") as file:
    fields = ["RollNo", "Name", "Department", "Mark"]

    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)

print("Student records written to CSV file successfully!")

# Read CSV file
print("\n--- Records from CSV ---")

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(
            row["RollNo"],
            row["Name"],
            row["Department"],
            row["Mark"]
        )

