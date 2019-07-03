import sys
import datetime

class Person:
    def __init__(self, lastName, firstName, status, phoneNum, email):
        self.lastName = lastName
        self.firstName = firstName
        self.status = status
        self.phoneNum = phoneNum
        self.email = email

class Service:
    def __init__(self, date, time, peopleList):
        self.date = date
        self.time = time
        self.peopleList = peopleList

# create lists for info
allPeople = list()
allPeopleString = ""
allServices = list()
thisWeekAttendance = list()

def writeToAllPeople(Person):
    file = open("allpeople.txt", "w")
    info = Person.lastName + "," + Person .firstName + "," + Person.status + "," + Person.phoneNum + "," + Person.email + "\n"
    file.write(info)
    file.close()

def writeToAttendance(Service):
    file = open("attendance.txt", "a+")
    weekInfo = Service.date + "," + Service.time + "," + Service.peopleList + "\n"
    file.write(weekInfo)
    file.close()

def readFromAllPeople():
    file = open("allpeople.txt", "a+")
    lines = file.read().splitlines()
    for line in lines:
        info = line.split(",")
        newPerson = Person(info[0], info[1], info[2], info[3], info[4])
        allPeople.append(newPerson)
    file.close()

def readFromAttendance():
    file = open("attendance.txt", "a+")
    lines = file.read().splitlines()
    for line in lines:
        attendance = list()
        info = line.split(",")
        date = info[0]
        time = info[1]
        numPeople = len(info) - 2
        i = 2
        while (i < numPeople):
            attendance.append(info[i])
            ++i
        newService = Service(date, time, ','.join(str(x) for x in attendance))
        allServices.append(newService)
    file.close()

def getDate():
    while True:
        isToday = input("Are you entering information for today?\n   If yes, press y.\n   If no, press n  ")
        if ((isToday == "y") | (isToday == "n")):
            break
    if (isToday == "y"):
        dateObj =  datetime.datetime.now()
        dateStr = dateObj.strftime("%Y/%m/%d")
        return dateStr
    else:
        while True:
            isValidDate = True
            date = input("Date? (mm/dd/yyyy)  ")
            if (len(date) == 10) & (date[2:3] == "/") & (date[5:6] == "/"):
                dateParts = date.split("/")
                try:
                    dateFormatted = datetime.date(int(dateParts[2]), int(dateParts[0]), int(dateParts[1]))
                except:
                    isValidDate = False
                if (isValidDate):
                    break
            print("Sorry, but that was not a valid option. Please enter again.\n")
        dateForStr = dateFormatted.strftime("%Y/%m/%d")
        return dateForStr

def getTime():
    while True:
<<<<<<< HEAD
        serviceCheck = input("Morning or Evening?\n   If morning, press m.\n   If evening, press e.\n").lower()
        if ((serviceCheck == "m") | (serviceCheck == "e")):
            break
        print("Sorry, but that was not a valid option. Please enter again.\n")
    if (serviceCheck == "m"):
        service = "morning"
    elif (serviceCheck == "e"):
        service = "evening"
    return service
=======
        time = input("Morning or Evening?\n   If morning, press m.\n   If evening, press e  ").lower()
        if (time == "m"):
            time = "morning"
            break
        elif (time == "e"):
            time = "evening"
            break
        else:
            print("Sorry, but that was not a valid option. Please enter again.\n")
    return time
>>>>>>> 5436b53340c633b30eaf7b1bef79b0ce824fb781

def askToAddOrDelete():
    while True:
        while True:
            plusPerson = input("Do you want to add or delete a person?\n   If add, press a.\n   If delete, press d.\n   If neither, press n  ").lower()
            if ((plusPerson == "a") | (plusPerson == "n") | (plusPerson == "d")):
                break
            print("Sorry, but that was not a valid option. Please enter again.\n")
        if (plusPerson == "n"):
            break
        elif (plusPerson == "a"):
            addPerson()
        else:
            deletePerson()

def addPerson():
    firstName = input("What is their first name?  ").lower()
    lastName = input("What is their last name?  ").lower()
    while True:
        statusCheck = input("What is their status?\n   If member, press m.\n   If` visitor, press v  ").lower()
        if ((statusCheck == "m") | (statusCheck == "v")):
            break
        print("Sorry, but that was not a valid option. Please enter again.\n")
    if (statusCheck == "m"):
        status = "member"
    else:
        status = "visitor"
    while True:
        phoneNum = input("What is their phone number (\"(xxx) xxx-xxxx\")  ")
        if (len(phoneNum) == 14):
            if ((phoneNum[0:1] == "(") & (phoneNum[4:5] == ")") & (phoneNum[5:6] == " ") & (phoneNum[9:10] == "-")):
                break
        print("Sorry, but that was not a valid option. Please enter again.\n")
    email = input("What is their email address?  ")
    print("")
    print("")
    newPerson = Person(lastName, firstName, status, phoneNum, email)
    allPeople.append(newPerson)

def deletePerson():
    firstName = input("What is their first name?  ").lower()
    lastName = input("What is their last name?  ").lower()
    for person in allPeople:
        if ((person.lastName == lastName) & (person.firstName == firstName)):
            allPeople.remove(person)

readFromAllPeople()
readFromAttendance()
date = getDate()
<<<<<<< HEAD
service = getService()
askToAdd()
=======
time = getTime()
askToAddOrDelete()
>>>>>>> 5436b53340c633b30eaf7b1bef79b0ce824fb781
for person in allPeople:
    #writeToAllPeople(person)
    print(person)
    allPeopleString += person.firstName.capitalize() + " " + person.lastName.capitalize() + ","
thisService = Service(date, time, allPeopleString)
writeToAttendance(thisService)
