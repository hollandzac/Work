#!/usr/bin/env python3
import numpy as np
import openpyxl as xl
from datetime import datetime
from collections import defaultdict
t=0
workb = xl.load_workbook('ClimateData.xlsx')
sheet = workb['Sheet1']
miny = datetime(1900,1,1)
maxy = datetime(2000,1,1)
london = dict(list)

for row in sheet.iter_rows(min_row=2):
    city = row[3].value
    temp = row[1].value
    year = row[0].value.year
    if 1900<=year<=2000:
        if city == 'London':
            london[year]+=temp
        elif city == 'Sydney':
            sydney[year].append(temp)
        elif city == 'Jakarta':
            jakarta[year].append(temp)
        elif city == 'New York':
            newyork[year].append(temp)
for i in sydney:
    sydney[i] = np.mean(sydney[i])
    print(sydney(i))
