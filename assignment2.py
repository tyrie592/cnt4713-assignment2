from socket import *

class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        age = currentYear - self.year
        print("Your age is", end = " ")
        print(age)

    def listAnniversaries(self):
        lst = []
        i = 10

        while (True):
            if self.year + i < 2022:
                lst.append(i)
            else:
                break
            i = i + 10
        return lst

    def modifyYear(self, n): #I CANT GET THIS TO WORK
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
