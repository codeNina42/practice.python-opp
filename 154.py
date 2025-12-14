students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90
}
min_key=min(students,key=students.get)
print("Student with minimum marks:", min_key, "=", students[min_key])