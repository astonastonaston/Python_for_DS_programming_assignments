class Rational:
    """Ratio of integers' class"""
    def __init__(self, numerator, denominator):
        """Keep the divisive rational numbers"""
        assert ((type(numerator)==int) and (type(denominator)==int))
        common = self._gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common

    def _gcd(self, a, b):
        """GCD helper"""
        while b:
            a, b = b, a % b
        return a

    def __repr__(self):
        """print out the ration numbers"""
        if self.denominator!=1:
            return f'{self.numerator}/{self.denominator}'
        else:
            return f'{self.numerator}'

    def __neg__(self):
        """judging not equal statement"""
        return Rational(-self.numerator, self.denominator)

    def __float__(self):
        """defining the way to convert to float"""
        return float(self.numerator) / float(self.denominator)

    def __int__(self):
        """defining the way to convert to int"""
        return self.numerator // self.denominator

    def __eq__(self, other):
        """defining the way to judge equation"""
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        """defining the way to judge less than or equal to some number"""
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __add__(self, other):
        """defining the way to add two rational numbers"""
        common_denominator = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        return Rational(new_numerator, common_denominator)

    def __mul__(self, other):
        """defining the way to multiply two rational numbers"""
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __sub__(self, other):
        """defining the way to subtract two rational numbers"""
        return Rational(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator
        )

    def __truediv__(self, other):
        """defining the way to divide two rational numbers"""
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
        elif isinstance(other, (int, float)):
            return Rational(self.numerator, self.denominator) / Rational(other, 1)

    def __rtruediv__(self, other):
        """defining the way to divide two rational numbers"""
        return Rational(other, 1) / self

# # Additional code to test the class
# r = Rational(3, 4)
# print(repr(r))
# print(-1 / r)
# print(float(-1 / r))
# print(int(r))
# print(int(Rational(10, 3)))
# print(Rational(10, 3) * Rational(101, 8) - Rational(11, 8))
# print(sorted([Rational(10, 3), Rational(9, 8), Rational(10, 1), Rational(1, 100)]))
# print(Rational(100, 10))
# print(-Rational(12345, 128191) + Rational(101, 103) * 30 / 44)
