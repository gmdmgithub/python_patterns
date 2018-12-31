from threading import Thread
from time import sleep
import threading

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

print('################## Thread communication = flag way #####')

prod = Producer()
consum = Consumer(prod)

tpr = Thread(target=prod.produce)
tcon = Thread(target=consum.consume)
tpr.start()
tcon.start()