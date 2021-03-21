'''Objective
Today, we're delving into Inheritance. Check out the attached tutorial for learning
materials and an instructional video.
Task
You are given two classes, Person and Student, where Person is the base class and
Student is the derived class. Completed code for Person and a declaration for
Student are provided for you in the editor. Observe that Student inherits all the
properties of Person.
Complete the Student class by writing the following:
A Student class constructor, which has  parameters:
A string, firstName.
A string, lastName.
An integer, idNumber.
An integer array (or vector) of test scores, .

A char calculate() method that calculates a Student object's average and returns
the grade character representative of their calculated average:
Grading.png'''

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, testScores):
        super().__init__(firstName, lastName, idNumber)
        self.testScores = testScores

    def calculate(self):
        total = 0

        for testScore in self.testScores:
            total += testScore

        avg = total / len(self.testScores)

        if 90 <= avg <= 100:
            return 'O'
        if 80 <= avg < 90:
            return 'E'
        if 70 <= avg < 80:
            return 'A'
        if 55 <= avg < 70:
            return 'P'
        if 40 <= avg < 55:
            return 'D'
        return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
