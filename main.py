from readwrite import readFromStudent
from TestData import Test
from QuestionsClass import Question
from Mangerclass import Manger
from lectureClass import lecturer
import datetime
from readwrite import FileToTest
from readwrite import FileTolecturer
from readwrite import FileToManger
from readwrite import FileToStudent
from readwrite import readFromlecturer
from readwrite import readFromTest
from readwrite import readFromManger
from studentClass import student
import cutt
import os
def writhtologfile(txt):
   with open ("logfile.txt",'a') as file:
        file.writelines(txt)
   """the list of data by type"""
questionslist=[]
testlist=[]
studentlist=[]
lecturerlist=[]
mangerlist=[]
"""read from file the data to list of obj"""
studentlist=FileToStudent(studentlist)
#questionslist=FileToStudent(questionslist)
testlist=FileToTest(testlist)
lecturerlist=FileTolecturer(lecturerlist)
mangerlist=FileToManger(mangerlist)

#cutt.PDFsplit(cutt.cutpdf(a.getexaminername()),[1,3])
"""enter username and password -chcing if the user in data base"""
def enter():
    print("enter your user name, password")
    userName=input()
    password=input()
    for i in studentlist:
        if userName==i.getName():
            if password==i.getpassword():
                return "s"
    for i in mangerlist:
        if userName==i.getName():
            if password==i.getpassword():
                return "m"
    for i in lecturerlist:
        if userName == i.getName():
            if password == i.getpassword():
                return "l"
    print("you dont have excess to the progrem")
    writhtologfile("error dosent have excess to the progrem " + str(datetime.datetime.now()))
    return
"""manger main:"""
def opManger():
    choice = 0
    while choice != 10:
        print("1=add test\n2=remove test\n3=update test")
        print("4=add lectucer\n5=remove lectucer\n6=update lectucer")
        print("7=add student\n8=remove student\n9=update student\n10=end\n")
        choice=int(input())
        if choice==1:
            name=input("exam name")
            f=open(name+'.pdf')
            datapath=os.path.realpath(f.name)
            NumQuestion = input("number of question")
            x=Test(input("date"),input("semester-a/b/c"),name,NumQuestion,'0',input("what is the test level? from 1-10,10-hardest"),datapath,input("enter Topic"))
            cut = cutt.cutpdf(x.getexaminername())
            cutt.new((cut))
            for i in range(1,int(NumQuestion)+1):
                p=x.getexaminername()+'cut'
                path = os.getcwd() + '\\'+p+str(i)+'.pdf'
                serialNum=(((int(len(testlist)))+1)*10)+int(i)
                y=Question(x.getDate(),x.getsemester(),x.getexaminername(), x.getnumberOfQuestions(),datapath,i,path,serialNum,input("enter level of question.from 1-10,10-hardest"),x.getTopic(),x.getstudentlevel(),x.getMangerlevel())
                x.setList(y)
            testlist.append(x)
            f.close()
        if choice==2:
            testname = input("enter test name you want to remove")
            date = input("enter test date you want to remove")
            for i in testlist:
                if testname == i.getexaminername():
                    if date == i.getDate():
                        i.remove()
        if choice==3:
            testname=input("enter test name you want to update")
            date=input("enter test date you want to update")
            for i in testlist:
                if testname == i.getexaminername():
                    if date == i.getDate():
                        print("1=update date\n2=update semester\n3=update name")
                        print("4=add question\n5=update manager level\n")
                        c=int(input())
                        if c==1:
                            i.setDate(input("enter date"))
                        if c==2:
                            i.setsemester(input("enter semester"))
                        if c==3:
                            i.setexaminername(input("enter name"))

                        if c==4:

                            i.setnumberOfQuestions((int(x.numberOfQuestions) +1))
                            p = i.getexaminername()
                            numberQuestion=input("enter the num of question")
                            path = os.getcwd() + '\\' + p+numberQuestion+ '.pdf'
                            y = Question(i.getDate(),i.getsemester(),i.getexaminername(), i.getnumberOfQuestions(),i.getTestpath(),(int(i.numberOfQuestions) +1), path, '0',input("enter level of question.from 1-10,10-hardest"), i.getTopic(), i.getstudentlevel(), i.getMangerlevel())
                            i.setList(y)
    

    
                        if c==5:
                            i.setMangerlevel(input("enter test level"))

        if choice==4:
            x = lecturer(input("name"), input("type"), input("password"), input("phone"),input("serial_number"))
            lecturerlist.append(x)
            writhtologfile("lecturer added "+str(datetime.datetime.now()))
        if choice==5:
            serialNumber = input("enter serial number of lecturer you want to remove")
            for i in lecturerlist:
                if serialNumber == i.getserial_number():
                    i.remove()
        if choice==6:
            serialNumber = input("enter serial number of lecturer you want to update")
            for i in lecturerlist:
                if serialNumber == i.getserial_number():
                    print("1=update name\n2=update type\n3=update password\n4=update phone\n")
                    c = int(input())
                    if c==1:
                        i.setName(input("enter name"))
                    if c==2:
                        i.setType(input("enter type"))
                    if c==3:
                        i.setpassword(input("enter password"))
                    if c==4:
                        i.setPhone(input("enter phone"))
        if choice==7:
            x = student(input("name"), input("type"), input("password"), input("phone"), input("serial number"))
            studentlist.append(x)
            writhtologfile("student added " + str(datetime.datetime.now()))
        if choice==8:
            serialNumber = input("enter serial number of student you want to remove")
            for i in studentlist:
                if serialNumber == i.getserial_number():
                    i.remove()
        if choice==9:
            serialNumber = input("enter serial number of student you want to update")
            for i in studentlist:
                if studentlist == i.getserial_number():
                    print("1=update name\n2=update type\n3=update password\n4=update phone\n")
                    c = int(input())
                    if c == 1:
                        i.setName(input("enter name"))
                    if c == 2:
                        i.setType(input("enter type"))
                    if c == 3:
                        i.setpassword(input("enter password"))
                    if c == 4:
                        i.setPhone(input("enter phone"))
    if choice==10:
        print("good bey")
        return
def opStudent_lecturer():
    category = 0
    flug=0
    while category != 9:
        print("search test with: 1-date\n,2-semester\n,3-examinername\n,4-studentlevel\n,5-Mangerlevel\n,6-levelQuestions\n,7-Topic\n,8-rate a tast\n9-end\n")
        category = int(input("enter category:"))
        if category == 1:
            x = input("enter data xx.xx.xxxx")
            for i in testlist:
                if x == i.getDate():
                    os.startfile(i.getexaminername() + '.pdf')
                    flug=1
            if flug!=1: print("There is no such test")
        if category == 2:
            x = input("enter semester(a/b/c)")
            for i in testlist:
                if x == i.getsemester():
                     os.startfile(i.getexaminername() + '.pdf')
                     flug = 1
            if flug != 1: print("There is no such test")
        if category == 3:
            x = input("enter test name:")
            for i in testlist:
                if x == i.getexaminername():
                      os.startfile(i.getexaminername() + '.pdf')
                      flug = 1
            if flug != 1: print("There is no such test")

        if category == 4:
            x = input("enter student level 1-10")
            for i in testlist:
                if x == i.getstudentlevel():
                      os.startfile(i.getexaminername() + '.pdf')
                      flug = 1
            if flug != 1: print("There is no such test")

        if category == 5:
            x = input("enter  manger level 1-10")
            x = input("enter Manger level")
            for i in testlist:
                if x == i.getMangerlevel():
                      os.startfile(i.getexaminername() + '.pdf')
                      flug = 1
            if flug != 1: print("There is no such test")

        if category == 6:
            x = input("enter Questions level")
            for i in testlist:
                if x == i.getlevelQuestions():
                      os.startfile(i.getexaminername() + '.pdf')
                      flug = 1
            if flug != 1: print("There is no such test")

        if category == 7:
            x = input("enter Topic")
            for i in testlist:
                x = input("enter Manger level")
                if x == i.getTopic():
                      os.startfile(i.getexaminername() + '.pdf')
                      flug = 1
            if flug != 1: print("There is no such test")

        if category == 8:
            if userType=='s':
                x = input("enter test name:")
                for i in testlist:
                    if x == i.getexaminername():
                        i.setstudentlevel(input("enter level of question.from 1-10,10-hardest"))
                        flug = 1
                if flug != 1: print("There is no such test")
    if category==13:
        print("Good-bey")
        return



"""Entering a user and checking if it is in the repository"""
userType=enter()
if userType=="m":
    opManger()#the main of manager
if userType=="s" or userType=="l":#the main of s and l
    opStudent_lecturer()


"""Update files with all current information"""
readFromStudent(studentlist)
readFromManger(mangerlist)
readFromlecturer(lecturerlist)
readFromTest(testlist)


















