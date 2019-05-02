"""
OPP: AN Example
"""

import datetime

class Person(object):
    def __init__(self,name):
        self.name= name
        self.birthday = None
        self.lastName = name.split(' ')[-1] # name is a string, so split into a list of strings
                                           # based on spaces
    def getLastName(self):
        return self.lastName
    
    def setBirthday(self,month,day,year):
        self.birthday = datetime.date(year,month,day)
    
    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today()-self.birthday).days # convert into days/years
    
    def __lt__(self,other): # lt = leass than, sort people by last name
        if self.lastName == other.lastName: # if than have same lastname, we sort them by their 
            return self.name < other.name   # fullname
        return self.lastName < other.lastName
    
    def __str__(self): # override the print method
        return self.name

#p1 = Person('Mark Zuckerberg')
#p1.setBirthday(5,14,84)
#p2 = Person('Drew Houston')
#p2.setBirthday(3,4,83)
#p3 = Person('Bill Gates')
#p3.setBirthday(10,28,55)
#p4 = Person('Andrew Gates')
#p5 = Person('Steve Wozniak')
#
#personList = [p1,p2,p3,p4,p5]
## print them in order
#for e in personList:
#    print(e)
## sort the names in order
#personList.sort()
#for e in personList:
#    print(e)


"""
USING INHERITANCE
"""
class MITPerson(Person): # subclass
    nextIdNum = 0 # next ID number to assign
    
    def __init__(self,name):
        Person.__init__(self,name) # initilaize Person attributes
        self.idNum = MITPerson.nextIdNum # MITPerosn attribute: unique ID
        MITPerson.nextIdNum += 1 # update the class variable
        
    def getIdNum(self):
        return self.idNum
    
    def __lt__(self,other): # sorting them by ID numbers
        return self.idNum < other.idNum
    
    def speak(self,utterance):
        return (self.getLastName()+" say:　"+ utterance)

#m3 = MITPerson('Mark Zuckerberg')
#Person.setBirthday(m3,5,14,84)
#m2 = MITPerson('Drew Houston')
#Person.setBirthday(m2,3,4,83)
#m1 = MITPerson('Bill Gates')
#Person.setBirthday(m1,10,28,55)
#
#MITPersonList = [m1, m2, m3]

## print outher the mit list
#for e in MITPersonList:
#    print(e)
## sort them by ID
#MITPersonList.sort()
#for e in MITPersonList:
#    print(e)

#
#p1 = MITPerson('Eric')
#p2 = MITPerson('John')
#p3 = MITPerson('John')
#p4 = Person('John')
#
#p1 < p2 # = p1.__lt__(p2), True, comared on id numbers
#p1 < p4 # = p1.__lt__(p4), Attribute error, p4 does not have a id attribute 
#p4 < p1 # = p4.__lt__(p1), Flase , p1 has a name attribute, compared with name



"""
ADD MORE CLASSES
"""
class Student(MITPerson): # better the create a superclass that covers all students
    pass

class UG(Student): # undergraduate student
    def __init__(self,name,classYear):
        MITPerson.__init__(self,name)
        self.year = classYear
    
    def getClass(self):
        return self.year
    
    def speak(self,utterance):
        return MITPerson.speak(self," Dude, "+utterance)
    
class Grad(Student):
    pass

class TransferStudent(Student):
    pass

def isStudent(obj): # check if is student
    return isinstance(obj,Student)


#s1 = UG('Matt Damon',2017)
#s2 = UG('Ben Affleck',2017)
#s3 = UG('Lin Manuel Miranda',2018)
#s4 = Grad('Leonard di Caprio')
#s5 = TransferStudent('Robert deNiro')
#
#print(s1)
#print(s1.getClass())
#print(s1.speak('Where is the quiz?'))
#print(s2.speak('I have no clue!'))


"""
USING INHEREITED METHODS
"""
class Professor(MITPerson):
    def __init__(self,name,department):
        MITPerson.__init__(self,name)
        self.department = department
        
    def speak(self, utterance): # shadow the MIT speak method, but uses the MIT speak method
        new = 'In course '+ self.department + ' we say '
        return MITPerson.speak(self,new + utterance)
    
    def lecture(self,topic):
        return self.speak('it is obvious that '+ topic)

faculty = Professor('Doctor Arrogant','six')




"""
EXAMPLE CLASS: GRADEBOOK
create class that includes instance of other classes within in
"""
class Grades(object):
    def __init__(self):
        self.students = [] # list of student object
        self.grades = {} # maps idNum -> list of grades
        self.isSorted = True # true if self.student is sorted
    
    def addStudent(self,student):
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student) # student is a list, we simply append it 
        self.grades[student.getIdNum()] = [] # grades is dict, student is another instance
                                             # create empty list associated with the key 
                                             # student.getIdNum() from another instance student
        self.isSorted = False
        
    def addGrade(self,student,grade):
        try: # student is another instance from other class
            self.grades[student.getIdNum()].append(grade) # is a list now, then we can append
        except KeyError:
            raise ValueError('Student not in grade book')
    
    def getGrades(self,student):
        try:
            # return a copy, which means I can do things onthat without destroying original set
            return self.grades[student.getIdNum()][:]  # a safe thing to do
        except KeyError:
            raise ValueError('Student not in grade book')
    
#    def allStudents(self):
#        if not self.isSorted: # if not sorted
#            self.students.sort() # sort the list
#            self.isSorted = True
#        return self.students[:] # return a copy of list of students
    
    # a new version with generator
    def allStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True # print(six00.allStudents().__next__())
        for s in self.students: # it gives the next one without generating the entire list
            yield s               
            
    def gradeReport(course): # assume course is a type of grades
        report = [] # empty list
        for s in course.allStudents(): # loop  over all the students
            tot = 0.0
            numGrades = 0
            for g in course.getGrades(s): # run every grade in the gardes associated with that student
                tot += g
                numGrades += 1
            try:
                average = tot/numGrades # report the average
                report.append(str(s)+'\'s mean grade is ' +str(average)) # \' = ' 
            except ZeroDivisionError:
                report.append(str(s)+' has no grades')
        return '\n'.join(report) # join the list with carriage return


ug1 = UG('Matt Damon', 2018)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Drew Houston', 2017)
ug4 = UG('Mark Zuckerberg', 2017)
g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')

six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)
six00.addStudent(ug3)

six00.addGrade(g1,100)
six00.addGrade(g2,25)
six00.addGrade(ug1,95)
six00.addGrade(ug2,85)
six00.addGrade(ug3,75)

# add more grades
six00.addGrade(g1,90)
six00.addGrade(g2,45)
six00.addGrade(ug1,80)
six00.addGrade(ug2,75)

print(six00.gradeReport())


"""
GENERATORS
solve the probelm - large list of student
"range" is same idea
"""
# any procedure or method with yield statement called a generator
# generators have a next() method which starts/resumes excution of the procedure
# yield suspends execution and returns a value
# returning from a generator raises a StopIteration
# It lets us known how far i go in the computation before i stop and return a value
def genTest():
    yield 1
    yield 2

# foo =genTest()
# foo.__next__() -> 1
# foo.__next__() -> 2
# foo.__next__() -> StopIteration

for n in genTest(): # print out 1, 2 in turn
    print(n)

def genFib():
    fibn_1 = 1 # fib(n-1)
    fibn_2 = 0 # fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

fib = genFib()
fib.__next__() # 1
fib.__next__() # 1
fib.__next__() # 2
fib.__next__() # 3

# for n in genFib():
#  print(n) 
# will produce all of the Fibonacci numbers (an infinite sequence)












