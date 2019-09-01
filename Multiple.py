
# Demo Multiple Inheritance
class Employee:
    department="IT"
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printDetails(self):
        return f"Name is {self.name}, Salary is {self.salary}, Role is {self.salary}"
    @classmethod
    def ChangeDepartment(cls,depart):
        cls.department=depart
    @staticmethod
    def printName(str):
        print("Name of Employee ",str)
class Player:
    no_of_game=4
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def printDetails(self):
        return f"Name is {self.name} , Game is {self.game}"

class CoolProgrammer(Player,Employee):
    lang="C++"
    def printLang(self):
        print(self.lang)

vijaya=Employee("Vijaya",25000,"Prof")
jaya=Employee("Jaya",15000,"Asst. Prof")
raj=Player("Raj",["Cricket"])
kajal=CoolProgrammer("Kajal","[Cricket,Football]")
print(kajal.printDetails())
