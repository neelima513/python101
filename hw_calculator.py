
//calculator in python using classes and objects 
class Cal():
          result = 0
          def __init__(self,a,b):
              self.a=a
              self.b=b
          def add(self):
              self.result=self.a+self.b
              return self.result
          def sub(self):
     	      self.result=self.a-self.b
     	      return self.result