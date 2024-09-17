#this will show you how to create a class 
class Myclass:
    #define objects here 
    name:str= 'Punit'
    age:int =25

    def call(self):
        print(f"Hi I am {Myclass.name} and i am {Myclass.age} years old")
#Myclass.call()  -- this will not work because To use the class, first create an instance, like so: 

myclass=Myclass()
myclass.call()
