from TestData import Test
"""Constructor question"""

class Question(Test):
    def __init__(self, date, semester, examinername, numberOfQuestions,Testpath, QuestionNumber,Questionspath,Serialnumber,levelQuestions,Topic, studentlevel, Mangerlevel):
        super().__init__(date, semester, examinername, numberOfQuestions,Testpath,Topic, studentlevel, Mangerlevel)
        self.QuestionNumber = QuestionNumber
        self.levelQuestions = levelQuestions
        self.Questionspath=Questionspath
        self.Serialnumber=Serialnumber

    def setQuestionNumber(self, QuestionNumber):
        self.QuestionNumber = QuestionNumber

    def getQuestionNumber(self):
        return self.QuestionNumber

    def setlevelQuestions(self, levelQuestions):
        self.levelQuestions = levelQuestions

    def getlevelQuestions(self):
        return self.levelQuestions

    def setQuestionspath(self, Questionspath):
        self.Questionspath = Questionspath

    def getQuestionspath(self):
        return self.Questionspath

    def setSerialnumber(self, Serialnumber):
        self.Serialnumber = Serialnumber

    def getSerialnumber(self):
        return self.Serialnumber

