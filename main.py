from socket import *

class assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        age = currentYear - self.year
        print("Your age is {age}")

    def listAnniversaries(self):
        currentYear = 2024
        anniversaries = [year for year in range(self.year + 10, currentYear + 1, 10)]
        return anniversaries

    def modifyYear(self, n):
        yearStr = str(self.year)
        part1 = yearStr[:2] * n
        part2 = yearStr[1::2] * n
        result = part1 + part2
        return result

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
ret = a.listAnniversaries()
print(ret)

a = Assignment2(1991)
ret = a.listAnniversaries()
print(ret)

a = Assignment2(1782)
ret = a.modifyYear(3)
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
