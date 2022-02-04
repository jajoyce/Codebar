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




# Test Code from README:

# workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

# workshop.add_participant(jane)
# workshop.add_participant(lena)
# workshop.add_participant(vicky)
# workshop.add_participant(nicole)
# workshop.print_details()
