from pyquery import PyQuery as pq
import pandas as pd


d = pq(filename='20160319RHIL0_edit.xml')

# from nominations
res = d('nomination')
nomID = [res.eq(i).attr('id') for i in range(len(res))]
horseName = [res.eq(i).attr('horse') for i in range(len(res))]

attrs = ('id', 'horse')
data = [[res.eq(i).attr(x) for x in attrs] for i in range(len(res))]

frames = pd.DataFrame(data)
print(frames)
