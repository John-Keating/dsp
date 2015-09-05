# Finding data from faculty.csv using regular expressions


import pandas as pd  # import pandas library


def read_data(data):
    facultydf = pd.read_csv(data, na_values=[""])
    return facultydf


def number_freq(data, request):
    req_l = []
    req_d = {}
    req_raw = data[request]
    for row in req_raw:
        no_punc = row.replace(".", "")
        req_l.append(no_punc.split())
    flat_list = [item for sublist in req_l for item in sublist]
    for item in flat_list:
        req_d[item] = 1 + req_d.get(item, 0)
    return req_d
