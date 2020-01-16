class Test:
    """Constructor Test"""
    def __init__(self, date, semester, examinername,numberOfQuestions, studentlevel, Mangerlevel,Testpath,Topic):
        self.date = date
        self.semester = semester
        self.examinername = examinername
        self.numberOfQuestions = numberOfQuestions
        self.studentlevel = studentlevel
        self.Mangerlevel = Mangerlevel
        self.Testpath=Testpath
        self.lst=[]
        self.Topic=Topic

    def setTopic(self, Topic):
        self.Topic=Topic
    def getTopic(self):
        return self.Topic
    def setRemoveIndexFList(self, i):
        self.lst[i].remove()

    def setList(self, question):
        self.lst.append(question)
    def getList(self):
        return self.lst
    def setDate(self, date):
        self.date = date

    def getDate(self):
        return self.date

    def setsemester(self, semester):
        self.semester = semester

    def getsemester(self):
        return self.semester

    def setexaminername(self, examinername):
        self.examinername = examinername


    def getexaminername(self):
        return self.examinername

    def setnumberOfQuestions(self, numberOfQuestions):
        self.numberOfQuestions = numberOfQuestions

    def getnumberOfQuestions(self):
        return self.numberOfQuestions

    def setstudentlevel(self, studentlevel):
        self.studentlevel = studentlevel

    def getstudentlevel(self):
        return self.studentlevel

    def setsMangerlevel(self, Mangerlevel):
        self.Mangerlevel = Mangerlevel

    def getMangerlevel(self):
        return self.Mangerlevel


    def setTestpath(self, Testpath):
        self.Testpath = Testpath

    def getTestpath(self):
        return self.Testpath


