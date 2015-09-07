# Finding data from faculty.csv using regular expressions


import pandas as pd  # import pandas library

#  read_data reads a cvs file and puts it into a pandas dataframe
#  empty entries are recorded as na values


def read_data(data):
    df = pd.read_csv(data, na_values=[""])
    df.rename(columns= lambda x: x.strip(), inplace= True) #remove wspace
    df.fillna(value="n/a", inplace=True)
    return df


#  reads data into data frame, selects information you request
#  Cleans selection and returns dictrionary histogram of data

def num_degrees(data):
    df = read_data(data)
    req_l = []
    req_d = {}
    req_raw = df["title"]
    for row in req_raw:
        no_punc = row.replace(".", "")
        req_l.append(no_punc.split())
    flat_list = [item for sublist in req_l for item in sublist]
    for item in flat_list:
        req_d[item] = 1 + req_d.get(item, 0)
    return req_d


def num_titles(data):
    df = read_data(data)
    title_d = {}
    titles_raw = df['email'].tolist()
    for item in titles_raw:
        title = item.partition("of")[0]
        title_d[title] = 1 + title_d.get(title, 0)
    return title_d


def all_email(data):
    df = read_data(data)
    email_list = df['email'].tolist()
    return email_list


def all_domains(data):
    emails = all_email(data)
    domains = []
    for item in emails:
        dom = item.partition("@")[2]
        domains.append(dom)
    uniq_domains = set(domains)
    return uniq_domains
