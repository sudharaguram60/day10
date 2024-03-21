#day-10
'''
#) Tasks
# Write the code for the belwo tasks using function
# 1.) d1 = {"shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30}
# a.) Find the min ans max priced product
# b.) Find the product starts with 's' and 'S'

# 2.) Find the n = 67, is strong number or not

# 3.) l1 = [1,2,3,4,5,6]
# n=2 --> [5, 6, 1,2,3,4]
# n=3--> [4,5,6, 1,2,3]

#method riding
#polymorpisam
class bank:
    def ratio(self):
        print("all banks has repo rate")
class sbi(bank):
    def ratio(self):
        print("sbi rate is 9%")

class iob(bank):
    def ratio(self):
        print("iob rate is 7.5%")

i = iob()
i.ratio()
s = sbi()
s.ratio()

#eg-2
class usa:
    def languge(self):
        print("english")
    def capital(self):
        print("washington dc")

class india:
    def languge(self):
        print("none")
    def capital(self):
        print("new delhi")

i = india()
i.languge()
i.capital()

#eg-3
#polymorisim using objects
#c1,c2-->c1=print(c1),print(c2)
#f1,f2
class c1:
    def f1(self):
        print("class1")
        
class c2( c1):
     def f1(self):
        super().f1()

        print("class2")
        
obj1 = c2()
obj2 =c1()
def display(a):
    a.f1()
display(obj1) 
display(obj2) 
'''
'''
#changing the functionality of builtin functions
a = 9
b = 6
print(a+b)
print(a.__add__(b))
class shopping:
    def__init__(self,l1):
        self.items = l1
    def__len__(self):
        length = len(self.items)
        return length
s = shopping([1,2,3,4,5])
print(len(s))
'''
'''
#--->method overloading
#eg-1
class suming:
    def  add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
s = suming()
#s.add(4,3)
s.add(4,5,1)
#eg-2
class summing:
    def add(self,a=none,b=none,c=none):
        if a!=none and b!=none and c!=none:
            print(a+b+c)
        elif a!=none and b!=none:
            print(a+b)
        else:
            print(a)
obj =summing()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)

#--->abstraction
#the process of hiding the implmentation details is abstraction
#eg-1
class triangle(shapes):
    def traingle_sides(self):
        print("3 sides")

    def name(self):
        print("Iam traingle")

   def sides (self):
       pass

class square(shapes):
    def square(self):
        print("4 sides")
        
tr triangle()
tr.traingle_sides()
tr.name()
'''
'''
# ! Rules to define abstract class 1
#2.) From abc import ABC, abstractmethod
#3.) subclass the normal class with ABC
# 4,) convert the normal method inside the abstract class to abstract method
#5.) All the child classes have to be subclassed with abstract class
#6.) The abstract method should be present in the child classes

# ! Eg:2
# super() ---. used to access the parent class method from child class method
from abc import ABC, abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("This is abstract class")

class c2(c1):
    def m2(self):
        super().m1()
        print("Iam child 1")

    def m1(self):
        pass
class2 = c2()
class2.m2()

#eg-3
from abc import ABC,abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd = "sneha123"
        return pswd
class login(password):
    def validate(self,name,password):
        if super().pwd() == password:
            print("welcome",name,'!!')
            print("login successful")
        else:
            print("please chek the password")
    def pwd(self):
        pass
login = login()
name = input("enter the name:")
pwd = input("enter the password:")
login.validate(name,pwd)
'''
'''
# encapsulationj1 n
#eg-1
class car:
    name = "bmw"
   print(name)
c1 = car()
print(c1.name)
c1.name = "aud1"
print(c1.name)
'''
'''
#--->eg-2
#accessing private date outside the class
class c1:
    __phone = '9704027601'
    def display(self):
        print(self.__phone)
c = c1()
c.display()
#--->eg3
#declare private method
class class1:
    def__m1(self):
        print("i am private method")
    def__init__(self):
        self.__m1()
c =class()
c.__m1()
'''
#-->nested class
class class1:
    class class2:
        name = "sneha"
        def display(self):
            print(self.name)
    obj1 = class2()
obj = class1()
obj.obj1.display()

# ! ---> TASK
# 1.) Write the code for the below tasks using function
#     d1 = {"shirt":1000, "pant":1500, "Shoes":900, "handkey":30}
#     a.) Find the min and max priced product
#     b.) Find the product starts with 's' and 'S'

# 2.) Find the n = 67, is strong number or not

# 3.) l1 =
d1 ("shirt", 1000, "pant": 1500, "Shoes": 900, "handkey": 30
for val in d1:
if d1 [val] = min(d1.values());
print(val)
for val in d1:
if d1 [val] max(d1.values()):
print(val)
for val in d1:
if val.startswith('s') or val.startswith('S'): print(val)c
