# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

# Abrir la base de datos
#!pip install pyreadstat
#!pip install pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import pyreadstat


dtafile = "C:/Users/carlo/OneDrive - Universidad de los Andes/Barómetro de las Américas/2020/Muestra Nacional 2020/Dataset/App Web/Datos 2004 - 2018.csv"
df = pd.read_csv(dtafile,sep = "|")

#df.wt.value_counts()
df2 = df[['year','soct2']]


df['year'] = df['year'].astype('int')

cross_tab_prop = pd.crosstab(index = df['year'],columns = df['soct2'], normalize="index")

cross_tab_prop.plot(kind='bar', 
                    stacked=True, 
                    colormap='tab10', 
                    figsize=(10, 6))