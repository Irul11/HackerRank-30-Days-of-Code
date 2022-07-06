class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores):
        super().__init__(firstName, lastName, idNum)
        self.avrScore = sum(scores) / len(scores)

    def calculate(self):
        if 90 <= self.avrScore <= 100:
            return 'O'
        elif self.avrScore >= 80:
            return 'E'
        elif self.avrScore >= 70:
            return 'A'
        elif self.avrScore >= 55:
            return 'P'
        elif self.avrScore >= 40:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())