#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sqlite3 as sql

connection = sql.connect('climate.db')
cursor = connection.cursor()

cursor.execute('SELECT Year FROM ClimateData ')
year = cursor.fetchall()

cursor.execute('SELECT CO2 FROM ClimateData ')
co2 = cursor.fetchall()

cursor.execute('SELECT Temperature FROM ClimateData ')
temp = cursor.fetchall()


plt.subplot(211)
plt.plot(year,co2, '--b')
plt.title('Climate')
plt.xlabel('Year')
plt.ylabel('CO2')
plt.subplot(212)
plt.plot(year,temp, '--r')
plt.xlabel('Year')
plt.ylabel('Temp')
plt.show()

print(year,co2,temp)



#
