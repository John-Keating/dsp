# this function takes output from other functions and writes it as csv file

import pandas


def all_email(data):
    df = read_data(data)
    email_list = df['email'].tolist()
    return set(email_list)


def produce_csv(output, name):
    pd.Series(output).to_csv(name, index=False)

emails = all_email("faculty.csv")

produce_csv(emails, "emails.csv")
