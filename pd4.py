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

def count_month_yr(x):
    """
    Count the times that key words happen in the answers
    """
    assert type(x)==pd.DataFrame
    return x.groupby("month-yr").agg("count").loc[:, ["Timestamp"]]

def fix_categorical(x):
    """
    Enumerate categorial type for indexing
    """
    assert type(x)==pd.DataFrame
    print(x)
    t = pd.CategoricalDtype(categories=["Sep-2017", "Jan-2018", "Feb-2018", "Mar-2018", "Apr-2018", "Sep-2018", "Oct-2018", "Jan-2019"], ordered=True)
    x["month-yr"] = x["month-yr"].astype(t)
    # x.index = x.index.astype(t)
    # x = x.sort_index() 
    x = x.sort_values(by=["month-yr"])
    # print(x["month-yr"], type(x), x.index)
    return x


# def fix_categorical(x):
#     """
#     Enumerate categorial type for indexing
#     """
#     assert type(x)==pd.DataFrame
#     x = x.groupby("month-yr").agg("count").loc[:, ["Timestamp"]]
#     t = pd.CategoricalDtype(categories=["Sep-2017", "Jan-2018", "Feb-2018", "Mar-2018", "Apr-2018", "Sep-2018", "Oct-2018", "Jan-2019"], ordered=True)
#     x.index = x.index.astype(t)
#     x = x.sort_index() 
#     print(x, type(x), x.index)
#     return x


# def main():
#     a = pd.read_csv('survey_data.csv')
#     # print(a)
#     # print(a["Is there anything in particular you want to use Python for?"])
#     # b = a["Is there anything in particular you want to use Python for?"]
#     # print(type(b))
#     # a.index = list(range(len(a)))
#     # c = add_month_yr(a)
#     # d = count_month_yr(c)
#     e = fix_categorical(add_month_yr(a))
#     # print(e)
#     # print(d.index)


#     return 0

# main()