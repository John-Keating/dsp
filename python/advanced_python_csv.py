# this function takes output from other functions and writes it as csv file

import pandas


def produce_csv(output, name):
    output.to_csv(name)
