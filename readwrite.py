from lectureClass import lecturer
from studentClass import student
from TestData import Test
from QuestionsClass import Question
from Mangerclass import Manger


def readFromStudent(studentlist):
    open('fileStudent.txt', 'w').close()
    fileStudent = open("fileStudent.txt", 'w')
    for i in studentlist:
        fileStudent.write(str(i.getName()))
        fileStudent.write("\n")
        fileStudent.write(str(i.getType()))
        fileStudent.write("\n")
        fileStudent.write(str(i.getpassword()))
        fileStudent.write("\n")
        fileStudent.write(str(i.getPhone()))
        fileStudent.write("\n")
        fileStudent.write(str(i.getserial_number()))
        fileStudent.write("\n")
    fileStudent.close()


def readFromlecturer(lrctuerlist):
    open('fileLectucer.txt', 'w').close()
    filelecturer = open("fileLectucer.txt", 'w')
    for obj in lrctuerlist:
        filelecturer.write(str(obj.getName()))
        filelecturer.write("\n")
        filelecturer.write(str(obj.getType()))
        filelecturer.write("\n")
        filelecturer.write(str(obj.getpassword()))
        filelecturer.write("\n")
        filelecturer.write(str(obj.getPhone()))
        filelecturer.write("\n")
        filelecturer.write(str(obj.getserial_number()))
        filelecturer.write("\n")
    filelecturer.close()


def readFromManger(mangerlist):
    open('fileManger.txt', 'w').close()
    fileManger = open("fileManger.txt", 'w')
    for obj in mangerlist:
        fileManger.write(str(obj.getName()))
        fileManger.write("\n")
        fileManger.write(str(obj.getType()))
        fileManger.write("\n")
        fileManger.write(str(obj.getpassword()))
        fileManger.write("\n")
        fileManger.write(str(obj.getPhone()))
        fileManger.write("\n")
        fileManger.write(str(obj.getserial_number()))
        fileManger.write("\n")
    fileManger.close()


def readFromTest(testlist):
    open('fileTest.txt', 'w').close()
    fileTest = open("fileTest.txt", 'w')
    for obj in testlist:
        fileTest.write(str(obj.getDate()))
        fileTest.write("\n")
        fileTest.write(str(obj.getsemester()))
        fileTest.write("\n")
        fileTest.write(str(obj.getexaminername()))
        fileTest.write("\n")
        fileTest.write(str(obj.getnumberOfQuestions()))
        fileTest.write("\n")
        fileTest.write(str(obj.getstudentlevel()))
        fileTest.write("\n")
        fileTest.write(str(obj.getMangerlevel()))
        fileTest.write("\n")
        fileTest.write(str(obj.getTestpath()))
        fileTest.write("\n")
        templist = obj.getList()
        for Questions in templist:
            fileTest.write(str(Questions.getDate()))
            fileTest.write("\n")
            fileTest.write(str(Questions.getsemester()))
            fileTest.write("\n")
            fileTest.write(str(Questions.getexaminername()))
            fileTest.write("\n")
            fileTest.write(str(Questions.getnumberOfQuestions()))
            fileTest.write("\n")
            fileTest.write(str(obj.getTestpath()))
            fileTest.write("\n")
            fileTest.write(str(Questions.getQuestionNumber()))
            fileTest.write("\n")
            fileTest.write(str(Questions.getQuestionspath()))
            fileTest.write("\n")
            fileTest.write(str(Questions.getSerialnumber()))
            fileTest.write("\n")
            fileTest.write(str(Questions.getlevelQuestions()))
            fileTest.write("\n")
            fileTest.write(str(obj.getTopic()))
            fileTest.write("\n")
            fileTest.write(str(obj.getstudentlevel()))
            fileTest.write("\n")
            fileTest.write(str(obj.getMangerlevel()))
            fileTest.write("\n")
        fileTest.write(str(obj.getTopic()))
        fileTest.write("\n")

    fileTest.close()


def FileToStudent(list):
    filename = open("fileStudent.txt", 'r')
    while True:
        name = filename.readline()
        name=name[:len(name)-1:]
        if name=="":
            break
        type = filename.readline()
        type=type[:len(type)-1:]
        password = filename.readline()
        password=password[:len(password)-1:]
        phone = filename.readline()
        phone=phone[:len(phone)-1:]
        slr = filename.readline()
        slr=slr[:len(slr)-1:]
        obj = student(name, type, password, phone, slr)
        list.append(obj)
    filename.close()
    return list
def FileToManger(list):
    filename = open("fileManger.txt", 'r')
    while True:
        name = filename.readline()
        name = name[:len(name) - 1:]
        if name == "":
            break
        type = filename.readline()
        type = type[:len(type) - 1:]
        password = filename.readline()
        password = password[:len(password) - 1:]
        phone = filename.readline()
        phone = phone[:len(phone) - 1:]
        slr = filename.readline()
        slr = slr[:len(slr) - 1:]
        obj=Manger(name,type,password,phone,slr)
        list.append(obj)
    filename.close()
    return list
def FileTolecturer(list):
    filename=open("fileLectucer.txt", 'r')
    while True:
        name = filename.readline()
        name = name[:len(name) - 1:]
        if name == "":
            break
        type = filename.readline()
        type = type[:len(type) - 1:]
        password = filename.readline()
        password = password[:len(password) - 1:]
        phone = filename.readline()
        phone = phone[:len(phone) - 1:]
        slr = filename.readline()
        slr = slr[:len(slr) - 1:]
        obj=lecturer(name,type,password,phone,slr)
        list.append(obj)
    filename.close()
    return list

def FileToTest(testlist):
    filename = open("fileTest.txt", 'r')
    while True:
        date = filename.readline()
        date=date[:len(date)-1:]
        if date == "":
            break
        semester = filename.readline()
        semester = semester[:len(semester) - 1:]
        examinername = filename.readline()
        examinername = examinername[:len(examinername) - 1:]
        numberOfQuestions = filename.readline()
        numberOfQuestions = numberOfQuestions[:len(numberOfQuestions) - 1:]
        studentlevel = filename.readline()
        studentlevel=studentlevel[:len(studentlevel) - 1:]
        Mangerlevel = filename.readline()
        Mangerlevel=Mangerlevel[:len(Mangerlevel) - 1:]
        Testpath = filename.readline()
        Testpath=Testpath[:len(Testpath) - 1:]
        qlist=[]
        for i in range(0,int(numberOfQuestions)):
            date = filename.readline()
            date = date[:len(date) - 1:]
            semester = filename.readline()
            semester = semester[:len(semester) - 1:]
            examinername = filename.readline()
            examinername = examinername[:len(examinername) - 1:]
            numberOfQuestions = filename.readline()
            numberOfQuestions = numberOfQuestions[:len(numberOfQuestions) - 1:]
            testpath=filename.readline()
            testpath = testpath[:len(testpath) - 1:]
            QuestionsNumber=filename.readline()
            QuestionsNumber=QuestionsNumber[:len(QuestionsNumber) - 1:]
            Questionspath=filename.readline()
            Questionspath = Questionspath[:len(Questionspath) - 1:]
            srl=filename.readline()
            srl = srl[:len(srl) - 1:]
            levelQuestions=filename.readline()
            levelQuestions = levelQuestions[:len(levelQuestions) - 1:]
            topic=filename.readline()
            topic=topic[:len(topic) - 1:]
            studentlevel=filename.readline()
            studentlevel = studentlevel[:len(studentlevel) - 1:]
            Mangerlevel = filename.readline()
            Mangerlevel = Mangerlevel[:len(Mangerlevel) - 1:]
            objquestion = Question(date, semester, examinername, numberOfQuestions, testpath, QuestionsNumber, Questionspath, srl, levelQuestions, topic, studentlevel, Mangerlevel)
            qlist.append(objquestion)
        Topic = filename.readline()
        Topic = Topic[:len(Topic) - 1:]


        obj=Test(date, semester,examinername, numberOfQuestions, studentlevel,
                 Mangerlevel,Testpath,Topic)
        testlist.append(obj)
        for i in qlist:
            obj.setList(i)
        qlist =[]


    filename.close()
    return testlist





