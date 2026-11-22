class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    def get_details(self):
        return f"Name: {self.name}, ID: {self.student_id}"
class GraduateStudent(Student):
    def __init__(self, thesis_topic, name, student_id):
        super().__init__(name, student_id)
        self.thesis_topic = thesis_topic
    def get_details(self):
        return f"{super().get_details()}, Thesis: {self.thesis_topic}"
S1 = Student("Asad", "23CABSA349")
G1 = GraduateStudent("AI/ML", "Asad", "23CABSA349")
print(S1.get_details())
print(G1.get_details())