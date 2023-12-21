from time import sleep
import random
from datetime import datetime
import itertools as it

def producer():
    'produce timestamps'
    starttime = datetime.now()
    while True:
        sleep(random.uniform(0,0.2))
        yield datetime.now()-starttime

class tracker():
    """
    Class for tracking the outputs of p
    """
    def __init__(self, p, limit=2):
        """
        initialize producer under tracking
        """
        self.p = p
        self.limit = limit
        self.oddCnt = 0
    def __iter__(self):
        """
        iterating to next element (assign some initial values for self) (convert to iterator)
        """
        # iter赋初始值，其后next先储值后更新，返回储的值
        return self
    def __next__(self):
        """
        next iterator
        """
        if (next(self.p).seconds % 2 == 1):
            self.oddCnt += 1
        if (self.oddCnt > self.limit):
            raise StopIteration
        return self.oddCnt
    def send(self, nwlim):
        """
        send new limit
        """
        assert nwlim >= self.oddCnt
        self.limit = nwlim
        return self.__next__()


# def tracker(p, limit=2):
#     """Track producer for timestamps"""
#     p = producer()
#     oddCnt = 0
#     while True:
#         a = next(p)
#         if (a.seconds%2==1):
#             oddCnt += 1
#         if (oddCnt > limit):
#             break
#         yield oddCnt 

# def main():
#     p = producer()
#     t = tracker(p, limit=2)
#     print(next(t))
#     print(list(t))


#     return 0

# main()