# The football.csv file contains the results from the English Premier League.
# The columns labeled Goals and Goals Allowed contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in for and against goals.


import csv


def min_team(data):
    team_results = csv.DictReader(open(data, 'rb'))
    mindiff = None
    team_name = None
    for line in team_results:
        diff = abs(int(line['Goals']) - int(line['Goals Allowed']))
        if mindiff == None or mindiff < diff:
            mindiff = diff
            team_name = line['Team']
    return team_name
