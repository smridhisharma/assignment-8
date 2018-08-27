#Q.1-Calculate Area and Circumference of a Circle
class circle:
    def __init__ (self,r):
        self.radius=r
    def getArea(self):
        self.area=3.14*self.radius*self.radius
        return self.area
    def getCircumference(self):
        self.c=2*3.14*self.radius
        return self.c
r=int(input("Enter radius of circle "))
c1=circle(r)
print("Area of circle is:",c1.getArea())
print("Circumference of circle is:", c1.getCircumference())

#Q.2-Make a Class Student and Display its Required Info
class student:
    def __init__(self,name,rno):
        self.name=name
        self.rollno=rno
    def setAge(self,age):
        self.age=age
    def setMarks(self,marks):
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Roll No.:",self.rollno)
        print("Age:",self.age)
        print("Marks:",self.marks)
name=input("Enter name: ")
rno=int(input("Enter rollno: "))
age=int(input("Enter the age of student "))
marks=int(input("Enter marks of student "))
s1=student(name,rno)
s1.setAge(age)
s1.setMarks(marks)
s1.display() 

#Q.3- Convert Temperature
class Temperature:
    def convertFahrenheit(self,c):
        f=((c*9)/5)+32
        return f
    def convertCelsius(self,f):
        c=(f-32)/1.8
        return c
t=Temperature()
temp1=int(input("Enter temperature in Celcius "))
temp2=int(input("Enter temperature in Fahrenheit "))
print(temp1,"in Fahrenheit is",t.convertFahrenheit(temp1),"and",temp2,"in Celclius is",t.convertCelsius(temp2))


#Q.4- Create a Class MovieDetails and Perform the Required Functionalities
class MovieDetails:
    def add(self,name,year,rating):
        self.artistname=name
        self.yearofrelease=year
        self.rating=rating
    def display(self):
        print("Artist Name: ",self.artistname,"\nYear of release:",self.yearofrelease,"\nRating:",self.rating)
    
m=MovieDetails()
name=input("Enter name of artist ")
year=int(input("Enter year of release "))
rating=int(input("Enter rating "))
m.add(name,year,rating)
m.display()

#Q.5- Inheritance(Animal)
class Animal:
    def animal_attribute(self):
        print("My attribute is: Lion")
class Tiger(Animal):
    def tiger_attr(self):
        print(" ")
a=Animal()
t=Tiger()
t.animal_attribute() 

#Q.6-Determine the output of following code.
'''
The output will be
A B
A B
because a.f() calls function f() which calls g() which returns 'A' and b.f() calls f() which calls self.g() so this means g() of class B will be called.
a.g() and b.g() will call g() of class A and B respectively. Here, method overriding is done. '''

#Q.7-Inheritance (Shapes)
class shape:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        self.area=self.length*self.breadth
        return self.area
class rect(shape):
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
class square(shape):
    def __init__(self,s):
        self.length=s
        self.breadth=s
r=rect(10,2)
s=square(5)
print("Area of rectangle:",r.area(),"and area of square:",s.area())
