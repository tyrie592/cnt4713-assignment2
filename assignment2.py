from socket import *

class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        age = currentYear - self.year
        print("Your age is", end = " ")
        print(age)

    def listAnniversaries(self):
        current_year = 2024  # Assuming today is the year 2024
        anniversaries = []
        for year in range(self.year, current_year + 1, 10):
            if year % 10 == 0:
                anniversaries.append(year % 100)
        return anniversaries

    def modifyYear(n):
        num = a
        res = ""
        arr = str(num)
        for i in range(n):
            res += arr[:2]
        num = num * n
        lst = str(num)
        arr1 = lst[::2]
        res += arr1
        return res

    def checkGoodString(string): #@staicmethod
        if len(string) < 9:
            return False
        if string[0].islower() == False:
            return False
        numCount = 0  # Initialize the count to 0
        for i in string:
            if i.isdigit():
                numCount += 1  # Increment the count if the character is a digit
            if numCount > 1:
                return False
        return True

    def connectTcp(host, port):#@staticmethod
         try:
             s = socket(AF_INET, SOCK_STREAM)
             hostAddress = gethostbyname(host)
             s.connect((hostAddress, port))
             s.close()
             return True
         except:
             return False

#test code below
a = Assignment2(2000)
ret = a.tellAge(2024)
print(ret)

a = Assignment2(2000)
ret = a.listAnniversaries()
print(ret)

a = Assignment2(1991)
ret = a.listAnniversaries()
print(ret)

a = 1782
ret = Assignment2.modifyYear(3)
print(ret)

ret = Assignment2.checkGoodString("f1obar0more")
print(ret)

ret = Assignment2.checkGoodString("foobar0more")
print(ret)

retval = Assignment2.connectTcp("www.google.com", 80)
if retval:
    print("Connection established correctly")
else:
    print("Some error")
