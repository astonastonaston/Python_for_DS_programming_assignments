import csv

def write_columns(data,fname):
    """
    Input: Data and output file name\n
    Return: The list of first-n fib numbers
    """
    assert type(data)==list
    assert type(fname)==str
    for i in data:
        assert type(i) in [int, float]

    f = open(fname, 'w', newline ='')
    w = csv.writer(f, delimiter = ',')
    for data_value in data:
        # print([float("{:.2f}".format(data_value)), float("{:.2f}".format(data_value**2)), round((data_value+data_value**2)/3, 2)])
        w.writerows([["{:.2f}".format(data_value) , "{:.2f}".format(data_value**2), "{:.2f}".format((data_value+data_value**2)/3)]])
    f.close()



# def main():
#     data=[5,4,6,1,9,0,3,9,2,7,10,8,4,7,1,2,7,6,5,2,8,2,0,1,1,1,2,10,6,2]
#     fname = "hi.csv"
#     write_columns(data,fname)
#     return 0

# main()