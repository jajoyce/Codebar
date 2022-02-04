class Member:
    def __init__(self, full_name):
        self.full_name = full_name
    
    def introduce(self):
        print(f"Hi, my name is {self.full_name}!")

class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason

class Instructor(Member):
    def __init__(self, full_name, bio, skills=None):
        super().__init__(full_name)
        self.bio = bio
        if skills is None:
            skills = []
        self.skills = skills
    
    def add_skill(self, skill):
        self.skills.append(skill)

class Workshop:
    def __init__(self, date, subject, instructors=None, students=None):
        self.date = date
        self.subject = subject
        if instructors is None:
            instructors = []
        self.instructors = instructors
        if students is None:
            students = []
        self.students = students
    
    def add_participant(self, member):
        if type(member).__name__ == "Instructor":
            self.instructors.append(member)
        elif type(member).__name__ == "Student":
            self.students.append(member)
        else:
            print("Participant is not a valid Member.")
    
    def print_details(self):
        self.__print_workshop()
        self.__print_students()
        self.__print_instructors()
    
    def __print_workshop(self):
        print(f"Workshop - {self.date} - {self.subject}")

    def __print_students(self):
        print("\nStudents")
        for i, student in enumerate(self.students, 1):
            print(f"{i}. {student.full_name} - {student.reason}")

    def __print_instructors(self):
        print("\nInstructors")
        for i, instructor in enumerate(self.instructors, 1):
            skills_string = ""
            for j, skill in enumerate(instructor.skills, 1):
                if j == len(instructor.skills):
                    skills_string += skill
                else:
                    skills_string += skill + ", "
            print(f"{i}. {instructor.full_name} - {skills_string}\n   {instructor.bio}")


# Test Code from README:

workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()
