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
print(fileList.files)

data = []
frames = pd.DataFrame([])

attrs = ('id', 'horse')

for items in fileList.files:
    d = pq(filename=items)
    res = d('nomination')
    dataSets = [[res.eq(i).attr(x)
                 for x in attrs] for i in range(len(res))]
    print(dataSets)
    aDF = pd.DataFrame(dataSets)
    frames = frames.append(aDF)


print(frames)
