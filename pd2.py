import pandas as pd

def add_month_yr(x):
    """
    Count the times that key words happen in the answers
    """
    assert type(x)==pd.DataFrame
    x.index = x["ID"]
    mn = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
    my = ["{}-{}".format(mn[int(j.split("/")[0])], j.split("/")[-1].split(" ")[0]) for j in x["Timestamp"]]
    x["month-yr"] = my
    return x




# def main():
#     a = pd.read_csv('survey_data.csv')
#     # print(a)
#     # print(a["Is there anything in particular you want to use Python for?"])
#     b = a["Is there anything in particular you want to use Python for?"]
#     # print(type(b))
#     # a.index = list(range(len(a)))
#     c = add_month_yr(a)
#     print(c)
#     return 0

# main()