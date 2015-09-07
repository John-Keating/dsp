import pandas as pd
from operator import itemgetter


# Question6. Create a dictionary based on family name


def faculty_dict(data):
    dframe = pd.read_csv(data)
    dframe.rename(columns= lambda x: x.strip(), inplace= True)
    dframe["firstname"], dframe["lastname"] = zip(*dframe["name"].apply(lambda x: x.rsplit(" ", 1)))
    dframe["title"] = dframe["title"].str.rsplit(" ", 2)
    dframe["title"] = dframe["title"].apply(lambda x: x[0])
    dt = {x: g[["degree", "title", "email"]].values.tolist() for x,g in dframe.groupby("lastname")}
    return dt

print faculty_dict("faculty.csv").items()[:3]


# Question 7 With full name dictionary


def professor_dict(data):
    dframe = pd.read_csv(data)
    dframe.rename(columns= lambda x: x.strip(), inplace= True)
    dframe["name"] = dframe["name"].apply(lambda x: x.split(" "))
    dframe["firstname"] = dframe["name"].apply(lambda x: x[0])
    dframe["lastname"] = dframe["name"].apply(lambda x: x[len(x)-1])
    dframe.name = zip(dframe.firstname, dframe.lastname)
    prof_d = {x: g[["degree", "title", "email"]].values.tolist() for x,g in dframe.groupby("name")}
    return prof_d


print professor_dict("faculty.csv").items()[:3]


# Question 8 sort the dictionary by last name

x = professor_dict("faculty.csv")

s = sorted(x.items(), key=lambda (k,v): (k[1], k[0]))

print s[:3]
