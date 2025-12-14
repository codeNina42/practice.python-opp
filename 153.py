students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90
}

max_key=max(students,key=students.get)
print("Student with maximum marks:", max_key, "=", students[max_key])