import datetime


class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay=6000):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    @property  # now accesable like attribute
    def email(self):
        try:  #check if the attibute was set
            return self.__email
        except AttributeError:
            return f"{self.first}.{self.last}@email.com"

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):  #usually reprent represent like constructor
        return f"Employee('{self.first}','{self.last}',{self.pay})"

    def __str__(self):  #str representrs to_string
        return f'Hi there {self.first}, {self.last} and my salary is: {self.pay} my email is {self.email}'

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def print_employees(self):
        for emp in self.employees:
            print(emp)

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def delete_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)


emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Mark', 'Mayer')
emp_2.apply_raise()

Employee.set_raise_amt(1.05)

emp_str_1 = 'John-Doe-8000'
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1)
print(new_emp_1.__repr__())
emp_2.email = "adam.colt@gmail.com"

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))

manager = Manager('Adam', 'Smith', 1234, [emp_1, emp_2])
manager.add_employee(new_emp_1)
manager.print_employees()

print(f'Num of emploees is {Employee.num_of_emps}')
