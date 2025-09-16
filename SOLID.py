#________________1________________________
class Report:
    def __init__(self,data,text):
        self.data=data
        self.text=text
class Text:
    def generate(self,report:Report):
        report.data = ["A", "B", "C"]
        report.text = "\n".join(report.data)
class Save:
    def save(self,report:Report):
        with open("report.txt", "w") as f:
            f.write(report.text)

#___________________2___________________
class Shape:
   def area(self):
      pass
class Circle(Shape):
   def circle(self,r):
      self.r=r
   def area(self):
      return 3.14 * self.r**2
    
class Square(Shape):
   def square(self,x):
      self.x=x
   def area(self):
      return self.x **2
class Rectangle(Shape):
   def rectangle(self,l,w):
      self.l=l
      self.w=w
   def area(self):
      return self.l * self.w
#_______________3___________________
class Bird:
   pass
class canfly(Bird):
   def canfly(self):
      print("i can fly")
class Cantfly(Bird):
   def cant_fly(self):
      print("i can't fly")
class Ostrich(Cantfly):
   pass


#____________4_______________
class Can_work:
   def can_work(self):
      print("i can work ")
class Can_eat:
   def eat(self):
      print("i can eat")
class Robot(Can_eat,Can_work):
   pass

focal_robot=Robot()
focal_robot.can_work()
#____________5____________
from abc import ABC,abstractmethod

class Database(ABC):
   @abstractmethod
   def fetch(self):
      pass

class MySQL(Database):
   def fetch(self):
      return ["data from MySQL"]

class Memory(Database):
   def fetch(self):
      return ["data from memory"]
class Service:
   def __init__(self,db):
      self.db=db
      pass

