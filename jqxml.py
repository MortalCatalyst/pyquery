from pyquery import PyQuery as pq
import pandas as pd

d = pq(filename='20160319RHIL0_edit.xml')

# from nominations
res = d('nomination')
nomID = [res.eq(i).attr('id') for i in range(len(res))]
horseName = [res.eq(i).attr('horse') for i in range(len(res))]

aList = []


def inputs(args):
    '''function to get elements matching criteria'''
    optsList = ['id', 'horse']
    for item in res:
        for attrs in optsList:
            if res.attr(attrs) in item:
                aList.append([res.eq(i).attr(attrs) for i in range(len(res))])

# print(aList)

zipped = list(zip(aList))

frames = pd.DataFrame(zipped)
print(frames)
