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
def square_root_rational(x, abs_tol=Rational(1, 1000)):
    """compute sqrt of rational numbers"""
    assert (type(x)==Rational)
    assert (type(abs_tol)==Rational)
    assert (x>Rational(0, 1))
    # Check if x is negative
    if x < Rational(0, 1):
        raise ValueError("Cannot compute square root of a negative number")

    # Special case for the square root of 0
    if x == Rational(0, 1):
        return Rational(0, 1)

    # Set initial bounds for bisection
    low_bound = Rational(0, 1)
    high_bound = x if x > Rational(1, 1) else Rational(1, 1)

    while True:
        # Bisection to find the square root within the specified tolerance
        mid_point = (low_bound + high_bound) / Rational(2, 1)
        error = mid_point * mid_point - x
        if (error < 0):
            error = Rational(-1, 1) * error

        if error < abs_tol:
            return mid_point
        elif mid_point * mid_point < x:
            low_bound = mid_point
        else:
            high_bound = mid_point

# # Example usage:
# result = square_root_rational(Rational(1112, 3), abs_tol=Rational(1, 1000))
# print(result)

# Using your Rational class for representing rational numbers, write a function square_root_rational which takes an input rational number x and returns the square root of x to absolute precision abs_tol. Your function should return a Rational number instance as output. Here is an example,

# >>> square_root_rational(Rational(1112,3),abs_tol=Rational(1,1000)) # output is `Rational` instance
#  10093849/524288
 

# Here is your function signature: square_root_rational(x,abs_tol=Rational(1,1000)).

# Hint: Use the bisection algorithm to compute the square root.

# Hint There are infinite solutions within a given error tolerance because rational numbers are dense i.e, you can always find a rational number arbitrarily close to a real number. Also, we use abs(estimate - sqrt(x)) to measure the error because sqrt(x) is what you are estimating.
# Please put your Python code in a Python script file and upload it. Please retain your submitted source files! Remember to use all the best practices we discussed in class. You can use any module in the Python standard library, but third-party modules (e.g., Numpy, Pandas) are restricted to those explicitly mentioned in the problem description.
# Tips:
# After you have submitted your file, do not use the browser back or reload buttons to navigate or open the page in multiple browser tabs, as this may cause your attempts to decrease unexpectedly. It may take up to thirty seconds for your code to be processed, so please be patient.
# If you find yourself back at the main page without any feedback or change in your attempts then it means that your code timed out or crashed in some unexpected way.
# Ensure that your development environment does not presume the existence of certain packages for the autograder. The autograder does not have anything other than the standard library and those third-party libraries explicitly named in the problem description.
# Do not leave extraneous statements in your code like test cases, print statements, or anything else besides what is needed to evaluate your submission because the the autograder will spend its limited time executing those lines, which may result in unexpected crashes or timeouts.