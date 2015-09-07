# this function takes output from other functions and writes it as csv file

import pandas as pd

def read_data(data):
    df = pd.read_csv(data, na_values=[""])
    df.rename(columns= lambda x: x.strip(), inplace= True) #remove wspace
    df.fillna(value="n/a", inplace=True)
    return df

def all_email(data):
    df = read_data(data)
    email_list = df['email'].tolist()
    return email_list


def produce_csv(output, name):
    pd.Series(output).to_csv(name, index=False)

emails = all_email("faculty.csv")

produce_csv(emails, "emails.csv")
