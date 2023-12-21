# fill out the necessary methods shown below and add others if need be.

class Interval(object):
    def __init__(self,a,b):
        """
        :a: integer
        :b: integer
        """
        assert a<b
        assert isinstance(a,int)
        assert isinstance(b,int)
        self._a = a
        self._b = b
    def __repr__(self):
        return "interval ({},{})".format(self._a, self._b)
    def __eq__(self,other):
        return ((self._a==other._a) & (self._b==other._b))
    def __lt__(self,other):
        return (self._b<=other._a)
    def __gt__(self,other):
        return (other._b<=self._a)
    def __ge__(self,other):
        return ((other._b<=self._a) or (self.__eq__(other)))
    def __le__(self,other):
        return ((self._b<=other._a) or (self.__eq__(other)))
    def __overlap(self, i1l, i1r, i2l, i2r):
        return (not ((i2l >= i1r) or (i1l >= i2r)))
    def __add__(self,other):
        sa, sb, oa, ob = self._a, self._b, other._a, other._b
        if self.__overlap(sa, sb, oa, ob):
            return Interval(min(sa, sb, oa, ob), max(sa, sb, oa, ob))
        else:
            return [self, other]
        

# def main():
#     a = Interval(2,3) 
#     b = Interval(1,2) 
#     c = Interval(2,3) 
#     d=a+b
#     print(d, type(d))  
#     print(a==b, a==c)  
#     # b+c 
#     return 0

# main()