class student:
    def __init__(self, name, type, password, phone, student_serial_number):
        """Student Constructor"""
        self.name = name
        self.password = password
        self.phone = phone
        self.type = type
        self.student_serial_number = student_serial_number

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setpassword(self, password):
        self.password = password

    def getpassword(self):
        return self.password

    def setPhone(self, phone):
        self.phone = phone

    def getPhone(self):
        return self.phone

    def setType(self, Type):
        self.type = Type

    def getType(self):
        return self.type


    def setserial_number(self, student_serial_number):
        self.student_serial_number = student_serial_number


    def getserial_number(self):
        return self.student_serial_number
