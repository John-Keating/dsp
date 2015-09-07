# Finding data from faculty.csv using regular expressions


import pandas as pd  # import pandas library


#  read_data reads a cvs file and puts it into a pandas dataframe
#  empty entries are recorded as na values


def read_data(data):
    df = pd.read_csv(data, na_values=[""])
    df.rename(columns= lambda x: x.strip(), inplace= True) #remove wspace
    df.fillna(value="n/a", inplace=True)
    return df



def num_degrees(data):
    df = read_data(data)
    deg_l = []
    deg_d = {}
    deg_raw = df["degree"]
    for row in deg_raw:
        no_punc = row.replace(".", "")
        deg_l.append(no_punc.split())
    flat_list = [item for sublist in deg_l for item in sublist]
    for item in flat_list:
        deg_d[item] = 1 + deg_d.get(item, 0)
    deg_frame = pd.DataFrame(deg_d.items(), columns=["degree", "frequency"])
    return deg_frame.sort("frequency", ascending=False).reset_index()


print num_degrees("faculty.csv")


def num_titles(data):
    df = read_data(data)
    title_d = {}
    titles_raw = df["title"].tolist()
    for item in titles_raw:
        title = item.partition(" of ")[0]
        title_d[title] = 1 + title_d.get(title, 0)
    title_frame = pd.DataFrame(title_d.items(), columns=["title", "frequency"])
    return title_frame.sort("frequency", ascending=False)


print num_titles("faculty.csv)


def all_email(data):
    df = read_data(data)
    email_list = df['email'].tolist()
    return email_list


len(all_email("faculty.csv))


def all_domains(data):
    emails = all_email(data)
    domains = []
    for item in emails:
        dom = item.partition("@")[2]
        domains.append(dom)
    uniq_domains = set(domains)
    return uniq_domains


print len(all_domains("faculty.csv"))
