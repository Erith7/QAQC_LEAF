# %%
# imports
import pandas as pd
import geopandas as gpd
import numpy as np
from functions import annual_data_extraction
from functions import set_order
from functions import nan_filler

# %% Reading data
# Reading the datafile
fullfile = pd.read_csv("./Datos/Ecuador/BSVTBA/ResultadosCUT_BSVTBA_02102023.csv")
print(fullfile.shape)
#%% 2000
result2000 = annual_data_extraction(fullfile, email='email1', coincidence='Coincidencia2000')
result2000.to_csv('./analisisresults/resultados2000.csv')
df2000 = pd.read_csv('./analisisresults/resultados2000.csv')
print('dataframe out of function:', df2000.columns)
df2000 = set_order(df2000, coincidence='Coincidencia2000')
df2000 = nan_filler(df2000, email= 'email1', coincidence='Coincidencia2000', count='count')
df2000.to_csv('./analisisresults/resultados2000.csv')

#%% 2008
result2008 = annual_data_extraction(fullfile, email='email1', coincidence='Coincidencia2008')
result2008.to_csv('./analisisresults/resultados2008.csv')
df2008 = pd.read_csv('./analisisresults/resultados2008.csv')
print('dataframe out of function:', df2008.columns)
df2008 = set_order(df2008, coincidence='Coincidencia2008')
df2008 = nan_filler(df2008, email= 'email1', coincidence='Coincidencia2008', count='count')
df2008.to_csv('./analisisresults/resultados2008.csv')

#%% 2012
result2012 = annual_data_extraction(fullfile, email='email1', coincidence='Coincidencia2012')
result2012.to_csv('./analisisresults/resultados2012.csv')
df2012 = pd.read_csv('./analisisresults/resultados2012.csv')
print('dataframe out of function:', df2012.columns)
df2012 = set_order(df2012, coincidence='Coincidencia2012')
df2012 = nan_filler(df2012, email= 'email1', coincidence='Coincidencia2012', count='count')
df2012.to_csv('./analisisresults/resultados2012.csv')

#%% 2013
result2013 = annual_data_extraction(fullfile, email='email1', coincidence='Coincidencia2013')
result2013.to_csv('./analisisresults/resultados2013.csv')
df2013 = pd.read_csv('./analisisresults/resultados2013.csv')
print('dataframe out of function:', df2013.columns)
df2013 = set_order(df2013, coincidence='Coincidencia2013')
df2013 = nan_filler(df2013, email= 'email1', coincidence='Coincidencia2013', count='count')
df2013.to_csv('./analisisresults/resultados2013.csv')

#%% 2014
result2014 = annual_data_extraction(fullfile, email='email1', coincidence='Coincidencia2014')
result2014.to_csv('./analisisresults/resultados2014.csv')
df2014 = pd.read_csv('./analisisresults/resultados2014.csv')
print('dataframe out of function:', df2014.columns)
df2014 = set_order(df2014, coincidence='Coincidencia2014')
df2014 = nan_filler(df2014, email= 'email1', coincidence='Coincidencia2014', count='count')
df2014.to_csv('./analisisresults/resultados2014.csv')
#%% 2015
result2015 = annual_data_extraction(fullfile, email='email1', coincidence='Coincidencia2015')
result2015.to_csv('./analisisresults/resultados2015.csv')
df2015 = pd.read_csv('./analisisresults/resultados2015.csv')
print('dataframe out of function:', df2015.columns)
df2015 = set_order(df2015, coincidence='Coincidencia2015')
df2015 = nan_filler(df2015, email= 'email1', coincidence='Coincidencia2015', count='count')
df2015.to_csv('./analisisresults/resultados2015.csv')

#%% 2016
result2016 = annual_data_extraction(fullfile, email='email1', coincidence='Coincidencia2016')
result2016.to_csv('./analisisresults/resultados2016.csv')
df2016 = pd.read_csv('./analisisresults/resultados2016.csv')
print('dataframe out of function:', df2016.columns)
df2016 = set_order(df2016, coincidence='Coincidencia2016')
df2016 = nan_filler(df2016, email= 'email1', coincidence='Coincidencia2016', count='count')
df2016.to_csv('./analisisresults/resultados2016.csv')

#%% 2017
result2017 = annual_data_extraction(fullfile, email='email1', coincidence='Coincidencia2017')
result2017.to_csv('./analisisresults/resultados2017.csv')
df2017 = pd.read_csv('./analisisresults/resultados2017.csv')
print('dataframe out of function:', df2017.columns)
df2017 = set_order(df2017, coincidence='Coincidencia2017')
df2017 = nan_filler(df2017, email= 'email1', coincidence='Coincidencia2017', count='count')
df2017.to_csv('./analisisresults/resultados2017.csv')

#%% 2018
result2018 = annual_data_extraction(fullfile, email='email1', coincidence='Coincidencia2018')
result2018.to_csv('./analisisresults/resultados2018.csv')
df2018 = pd.read_csv('./analisisresults/resultados2018.csv')
print('dataframe out of function:', df2018.columns)
df2018 = set_order(df2018, coincidence='Coincidencia2018')
df2018 = nan_filler(df2018, email= 'email1', coincidence='Coincidencia2018', count='count')
df2018.to_csv('./analisisresults/resultados2018.csv')
#%% 2019
result2019 = annual_data_extraction(fullfile, email='email1', coincidence='Coincidencia2019')
result2019.to_csv('./analisisresults/resultados2019.csv')
df2019 = pd.read_csv('./analisisresults/resultados2019.csv')
print('dataframe out of function:', df2019.columns)
df2019 = set_order(df2019, coincidence='Coincidencia2019')
df2019 = nan_filler(df2019, email= 'email1', coincidence='Coincidencia2019', count='count')
df2019.to_csv('./analisisresults/resultados2019.csv')
#%% 2020
result2020 = annual_data_extraction(fullfile, email='email1', coincidence='Coincidencia2020')
result2020.to_csv('./analisisresults/resultados2020.csv')
df2020 = pd.read_csv('./analisisresults/resultados2020.csv')
print('dataframe out of function:', df2020.columns)
df2020 = set_order(df2020, coincidence='Coincidencia2020')
df2020 = nan_filler(df2020, email= 'email1', coincidence='Coincidencia2020', count='count')
df2020.to_csv('./analisisresults/resultados2020.csv')
#%% 2021
result2021 = annual_data_extraction(fullfile, email='email1', coincidence='Coincidencia2021')
result2021.to_csv('./analisisresults/resultados2021.csv')
df2021 = pd.read_csv('./analisisresults/resultados2021.csv')
print('dataframe out of function:', df2021.columns)
df2021 = set_order(df2021, coincidence='Coincidencia2021')
df2021 = nan_filler(df2021, email= 'email1', coincidence='Coincidencia2021', count='count')
df2021.to_csv('./analisisresults/resultados2021.csv')
#%% 2022
result2022 = annual_data_extraction(fullfile, email='email1', coincidence='Coincidencia2022')
result2022.to_csv('./analisisresults/resultados2022.csv')
df2022 = pd.read_csv('./analisisresults/resultados2022.csv')
print('dataframe out of function:', df2022.columns)
df2022 = set_order(df2022, coincidence='Coincidencia2022')
df2022 = nan_filler(df2022, email= 'email1', coincidence='Coincidencia2022', count='count')
df2022.to_csv('./analisisresults/resultados2022.csv')
# %%
# Mergin annual csvs
# 2000-2008
df2000 = df2000.rename(columns={"Coincidencia2000": "Coincidencia"})
df2008 = df2008.rename(columns={"Coincidencia2008": "Coincidencia"})
df2000_2008 = df2000.merge(df2008, how='outer', on=['email1', 'Coincidencia'])
df2000_2008 = df2000_2008.rename(columns={'count_x':'2000', 'count_y':'2008'})
#%%
# 2008-2012
df2012 = df2012.rename(columns={"Coincidencia2012": "Coincidencia"})
df2008_2012 = df2000_2008.merge(df2012, how='outer', on=['email1', 'Coincidencia'])
df2008_2012 = df2008_2012.rename(columns={'count':'2012'})
#%%
#2012-2013
df2013 = df2013.rename(columns={"Coincidencia2013": "Coincidencia"})
df2012_2013 = df2008_2012.merge(df2013, how='outer', on=['email1', 'Coincidencia'])
df2012_2013 = df2012_2013.rename(columns={'count':'2013'})
#%%
#2013-2014
df2014 = df2014.rename(columns={"Coincidencia2014": "Coincidencia"})
df2013_2014 = df2012_2013.merge(df2014, how='outer', on=['email1', 'Coincidencia'])
df2013_2014 = df2013_2014.rename(columns={'count':'2014'})
#%%
#2014-2015
df2015 = df2015.rename(columns={"Coincidencia2015": "Coincidencia"})
df2014_2015 = df2013_2014.merge(df2015, how='outer', on=['email1', 'Coincidencia'])
df2014_2015 = df2014_2015.rename(columns={'count':'2015'})
#%%
#2015-2016
df2016 = df2016.rename(columns={"Coincidencia2016": "Coincidencia"})
df2015_2016 = df2014_2015.merge(df2016, how='outer', on=['email1', 'Coincidencia'])
df2015_2016 = df2015_2016.rename(columns={'count':'2016'})
#%%
#2016-2017
df2017 = df2017.rename(columns={"Coincidencia2017": "Coincidencia"})
df2016_2017 = df2015_2016.merge(df2017, how='outer', on=['email1', 'Coincidencia'])
df2016_2017 = df2016_2017.rename(columns={'count':'2017'})
#%%
#2017-2018
df2018 = df2018.rename(columns={"Coincidencia2018": "Coincidencia"})
df2017_2018 = df2016_2017.merge(df2018, how='outer', on=['email1', 'Coincidencia'])
df2017_2018 = df2017_2018.rename(columns={'count':'2018'})
#%%
#2018-2019
df2019 = df2019.rename(columns={"Coincidencia2019": "Coincidencia"})
df2018_2019 = df2017_2018.merge(df2019, how='outer', on=['email1', 'Coincidencia'])
df2018_2019 = df2018_2019.rename(columns={'count':'2019'})
#%%
#2019-2020
df2020 = df2020.rename(columns={"Coincidencia2020": "Coincidencia"})
df2019_2020 = df2018_2019.merge(df2020, how='outer', on=['email1', 'Coincidencia'])
df2019_2020 = df2019_2020.rename(columns={'count':'2020'})
#%%
#2020-2021
df2021 = df2021.rename(columns={"Coincidencia2021": "Coincidencia"})
df2020_2021 = df2019_2020.merge(df2021, how='outer', on=['email1', 'Coincidencia'])
df2020_2021 = df2020_2021.rename(columns={'count':'2021'})
#%%
#2021-2022
df2022 = df2022.rename(columns={"Coincidencia2022": "Coincidencia"})
df2021_2022 = df2020_2021.merge(df2022, how='outer', on=['email1', 'Coincidencia'])
df2021_2022 = df2021_2022.rename(columns={'count':'2022'})
df2021_2022.to_csv('./analisisresults/resultadosALLYEARS_tecnico1.csv')



