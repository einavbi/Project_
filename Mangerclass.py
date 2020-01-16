






from studentClass import student
from TestData import Test
from QuestionsClass import Question
from lectureClass import lecturer
"""Constructor manager"""

class Manger(lecturer):
    def __init__(self, name, type, password, phone,student_serial_number):
        super().__init__( name, type, password, phone,student_serial_number)
        #self.serial_number=serial_number

    def newLecturer(self,name, type, password, phone, lecturerType):
        """Creates and returns new lecturer"""
        return lecturer(name, type, password, phone, lecturerType)
    def newTest(self,date, semester, examinername, numberOfQuestions, studentlevel, Mangerlevel):
        """Creates and returns new Test"""
        return Test(date, semester, examinername, numberOfQuestions, studentlevel, Mangerlevel)
