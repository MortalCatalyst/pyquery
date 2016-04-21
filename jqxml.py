from pyquery import PyQuery as pq
import pandas as pd
import argparse
# from glob import glob


parser = argparse.ArgumentParser(description=None)


def GetArgs(parser):
    """Parser function using argparse"""
    # parser.add_argument('directory', help='directory use',
    #                     action='store', nargs='*')
    parser.add_argument("files", nargs="+")
    return parser.parse_args()

fileList = GetArgs(parser)
# print(fileList.files)

data = []


horseattrs = ('id', 'horse', 'number', 'finished', 'age', 'sex', 'blinkers',
              'trainernumber', 'career', 'thistrack', 'firstup',
              'secondup', 'variedweight', 'weight', 'pricestarting')
meetattrs = ('id', 'venue', 'date', 'rail', 'weather', 'trackcondition')
raceattrs = ('id', 'number', 'shortname', 'stage', 'distance', 'grade',
             'age', 'weightcondition', 'fastesttime', 'sectionaltime')
clubattrs = ('code')

frames = pd.DataFrame([])

for items in fileList.files:
    d = pq(filename=items)
    meet = d('meeting')
    club = d('club')
    race = d('race')
    res = d('nomination')
    resdata = [[res.eq(i).attr(x)
                for x in horseattrs] for i in range(len(res))]
    # print(dataSets)
    meetdata = [[meet.eq(i).attr(x)
                 for x in meetattrs] for i in range(len(meet))]
    racedata = [[race.eq(i).attr(x)
                 for x in raceattrs] for i in range(len(race))]
    clubdata = [[club.eq(i).attr(x)
                 for x in clubattrs] for i in range(len(club))]
    raceid = [row[0] for row in racedata]
    # L = [x + [0] for x in L]
    print(resdata)
    # resdata = [raceid[i] for i in raceid  x + i for x in resdata]

    # for number of classes equalling nomination in the each category of
    # race inset raceid into resdata
    #
    print(resdata)
    clubdf = pd.DataFrame(clubdata)
    meetdf = pd.DataFrame(meetdata)
    racedf = pd.DataFrame(racedata)
    resdf = pd.DataFrame(resdata)
    frames = frames.append(clubdf)
    frames = frames.append(meetdf)
    frames = frames.append(racedf)
    frames = frames.append(resdf)

# print(frames)
# frames.to_csv('~/testingFrame3.csv', encoding='utf-8')
