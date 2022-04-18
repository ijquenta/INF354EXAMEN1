# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 00:30:26 2022

@author: Ivan-Dev
"""


import pandas as pd
import matplotlib.pyplot as plt

cancer = pd.read_csv("cancer.csv", sep=",")

pd.options.display.max_rows = 100
print('Conjunto de datos de Wisconsin (diagnóstico) de cáncer de mama'.center(50,' '))
print(cancer['diagnosis'][:100])

x_values = cancer['radius_mean'] 
y_values = cancer['radius_worst']


plt.bar(x_values, y_values)
plt.xlim(0, 35)
plt.ylim(0, 40)
plt.title('Conjunto de datos de Wisconsin (diagnóstico) de cáncer de mama')
plt.xlabel('Radio Promedio del cáncer de mama')
plt.ylabel("Radio Peor del cáncer de mama")
plt.show()


x_values = cancer['texture_mean'] 
y_values = cancer['texture_worst']


plt.bar(x_values, y_values)
plt.xlim(0, 45)
plt.ylim(0, 55)
plt.title('Conjunto de datos de Wisconsin (diagnóstico) de cáncer de mama')
plt.xlabel('Textura Promedio del cáncer de mama')
plt.ylabel("Textura Peor del cáncer de mama")
plt.show()

x_values = cancer['perimeter_mean'] 
y_values = cancer['perimeter_worst']


plt.bar(x_values, y_values)
plt.xlim(40, 200)
plt.ylim(0, 270)
plt.title('Conjunto de datos de Wisconsin (diagnóstico) de cáncer de mama')
plt.xlabel('Perimetro Promedio del cáncer de mama')
plt.ylabel("Perimetro Peor del cáncer de mama")
plt.show()

x_values = cancer['area_mean'] 
y_values = cancer['area_worst']


plt.bar(x_values, y_values)
plt.xlim(140, 200)
plt.ylim(0, 300)
plt.title('Conjunto de datos de Wisconsin (diagnóstico) de cáncer de mama')
plt.xlabel('Area Promedio del cáncer de mama')
plt.ylabel("Area Peor del cáncer de mama")
plt.show()



