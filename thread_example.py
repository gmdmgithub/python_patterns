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

sleep(5)
################## implementing booking #####
print('\n')
print('################## implementing booking #####')
from threading import Lock,Semaphore

class BookRoom:

    def __init__(self,evailable_rooms):
        self.evailable_rooms = evailable_rooms
        #self.lock = Lock() # allowes to lock for synchronisation
        self.lock = Semaphore() # allowes to lock for synchronisation - the same as lock

    def book(self,room_requested):
        tn = threading.current_thread().getName()
        print(f'Current available rooms no is {self.evailable_rooms}, working thread: {tn}')

        self.lock.acquire()  # with release are both keys for semaphore
        if self.evailable_rooms >= room_requested:
            print(f'Room choose, thread {tn}')
            print(f'Payment processing ... thread {tn}')
            print(f'Giving key .... thread {tn}')
            self.evailable_rooms -= room_requested
        else:
            print(f'Sorry not enouth rooms ... thread {tn}')
        self.lock.release()

my_booking = BookRoom(6)
bt = Thread(target=my_booking.book,args=(3,))
bt.start()
b2 = Thread(target=my_booking.book, args=(4,))
b2.start()
b3 = Thread(target=my_booking.book, args=(2,))
b3.start()

sleep(3)
print('\n')
print('################## Thread communication = flag way #####')

class Producer:
    def __init__(self):
        self.products = []
        self.order_praced = False

    def produce(self):
        print(f'Producer launched {threading.current_thread().getName()}')
        for i in range(1,5):
            self.products.append(f'Product {i}')            
            sleep(1)
            print('Product added')
        self.order_praced = True

class Consumer:
    def __init__(self,prod):
        self.prod = prod

    def consume(self):
        print(f'Consumer launched {threading.current_thread().getName()}')
        while self.prod.order_praced == False:
            sleep(0.2)

        print(f'Order shipped for product {self.prod.products}')

prod = Producer()
consum = Consumer(prod)

tpr = Thread(target=prod.produce)
tcon = Thread(target=consum.consume)
tpr.start()
tcon.start()