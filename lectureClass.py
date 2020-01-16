from studentClass import student
"""Constructor lecturer"""

class lecturer(student):

    def __init__(self, name, type, password, phone,student_serial_number):
        super().__init__( name, type, password, phone,student_serial_number)  # Use the super class constructor


