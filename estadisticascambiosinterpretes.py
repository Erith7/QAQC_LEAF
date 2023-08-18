# %%
# imports
import numpy as np
import pandas as pd
import geopandas as gpd
import os
import fiona
from shapely import wkt
# %%
# Reading the datafile
fullfile = pd.read_csv("./Datos/ResultadosCambios_BSVAPM_22082023.csv")
print(fullfile.head(10))
fullfile['geometry'] = fullfile['geometry'].apply(wkt.loads)
gdf = gpd.GeoDataFrame(fullfile, crs="EPSG:4326")
gdf.drop(['plotid.1'], axis=1, inplace=True)
print(gdf.head(10))


# %%
# resumen de coincidencias de técnicos especialistas
print(gdf['Coincidencia0008'].value_counts())
# 1. Especialistas que no coinciden (CASO B)
casoB = gdf.loc[gdf['Coincidencia0008'] == 'B']
casoB1 = casoB[['plotid', 'email1', 'Coincidencia0008']]
casoB = gdf.loc[gdf['Coincidencia0812'] == 'B']
casoB2 = casoB[['plotid', 'email1', 'Coincidencia0812']]
casoB = gdf.loc[gdf['Coincidencia1213'] == 'B']
casoB3 = casoB[['plotid', 'email1', 'Coincidencia1213']]
casoB = gdf.loc[gdf['Coincidencia1314'] == 'B']
casoB4 = casoB[['plotid', 'email1', 'Coincidencia1314']]
casoB = gdf.loc[gdf['Coincidencia1415'] == 'B']
casoB5 = casoB[['plotid', 'email1', 'Coincidencia1415']]
casoB = gdf.loc[gdf['Coincidencia1516'] == 'B']
casoB6 = casoB[['plotid', 'email1', 'Coincidencia1516']]
casoB = gdf.loc[gdf['Coincidencia1617'] == 'B']
casoB7 = casoB[['plotid', 'email1', 'Coincidencia1617']]
casoB = gdf.loc[gdf['Coincidencia1718'] == 'B']
casoB8 = casoB[['plotid', 'email1', 'Coincidencia1718']]
casoB = gdf.loc[gdf['Coincidencia1819'] == 'B']
casoB9 = casoB[['plotid', 'email1', 'Coincidencia1819']]
casoB = gdf.loc[gdf['Coincidencia1920'] == 'B']
casoB10 = casoB[['plotid', 'email1', 'Coincidencia1920']]
casoB = gdf.loc[gdf['Coincidencia2021'] == 'B']
casoB11 = casoB[['plotid', 'email1', 'Coincidencia2021']]
casoB = gdf.loc[gdf['Coincidencia2122'] == 'B']
casoB12 = casoB[['plotid', 'email1', 'Coincidencia2122']]
#print(casoB1['email1'].value_counts())

fileB = casoB1.merge(casoB2, how='outer', on=['plotid', 'email1'])
fileB = fileB.merge(casoB3, how='outer', on=['plotid', 'email1'])
fileB = fileB.merge(casoB4, how='outer', on=['plotid', 'email1'])
fileB = fileB.merge(casoB5, how='outer', on=['plotid', 'email1'])
fileB = fileB.merge(casoB6, how='outer', on=['plotid', 'email1'])
fileB = fileB.merge(casoB7, how='outer', on=['plotid', 'email1'])
fileB = fileB.merge(casoB8, how='outer', on=['plotid', 'email1'])
fileB = fileB.merge(casoB9, how='outer', on=['plotid', 'email1'])
fileB = fileB.merge(casoB10, how='outer', on=['plotid', 'email1'])
fileB = fileB.merge(casoB11, how='outer', on=['plotid', 'email1'])
fileB = fileB.merge(casoB12, how='outer', on=['plotid', 'email1'])

# %%
# Resumen especialistas
fileB = fileB.fillna('0')
fileB = fileB.replace('B', '1')
fileB[['Coincidencia0008', 'Coincidencia0812', 'Coincidencia1213', 'Coincidencia1314', 'Coincidencia1415', 'Coincidencia1516', 'Coincidencia1617', 'Coincidencia1718', 'Coincidencia1819', 'Coincidencia1920', 'Coincidencia2021', 'Coincidencia2122']] = fileB[['Coincidencia0008', 'Coincidencia0812', 'Coincidencia1213', 'Coincidencia1314', 'Coincidencia1415', 'Coincidencia1516', 'Coincidencia1617', 'Coincidencia1718', 'Coincidencia1819', 'Coincidencia1920', 'Coincidencia2021', 'Coincidencia2122']].astype(str).astype(int)
print(fileB.dtypes)
fileB['Resumen'] = ''
fileB['Resumen'] = fileB['Coincidencia0008'] + fileB['Coincidencia0812'] + fileB['Coincidencia1213'] + fileB['Coincidencia1314'] + fileB['Coincidencia1415'] + fileB['Coincidencia1516'] + fileB['Coincidencia1617'] + fileB['Coincidencia1718'] + fileB['Coincidencia1819'] + fileB['Coincidencia1920'] + fileB['Coincidencia2021'] + fileB['Coincidencia2122']
fileB1 = fileB[['email1', 'Resumen']]
fileB2 = fileB1.groupby('email1')['Resumen'].sum()
# %%
# resumen de coincidencias de técnicos juniors 1
print(gdf['Coincidencia0008'].value_counts())
# 1. Juniors1 que no coinciden (CASO D)
casoD = gdf.loc[gdf['Coincidencia0008'] == 'D']
casoD1 = casoD[['plotid', 'email2', 'Coincidencia0008']]
casoD = gdf.loc[gdf['Coincidencia0812'] == 'D']
casoD2 = casoD[['plotid', 'email2', 'Coincidencia0812']]
casoD = gdf.loc[gdf['Coincidencia1213'] == 'D']
casoD3 = casoD[['plotid', 'email2', 'Coincidencia1213']]
casoD = gdf.loc[gdf['Coincidencia1314'] == 'D']
casoD4 = casoD[['plotid', 'email2', 'Coincidencia1314']]
casoD = gdf.loc[gdf['Coincidencia1415'] == 'D']
casoD5 = casoD[['plotid', 'email2', 'Coincidencia1415']]
casoD = gdf.loc[gdf['Coincidencia1516'] == 'D']
casoD6 = casoD[['plotid', 'email2', 'Coincidencia1516']]
casoD = gdf.loc[gdf['Coincidencia1617'] == 'D']
casoD7 = casoD[['plotid', 'email2', 'Coincidencia1617']]
casoD = gdf.loc[gdf['Coincidencia1718'] == 'D']
casoD8 = casoD[['plotid', 'email2', 'Coincidencia1718']]
casoD = gdf.loc[gdf['Coincidencia1819'] == 'D']
casoD9 = casoD[['plotid', 'email2', 'Coincidencia1819']]
casoD = gdf.loc[gdf['Coincidencia1920'] == 'D']
casoD10 = casoD[['plotid', 'email2', 'Coincidencia1920']]
casoD = gdf.loc[gdf['Coincidencia2021'] == 'D']
casoD11 = casoD[['plotid', 'email2', 'Coincidencia2021']]
casoD = gdf.loc[gdf['Coincidencia2122'] == 'D']
casoD12 = casoD[['plotid', 'email2', 'Coincidencia2122']]
#print(casoD1['email2'].value_counts())

fileD = casoD1.merge(casoD2, how='outer', on=['plotid', 'email2'])
fileD = fileD.merge(casoD3, how='outer', on=['plotid', 'email2'])
fileD = fileD.merge(casoD4, how='outer', on=['plotid', 'email2'])
fileD = fileD.merge(casoD5, how='outer', on=['plotid', 'email2'])
fileD = fileD.merge(casoD6, how='outer', on=['plotid', 'email2'])
fileD = fileD.merge(casoD7, how='outer', on=['plotid', 'email2'])
fileD = fileD.merge(casoD8, how='outer', on=['plotid', 'email2'])
fileD = fileD.merge(casoD9, how='outer', on=['plotid', 'email2'])
fileD = fileD.merge(casoD10, how='outer', on=['plotid', 'email2'])
fileD = fileD.merge(casoD11, how='outer', on=['plotid', 'email2'])
fileD = fileD.merge(casoD12, how='outer', on=['plotid', 'email2'])

# %%
# Resumen Junior1
fileD = fileD.fillna('0')
fileD = fileD.replace('D', '1')
fileD[['Coincidencia0008', 'Coincidencia0812', 'Coincidencia1213', 'Coincidencia1314', 'Coincidencia1415', 'Coincidencia1516', 'Coincidencia1617', 'Coincidencia1718', 'Coincidencia1819', 'Coincidencia1920', 'Coincidencia2021', 'Coincidencia2122']] = fileD[['Coincidencia0008', 'Coincidencia0812', 'Coincidencia1213', 'Coincidencia1314', 'Coincidencia1415', 'Coincidencia1516', 'Coincidencia1617', 'Coincidencia1718', 'Coincidencia1819', 'Coincidencia1920', 'Coincidencia2021', 'Coincidencia2122']].astype(str).astype(int)
print(fileD.dtypes)
fileD['Resumen'] = ''
fileD['Resumen'] = fileD['Coincidencia0008'] + fileD['Coincidencia0812'] + fileD['Coincidencia1213'] + fileD['Coincidencia1314'] + fileD['Coincidencia1415'] + fileD['Coincidencia1516'] + fileD['Coincidencia1617'] + fileD['Coincidencia1718'] + fileD['Coincidencia1819'] + fileD['Coincidencia1920'] + fileD['Coincidencia2021'] + fileD['Coincidencia2122']
fileD1 = fileD[['email2', 'Resumen']]
fileD2 = fileD1.groupby('email2')['Resumen'].sum()
# %%
# resumen de coincidencias de técnicos juniors 2
print(gdf['Coincidencia0008'].value_counts())
# 1. Juniors2 que no coinciden (CASO C)
casoC = gdf.loc[gdf['Coincidencia0008'] == 'C']
casoC1 = casoC[['plotid', 'email3', 'Coincidencia0008']]
casoC = gdf.loc[gdf['Coincidencia0812'] == 'C']
casoC2 = casoC[['plotid', 'email3', 'Coincidencia0812']]
casoC = gdf.loc[gdf['Coincidencia1213'] == 'C']
casoC3 = casoC[['plotid', 'email3', 'Coincidencia1213']]
casoC = gdf.loc[gdf['Coincidencia1314'] == 'C']
casoC4 = casoC[['plotid', 'email3', 'Coincidencia1314']]
casoC = gdf.loc[gdf['Coincidencia1415'] == 'C']
casoC5 = casoC[['plotid', 'email3', 'Coincidencia1415']]
casoC = gdf.loc[gdf['Coincidencia1516'] == 'C']
casoC6 = casoC[['plotid', 'email3', 'Coincidencia1516']]
casoC = gdf.loc[gdf['Coincidencia1617'] == 'C']
casoC7 = casoC[['plotid', 'email3', 'Coincidencia1617']]
casoC = gdf.loc[gdf['Coincidencia1718'] == 'C']
casoC8 = casoC[['plotid', 'email3', 'Coincidencia1718']]
casoC = gdf.loc[gdf['Coincidencia1819'] == 'C']
casoC9 = casoC[['plotid', 'email3', 'Coincidencia1819']]
casoC = gdf.loc[gdf['Coincidencia1920'] == 'C']
casoC10 = casoC[['plotid', 'email3', 'Coincidencia1920']]
casoC = gdf.loc[gdf['Coincidencia2021'] == 'C']
casoC11 = casoC[['plotid', 'email3', 'Coincidencia2021']]
casoC = gdf.loc[gdf['Coincidencia2122'] == 'C']
casoC12 = casoC[['plotid', 'email3', 'Coincidencia2122']]
#print(casoC1['email3'].value_counts())

fileC = casoC1.merge(casoC2, how='outer', on=['plotid', 'email3'])
fileC = fileC.merge(casoC3, how='outer', on=['plotid', 'email3'])
fileC = fileC.merge(casoC4, how='outer', on=['plotid', 'email3'])
fileC = fileC.merge(casoC5, how='outer', on=['plotid', 'email3'])
fileC = fileC.merge(casoC6, how='outer', on=['plotid', 'email3'])
fileC = fileC.merge(casoC7, how='outer', on=['plotid', 'email3'])
fileC = fileC.merge(casoC8, how='outer', on=['plotid', 'email3'])
fileC = fileC.merge(casoC9, how='outer', on=['plotid', 'email3'])
fileC = fileC.merge(casoC10, how='outer', on=['plotid', 'email3'])
fileC = fileC.merge(casoC11, how='outer', on=['plotid', 'email3'])
fileC = fileC.merge(casoC12, how='outer', on=['plotid', 'email3'])

# %%
# Resumen junior2
fileC = fileC.fillna('0')
fileC = fileC.replace('C', '1')
fileC[['Coincidencia0008', 'Coincidencia0812', 'Coincidencia1213', 'Coincidencia1314', 'Coincidencia1415', 'Coincidencia1516', 'Coincidencia1617', 'Coincidencia1718', 'Coincidencia1819', 'Coincidencia1920', 'Coincidencia2021', 'Coincidencia2122']] = fileC[['Coincidencia0008', 'Coincidencia0812', 'Coincidencia1213', 'Coincidencia1314', 'Coincidencia1415', 'Coincidencia1516', 'Coincidencia1617', 'Coincidencia1718', 'Coincidencia1819', 'Coincidencia1920', 'Coincidencia2021', 'Coincidencia2122']].astype(str).astype(int)
print(fileC.dtypes)
fileC['Resumen'] = ''
fileC['Resumen'] = fileC['Coincidencia0008'] + fileC['Coincidencia0812'] + fileC['Coincidencia1213'] + fileC['Coincidencia1314'] + fileC['Coincidencia1415'] + fileC['Coincidencia1516'] + fileC['Coincidencia1617'] + fileC['Coincidencia1718'] + fileC['Coincidencia1819'] + fileC['Coincidencia1920'] + fileC['Coincidencia2021'] + fileC['Coincidencia2122']
fileC1 = fileC[['email3', 'Resumen']]
fileC2 = fileC1.groupby('email3')['Resumen'].sum()