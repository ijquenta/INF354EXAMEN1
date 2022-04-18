# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 00:28:56 2022

@author: Ivan-Dev
"""
import numpy as np
import pandas as pd

cancer = pd.read_csv("cancer.csv", sep=",")
#print(cancer)
#print(cancer.head)


print("--- Primer Cuartil --- \n"
      "Radio Prom.: ", np.percentile(cancer["radius_mean"], 25) , "\n"
      "Textura Prom.: ", np.percentile(cancer["texture_mean"], 25) , "\n"
      "Perimetro Prom.: ", np.percentile(cancer["perimeter_mean"], 25) , "\n"
      "Area Prom.: ", np.percentile(cancer["area_mean"], 25) , "\n"  
      )
print()

radi = round(cancer["radius_mean"].mean(),3)
text = round(cancer["texture_mean"].mean(),3)
peri = round(cancer["perimeter_mean"].mean(),3)
area = round(cancer["area_mean"].mean(),3)


print("--- Percentil 50 --- \n"
      "Radio Prom.: ", radi, "\n"
      "Textura Prom.: ", text, "\n"
      "Perimetro Prom.: ", peri, "\n"
      "Area Prom.: ", area, "\n"  
      )
print()
radi_de = round(cancer["radius_mean"].std(),3)
text_de = round(cancer["texture_mean"].std(),3)
peri_de = round(cancer["perimeter_mean"].std(),3)
area_de = round(cancer["area_mean"].std(),3)
print("--- Desviación estándar ---\n"
      "Radio Prom.: ", radi_de , "\n" 
      "Textura Prom: ", text_de , "\n" 
      "Perimetro Prom: ", peri_de , "\n" 
      "Perimetro Prom: ", area_de , "\n"
      )