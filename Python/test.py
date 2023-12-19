from abc import ABC, abstractmethod

class Human(ABC):

    @abstractmethod
    def speak(self):
        pass


class Student(Human):

    def get_info(self):
        return "Getting info"

    def speak(self):
        return "I'm student"

student = Student()
print(student.get_info())
print(student.speak())