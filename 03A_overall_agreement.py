# %%
# imports
import pandas as pd
import os
import geopandas as gpd
import numpy as np
from functions import annual_data_extraction
from functions import set_order
from functions import set_order2
from functions import conversion
from functions import nan_filler
from functions import nan_filler2
from functions import nan_fillerB
from functions import rellenado
from itertools import cycle

# %% Reading data
# Reading the datafile
fullfile2 = pd.read_csv("./MAATE2023/Resultados2/10_NBE/ResultadosCambios_NBE_11042024.csv")
print("Tamaño del archivo general:", fullfile2.shape)
fullfile2.dropna()
fullfile = fullfile2.copy()
print("Tamaño del archivo sin NPs:", fullfile.shape)
# %% Parameters Settings
email = 'email3'
ruta_folder = './MAATE2023/Resultados2/10_NBE/OverallAgreement/'
folder = email
ruta_salida = os.path.join(ruta_folder, folder)

#%% Cambios al 2008
ordenado = conversion(fullfile, email=email, coincidence='Coincidencia0008')
result2008 = annual_data_extraction(ordenado, email=email, coincidence='Coincidencia0008')
archivo_actual = 'resultados2008Paso1.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
result2008.to_csv(ruta_ajustada)
print('The file '+archivo_actual+' has been saved!')
df2008 = pd.read_csv(ruta_ajustada)
print('dataframe out of function:', df2008.columns)
df2008 = set_order(df2008, coincidence='Coincidencia0008')
df2008 = nan_fillerB(df2008, email=email, coincidence='Coincidencia0008', count='count')
df2008 = nan_filler2(df2008, email=email)
archivo_actual = 'resultados2008.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
df2008.to_csv(ruta_ajustada)
print("El siguiente archivo ha sido guardado:", archivo_actual)
#%% Cambios al 2012
ordenado = conversion(fullfile, email=email, coincidence='Coincidencia0812')
result2012 = annual_data_extraction(ordenado, email=email, coincidence='Coincidencia0812')
archivo_actual = 'resultados2012Paso1.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
result2012.to_csv(ruta_ajustada)
print('The file '+archivo_actual+' has been saved!')
df2012 = pd.read_csv(ruta_ajustada)
print('dataframe out of function:', df2012.columns)
df2012 = set_order(df2012, coincidence='Coincidencia0812')
df2012 = nan_fillerB(df2012, email=email, coincidence='Coincidencia0812', count='count')
df2012 = nan_filler2(df2012, email=email)
archivo_actual = 'resultados2012.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
df2012.to_csv(ruta_ajustada)
print("El siguiente archivo ha sido guardado:", archivo_actual)
#%% Cambios al 2013
ordenado = conversion(fullfile, email=email, coincidence='Coincidencia1213')
result2013 = annual_data_extraction(ordenado, email=email, coincidence='Coincidencia1213')
archivo_actual = 'resultados2013Paso1.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
result2013.to_csv(ruta_ajustada)
print('The file '+archivo_actual+' has been saved!')
df2013 = pd.read_csv(ruta_ajustada)
print('dataframe out of function:', df2013.columns)
df2013 = set_order(df2013, coincidence='Coincidencia1213')
df2013 = nan_fillerB(df2013, email=email, coincidence='Coincidencia1213', count='count')
df2013 = nan_filler2(df2013, email=email)
archivo_actual = 'resultados2013.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
df2013.to_csv(ruta_ajustada)
print("El siguiente archivo ha sido guardado:", archivo_actual)
#%% Cambios al 2014
ordenado = conversion(fullfile, email=email, coincidence='Coincidencia1314')
result2014 = annual_data_extraction(ordenado, email=email, coincidence='Coincidencia1314')
archivo_actual = 'resultados2014Paso1.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
result2014.to_csv(ruta_ajustada)
print('The file '+archivo_actual+' has been saved!')
df2014 = pd.read_csv(ruta_ajustada)
print('dataframe out of function:', df2014.columns)
df2014 = set_order(df2014, coincidence='Coincidencia1314')
df2014 = nan_fillerB(df2014, email=email, coincidence='Coincidencia1314', count='count')
df2014 = nan_filler2(df2014, email=email)
archivo_actual = 'resultados2014.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
df2014.to_csv(ruta_ajustada)
print("El siguiente archivo ha sido guardado:", archivo_actual)
#%% Cambios al 2015
ordenado = conversion(fullfile, email=email, coincidence='Coincidencia1415')
result2015 = annual_data_extraction(ordenado, email=email, coincidence='Coincidencia1415')
archivo_actual = 'resultados2015Paso1.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
result2015.to_csv(ruta_ajustada)
print('The file '+archivo_actual+' has been saved!')
df2015 = pd.read_csv(ruta_ajustada)
print('dataframe out of function:', df2015.columns)
df2015 = set_order(df2015, coincidence='Coincidencia1415')
df2015 = nan_fillerB(df2015, email=email, coincidence='Coincidencia1415', count='count')
df2015 = nan_filler2(df2015, email=email)
archivo_actual = 'resultados2015.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
df2015.to_csv(ruta_ajustada)
print("El siguiente archivo ha sido guardado:", archivo_actual)
#%% Cambios al 2016
ordenado = conversion(fullfile, email=email, coincidence='Coincidencia1516')
result2016 = annual_data_extraction(ordenado, email=email, coincidence='Coincidencia1516')
archivo_actual = 'resultados2016Paso1.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
result2016.to_csv(ruta_ajustada)
print('The file '+archivo_actual+' has been saved!')
df2016 = pd.read_csv(ruta_ajustada)
print('dataframe out of function:', df2016.columns)
df2016 = set_order(df2016, coincidence='Coincidencia1516')
df2016 = nan_fillerB(df2016, email=email, coincidence='Coincidencia1516', count='count')
df2016 = nan_filler2(df2016, email=email)
archivo_actual = 'resultados2016.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
df2016.to_csv(ruta_ajustada)
print("El siguiente archivo ha sido guardado:", archivo_actual)
#%% Cambios al 2017
ordenado = conversion(fullfile, email=email, coincidence='Coincidencia1617')
result2017 = annual_data_extraction(ordenado, email=email, coincidence='Coincidencia1617')
archivo_actual = 'resultados2017Paso1.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
result2017.to_csv(ruta_ajustada)
print('The file '+archivo_actual+' has been saved!')
df2017 = pd.read_csv(ruta_ajustada)
print('dataframe out of function:', df2017.columns)
df2017 = set_order(df2017, coincidence='Coincidencia1617')
df2017 = nan_fillerB(df2017, email=email, coincidence='Coincidencia1617', count='count')
df2017 = nan_filler2(df2017, email=email)
archivo_actual = 'resultados2017.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
df2017.to_csv(ruta_ajustada)
print("El siguiente archivo ha sido guardado:", archivo_actual)
#%% Cambios al 2018
ordenado = conversion(fullfile, email=email, coincidence='Coincidencia1718')
result2018 = annual_data_extraction(ordenado, email=email, coincidence='Coincidencia1718')
archivo_actual = 'resultados2018Paso1.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
result2018.to_csv(ruta_ajustada)
print('The file '+archivo_actual+' has been saved!')
df2018 = pd.read_csv(ruta_ajustada)
print('dataframe out of function:', df2018.columns)
df2018 = set_order(df2018, coincidence='Coincidencia1718')
df2018 = nan_fillerB(df2018, email=email, coincidence='Coincidencia1718', count='count')
df2018 = nan_filler2(df2018, email=email)
archivo_actual = 'resultados2018.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
df2018.to_csv(ruta_ajustada)
print("El siguiente archivo ha sido guardado:", archivo_actual)
#%% Cambios al 2019
ordenado = conversion(fullfile, email=email, coincidence='Coincidencia1819')
result2019 = annual_data_extraction(ordenado, email=email, coincidence='Coincidencia1819')
archivo_actual = 'resultados2019Paso1.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
result2019.to_csv(ruta_ajustada)
print('The file '+archivo_actual+' has been saved!')
df2019 = pd.read_csv(ruta_ajustada)
print('dataframe out of function:', df2019.columns)
df2019 = set_order(df2019, coincidence='Coincidencia1819')
df2019 = nan_fillerB(df2019, email=email, coincidence='Coincidencia1819', count='count')
df2019 = nan_filler2(df2019, email=email)
archivo_actual = 'resultados2019.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
df2019.to_csv(ruta_ajustada)
print("El siguiente archivo ha sido guardado:", archivo_actual)
#%% Cambios al 2020
ordenado = conversion(fullfile, email=email, coincidence='Coincidencia1920')
result2020 = annual_data_extraction(ordenado, email=email, coincidence='Coincidencia1920')
archivo_actual = 'resultados2020Paso1.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
result2020.to_csv(ruta_ajustada)
print('The file '+archivo_actual+' has been saved!')
df2020 = pd.read_csv(ruta_ajustada)
print('dataframe out of function:', df2020.columns)
df2020 = set_order(df2020, coincidence='Coincidencia1920')
df2020 = nan_fillerB(df2020, email=email, coincidence='Coincidencia1920', count='count')
df2020 = nan_filler2(df2020, email=email)
archivo_actual = 'resultados2020.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
df2020.to_csv(ruta_ajustada)
print("El siguiente archivo ha sido guardado:", archivo_actual)
#%% Cambios al 2021
ordenado = conversion(fullfile, email=email, coincidence='Coincidencia2021')
result2021 = annual_data_extraction(ordenado, email=email, coincidence='Coincidencia2021')
archivo_actual = 'resultados2021Paso1.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
result2021.to_csv(ruta_ajustada)
print('The file '+archivo_actual+' has been saved!')
df2021 = pd.read_csv(ruta_ajustada)
print('dataframe out of function:', df2021.columns)
df2021 = set_order(df2021, coincidence='Coincidencia2021')
df2021 = nan_fillerB(df2021, email=email, coincidence='Coincidencia2021', count='count')
df2021 = nan_filler2(df2021, email=email)
archivo_actual = 'resultados2021.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
df2021.to_csv(ruta_ajustada)
print("El siguiente archivo ha sido guardado:", archivo_actual)
#%% Cambios al 2022
ordenado = conversion(fullfile, email=email, coincidence='Coincidencia2122')
result2022 = annual_data_extraction(ordenado, email=email, coincidence='Coincidencia2122')
archivo_actual = 'resultados2022Paso1.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
result2022.to_csv(ruta_ajustada)
print('The file '+archivo_actual+' has been saved!')
df2022 = pd.read_csv(ruta_ajustada)
print('dataframe out of function:', df2022.columns)
df2022 = set_order(df2022, coincidence='Coincidencia2122')
df2022 = nan_fillerB(df2022, email=email, coincidence='Coincidencia2122', count='count')
df2022 = nan_filler2(df2022, email=email)
archivo_actual = 'resultados2022.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
df2022.to_csv(ruta_ajustada)
print("El siguiente archivo ha sido guardado:", archivo_actual)
#%%
# 2008-2012
df2008 = df2008.rename(columns={"Coincidencia0008": "Coincidencia"})
df2012 = df2012.rename(columns={"Coincidencia0812": "Coincidencia"})
df2008_2012 = df2008.merge(df2012, how='outer', on=[email, 'Coincidencia'])
df2008_2012 = df2008_2012.rename(columns={'count_x':'2008', 'count_y':'2012'})
#%%
#2012-2013
df2013 = df2013.rename(columns={"Coincidencia1213": "Coincidencia"})
df2012_2013 = df2008_2012.merge(df2013, how='outer', on=[email, 'Coincidencia'])
df2012_2013 = df2012_2013.rename(columns={'count':'2013'})
#%%
#2013-2014
df2014 = df2014.rename(columns={"Coincidencia1314": "Coincidencia"})
df2013_2014 = df2012_2013.merge(df2014, how='outer', on=[email, 'Coincidencia'])
df2013_2014 = df2013_2014.rename(columns={'count':'2014'})
#%%
#2014-2015
df2015 = df2015.rename(columns={"Coincidencia1415": "Coincidencia"})
df2014_2015 = df2013_2014.merge(df2015, how='outer', on=[email, 'Coincidencia'])
df2014_2015 = df2014_2015.rename(columns={'count':'2015'})
#%%
#2015-2016
df2016 = df2016.rename(columns={"Coincidencia1516": "Coincidencia"})
df2015_2016 = df2014_2015.merge(df2016, how='outer', on=[email, 'Coincidencia'])
df2015_2016 = df2015_2016.rename(columns={'count':'2016'})
#%%
#2016-2017
df2017 = df2017.rename(columns={"Coincidencia1617": "Coincidencia"})
df2016_2017 = df2015_2016.merge(df2017, how='outer', on=[email, 'Coincidencia'])
df2016_2017 = df2016_2017.rename(columns={'count':'2017'})
#%%
#2017-2018
df2018 = df2018.rename(columns={"Coincidencia1718": "Coincidencia"})
df2017_2018 = df2016_2017.merge(df2018, how='outer', on=[email, 'Coincidencia'])
df2017_2018 = df2017_2018.rename(columns={'count':'2018'})
#%%
#2018-2019
df2019 = df2019.rename(columns={"Coincidencia1819": "Coincidencia"})
df2018_2019 = df2017_2018.merge(df2019, how='outer', on=[email, 'Coincidencia'])
df2018_2019 = df2018_2019.rename(columns={'count':'2019'})
#%%
#2019-2020
df2020 = df2020.rename(columns={"Coincidencia1920": "Coincidencia"})
df2019_2020 = df2018_2019.merge(df2020, how='outer', on=[email, 'Coincidencia'])
df2019_2020 = df2019_2020.rename(columns={'count':'2020'})
#%%
#2020-2021
df2021 = df2021.rename(columns={"Coincidencia2021": "Coincidencia"})
df2020_2021 = df2019_2020.merge(df2021, how='outer', on=[email, 'Coincidencia'])
df2020_2021 = df2020_2021.rename(columns={'count':'2021'})
#%%
#2021-2022
df2022 = df2022.rename(columns={"Coincidencia2122": "Coincidencia"})
df2021_2022 = df2020_2021.merge(df2022, how='outer', on=[email, 'Coincidencia'])
df2021_2022 = df2021_2022.rename(columns={'count':'2022'})
#%%
archivo_actual = 'resultadosALLYEARS_tecnico3.csv'
ruta_ajustada = os.path.join(ruta_salida, archivo_actual)
df2021_2022.to_csv(ruta_ajustada)
print("Se ha guaRDADO EL ARCHIVO: ", ruta_ajustada)
