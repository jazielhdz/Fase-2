class student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
        
    def __repr__(self):
        return f"{self.name}, {self.grade}, {self.age}"
    
student_objects = [
    student('John', 'A', 15),
    student('Jane', 'B', 12),
    student('Dave', 'B', 10)
]

print(student_objects)
estudiantes = sorted(student_objects, key = lambda student: student.age)
print(estudiantes)