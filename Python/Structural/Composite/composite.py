from abc import ABC, abstractmethod, abstractstaticmethod

class Component:

    def __init__(self, *args, **kwargs):
        pass

    def componenet_function(self):
        raise NotImplementedError

class Child(Component):
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]

    def componenet_function(self):
        print(f"\t{self.name}")

class Composite(Component):

    def __init__(self, *args, **kwargs):
        self.children = []
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def componenet_function(self):
        print(self.name)
        for i in self.children:
            i.componenet_function()

sub1 = Composite("submenu1")

# create child submenu
sub11 = Child("submenu 11")
sub12 = Child("submenu 12")

sub1.append_child(sub11)
sub1.append_child(sub12)

# Build composite top level menu
top = Composite("top menu")

sub2 = Child("submenu 2")
# Add the composite submenu 1 to the top level composite menu
top.append_child(sub1)

# Add the plain submenu 2 to the top level composite menu
top.append_child(sub2)

top.componenet_function()

# Example 2

class IDepartment(ABC):
    @abstractmethod
    def __init__(self, employees):
        pass

    @abstractstaticmethod
    def print_department(self):
        raise NotImplementedError

class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting Department: {self.employees}")

class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Development Department: {self.employees}")

class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def print_department(self):
        print("Parent Department")
        print(f"Parent Department Base Employess: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total number of employess {self.employees}")

dept1 = Accounting(200)
dept2 = Development(170)

parent_dept = ParentDepartment(30)
parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_department()
