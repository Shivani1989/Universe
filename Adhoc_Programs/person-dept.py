class Person:
    def __init__(self, name, job=None, pay=0):
        self.name=name
        self.job=job
        self.pay=pay
    def lastName(self):
        return(self.name.split()[-1])
    def giveRaise(self, percent):
        self.pay= int(self.pay*(1+percent))
    def __repr__(self):
        return ('[Person : %s %s %s]' % (self.name, self.pay, self.job))
class Manager(Person):
    def __init__(self, name,pay):
        Person.__init__(self, name, 'mgr', pay)
    def giveRaise(self, percent, bonus=0.10):
        Person.giveRaise(self, percent+bonus)
class Department:
    def __init__(self, *args):
        self.members=list(args)
    def addMember(self, name):
        self.members.append(name)
    def giveRaises(self, percent):
        for name in self.members:
            name.giveRaise(percent)
    def showAll(self):
        for name in self.members:
            print(name)
if __name__=='__main__':
    bob=Person('Bob Smith')
    sue=Person('Sue Jones', job='dev', pay=100000)
    tom=Manager('Tom Jindal', 100000)
    dev=Department(bob, sue)
    dev.addMember(tom)
    dev.giveRaises(0.10)
    dev.showAll()
