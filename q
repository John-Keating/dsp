# Finding data from faculty.csv using regular expressions


import pandas as pd  # import pandas library
import string


def read_data(data):
    facultydf = pd.read_csv(data)
    return facultydf


def number_freq(data, request):
    req_list = []
    req_dict = {}
    req_raw = data[request]
    for row in req_raw:
        no_punc = row.replace(".", "")
        req_list.append(no_punc.split())
    flat_list = [item for sublist in req_list
    return req_list
