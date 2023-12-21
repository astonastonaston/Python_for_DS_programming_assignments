import calendar
import datetime

def number_of_days(year,month):
    """
    Input: Data and output file name\n
    Return: The list of first-n fib numbers
    """
    assert month<13
    assert month>0
    assert year>0
    return calendar.monthrange(year, month)[1]

def number_of_leap_years(year1,year2):
    """
    Input: Data and output file name\n
    Return: The list of first-n fib numbers
    """
    assert year1>0
    assert year2>0
    year1, year2 = min(year1, year2), max(year2, year1)
    n = (year2//4) - (year1//4)
    if (year1%4==0):
        n += 1
    return n


def get_day_of_week(year,month,day):
    """
    Input: Data and output file name\n
    Return: The list of first-n fib numbers
    """
    assert day<=number_of_days(year,month)
    assert day>0
    assert month>0
    assert month<13
    assert year>0
    dt = datetime.date(year, month, day)
    x = dt.weekday()
    d = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
    return d[x]


# def main():
#     print(number_of_days(2017, 12))
#     print(number_of_leap_years(2020, 2029))
#     print(get_day_of_week(1970,12,29))
#     return 0

# main()