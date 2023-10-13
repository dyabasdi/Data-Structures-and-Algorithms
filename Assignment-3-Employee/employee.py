class Employee:

    def __init__(self, **kwargs):
    # Add your code here!
        self.name = kwargs['name']
        self.identifier = kwargs['identifier']
        self.salary = kwargs['salary']
    def cal_salary(self):
        return self.salary
    def __str__(self):
    # Add your code here!
        print('Employee')
        print(self.name + ', ' + self.identifier + ', ' + str(self.salary))
        return
############################################################
############################################################
############################################################

class PermanentEmployee(Employee):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.benefits = kwargs['benefits']
    def cal_salary(self):
        if self.benefits == ["retirement", "health_insurance"]:
            return self.salary*0.7
        elif self.benefits == ["health_insurance"]:
            return self.salary*0.9
        elif self.benefits == ["retirement"]:
            return self.salary*0.8

    def __str__(self):
        print('Permanent Employee')
        print(self.name + ', ' + self.identifier + ', ' + str(self.salary) + ', ' + str(self.benefits))
        return

############################################################
############################################################
############################################################

class Manager(Employee):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bonus = kwargs['bonus']
    def cal_salary(self):
        return self.salary + self.bonus
    def __str__(self):
        print('Manager')
        print(self.name + ', ' + self.identifier + ', ' + str(self.salary) + ', ' + str(self.bonus))
        return



############################################################
############################################################
############################################################
class TemporaryEmployee(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hours = kwargs['hours']
    def cal_salary(self):
        return self.salary * self.hours
    def __str__(self):
        print('Temporary Employee')
        print(self.name + ', ' + self.identifier + ', ' + str(self.salary) + ', ' + str(self.hours))
        return

    
############################################################
############################################################
############################################################


class Consultant(TemporaryEmployee):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.travel = kwargs['travel']

    def cal_salary(self):
        return (self.travel * 1000) + self.salary
    def __str__(self):
        print('Consultant')
        print(self.name + ', ' + self.identifier + ', ' + str(self.salary) + ', ' + str(self.hours) + ', ' + str(self.travel))
        return
  
############################################################
############################################################
############################################################


class ConsultantManager(Manager, Consultant):
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
    def cal_salary(self):
        return self.salary * self.hours + self.travel*1000 + self.bonus
    def __str__(self):
        print('Consultant Manager')
        print(self.name + ', ' + self.identifier + ', ' + str(self.salary) + ', ' + str(self.hours) + ', ' + str(self.travel) + ', ' + str(self.benefits)
        return


############################################################
############################################################
############################################################





###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():
    """
    A Main function to create some example objects of our classes. 
    """

    chris = Employee(name="Chris", identifier="UT1", salary="None")
    print(chris, "\n")

    emma = PermanentEmployee(name="Emma", identifier="UT2",
                              salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = TemporaryEmployee(name="Sam", identifier="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", identifier="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", identifier="UT5",
                        salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = ConsultantManager(name="Matt", identifier="UT6",
                              salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")

if __name__ == "__main__":
  main()



