#in this file we will gonna earn constructors 
#__init__ is python constructor it;s there to define object , if we create objects manually it is there as an empty constructor 
#__init__(self):
#   pass-- like this 

# three type , empty like above one 
#no parameter like below one 
class myclass:
    def __init__(self) :
        print ('this is myclass')
myclass()

#parameter 

class info:
    def __init__(self,first_name, last_name, age, nationality):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.nationality=nationality
Info=info('Punit',"Jhorar",25,"Indian")
print(F"HI My NAME IS  {Info.first_name} {Info.last_name}, I AM AN {Info.nationality} OF AGE {Info.age}.")
