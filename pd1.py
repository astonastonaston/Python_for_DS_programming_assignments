import pandas as pd

def split_count(x):
    """
    Count the times that key words happen in the answers
    """
    assert type(x)==pd.core.series.Series
    cnt = {}
    for i in x:
        for j in i.split(", "):
            cnt[j] = cnt.get(j, 0) + 1
    df1 = pd.DataFrame(data=cnt, index=["count"])
    df1 = df1.T
    df1 = df1.sort_values(by=['count'])
    return df1




# def main():
#     a = pd.read_csv('survey_data.csv')
#     # print(a)
#     # print(a["Is there anything in particular you want to use Python for?"])
#     b = a["Is there anything in particular you want to use Python for?"]
#     # print(type(b))
#     c = split_count(b)
#     print(c)
#     return 0

# main()