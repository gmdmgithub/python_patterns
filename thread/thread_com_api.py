from threading import Thread,Condition
from time import sleep
import threading

class Producer:
    def __init__(self):
        self.products = []
        self.condition = Condition()# not a flag but condition

    def produce(self):
        print(f'Producer launched {threading.current_thread().getName()}')
        self.condition.acquire() #now we lock
        for i in range(1,5):
            self.products.append(f'Product {i}')            
            sleep(1)
            print('Product added')
        self.condition.notify() # notify consumer its done
        self.condition.release() # and now we unlock 

class Consumer:
    def __init__(self,prod):
        self.prod = prod

    def consume(self):
        print(f'Consumer launched {threading.current_thread().getName()}')
        self.prod.condition.acquire() # instint of chacking get the request
        self.prod.condition.wait(timeout=0) #timeout 0 means next thread does not have to wait any more
        self.prod.condition.release() #once done release 
        # while self.prod.order_praced == False: # it was with flag approach
        #     sleep(0.2)

        print(f'Order shipped for product {self.prod.products}')

print('################## Thread communication = API - wait and release #####')

prod = Producer()
consum = Consumer(prod)

tpr = Thread(target=prod.produce)
tcon = Thread(target=consum.consume)
tpr.start()
tcon.start()