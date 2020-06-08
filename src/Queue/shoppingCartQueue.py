import threading
import time

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

food_order_queue = Queue()

def placeOrders(orders):
    for order in orders:
        print("Placing order for:",order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)


def deliverOrders():
    time.sleep(1)
    while True:
        order = food_order_queue.dequeue()
        print("Now Delivering: ",order)
        time.sleep(2)

if __name__ == '__main__':
    orders = ['shirt','coolers','TV','Perform','closet']
    th1 = threading.Thread(target=placeOrders, args=(orders,))
    th2 = threading.Thread(target=deliverOrders)

    th1.start()
    th2.start()