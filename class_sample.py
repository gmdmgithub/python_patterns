print('################### simple example ############################')


class Person:
    def __init__(self, name):
        self.__hands = 2
        self.__legs = 2
        self.__name = name

    def nimble(self):
        print(f'person has {self.__hands} hands and {self.__legs} legs')

    def __repr__(self): #its not to string method __str__
        return f'Person name is: {self.__name}'


alan = Person('Alan')
#alan.__hands - cause compilation error
alan.nimble()
print('Strange access to private field - called "Mangling"',
      alan._Person__name)
print(alan)  # to string methot should be called (__repr__)

print('################### encapsulation ############################')


class Patient:
    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_ssn(self, ssn):
        self.__ssn = ssn

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_ssn(self):
        return self.__ssn


patient = Patient()

patient.set_id(1)
patient.set_name('Alex')
patient.set_ssn('AAC-1234')
print(patient.get_id(), patient.get_name(), patient.get_ssn())

print('################### inheritance ############################')


class IPhone:
    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    def __repr__(self):
        return f'Name from toString is {self.__name}'

    def show(self):
        print(f'the best phone in the world is {self.__name}')

    def get_name(self):
        return self.__name


class IPhoneX(IPhone):
    def __init__(self, name, size, headphones):
        super().__init__(name, size)
        self.__headphones = headphones

    def ring(self):
        print(f'Hi here iPhone x is ringing {self.get_name()}')


iphx = IPhoneX('model X', 10, False)
iphx.show()
iphx.ring()
print(iphx)

print(
    '################### abstract class - interface ############################'
)
#in python its a class with all abstract methods @abstractmethod
from abc import abstractmethod, ABC


class Car(ABC):  #must inherit from ABC class
    @abstractmethod
    def drive(self):
        pass


class BMW(Car):
    def __init__(self, name):
        self.__name = name

    def drive(self):
        print('I am driving')

    def __repr__(self):
        return f'I am a {self.__name}'


bmw = BMW('BMW')
bmw.drive()
print(bmw)


class TouchScreenLaptop(ABC):
    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass


class HP(TouchScreenLaptop):
    def scroll(self):
        print('HP is scrolling')


class DELL(TouchScreenLaptop):
    def scroll(self):
        print('DELL is scrolling')


class HPNotebook(HP):
    def click(self):
        print('HP is clicking')


class DELLNotebook(DELL):
    def click(self):
        print('DELL is clicking')


hp_notebook = HPNotebook()
dell_notebook = DELLNotebook()
hp_notebook.click()
hp_notebook.scroll()
dell_notebook.click()
dell_notebook.scroll()

print('################### exception ############################')


class InvaliPasswordException(Exception):
    pass


def get_password():
    password = input('Please enter a pass: ')
    if len(password) < 8:
        raise InvaliPasswordException()
    return password


try:
    get_password()
except InvaliPasswordException:
    print('Password must have at least 8 characters')
finally:
    print('Get password was called')