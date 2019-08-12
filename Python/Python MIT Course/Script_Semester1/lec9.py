# -*- coding: utf-8 -*-
"""
OBJECT ORIENTED PROGRAMMING
1.BUNDLE DATA INTO PACKAGES TOGETHER WITH PROCEDURES THAT WORK ON THEM THROUGH 
WELL-DEFINED INTERFACES
2. DIVIDE AND CONQUER DEVELOPMENT
3. EASY TO REUSE CODE
"""

# OBJECTS
# python supports many different kinds of data 
# 1234 3.1415 "hello" [1,5,7] {"ca":"ca","ma":"mass"}
# each is an instance of an object, and very object has 
# 1. type, 2. datd representation, 3. interaction
# each instance is a particular type of object
# 1. 1234 is an instance of an int 2. a = "hello", a is an instance of a string

# STANDARD DATA OBJECTS
# lists, tuples, strings

"""
CREATING AND USING YOUR OWN OBJECTS WITH CLASSES
"""
# Creating a class: define name/attribute
# Using an instance of the class: new instances/doing operation

"""
DEFINE YOUR OWN TYPES
WHAT ARE ATTRIBUTES? (data and procedures (method) associated with a class)
"""
# ATTRIBUTES: data and procedures that belong to the class
class Coordinate(object): # python object is the superclass of coordinate
    # Typically the fsirt function in a class
    def __init__(self,x,y): # double underscore, self->instance, this func calls when you ｉｎｖｏｋｅ
        self.x = x          #　ｃｒｅａｔｉｏｎ　ｏｆ　ａ　ｉｎｓｔａｎｃｅ, self automatically points the instance
        self.y = y
    
    # Methods are procudeure attributes that can manipulate the data attributes
    def distance(self,other): # other is another instance
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq+y_diff_sq)**0.5
    
    # Python calls the __str__ method when used with print on you class object
    # You choose what it does! e.g. print(c) -> <3,4>
    def __str__(self): # override internal print
        return "<"+str(self.x)+","+str(self.y)+">"
    # Other special methods
    # https://docs.python.org/3/reference/datamodel.html#basic-customization
    def __sub__(self,other): # override the interal substraction for instances in this class
        return Coordinate(self.x-other.x,self.y-other.y) # create a instance
    # eval(repr(c)) == c
    # a string that looks like a valid Python expression that could be used to 
    # recreate an object with the same value
    def __repr__(self):
        return "Coordinate({},{})".format(self.getX(),self.getY())
    
c = Coordinate(3,4) # create a new instance, c frame , like functions
origin = Coordinate(0,0) # creat another instance, origin fram 
#　Ｔｈｅｓｅ　ｔｗｏｓ　ａｒｅ　ｅｑｕｉｖａｌｅｎｔ　
print(c.distance(origin)) # print the distance to another instance, c is a  frame
print(Coordinate.distance(c,origin)) # equivalent to aobve but in a different way
#PRINT REPRESENTATION OF AN OBJECT
print(c) #-> <3,4>, you control what prints out
print(type(c))
print(Coordinate, type(Coordinate))
print(isinstance(c,Coordinate)) # check is an object a instance of a class
print(c-origin) # -> <3,4>


"""
EXAMPLE: FRACTIONS
"""
class fraction(object):
    def __init__(self,numer,denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer)+'/'+str(self.denom)
    # getters, but why we use them? can be just directly use self.numer? 
    # The reason is that we donot want to directly manipulator the attributes associated with 
    # those instances
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self,other):
        numerNew = other.getDenom()*self.getNumer()+ other.getNumer()*self.getDenom()
        denomNew = other.getDenom()*self.getDenom()
        return fraction(numerNew,denomNew)
    def __sub__(self,other):
        numerNew = other.getDenom()*self.getNumer()- other.getNumer()*self.getDenom()
        denomNew = other.getDenom()*self.getDenom()
        return fraction(numerNew,denomNew)
    def convert(self):
        return self.getNumer()/self.getDenom()
    
oneHalf = fraction(1,2)
twoThirds = fraction(2,3)

print(oneHalf) # -> 1/2
print(twoThirds) # -> 2/3
print(oneHalf.getNumer())

new = oneHalf + twoThirds
print(new.convert()) # -> 7/6

"""
EXAMPLE: A SET OF INTEGERS
"""
class intSet(object):
    def __init__(self):
        self.vals = []
    def insert(self,e):
        if not e in self.vals:
            self.vals.append(e)
    def member(self,e):
        return e in self.vals
    def remove(self,e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e)+' not found') # raise my own particular error
    
    # return an intersect instance      
    def intersect(self, other):
        result = intSet()
        for i in self.vals:
            if other.member(i):
                 result.insert(i)
        return result        
    
    # modify the print()       
    def __str__(self):
        self.vals.sort()
        #  return '{' + ','.join([str(e) for e in self.vals]) + '}' does the same job
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{'+ result[:-1] +'}'

    # modify the len()
    def __len__(self):
        return len(self.vals)
       
"""
ANOTHER EXAMPLE - ANIMALS
"""
class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None # define other data attribute even we dont pass them into an instance                  
    # getters
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    # setters, can change the binding for attributes
    def set_age(self,newage):
        self.age = newage
    def set_name(self,newname=""): # default argument is an empty string
        self.name = newname
    # special print
    def __str__(self):
        return "animal: "+str(self.name)+":"+str(self.age)
        
myAnimal = Animal(3)
myAnimal.set_name('foobar')
# why we want to use getters and setters:
myAnimal.age # directly access the attribute
myAnimal.get_age() # use the method and calling to access the attirbute (better)
                   # becasue we want to seperate the internal representation from access to that
                   # representation (it's called information hidding)
print(myAnimal)


"""
EXAMPLE-WHY USING GETTERS AND SETTERS
"""
# use a.get_age() NOT a.age: good style, easy to maintain code, prevent bugs
# always write a method to store the attributes inside it (setters), to access using getters
class Animal(object):
    def __init__(self,age):
        self.years = age # class definition changes, age -> years
    def get_age(self):
        return self.years

"""
HIERARCHIES
parent class (superclass), child class (subclass)
e.g. animal-> person, cat, rabbit. persion-> student
"""

class Cat(Animal): # inherits all attributes of Animal
    def speak(self): # add new functionality via new methods
        print("meow")
    def __str__(self): # overrides __str__ from Animal
        return "cat:"+str(self.name)+":"+str(self.age)
    
class Rabbit(Animal):
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit"+str(self.name)+":"+str(self.age)

class Person(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age) # explicity call Animal constructor, in the superclass
        Animal.set_name(self,name) # call Animal's method to change the name associated with
                                   # instance of a person
        self.freinds = [] # add a new data attribute
    def get_friends(self):
        return self.friends
    def add_friend(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self,other): # new method to give age diff in a user friendly way
        diff = self.get_age()-other.get_age()
        if self.age > other.age:
            print(self.name,"is",diff,"years older than", other.name)
        else:
            print(self.name,"is",-diff,"years younger than",other.name)
    def __str__(self): # override Animal's __str__method
        return "person:"+str(self.name)+":"+str(self.age)


jelly = Cat(1)
jelly.set_name("JellyBelly")
print(jelly) # print cat: JeLLyBelly:1
# we can explicilty recover the underlying Animal method by 
print(Animal.__str__(jelly)) # animal: JellyBelly:1

eric = Person("eric",45)
john = Person("john",55)
eric.speak()

"""
ANOTHER SUBSUBCLASS EXAMPLE Animal->Person->Student
"""
import random

class Student(Person):
    def __init__(self,name,age,major = None):
        Person.__init__(self,name,age)
        self.major = major
    def change_major(self,major):
        self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r <= 0.5:
            print("i need sleep")
        elif 0.5 <= r <= 0.75: 
            print("i should eat")
        else:
            print("i am watching tv")
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
    
eric = Person('Eric',45)
fred = Student('Fred',18,'Course VI')
print(fred)

"""
CLASS VARIABLES
"""
# define inside the class definition, but outside the of any of the methods
# shared among all objects/instances of that class

class Rabbit(Animal): # parent class
    tag = 1 # class variable
    def __init__(self,age,parent1 = None, parent2 = None):
        Animal.__init__(self,age)
        self.parent1 = parent1 
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1 # incremneting class variable and changes it for all instances that 
                        # may reference it
    def get_rid(self):
        return str(self.rid).zfill(3) # method on string to pad the beginning with zeros
    def get_parent1(self):            # e.g. 001 not 1
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self,other):
        return Rabbit(0,self,other) # modify the addition to create new instance
    def __eq__(self,other): # special method to compare two rabbits
        parents_same = self.parent1.rid == other.parent1.rid \
                       and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
                       and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite

peter = Rabbit(2)
peter.set_name('Peter')
hopsy = Rabbit(3)
hopsy.set_name('Hopsy')
cotton = Rabbit(1,peter,hopsy) # here peter and hopsy are instances
cotton.set_name('Cottontail')
mopsy = peter + hopsy
mopsy.set_name('Mopsy')
print(mopsy.get_parent1())
print(mopsy.get_parent2())
print(mopsy==cotton) # return true








