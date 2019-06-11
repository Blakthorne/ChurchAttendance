import sys
import datetime

class Person:
    def __init__(self, lastName, firstName, status, phoneNum):
        self.lastName = lastName
        self.firstName = firstName
        self.status = status
        self.phoneNum = phoneNum
        # self.numWeeksPresent = numWeeksPresent
        # self.numWeeksAbsent = numWeeksAbsent 

# create lists for info
allPeople = list()

def writeToList(Person):
    file = open("list.txt", "a+")
    info = Person.lastName + "," + Person.firstName + "," + Person.status + "," + Person.phoneNum + "\n"
    file.write(info)
    file.close()

def readFromList():
    with open("list.txt") as f:
        lines = f.read().splitlines()
    for line in lines:
        info = line.split(",")
        newPerson = Person(info[0], info[1], info[2], info[3])
        allPeople.append(newPerson)

def getDate():
    while True:
        isToday = input("Are you entering information for today?  ")
        if ((isToday == "yes") | (isToday == "no")):
            break
    if (isToday == "yes"):
        print(datetime.datetime.now())
        return datetime.datetime.now()
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
        return dateFormatted

def getService():
    while True:
        service = input("Morning or Evening?  ").lower()
        if ((service == "morning") | (service == "evening")):
            break
        print("Sorry, but that was not a valid option. Please enter again.\n")
    return service

def askToAdd():
    while True:
        while True:
            plusPerson = input("Do you want to add another person?  ").lower()
            if ((plusPerson == "yes") | (plusPerson == "no")):
                break
            print("Sorry, but that was not a valid option. Please enter again.\n")
        if (plusPerson == "no"):
            break
        addPerson()

def addPerson():
    firstName = input("What is their first name?  ").lower()
    lastName = input("What is their last name?  ").lower()
    while True:
        statusCheck = input("What is their status?\n   If member, press m.\n   If first time visitor, press f.\n   If returning visitor, press r  ").lower()
        if ((statusCheck == "m") | (statusCheck == "f") | (statusCheck == "r")):
            break
        print("Sorry, but that was not a valid option. Please enter again.\n")
    if (statusCheck == "m"):
        status = "member"
    elif (statusCheck == "f"):
        status = "first time visitor"
    else:
        status = "returning visitor"
    while True:
        phoneNum = input("What is their phone number (\"(xxx) xxx-xxxx\")  ")
        if ((phoneNum[0:1] == "(") & (phoneNum[4:5] == ")") & (phoneNum[5:6] == " ") & (phoneNum[9:10] == "-")):
            break
        print("Sorry, but that was not a valid option. Please enter again.\n")
    print("")
    print("")
    newPerson = Person(lastName, firstName, status, phoneNum)
    allPeople.append(newPerson)

date = getDate()
# service = getService()
askToAdd()
for person in allPeople:
    writeToList(person)
readFromList() 
