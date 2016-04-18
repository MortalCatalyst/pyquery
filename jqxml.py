from pyquery import PyQuery as pq
import pandas as pd
import os
import sys

if len(sys.argv) == 2:
    print("no params")
    sys.exit(1)

dir = sys.argv[1]
mask = sys.argv[2]

files = os.listdir(dir)

fileResult = filter(lambda x: x.endswith(mask), files)

# d = pq(filename='20160319RHIL0_edit.xml')

for items in fileResult:
    d = pq(filename=items)
    res = d('nomination')
    attrs = ('id', 'horse')
    data = [[res.eq(i).attr(x) for x in attrs] for i in range(len(res))]

    # from nominations
# res = d('nomination')
# nomID = [res.eq(i).attr('id') for i in range(len(res))]
# horseName = [res.eq(i).attr('horse') for i in range(len(res))]

# attrs = ('id', 'horse')

frames = pd.DataFrame(data)
print(frames)
