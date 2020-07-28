import time
import sys
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
#enemy classes
class Enemy(object):
    def _init_(self,patk,pdef,exp):
        self.patk=patk
        self.pdef=pdef
        self.exp=exp
#enemy list
        Slime=Enemy(2,1,5)

#character class
class Job:
    def __init__(self,atk,vit,exp):
        self.atk=atk
        self.vit=vit
        self.exp=exp

    def levelUp(){
        self.exp=10
    }

warrior=Job(3,2,0)
thief=Job(2,2,0)
mage=Job(1,3,0)

"""
    def _init_(self,catk,cdef,cexp):
        self.catk=catk;
        self.cdef=cdef;
        self.cexp=cexp;
    def wlevel (self):
        self.catk=self.catk+3
        self.cdef=self.cdef+2
        self.cexp=self.cexp+0
    def tlevel (self):
        self.catk=self.catk+2
        self.cdef=self.cdef+2
        self.cexp=self.cexp+0
    def mlevel (self):
        self.catk=self.catk+1
        self.cdef=self.cdef+2
        self.cexp=self.cexp+0
#classes
        warrior = Jobs(3,2,0)
        thief=Jobs(2,2,0)
        mage=Jobs(1,3,0)

"""
#Old Code
"""
print_slow('Hi my name is NERD. \nAnd before you say anything it is an acronym.\n')
time.sleep(1)
print_slow("It stands for Neo Education Rendering Device. Aka NERD.\n")
time.sleep(1)
print_slow('What is your name?\n')
name = input('Please enter your name:')
time.sleep(1)
print_slow('Hello ' + name +'\n')
time.sleep(1)
print_slow('You have been asleep for a very long time \n')
time.sleep(1)
print_slow('And the world has changed ALOT\n')
time.sleep(1)
print_slow('Okay so random question. Do you feel more like a warrior, thief, or mage? \n')
time.sleep(1)
print_slow('You should answer quickly. There is a monster heading this way!\n')
job=input('Choose before monster attacks: ')
time.sleep(1)
def char_class(str):
    if (job == warrior):
        warrior(self)
    elif (job == mage):
        mage(self)
    elif (job == thief):
        thief(self)
    else:\
        return 'Try Again'
print_slow('Okay great! I hope you\'re a good ' + job + ' because the monster is HERE!')
print(warrior(self))
"""
        


