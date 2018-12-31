import threading
from threading import Lock, Semaphore, Thread


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

print('################## implementing booking #####')
my_booking = BookRoom(6)
bt = Thread(target=my_booking.book,args=(3,))
bt.start()
b2 = Thread(target=my_booking.book, args=(4,))
b2.start()
b3 = Thread(target=my_booking.book, args=(2,))
b3.start()