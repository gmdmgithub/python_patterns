import threading

from time import sleep

from threading import Thread

print('Get current thread',threading.current_thread().getName())

if threading.current_thread().getName() == threading.main_thread().getName():
    print('Main thered is running')

# three ways to use threading

# first by function
def display_names():
    i = 0
    while(i <= 3):
        print(i, 'Get current thread - function', threading.current_thread().getName())
        i +=1

t = Thread(target=display_names)
t.start()

# second by subclassing

class MyThread(Thread):
    """"just simple example of thread - override run is essential"""
    
    def run(self):
        i = 0
        
        while(i <= 3):
            print(i,'Get current thread -subclass', threading.current_thread().getName())
            i +=1
tc = MyThread()
tc.start()# start method not run

# third is using class
class MyNotExtendThread:
    def display_names(self):
        i = 0
        sleep(1)
        while(i <= 3):
            print(i,'Get current thread - class', threading.current_thread().getName())
            i +=1

my_class = MyNotExtendThread()
tcm = Thread(target=my_class.display_names) #just show the class and the name of the method to be invoke
tcm.start()

tcm2 = Thread(target=my_class.display_names) #just show the class and the name of the method to be invoke
tcm2.start()

sleep(3)

class EvenNumbers:
    def print_event_num(self, from_n=1, to_n=10):
        print('Even num - current thread', threading.current_thread().getName())
        if from_n >= to_n:
            return 'You mast be joking'
        for i in range(from_n,to_n):
            if i % 2 == 0:
                print(i) 

class OddNumbers:
    def print_odd_num(self, from_n=5, to_n=25):
        print('Odd num - current thread', threading.current_thread().getName())
        if from_n >= to_n:
            return 'You mast be joking'
        for i in range(from_n,to_n):
            if i % 2 != 0:
                print(i)
class Main:
    def print_num(self,to_n=10):
        print('Main - current thread', threading.current_thread().getName())
        for i in range(0,to_n):
            print(i)

my_evens = EvenNumbers()
my_odds = OddNumbers()
my_main = Main()

teven = Thread(target=my_evens.print_event_num,args=[2,10])
todds = Thread(target=my_odds.print_odd_num,args=[1,14])
tmain = Thread(target=my_main.print_num, args=[8])

teven.start()
todds.start()
tmain.start()