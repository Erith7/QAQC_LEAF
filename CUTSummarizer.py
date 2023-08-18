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
fullfile = pd.read_csv("./Datos/Ecuador/BSVTBA/ResultadosInterpretacion_BSVTBA_02102023.csv")
print(fullfile.head(10))
fullfile['geometry'] = fullfile['geometry'].apply(wkt.loads)
gdf = gpd.GeoDataFrame(fullfile, crs="EPSG:4326")
# %%
# Selection of changes columns and deleting the previous dataframes
gdfSel = gdf[["plotid", "sampleid", "lon", "lat", "geometry", "pl_id", "pl_cluster", "pl_monimages", "email1", "email2", "email3", "CUT2000_1", "CUT2000_2", "CUT2000_3", "CUT2008_1", "CUT2008_2", "CUT2008_3", "CUT2012_1", "CUT2012_2", "CUT2012_3", "CUT2013_1", "CUT2013_2", "CUT2013_3", "CUT2014_1", "CUT2014_2", "CUT2014_3", "CUT2015_1", "CUT2015_2", "CUT2015_3", "CUT2016_1", "CUT2016_2", "CUT2016_3", "CUT2017_1", "CUT2017_2", "CUT2017_3", "CUT2018_1", "CUT2018_2", "CUT2018_3", "CUT2019_1", "CUT2019_2", "CUT2019_3", "CUT2020_1", "CUT2020_2", "CUT2020_3", "CUT2021_1", "CUT2021_2", "CUT2021_3", "CUT2022_1", "CUT2022_2", "CUT2022_3"]]
del gdf
del fullfile

# %%
# CUT 2000:
gdfSel.loc[(gdfSel['CUT2000_1'] == gdfSel['CUT2000_2']) & (gdfSel['CUT2000_3'].isnull()), 'CUT2000'] = gdfSel['CUT2000_1']
gdfSel.loc[(gdfSel['CUT2000_1'] == gdfSel['CUT2000_2']) & (gdfSel['CUT2000_3'].isnull()), 'Coincidencia2000'] = 'EA'
gdfSel.loc[(gdfSel['CUT2000_1'] != gdfSel['CUT2000_2']) & (gdfSel['CUT2000_3'].isnull()), 'CUT2000'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2000_1'] != gdfSel['CUT2000_2']) & (gdfSel['CUT2000_3'].isnull()), 'Coincidencia2000'] = 'AA'
gdfSel.loc[(gdfSel['CUT2000_1'].isnull()) & (gdfSel['CUT2000_2'].isnull()) & (gdfSel['CUT2000_3'].isnull()), 'CUT2000'] = np.nan
gdfSel.loc[(gdfSel['CUT2000_1'].isnull()) & (gdfSel['CUT2000_2'].isnull()) & (gdfSel['CUT2000_3'].isnull()), 'Coincidencia2000'] = 'A'
gdfSel.loc[(gdfSel['CUT2000_1'].notnull()) & (gdfSel['CUT2000_2'].isnull()) & (gdfSel['CUT2000_3'].isnull()), 'CUT2000'] = gdfSel['CUT2000_1']
gdfSel.loc[(gdfSel['CUT2000_1'].notnull()) & (gdfSel['CUT2000_2'].isnull()) & (gdfSel['CUT2000_3'].isnull()), 'Coincidencia2000'] = 'BB'
gdfSel.loc[(gdfSel['CUT2000_1'].isnull()) & (gdfSel['CUT2000_2'].notnull()) & (gdfSel['CUT2000_3'].isnull()), 'CUT2000'] = gdfSel['CUT2000_2']
gdfSel.loc[(gdfSel['CUT2000_1'].isnull()) & (gdfSel['CUT2000_2'].notnull()) & (gdfSel['CUT2000_3'].isnull()), 'Coincidencia2000'] = 'CC'
gdfSel.loc[(gdfSel['CUT2000_1'].isnull()) & (gdfSel['CUT2000_2'].isnull()) & (gdfSel['CUT2000_3'].notnull()), 'CUT2000'] = gdfSel['CUT2000_3']
gdfSel.loc[(gdfSel['CUT2000_1'].isnull()) & (gdfSel['CUT2000_2'].isnull()) & (gdfSel['CUT2000_3'].notnull()), 'Coincidencia2000'] = 'HH'
gdfSel.loc[(gdfSel['CUT2000_1'] == gdfSel['CUT2000_2']) & (gdfSel['CUT2000_3'] == gdfSel['CUT2000_2']) & (gdfSel['CUT2000_1'] == gdfSel['CUT2000_3']) & (gdfSel['CUT2000_1'].notnull()) & (gdfSel['CUT2000_2'].notnull()) & (gdfSel['CUT2000_3'].notnull()), 'CUT2000'] = gdfSel['CUT2000_1']
gdfSel.loc[(gdfSel['CUT2000_1'] == gdfSel['CUT2000_2']) & (gdfSel['CUT2000_3'] == gdfSel['CUT2000_2']) & (gdfSel['CUT2000_1'] == gdfSel['CUT2000_3']) & (gdfSel['CUT2000_1'].notnull()) & (gdfSel['CUT2000_2'].notnull()) & (gdfSel['CUT2000_3'].notnull()), 'Coincidencia2000'] = 'E'
gdfSel.loc[(gdfSel['CUT2000_1'] != gdfSel['CUT2000_2']) & (gdfSel['CUT2000_2'] == gdfSel['CUT2000_3']) & (gdfSel['CUT2000_1'].notnull()) & (gdfSel['CUT2000_2'].notnull()) & (gdfSel['CUT2000_3'].notnull()), 'CUT2000'] = gdfSel['CUT2000_2']
gdfSel.loc[(gdfSel['CUT2000_1'] != gdfSel['CUT2000_2']) & (gdfSel['CUT2000_2'] == gdfSel['CUT2000_3']) & (gdfSel['CUT2000_1'].notnull()) & (gdfSel['CUT2000_2'].notnull()) & (gdfSel['CUT2000_3'].notnull()), 'Coincidencia2000'] = 'B'
gdfSel.loc[(gdfSel['CUT2000_1'] == gdfSel['CUT2000_2']) & (gdfSel['CUT2000_2'] != gdfSel['CUT2000_3']) & (gdfSel['CUT2000_1'].notnull()) & (gdfSel['CUT2000_2'].notnull()) & (gdfSel['CUT2000_3'].notnull()), 'CUT2000'] = gdfSel['CUT2000_1']
gdfSel.loc[(gdfSel['CUT2000_1'] == gdfSel['CUT2000_2']) & (gdfSel['CUT2000_2'] != gdfSel['CUT2000_3']) & (gdfSel['CUT2000_1'].notnull()) & (gdfSel['CUT2000_2'].notnull()) & (gdfSel['CUT2000_3'].notnull()), 'Coincidencia2000'] = 'C'
gdfSel.loc[(gdfSel['CUT2000_1'] == gdfSel['CUT2000_3']) & (gdfSel['CUT2000_2'] != gdfSel['CUT2000_3']) & (gdfSel['CUT2000_1'].notnull()) & (gdfSel['CUT2000_2'].notnull()) & (gdfSel['CUT2000_3'].notnull()), 'CUT2000'] = gdfSel['CUT2000_1']
gdfSel.loc[(gdfSel['CUT2000_1'] == gdfSel['CUT2000_3']) & (gdfSel['CUT2000_2'] != gdfSel['CUT2000_3']) & (gdfSel['CUT2000_1'].notnull()) & (gdfSel['CUT2000_2'].notnull()) & (gdfSel['CUT2000_3'].notnull()), 'Coincidencia2000'] = 'D'
gdfSel.loc[(gdfSel['CUT2000_1'].isnull()) & (gdfSel['CUT2000_2'] == gdfSel['CUT2000_3']) & (gdfSel['CUT2000_3'].notnull()), 'CUT2000'] = gdfSel['CUT2000_2']
gdfSel.loc[(gdfSel['CUT2000_1'].isnull()) & (gdfSel['CUT2000_2'] == gdfSel['CUT2000_3']) & (gdfSel['CUT2000_3'].notnull()), 'Coincidencia2000'] = 'DD'
gdfSel.loc[(gdfSel['CUT2000_1'].isnull()) & (gdfSel['CUT2000_2'] != gdfSel['CUT2000_3']) & (gdfSel['CUT2000_3'].notnull()), 'CUT2000'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2000_1'].isnull()) & (gdfSel['CUT2000_2'] != gdfSel['CUT2000_3']) & (gdfSel['CUT2000_3'].notnull()), 'Coincidencia2000'] = 'FF'
gdfSel.loc[(gdfSel['CUT2000_1'] != gdfSel['CUT2000_3']) & (gdfSel['CUT2000_2'] != gdfSel['CUT2000_3']) & (gdfSel['CUT2000_1'] != gdfSel['CUT2000_2']) & (gdfSel['CUT2000_1'].notnull()) & (gdfSel['CUT2000_2'].notnull()) & (gdfSel['CUT2000_3'].notnull()), 'CUT2000'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2000_1'] != gdfSel['CUT2000_3']) & (gdfSel['CUT2000_2'] != gdfSel['CUT2000_3']) & (gdfSel['CUT2000_1'] != gdfSel['CUT2000_2']) & (gdfSel['CUT2000_1'].notnull()) & (gdfSel['CUT2000_2'].notnull()) & (gdfSel['CUT2000_3'].notnull()), 'Coincidencia2000'] = 'F'


# %%
# CUT2008
gdfSel.loc[(gdfSel['CUT2008_1'] == gdfSel['CUT2008_2']) & (gdfSel['CUT2008_3'].isnull()), 'CUT2008'] = gdfSel['CUT2008_1']
gdfSel.loc[(gdfSel['CUT2008_1'] == gdfSel['CUT2008_2']) & (gdfSel['CUT2008_3'].isnull()), 'Coincidencia2008'] = 'EA'
gdfSel.loc[(gdfSel['CUT2008_1'] != gdfSel['CUT2008_2']) & (gdfSel['CUT2008_3'].isnull()), 'CUT2008'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2008_1'] != gdfSel['CUT2008_2']) & (gdfSel['CUT2008_3'].isnull()), 'Coincidencia2008'] = 'AA'
gdfSel.loc[(gdfSel['CUT2008_1'].isnull()) & (gdfSel['CUT2008_2'].isnull()) & (gdfSel['CUT2008_3'].isnull()), 'CUT2008'] = np.nan
gdfSel.loc[(gdfSel['CUT2008_1'].isnull()) & (gdfSel['CUT2008_2'].isnull()) & (gdfSel['CUT2008_3'].isnull()), 'Coincidencia2008'] = 'A'
gdfSel.loc[(gdfSel['CUT2008_1'].notnull()) & (gdfSel['CUT2008_2'].isnull()) & (gdfSel['CUT2008_3'].isnull()), 'CUT2008'] = gdfSel['CUT2008_1']
gdfSel.loc[(gdfSel['CUT2008_1'].notnull()) & (gdfSel['CUT2008_2'].isnull()) & (gdfSel['CUT2008_3'].isnull()), 'Coincidencia2008'] = 'BB'
gdfSel.loc[(gdfSel['CUT2008_1'].isnull()) & (gdfSel['CUT2008_2'].notnull()) & (gdfSel['CUT2008_3'].isnull()), 'CUT2008'] = gdfSel['CUT2008_2']
gdfSel.loc[(gdfSel['CUT2008_1'].isnull()) & (gdfSel['CUT2008_2'].notnull()) & (gdfSel['CUT2008_3'].isnull()), 'Coincidencia2008'] = 'CC'
gdfSel.loc[(gdfSel['CUT2008_1'].isnull()) & (gdfSel['CUT2008_2'].isnull()) & (gdfSel['CUT2008_3'].notnull()), 'CUT2008'] = gdfSel['CUT2008_3']
gdfSel.loc[(gdfSel['CUT2008_1'].isnull()) & (gdfSel['CUT2008_2'].isnull()) & (gdfSel['CUT2008_3'].notnull()), 'Coincidencia2008'] = 'HH'
gdfSel.loc[(gdfSel['CUT2008_1'] == gdfSel['CUT2008_2']) & (gdfSel['CUT2008_3'] == gdfSel['CUT2008_2']) & (gdfSel['CUT2008_1'] == gdfSel['CUT2008_3']) & (gdfSel['CUT2008_1'].notnull()) & (gdfSel['CUT2008_2'].notnull()) & (gdfSel['CUT2008_3'].notnull()), 'CUT2008'] = gdfSel['CUT2008_1']
gdfSel.loc[(gdfSel['CUT2008_1'] == gdfSel['CUT2008_2']) & (gdfSel['CUT2008_3'] == gdfSel['CUT2008_2']) & (gdfSel['CUT2008_1'] == gdfSel['CUT2008_3']) & (gdfSel['CUT2008_1'].notnull()) & (gdfSel['CUT2008_2'].notnull()) & (gdfSel['CUT2008_3'].notnull()), 'Coincidencia2008'] = 'E'
gdfSel.loc[(gdfSel['CUT2008_1'] != gdfSel['CUT2008_2']) & (gdfSel['CUT2008_2'] == gdfSel['CUT2008_3']) & (gdfSel['CUT2008_1'].notnull()) & (gdfSel['CUT2008_2'].notnull()) & (gdfSel['CUT2008_3'].notnull()), 'CUT2008'] = gdfSel['CUT2008_2']
gdfSel.loc[(gdfSel['CUT2008_1'] != gdfSel['CUT2008_2']) & (gdfSel['CUT2008_2'] == gdfSel['CUT2008_3']) & (gdfSel['CUT2008_1'].notnull()) & (gdfSel['CUT2008_2'].notnull()) & (gdfSel['CUT2008_3'].notnull()), 'Coincidencia2008'] = 'B'
gdfSel.loc[(gdfSel['CUT2008_1'] == gdfSel['CUT2008_2']) & (gdfSel['CUT2008_2'] != gdfSel['CUT2008_3']) & (gdfSel['CUT2008_1'].notnull()) & (gdfSel['CUT2008_2'].notnull()) & (gdfSel['CUT2008_3'].notnull()), 'CUT2008'] = gdfSel['CUT2008_1']
gdfSel.loc[(gdfSel['CUT2008_1'] == gdfSel['CUT2008_2']) & (gdfSel['CUT2008_2'] != gdfSel['CUT2008_3']) & (gdfSel['CUT2008_1'].notnull()) & (gdfSel['CUT2008_2'].notnull()) & (gdfSel['CUT2008_3'].notnull()), 'Coincidencia2008'] = 'C'
gdfSel.loc[(gdfSel['CUT2008_1'] == gdfSel['CUT2008_3']) & (gdfSel['CUT2008_2'] != gdfSel['CUT2008_3']) & (gdfSel['CUT2008_1'].notnull()) & (gdfSel['CUT2008_2'].notnull()) & (gdfSel['CUT2008_3'].notnull()), 'CUT2008'] = gdfSel['CUT2008_1']
gdfSel.loc[(gdfSel['CUT2008_1'] == gdfSel['CUT2008_3']) & (gdfSel['CUT2008_2'] != gdfSel['CUT2008_3']) & (gdfSel['CUT2008_1'].notnull()) & (gdfSel['CUT2008_2'].notnull()) & (gdfSel['CUT2008_3'].notnull()), 'Coincidencia2008'] = 'D'
gdfSel.loc[(gdfSel['CUT2008_1'].isnull()) & (gdfSel['CUT2008_2'] == gdfSel['CUT2008_3']) & (gdfSel['CUT2008_3'].notnull()), 'CUT2008'] = gdfSel['CUT2008_2']
gdfSel.loc[(gdfSel['CUT2008_1'].isnull()) & (gdfSel['CUT2008_2'] == gdfSel['CUT2008_3']) & (gdfSel['CUT2008_3'].notnull()), 'Coincidencia2008'] = 'DD'
gdfSel.loc[(gdfSel['CUT2008_1'].isnull()) & (gdfSel['CUT2008_2'] != gdfSel['CUT2008_3']) & (gdfSel['CUT2008_3'].notnull()), 'CUT2008'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2008_1'].isnull()) & (gdfSel['CUT2008_2'] != gdfSel['CUT2008_3']) & (gdfSel['CUT2008_3'].notnull()), 'Coincidencia2008'] = 'FF'
gdfSel.loc[(gdfSel['CUT2008_1'] != gdfSel['CUT2008_3']) & (gdfSel['CUT2008_2'] != gdfSel['CUT2008_3']) & (gdfSel['CUT2008_1'] != gdfSel['CUT2008_2']) & (gdfSel['CUT2008_1'].notnull()) & (gdfSel['CUT2008_2'].notnull()) & (gdfSel['CUT2008_3'].notnull()), 'CUT2008'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2008_1'] != gdfSel['CUT2008_3']) & (gdfSel['CUT2008_2'] != gdfSel['CUT2008_3']) & (gdfSel['CUT2008_1'] != gdfSel['CUT2008_2']) & (gdfSel['CUT2008_1'].notnull()) & (gdfSel['CUT2008_2'].notnull()) & (gdfSel['CUT2008_3'].notnull()), 'Coincidencia2008'] = 'F'


# %%
# CUT2012
gdfSel.loc[(gdfSel['CUT2012_1'] == gdfSel['CUT2012_2']) & (gdfSel['CUT2012_3'].isnull()), 'CUT2012'] = gdfSel['CUT2012_1']
gdfSel.loc[(gdfSel['CUT2012_1'] == gdfSel['CUT2012_2']) & (gdfSel['CUT2012_3'].isnull()), 'Coincidencia2012'] = 'EA'
gdfSel.loc[(gdfSel['CUT2012_1'] != gdfSel['CUT2012_2']) & (gdfSel['CUT2012_3'].isnull()), 'CUT2012'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2012_1'] != gdfSel['CUT2012_2']) & (gdfSel['CUT2012_3'].isnull()), 'Coincidencia2012'] = 'AA'
gdfSel.loc[(gdfSel['CUT2012_1'].isnull()) & (gdfSel['CUT2012_2'].isnull()) & (gdfSel['CUT2012_3'].isnull()), 'CUT2012'] = np.nan
gdfSel.loc[(gdfSel['CUT2012_1'].isnull()) & (gdfSel['CUT2012_2'].isnull()) & (gdfSel['CUT2012_3'].isnull()), 'Coincidencia2012'] = 'A'
gdfSel.loc[(gdfSel['CUT2012_1'].notnull()) & (gdfSel['CUT2012_2'].isnull()) & (gdfSel['CUT2012_3'].isnull()), 'CUT2012'] = gdfSel['CUT2012_1']
gdfSel.loc[(gdfSel['CUT2012_1'].notnull()) & (gdfSel['CUT2012_2'].isnull()) & (gdfSel['CUT2012_3'].isnull()), 'Coincidencia2012'] = 'BB'
gdfSel.loc[(gdfSel['CUT2012_1'].isnull()) & (gdfSel['CUT2012_2'].notnull()) & (gdfSel['CUT2012_3'].isnull()), 'CUT2012'] = gdfSel['CUT2012_2']
gdfSel.loc[(gdfSel['CUT2012_1'].isnull()) & (gdfSel['CUT2012_2'].notnull()) & (gdfSel['CUT2012_3'].isnull()), 'Coincidencia2012'] = 'CC'
gdfSel.loc[(gdfSel['CUT2012_1'].isnull()) & (gdfSel['CUT2012_2'].isnull()) & (gdfSel['CUT2012_3'].notnull()), 'CUT2012'] = gdfSel['CUT2012_3']
gdfSel.loc[(gdfSel['CUT2012_1'].isnull()) & (gdfSel['CUT2012_2'].isnull()) & (gdfSel['CUT2012_3'].notnull()), 'Coincidencia2012'] = 'HH'
gdfSel.loc[(gdfSel['CUT2012_1'] == gdfSel['CUT2012_2']) & (gdfSel['CUT2012_3'] == gdfSel['CUT2012_2']) & (gdfSel['CUT2012_1'] == gdfSel['CUT2012_3']) & (gdfSel['CUT2012_1'].notnull()) & (gdfSel['CUT2012_2'].notnull()) & (gdfSel['CUT2012_3'].notnull()), 'CUT2012'] = gdfSel['CUT2012_1']
gdfSel.loc[(gdfSel['CUT2012_1'] == gdfSel['CUT2012_2']) & (gdfSel['CUT2012_3'] == gdfSel['CUT2012_2']) & (gdfSel['CUT2012_1'] == gdfSel['CUT2012_3']) & (gdfSel['CUT2012_1'].notnull()) & (gdfSel['CUT2012_2'].notnull()) & (gdfSel['CUT2012_3'].notnull()), 'Coincidencia2012'] = 'E'
gdfSel.loc[(gdfSel['CUT2012_1'] != gdfSel['CUT2012_2']) & (gdfSel['CUT2012_2'] == gdfSel['CUT2012_3']) & (gdfSel['CUT2012_1'].notnull()) & (gdfSel['CUT2012_2'].notnull()) & (gdfSel['CUT2012_3'].notnull()), 'CUT2012'] = gdfSel['CUT2012_2']
gdfSel.loc[(gdfSel['CUT2012_1'] != gdfSel['CUT2012_2']) & (gdfSel['CUT2012_2'] == gdfSel['CUT2012_3']) & (gdfSel['CUT2012_1'].notnull()) & (gdfSel['CUT2012_2'].notnull()) & (gdfSel['CUT2012_3'].notnull()), 'Coincidencia2012'] = 'B'
gdfSel.loc[(gdfSel['CUT2012_1'] == gdfSel['CUT2012_2']) & (gdfSel['CUT2012_2'] != gdfSel['CUT2012_3']) & (gdfSel['CUT2012_1'].notnull()) & (gdfSel['CUT2012_2'].notnull()) & (gdfSel['CUT2012_3'].notnull()), 'CUT2012'] = gdfSel['CUT2012_1']
gdfSel.loc[(gdfSel['CUT2012_1'] == gdfSel['CUT2012_2']) & (gdfSel['CUT2012_2'] != gdfSel['CUT2012_3']) & (gdfSel['CUT2012_1'].notnull()) & (gdfSel['CUT2012_2'].notnull()) & (gdfSel['CUT2012_3'].notnull()), 'Coincidencia2012'] = 'C'
gdfSel.loc[(gdfSel['CUT2012_1'] == gdfSel['CUT2012_3']) & (gdfSel['CUT2012_2'] != gdfSel['CUT2012_3']) & (gdfSel['CUT2012_1'].notnull()) & (gdfSel['CUT2012_2'].notnull()) & (gdfSel['CUT2012_3'].notnull()), 'CUT2012'] = gdfSel['CUT2012_1']
gdfSel.loc[(gdfSel['CUT2012_1'] == gdfSel['CUT2012_3']) & (gdfSel['CUT2012_2'] != gdfSel['CUT2012_3']) & (gdfSel['CUT2012_1'].notnull()) & (gdfSel['CUT2012_2'].notnull()) & (gdfSel['CUT2012_3'].notnull()), 'Coincidencia2012'] = 'D'
gdfSel.loc[(gdfSel['CUT2012_1'].isnull()) & (gdfSel['CUT2012_2'] == gdfSel['CUT2012_3']) & (gdfSel['CUT2012_3'].notnull()), 'CUT2012'] = gdfSel['CUT2012_2']
gdfSel.loc[(gdfSel['CUT2012_1'].isnull()) & (gdfSel['CUT2012_2'] == gdfSel['CUT2012_3']) & (gdfSel['CUT2012_3'].notnull()), 'Coincidencia2012'] = 'DD'
gdfSel.loc[(gdfSel['CUT2012_1'].isnull()) & (gdfSel['CUT2012_2'] != gdfSel['CUT2012_3']) & (gdfSel['CUT2012_3'].notnull()), 'CUT2012'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2012_1'].isnull()) & (gdfSel['CUT2012_2'] != gdfSel['CUT2012_3']) & (gdfSel['CUT2012_3'].notnull()), 'Coincidencia2012'] = 'FF'
gdfSel.loc[(gdfSel['CUT2012_1'] != gdfSel['CUT2012_3']) & (gdfSel['CUT2012_2'] != gdfSel['CUT2012_3']) & (gdfSel['CUT2012_1'] != gdfSel['CUT2012_2']) & (gdfSel['CUT2012_1'].notnull()) & (gdfSel['CUT2012_2'].notnull()) & (gdfSel['CUT2012_3'].notnull()), 'CUT2012'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2012_1'] != gdfSel['CUT2012_3']) & (gdfSel['CUT2012_2'] != gdfSel['CUT2012_3']) & (gdfSel['CUT2012_1'] != gdfSel['CUT2012_2']) & (gdfSel['CUT2012_1'].notnull()) & (gdfSel['CUT2012_2'].notnull()) & (gdfSel['CUT2012_3'].notnull()), 'Coincidencia2012'] = 'F'


# %%
#CUT2013
gdfSel.loc[(gdfSel['CUT2013_1'] == gdfSel['CUT2013_2']) & (gdfSel['CUT2013_3'].isnull()), 'CUT2013'] = gdfSel['CUT2013_1']
gdfSel.loc[(gdfSel['CUT2013_1'] == gdfSel['CUT2013_2']) & (gdfSel['CUT2013_3'].isnull()), 'Coincidencia2013'] = 'EA'
gdfSel.loc[(gdfSel['CUT2013_1'] != gdfSel['CUT2013_2']) & (gdfSel['CUT2013_3'].isnull()), 'CUT2013'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2013_1'] != gdfSel['CUT2013_2']) & (gdfSel['CUT2013_3'].isnull()), 'Coincidencia2013'] = 'AA'
gdfSel.loc[(gdfSel['CUT2013_1'].isnull()) & (gdfSel['CUT2013_2'].isnull()) & (gdfSel['CUT2013_3'].isnull()), 'CUT2013'] = np.nan
gdfSel.loc[(gdfSel['CUT2013_1'].isnull()) & (gdfSel['CUT2013_2'].isnull()) & (gdfSel['CUT2013_3'].isnull()), 'Coincidencia2013'] = 'A'
gdfSel.loc[(gdfSel['CUT2013_1'].notnull()) & (gdfSel['CUT2013_2'].isnull()) & (gdfSel['CUT2013_3'].isnull()), 'CUT2013'] = gdfSel['CUT2013_1']
gdfSel.loc[(gdfSel['CUT2013_1'].notnull()) & (gdfSel['CUT2013_2'].isnull()) & (gdfSel['CUT2013_3'].isnull()), 'Coincidencia2013'] = 'BB'
gdfSel.loc[(gdfSel['CUT2013_1'].isnull()) & (gdfSel['CUT2013_2'].notnull()) & (gdfSel['CUT2013_3'].isnull()), 'CUT2013'] = gdfSel['CUT2013_2']
gdfSel.loc[(gdfSel['CUT2013_1'].isnull()) & (gdfSel['CUT2013_2'].notnull()) & (gdfSel['CUT2013_3'].isnull()), 'Coincidencia2013'] = 'CC'
gdfSel.loc[(gdfSel['CUT2013_1'].isnull()) & (gdfSel['CUT2013_2'].isnull()) & (gdfSel['CUT2013_3'].notnull()), 'CUT2013'] = gdfSel['CUT2013_3']
gdfSel.loc[(gdfSel['CUT2013_1'].isnull()) & (gdfSel['CUT2013_2'].isnull()) & (gdfSel['CUT2013_3'].notnull()), 'Coincidencia2013'] = 'HH'
gdfSel.loc[(gdfSel['CUT2013_1'] == gdfSel['CUT2013_2']) & (gdfSel['CUT2013_3'] == gdfSel['CUT2013_2']) & (gdfSel['CUT2013_1'] == gdfSel['CUT2013_3']) & (gdfSel['CUT2013_1'].notnull()) & (gdfSel['CUT2013_2'].notnull()) & (gdfSel['CUT2013_3'].notnull()), 'CUT2013'] = gdfSel['CUT2013_1']
gdfSel.loc[(gdfSel['CUT2013_1'] == gdfSel['CUT2013_2']) & (gdfSel['CUT2013_3'] == gdfSel['CUT2013_2']) & (gdfSel['CUT2013_1'] == gdfSel['CUT2013_3']) & (gdfSel['CUT2013_1'].notnull()) & (gdfSel['CUT2013_2'].notnull()) & (gdfSel['CUT2013_3'].notnull()), 'Coincidencia2013'] = 'E'
gdfSel.loc[(gdfSel['CUT2013_1'] != gdfSel['CUT2013_2']) & (gdfSel['CUT2013_2'] == gdfSel['CUT2013_3']) & (gdfSel['CUT2013_1'].notnull()) & (gdfSel['CUT2013_2'].notnull()) & (gdfSel['CUT2013_3'].notnull()), 'CUT2013'] = gdfSel['CUT2013_2']
gdfSel.loc[(gdfSel['CUT2013_1'] != gdfSel['CUT2013_2']) & (gdfSel['CUT2013_2'] == gdfSel['CUT2013_3']) & (gdfSel['CUT2013_1'].notnull()) & (gdfSel['CUT2013_2'].notnull()) & (gdfSel['CUT2013_3'].notnull()), 'Coincidencia2013'] = 'B'
gdfSel.loc[(gdfSel['CUT2013_1'] == gdfSel['CUT2013_2']) & (gdfSel['CUT2013_2'] != gdfSel['CUT2013_3']) & (gdfSel['CUT2013_1'].notnull()) & (gdfSel['CUT2013_2'].notnull()) & (gdfSel['CUT2013_3'].notnull()), 'CUT2013'] = gdfSel['CUT2013_1']
gdfSel.loc[(gdfSel['CUT2013_1'] == gdfSel['CUT2013_2']) & (gdfSel['CUT2013_2'] != gdfSel['CUT2013_3']) & (gdfSel['CUT2013_1'].notnull()) & (gdfSel['CUT2013_2'].notnull()) & (gdfSel['CUT2013_3'].notnull()), 'Coincidencia2013'] = 'C'
gdfSel.loc[(gdfSel['CUT2013_1'] == gdfSel['CUT2013_3']) & (gdfSel['CUT2013_2'] != gdfSel['CUT2013_3']) & (gdfSel['CUT2013_1'].notnull()) & (gdfSel['CUT2013_2'].notnull()) & (gdfSel['CUT2013_3'].notnull()), 'CUT2013'] = gdfSel['CUT2013_1']
gdfSel.loc[(gdfSel['CUT2013_1'] == gdfSel['CUT2013_3']) & (gdfSel['CUT2013_2'] != gdfSel['CUT2013_3']) & (gdfSel['CUT2013_1'].notnull()) & (gdfSel['CUT2013_2'].notnull()) & (gdfSel['CUT2013_3'].notnull()), 'Coincidencia2013'] = 'D'
gdfSel.loc[(gdfSel['CUT2013_1'].isnull()) & (gdfSel['CUT2013_2'] == gdfSel['CUT2013_3']) & (gdfSel['CUT2013_3'].notnull()), 'CUT2013'] = gdfSel['CUT2013_2']
gdfSel.loc[(gdfSel['CUT2013_1'].isnull()) & (gdfSel['CUT2013_2'] == gdfSel['CUT2013_3']) & (gdfSel['CUT2013_3'].notnull()), 'Coincidencia2013'] = 'DD'
gdfSel.loc[(gdfSel['CUT2013_1'].isnull()) & (gdfSel['CUT2013_2'] != gdfSel['CUT2013_3']) & (gdfSel['CUT2013_3'].notnull()), 'CUT2013'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2013_1'].isnull()) & (gdfSel['CUT2013_2'] != gdfSel['CUT2013_3']) & (gdfSel['CUT2013_3'].notnull()), 'Coincidencia2013'] = 'FF'
gdfSel.loc[(gdfSel['CUT2013_1'] != gdfSel['CUT2013_3']) & (gdfSel['CUT2013_2'] != gdfSel['CUT2013_3']) & (gdfSel['CUT2013_1'] != gdfSel['CUT2013_2']) & (gdfSel['CUT2013_1'].notnull()) & (gdfSel['CUT2013_2'].notnull()) & (gdfSel['CUT2013_3'].notnull()), 'CUT2013'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2013_1'] != gdfSel['CUT2013_3']) & (gdfSel['CUT2013_2'] != gdfSel['CUT2013_3']) & (gdfSel['CUT2013_1'] != gdfSel['CUT2013_2']) & (gdfSel['CUT2013_1'].notnull()) & (gdfSel['CUT2013_2'].notnull()) & (gdfSel['CUT2013_3'].notnull()), 'Coincidencia2013'] = 'F'

# %%
# CUT2014
gdfSel.loc[(gdfSel['CUT2014_1'] == gdfSel['CUT2014_2']) & (gdfSel['CUT2014_3'].isnull()), 'CUT2014'] = gdfSel['CUT2014_1']
gdfSel.loc[(gdfSel['CUT2014_1'] == gdfSel['CUT2014_2']) & (gdfSel['CUT2014_3'].isnull()), 'Coincidencia2014'] = 'EA'
gdfSel.loc[(gdfSel['CUT2014_1'] != gdfSel['CUT2014_2']) & (gdfSel['CUT2014_3'].isnull()), 'CUT2014'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2014_1'] != gdfSel['CUT2014_2']) & (gdfSel['CUT2014_3'].isnull()), 'Coincidencia2014'] = 'AA'
gdfSel.loc[(gdfSel['CUT2014_1'].isnull()) & (gdfSel['CUT2014_2'].isnull()) & (gdfSel['CUT2014_3'].isnull()), 'CUT2014'] = np.nan
gdfSel.loc[(gdfSel['CUT2014_1'].isnull()) & (gdfSel['CUT2014_2'].isnull()) & (gdfSel['CUT2014_3'].isnull()), 'Coincidencia2014'] = 'A'
gdfSel.loc[(gdfSel['CUT2014_1'].notnull()) & (gdfSel['CUT2014_2'].isnull()) & (gdfSel['CUT2014_3'].isnull()), 'CUT2014'] = gdfSel['CUT2014_1']
gdfSel.loc[(gdfSel['CUT2014_1'].notnull()) & (gdfSel['CUT2014_2'].isnull()) & (gdfSel['CUT2014_3'].isnull()), 'Coincidencia2014'] = 'BB'
gdfSel.loc[(gdfSel['CUT2014_1'].isnull()) & (gdfSel['CUT2014_2'].notnull()) & (gdfSel['CUT2014_3'].isnull()), 'CUT2014'] = gdfSel['CUT2014_2']
gdfSel.loc[(gdfSel['CUT2014_1'].isnull()) & (gdfSel['CUT2014_2'].notnull()) & (gdfSel['CUT2014_3'].isnull()), 'Coincidencia2014'] = 'CC'
gdfSel.loc[(gdfSel['CUT2014_1'].isnull()) & (gdfSel['CUT2014_2'].isnull()) & (gdfSel['CUT2014_3'].notnull()), 'CUT2014'] = gdfSel['CUT2014_3']
gdfSel.loc[(gdfSel['CUT2014_1'].isnull()) & (gdfSel['CUT2014_2'].isnull()) & (gdfSel['CUT2014_3'].notnull()), 'Coincidencia2014'] = 'HH'
gdfSel.loc[(gdfSel['CUT2014_1'] == gdfSel['CUT2014_2']) & (gdfSel['CUT2014_3'] == gdfSel['CUT2014_2']) & (gdfSel['CUT2014_1'] == gdfSel['CUT2014_3']) & (gdfSel['CUT2014_1'].notnull()) & (gdfSel['CUT2014_2'].notnull()) & (gdfSel['CUT2014_3'].notnull()), 'CUT2014'] = gdfSel['CUT2014_1']
gdfSel.loc[(gdfSel['CUT2014_1'] == gdfSel['CUT2014_2']) & (gdfSel['CUT2014_3'] == gdfSel['CUT2014_2']) & (gdfSel['CUT2014_1'] == gdfSel['CUT2014_3']) & (gdfSel['CUT2014_1'].notnull()) & (gdfSel['CUT2014_2'].notnull()) & (gdfSel['CUT2014_3'].notnull()), 'Coincidencia2014'] = 'E'
gdfSel.loc[(gdfSel['CUT2014_1'] != gdfSel['CUT2014_2']) & (gdfSel['CUT2014_2'] == gdfSel['CUT2014_3']) & (gdfSel['CUT2014_1'].notnull()) & (gdfSel['CUT2014_2'].notnull()) & (gdfSel['CUT2014_3'].notnull()), 'CUT2014'] = gdfSel['CUT2014_2']
gdfSel.loc[(gdfSel['CUT2014_1'] != gdfSel['CUT2014_2']) & (gdfSel['CUT2014_2'] == gdfSel['CUT2014_3']) & (gdfSel['CUT2014_1'].notnull()) & (gdfSel['CUT2014_2'].notnull()) & (gdfSel['CUT2014_3'].notnull()), 'Coincidencia2014'] = 'B'
gdfSel.loc[(gdfSel['CUT2014_1'] == gdfSel['CUT2014_2']) & (gdfSel['CUT2014_2'] != gdfSel['CUT2014_3']) & (gdfSel['CUT2014_1'].notnull()) & (gdfSel['CUT2014_2'].notnull()) & (gdfSel['CUT2014_3'].notnull()), 'CUT2014'] = gdfSel['CUT2014_1']
gdfSel.loc[(gdfSel['CUT2014_1'] == gdfSel['CUT2014_2']) & (gdfSel['CUT2014_2'] != gdfSel['CUT2014_3']) & (gdfSel['CUT2014_1'].notnull()) & (gdfSel['CUT2014_2'].notnull()) & (gdfSel['CUT2014_3'].notnull()), 'Coincidencia2014'] = 'C'
gdfSel.loc[(gdfSel['CUT2014_1'] == gdfSel['CUT2014_3']) & (gdfSel['CUT2014_2'] != gdfSel['CUT2014_3']) & (gdfSel['CUT2014_1'].notnull()) & (gdfSel['CUT2014_2'].notnull()) & (gdfSel['CUT2014_3'].notnull()), 'CUT2014'] = gdfSel['CUT2014_1']
gdfSel.loc[(gdfSel['CUT2014_1'] == gdfSel['CUT2014_3']) & (gdfSel['CUT2014_2'] != gdfSel['CUT2014_3']) & (gdfSel['CUT2014_1'].notnull()) & (gdfSel['CUT2014_2'].notnull()) & (gdfSel['CUT2014_3'].notnull()), 'Coincidencia2014'] = 'D'
gdfSel.loc[(gdfSel['CUT2014_1'].isnull()) & (gdfSel['CUT2014_2'] == gdfSel['CUT2014_3']) & (gdfSel['CUT2014_3'].notnull()), 'CUT2014'] = gdfSel['CUT2014_2']
gdfSel.loc[(gdfSel['CUT2014_1'].isnull()) & (gdfSel['CUT2014_2'] == gdfSel['CUT2014_3']) & (gdfSel['CUT2014_3'].notnull()), 'Coincidencia2014'] = 'DD'
gdfSel.loc[(gdfSel['CUT2014_1'].isnull()) & (gdfSel['CUT2014_2'] != gdfSel['CUT2014_3']) & (gdfSel['CUT2014_3'].notnull()), 'CUT2014'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2014_1'].isnull()) & (gdfSel['CUT2014_2'] != gdfSel['CUT2014_3']) & (gdfSel['CUT2014_3'].notnull()), 'Coincidencia2014'] = 'FF'
gdfSel.loc[(gdfSel['CUT2014_1'] != gdfSel['CUT2014_3']) & (gdfSel['CUT2014_2'] != gdfSel['CUT2014_3']) & (gdfSel['CUT2014_1'] != gdfSel['CUT2014_2']) & (gdfSel['CUT2014_1'].notnull()) & (gdfSel['CUT2014_2'].notnull()) & (gdfSel['CUT2014_3'].notnull()), 'CUT2014'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2014_1'] != gdfSel['CUT2014_3']) & (gdfSel['CUT2014_2'] != gdfSel['CUT2014_3']) & (gdfSel['CUT2014_1'] != gdfSel['CUT2014_2']) & (gdfSel['CUT2014_1'].notnull()) & (gdfSel['CUT2014_2'].notnull()) & (gdfSel['CUT2014_3'].notnull()), 'Coincidencia2014'] = 'F'



# %%
# CUT2015
gdfSel.loc[(gdfSel['CUT2015_1'] == gdfSel['CUT2015_2']) & (gdfSel['CUT2015_3'].isnull()), 'CUT2015'] = gdfSel['CUT2015_1']
gdfSel.loc[(gdfSel['CUT2015_1'] == gdfSel['CUT2015_2']) & (gdfSel['CUT2015_3'].isnull()), 'Coincidencia2015'] = 'EA'
gdfSel.loc[(gdfSel['CUT2015_1'] != gdfSel['CUT2015_2']) & (gdfSel['CUT2015_3'].isnull()), 'CUT2015'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2015_1'] != gdfSel['CUT2015_2']) & (gdfSel['CUT2015_3'].isnull()), 'Coincidencia2015'] = 'AA'
gdfSel.loc[(gdfSel['CUT2015_1'].isnull()) & (gdfSel['CUT2015_2'].isnull()) & (gdfSel['CUT2015_3'].isnull()), 'CUT2015'] = np.nan
gdfSel.loc[(gdfSel['CUT2015_1'].isnull()) & (gdfSel['CUT2015_2'].isnull()) & (gdfSel['CUT2015_3'].isnull()), 'Coincidencia2015'] = 'A'
gdfSel.loc[(gdfSel['CUT2015_1'].notnull()) & (gdfSel['CUT2015_2'].isnull()) & (gdfSel['CUT2015_3'].isnull()), 'CUT2015'] = gdfSel['CUT2015_1']
gdfSel.loc[(gdfSel['CUT2015_1'].notnull()) & (gdfSel['CUT2015_2'].isnull()) & (gdfSel['CUT2015_3'].isnull()), 'Coincidencia2015'] = 'BB'
gdfSel.loc[(gdfSel['CUT2015_1'].isnull()) & (gdfSel['CUT2015_2'].notnull()) & (gdfSel['CUT2015_3'].isnull()), 'CUT2015'] = gdfSel['CUT2015_2']
gdfSel.loc[(gdfSel['CUT2015_1'].isnull()) & (gdfSel['CUT2015_2'].notnull()) & (gdfSel['CUT2015_3'].isnull()), 'Coincidencia2015'] = 'CC'
gdfSel.loc[(gdfSel['CUT2015_1'].isnull()) & (gdfSel['CUT2015_2'].isnull()) & (gdfSel['CUT2015_3'].notnull()), 'CUT2015'] = gdfSel['CUT2015_3']
gdfSel.loc[(gdfSel['CUT2015_1'].isnull()) & (gdfSel['CUT2015_2'].isnull()) & (gdfSel['CUT2015_3'].notnull()), 'Coincidencia2015'] = 'HH'
gdfSel.loc[(gdfSel['CUT2015_1'] == gdfSel['CUT2015_2']) & (gdfSel['CUT2015_3'] == gdfSel['CUT2015_2']) & (gdfSel['CUT2015_1'] == gdfSel['CUT2015_3']) & (gdfSel['CUT2015_1'].notnull()) & (gdfSel['CUT2015_2'].notnull()) & (gdfSel['CUT2015_3'].notnull()), 'CUT2015'] = gdfSel['CUT2015_1']
gdfSel.loc[(gdfSel['CUT2015_1'] == gdfSel['CUT2015_2']) & (gdfSel['CUT2015_3'] == gdfSel['CUT2015_2']) & (gdfSel['CUT2015_1'] == gdfSel['CUT2015_3']) & (gdfSel['CUT2015_1'].notnull()) & (gdfSel['CUT2015_2'].notnull()) & (gdfSel['CUT2015_3'].notnull()), 'Coincidencia2015'] = 'E'
gdfSel.loc[(gdfSel['CUT2015_1'] != gdfSel['CUT2015_2']) & (gdfSel['CUT2015_2'] == gdfSel['CUT2015_3']) & (gdfSel['CUT2015_1'].notnull()) & (gdfSel['CUT2015_2'].notnull()) & (gdfSel['CUT2015_3'].notnull()), 'CUT2015'] = gdfSel['CUT2015_2']
gdfSel.loc[(gdfSel['CUT2015_1'] != gdfSel['CUT2015_2']) & (gdfSel['CUT2015_2'] == gdfSel['CUT2015_3']) & (gdfSel['CUT2015_1'].notnull()) & (gdfSel['CUT2015_2'].notnull()) & (gdfSel['CUT2015_3'].notnull()), 'Coincidencia2015'] = 'B'
gdfSel.loc[(gdfSel['CUT2015_1'] == gdfSel['CUT2015_2']) & (gdfSel['CUT2015_2'] != gdfSel['CUT2015_3']) & (gdfSel['CUT2015_1'].notnull()) & (gdfSel['CUT2015_2'].notnull()) & (gdfSel['CUT2015_3'].notnull()), 'CUT2015'] = gdfSel['CUT2015_1']
gdfSel.loc[(gdfSel['CUT2015_1'] == gdfSel['CUT2015_2']) & (gdfSel['CUT2015_2'] != gdfSel['CUT2015_3']) & (gdfSel['CUT2015_1'].notnull()) & (gdfSel['CUT2015_2'].notnull()) & (gdfSel['CUT2015_3'].notnull()), 'Coincidencia2015'] = 'C'
gdfSel.loc[(gdfSel['CUT2015_1'] == gdfSel['CUT2015_3']) & (gdfSel['CUT2015_2'] != gdfSel['CUT2015_3']) & (gdfSel['CUT2015_1'].notnull()) & (gdfSel['CUT2015_2'].notnull()) & (gdfSel['CUT2015_3'].notnull()), 'CUT2015'] = gdfSel['CUT2015_1']
gdfSel.loc[(gdfSel['CUT2015_1'] == gdfSel['CUT2015_3']) & (gdfSel['CUT2015_2'] != gdfSel['CUT2015_3']) & (gdfSel['CUT2015_1'].notnull()) & (gdfSel['CUT2015_2'].notnull()) & (gdfSel['CUT2015_3'].notnull()), 'Coincidencia2015'] = 'D'
gdfSel.loc[(gdfSel['CUT2015_1'].isnull()) & (gdfSel['CUT2015_2'] == gdfSel['CUT2015_3']) & (gdfSel['CUT2015_3'].notnull()), 'CUT2015'] = gdfSel['CUT2015_2']
gdfSel.loc[(gdfSel['CUT2015_1'].isnull()) & (gdfSel['CUT2015_2'] == gdfSel['CUT2015_3']) & (gdfSel['CUT2015_3'].notnull()), 'Coincidencia2015'] = 'DD'
gdfSel.loc[(gdfSel['CUT2015_1'].isnull()) & (gdfSel['CUT2015_2'] != gdfSel['CUT2015_3']) & (gdfSel['CUT2015_3'].notnull()), 'CUT2015'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2015_1'].isnull()) & (gdfSel['CUT2015_2'] != gdfSel['CUT2015_3']) & (gdfSel['CUT2015_3'].notnull()), 'Coincidencia2015'] = 'FF'
gdfSel.loc[(gdfSel['CUT2015_1'] != gdfSel['CUT2015_3']) & (gdfSel['CUT2015_2'] != gdfSel['CUT2015_3']) & (gdfSel['CUT2015_1'] != gdfSel['CUT2015_2']) & (gdfSel['CUT2015_1'].notnull()) & (gdfSel['CUT2015_2'].notnull()) & (gdfSel['CUT2015_3'].notnull()), 'CUT2015'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2015_1'] != gdfSel['CUT2015_3']) & (gdfSel['CUT2015_2'] != gdfSel['CUT2015_3']) & (gdfSel['CUT2015_1'] != gdfSel['CUT2015_2']) & (gdfSel['CUT2015_1'].notnull()) & (gdfSel['CUT2015_2'].notnull()) & (gdfSel['CUT2015_3'].notnull()), 'Coincidencia2015'] = 'F'


# %%
# CUT2016
gdfSel.loc[(gdfSel['CUT2016_1'] == gdfSel['CUT2016_2']) & (gdfSel['CUT2016_3'].isnull()), 'CUT2016'] = gdfSel['CUT2016_1']
gdfSel.loc[(gdfSel['CUT2016_1'] == gdfSel['CUT2016_2']) & (gdfSel['CUT2016_3'].isnull()), 'Coincidencia2016'] = 'EA'
gdfSel.loc[(gdfSel['CUT2016_1'] != gdfSel['CUT2016_2']) & (gdfSel['CUT2016_3'].isnull()), 'CUT2016'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2016_1'] != gdfSel['CUT2016_2']) & (gdfSel['CUT2016_3'].isnull()), 'Coincidencia2016'] = 'AA'
gdfSel.loc[(gdfSel['CUT2016_1'].isnull()) & (gdfSel['CUT2016_2'].isnull()) & (gdfSel['CUT2016_3'].isnull()), 'CUT2016'] = np.nan
gdfSel.loc[(gdfSel['CUT2016_1'].isnull()) & (gdfSel['CUT2016_2'].isnull()) & (gdfSel['CUT2016_3'].isnull()), 'Coincidencia2016'] = 'A'
gdfSel.loc[(gdfSel['CUT2016_1'].notnull()) & (gdfSel['CUT2016_2'].isnull()) & (gdfSel['CUT2016_3'].isnull()), 'CUT2016'] = gdfSel['CUT2016_1']
gdfSel.loc[(gdfSel['CUT2016_1'].notnull()) & (gdfSel['CUT2016_2'].isnull()) & (gdfSel['CUT2016_3'].isnull()), 'Coincidencia2016'] = 'BB'
gdfSel.loc[(gdfSel['CUT2016_1'].isnull()) & (gdfSel['CUT2016_2'].notnull()) & (gdfSel['CUT2016_3'].isnull()), 'CUT2016'] = gdfSel['CUT2016_2']
gdfSel.loc[(gdfSel['CUT2016_1'].isnull()) & (gdfSel['CUT2016_2'].notnull()) & (gdfSel['CUT2016_3'].isnull()), 'Coincidencia2016'] = 'CC'
gdfSel.loc[(gdfSel['CUT2016_1'].isnull()) & (gdfSel['CUT2016_2'].isnull()) & (gdfSel['CUT2016_3'].notnull()), 'CUT2016'] = gdfSel['CUT2016_3']
gdfSel.loc[(gdfSel['CUT2016_1'].isnull()) & (gdfSel['CUT2016_2'].isnull()) & (gdfSel['CUT2016_3'].notnull()), 'Coincidencia2016'] = 'HH'
gdfSel.loc[(gdfSel['CUT2016_1'] == gdfSel['CUT2016_2']) & (gdfSel['CUT2016_3'] == gdfSel['CUT2016_2']) & (gdfSel['CUT2016_1'] == gdfSel['CUT2016_3']) & (gdfSel['CUT2016_1'].notnull()) & (gdfSel['CUT2016_2'].notnull()) & (gdfSel['CUT2016_3'].notnull()), 'CUT2016'] = gdfSel['CUT2016_1']
gdfSel.loc[(gdfSel['CUT2016_1'] == gdfSel['CUT2016_2']) & (gdfSel['CUT2016_3'] == gdfSel['CUT2016_2']) & (gdfSel['CUT2016_1'] == gdfSel['CUT2016_3']) & (gdfSel['CUT2016_1'].notnull()) & (gdfSel['CUT2016_2'].notnull()) & (gdfSel['CUT2016_3'].notnull()), 'Coincidencia2016'] = 'E'
gdfSel.loc[(gdfSel['CUT2016_1'] != gdfSel['CUT2016_2']) & (gdfSel['CUT2016_2'] == gdfSel['CUT2016_3']) & (gdfSel['CUT2016_1'].notnull()) & (gdfSel['CUT2016_2'].notnull()) & (gdfSel['CUT2016_3'].notnull()), 'CUT2016'] = gdfSel['CUT2016_2']
gdfSel.loc[(gdfSel['CUT2016_1'] != gdfSel['CUT2016_2']) & (gdfSel['CUT2016_2'] == gdfSel['CUT2016_3']) & (gdfSel['CUT2016_1'].notnull()) & (gdfSel['CUT2016_2'].notnull()) & (gdfSel['CUT2016_3'].notnull()), 'Coincidencia2016'] = 'B'
gdfSel.loc[(gdfSel['CUT2016_1'] == gdfSel['CUT2016_2']) & (gdfSel['CUT2016_2'] != gdfSel['CUT2016_3']) & (gdfSel['CUT2016_1'].notnull()) & (gdfSel['CUT2016_2'].notnull()) & (gdfSel['CUT2016_3'].notnull()), 'CUT2016'] = gdfSel['CUT2016_1']
gdfSel.loc[(gdfSel['CUT2016_1'] == gdfSel['CUT2016_2']) & (gdfSel['CUT2016_2'] != gdfSel['CUT2016_3']) & (gdfSel['CUT2016_1'].notnull()) & (gdfSel['CUT2016_2'].notnull()) & (gdfSel['CUT2016_3'].notnull()), 'Coincidencia2016'] = 'C'
gdfSel.loc[(gdfSel['CUT2016_1'] == gdfSel['CUT2016_3']) & (gdfSel['CUT2016_2'] != gdfSel['CUT2016_3']) & (gdfSel['CUT2016_1'].notnull()) & (gdfSel['CUT2016_2'].notnull()) & (gdfSel['CUT2016_3'].notnull()), 'CUT2016'] = gdfSel['CUT2016_1']
gdfSel.loc[(gdfSel['CUT2016_1'] == gdfSel['CUT2016_3']) & (gdfSel['CUT2016_2'] != gdfSel['CUT2016_3']) & (gdfSel['CUT2016_1'].notnull()) & (gdfSel['CUT2016_2'].notnull()) & (gdfSel['CUT2016_3'].notnull()), 'Coincidencia2016'] = 'D'
gdfSel.loc[(gdfSel['CUT2016_1'].isnull()) & (gdfSel['CUT2016_2'] == gdfSel['CUT2016_3']) & (gdfSel['CUT2016_3'].notnull()), 'CUT2016'] = gdfSel['CUT2016_2']
gdfSel.loc[(gdfSel['CUT2016_1'].isnull()) & (gdfSel['CUT2016_2'] == gdfSel['CUT2016_3']) & (gdfSel['CUT2016_3'].notnull()), 'Coincidencia2016'] = 'DD'
gdfSel.loc[(gdfSel['CUT2016_1'].isnull()) & (gdfSel['CUT2016_2'] != gdfSel['CUT2016_3']) & (gdfSel['CUT2016_3'].notnull()), 'CUT2016'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2016_1'].isnull()) & (gdfSel['CUT2016_2'] != gdfSel['CUT2016_3']) & (gdfSel['CUT2016_3'].notnull()), 'Coincidencia2016'] = 'FF'
gdfSel.loc[(gdfSel['CUT2016_1'] != gdfSel['CUT2016_3']) & (gdfSel['CUT2016_2'] != gdfSel['CUT2016_3']) & (gdfSel['CUT2016_1'] != gdfSel['CUT2016_2']) & (gdfSel['CUT2016_1'].notnull()) & (gdfSel['CUT2016_2'].notnull()) & (gdfSel['CUT2016_3'].notnull()), 'CUT2016'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2016_1'] != gdfSel['CUT2016_3']) & (gdfSel['CUT2016_2'] != gdfSel['CUT2016_3']) & (gdfSel['CUT2016_1'] != gdfSel['CUT2016_2']) & (gdfSel['CUT2016_1'].notnull()) & (gdfSel['CUT2016_2'].notnull()) & (gdfSel['CUT2016_3'].notnull()), 'Coincidencia2016'] = 'F'



# %%
# CUT2017
gdfSel.loc[(gdfSel['CUT2017_1'] == gdfSel['CUT2017_2']) & (gdfSel['CUT2017_3'].isnull()), 'CUT2017'] = gdfSel['CUT2017_1']
gdfSel.loc[(gdfSel['CUT2017_1'] == gdfSel['CUT2017_2']) & (gdfSel['CUT2017_3'].isnull()), 'Coincidencia2017'] = 'EA'
gdfSel.loc[(gdfSel['CUT2017_1'] != gdfSel['CUT2017_2']) & (gdfSel['CUT2017_3'].isnull()), 'CUT2017'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2017_1'] != gdfSel['CUT2017_2']) & (gdfSel['CUT2017_3'].isnull()), 'Coincidencia2017'] = 'AA'
gdfSel.loc[(gdfSel['CUT2017_1'].isnull()) & (gdfSel['CUT2017_2'].isnull()) & (gdfSel['CUT2017_3'].isnull()), 'CUT2017'] = np.nan
gdfSel.loc[(gdfSel['CUT2017_1'].isnull()) & (gdfSel['CUT2017_2'].isnull()) & (gdfSel['CUT2017_3'].isnull()), 'Coincidencia2017'] = 'A'
gdfSel.loc[(gdfSel['CUT2017_1'].notnull()) & (gdfSel['CUT2017_2'].isnull()) & (gdfSel['CUT2017_3'].isnull()), 'CUT2017'] = gdfSel['CUT2017_1']
gdfSel.loc[(gdfSel['CUT2017_1'].notnull()) & (gdfSel['CUT2017_2'].isnull()) & (gdfSel['CUT2017_3'].isnull()), 'Coincidencia2017'] = 'BB'
gdfSel.loc[(gdfSel['CUT2017_1'].isnull()) & (gdfSel['CUT2017_2'].notnull()) & (gdfSel['CUT2017_3'].isnull()), 'CUT2017'] = gdfSel['CUT2017_2']
gdfSel.loc[(gdfSel['CUT2017_1'].isnull()) & (gdfSel['CUT2017_2'].notnull()) & (gdfSel['CUT2017_3'].isnull()), 'Coincidencia2017'] = 'CC'
gdfSel.loc[(gdfSel['CUT2017_1'].isnull()) & (gdfSel['CUT2017_2'].isnull()) & (gdfSel['CUT2017_3'].notnull()), 'CUT2017'] = gdfSel['CUT2017_3']
gdfSel.loc[(gdfSel['CUT2017_1'].isnull()) & (gdfSel['CUT2017_2'].isnull()) & (gdfSel['CUT2017_3'].notnull()), 'Coincidencia2017'] = 'HH'
gdfSel.loc[(gdfSel['CUT2017_1'] == gdfSel['CUT2017_2']) & (gdfSel['CUT2017_3'] == gdfSel['CUT2017_2']) & (gdfSel['CUT2017_1'] == gdfSel['CUT2017_3']) & (gdfSel['CUT2017_1'].notnull()) & (gdfSel['CUT2017_2'].notnull()) & (gdfSel['CUT2017_3'].notnull()), 'CUT2017'] = gdfSel['CUT2017_1']
gdfSel.loc[(gdfSel['CUT2017_1'] == gdfSel['CUT2017_2']) & (gdfSel['CUT2017_3'] == gdfSel['CUT2017_2']) & (gdfSel['CUT2017_1'] == gdfSel['CUT2017_3']) & (gdfSel['CUT2017_1'].notnull()) & (gdfSel['CUT2017_2'].notnull()) & (gdfSel['CUT2017_3'].notnull()), 'Coincidencia2017'] = 'E'
gdfSel.loc[(gdfSel['CUT2017_1'] != gdfSel['CUT2017_2']) & (gdfSel['CUT2017_2'] == gdfSel['CUT2017_3']) & (gdfSel['CUT2017_1'].notnull()) & (gdfSel['CUT2017_2'].notnull()) & (gdfSel['CUT2017_3'].notnull()), 'CUT2017'] = gdfSel['CUT2017_2']
gdfSel.loc[(gdfSel['CUT2017_1'] != gdfSel['CUT2017_2']) & (gdfSel['CUT2017_2'] == gdfSel['CUT2017_3']) & (gdfSel['CUT2017_1'].notnull()) & (gdfSel['CUT2017_2'].notnull()) & (gdfSel['CUT2017_3'].notnull()), 'Coincidencia2017'] = 'B'
gdfSel.loc[(gdfSel['CUT2017_1'] == gdfSel['CUT2017_2']) & (gdfSel['CUT2017_2'] != gdfSel['CUT2017_3']) & (gdfSel['CUT2017_1'].notnull()) & (gdfSel['CUT2017_2'].notnull()) & (gdfSel['CUT2017_3'].notnull()), 'CUT2017'] = gdfSel['CUT2017_1']
gdfSel.loc[(gdfSel['CUT2017_1'] == gdfSel['CUT2017_2']) & (gdfSel['CUT2017_2'] != gdfSel['CUT2017_3']) & (gdfSel['CUT2017_1'].notnull()) & (gdfSel['CUT2017_2'].notnull()) & (gdfSel['CUT2017_3'].notnull()), 'Coincidencia2017'] = 'C'
gdfSel.loc[(gdfSel['CUT2017_1'] == gdfSel['CUT2017_3']) & (gdfSel['CUT2017_2'] != gdfSel['CUT2017_3']) & (gdfSel['CUT2017_1'].notnull()) & (gdfSel['CUT2017_2'].notnull()) & (gdfSel['CUT2017_3'].notnull()), 'CUT2017'] = gdfSel['CUT2017_1']
gdfSel.loc[(gdfSel['CUT2017_1'] == gdfSel['CUT2017_3']) & (gdfSel['CUT2017_2'] != gdfSel['CUT2017_3']) & (gdfSel['CUT2017_1'].notnull()) & (gdfSel['CUT2017_2'].notnull()) & (gdfSel['CUT2017_3'].notnull()), 'Coincidencia2017'] = 'D'
gdfSel.loc[(gdfSel['CUT2017_1'].isnull()) & (gdfSel['CUT2017_2'] == gdfSel['CUT2017_3']) & (gdfSel['CUT2017_3'].notnull()), 'CUT2017'] = gdfSel['CUT2017_2']
gdfSel.loc[(gdfSel['CUT2017_1'].isnull()) & (gdfSel['CUT2017_2'] == gdfSel['CUT2017_3']) & (gdfSel['CUT2017_3'].notnull()), 'Coincidencia2017'] = 'DD'
gdfSel.loc[(gdfSel['CUT2017_1'].isnull()) & (gdfSel['CUT2017_2'] != gdfSel['CUT2017_3']) & (gdfSel['CUT2017_3'].notnull()), 'CUT2017'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2017_1'].isnull()) & (gdfSel['CUT2017_2'] != gdfSel['CUT2017_3']) & (gdfSel['CUT2017_3'].notnull()), 'Coincidencia2017'] = 'FF'
gdfSel.loc[(gdfSel['CUT2017_1'] != gdfSel['CUT2017_3']) & (gdfSel['CUT2017_2'] != gdfSel['CUT2017_3']) & (gdfSel['CUT2017_1'] != gdfSel['CUT2017_2']) & (gdfSel['CUT2017_1'].notnull()) & (gdfSel['CUT2017_2'].notnull()) & (gdfSel['CUT2017_3'].notnull()), 'CUT2017'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2017_1'] != gdfSel['CUT2017_3']) & (gdfSel['CUT2017_2'] != gdfSel['CUT2017_3']) & (gdfSel['CUT2017_1'] != gdfSel['CUT2017_2']) & (gdfSel['CUT2017_1'].notnull()) & (gdfSel['CUT2017_2'].notnull()) & (gdfSel['CUT2017_3'].notnull()), 'Coincidencia2017'] = 'F'


# %%
# CUT2018
gdfSel.loc[(gdfSel['CUT2018_1'] == gdfSel['CUT2018_2']) & (gdfSel['CUT2018_3'].isnull()), 'CUT2018'] = gdfSel['CUT2018_1']
gdfSel.loc[(gdfSel['CUT2018_1'] == gdfSel['CUT2018_2']) & (gdfSel['CUT2018_3'].isnull()), 'Coincidencia2018'] = 'EA'
gdfSel.loc[(gdfSel['CUT2018_1'] != gdfSel['CUT2018_2']) & (gdfSel['CUT2018_3'].isnull()), 'CUT2018'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2018_1'] != gdfSel['CUT2018_2']) & (gdfSel['CUT2018_3'].isnull()), 'Coincidencia2018'] = 'AA'
gdfSel.loc[(gdfSel['CUT2018_1'].isnull()) & (gdfSel['CUT2018_2'].isnull()) & (gdfSel['CUT2018_3'].isnull()), 'CUT2018'] = np.nan
gdfSel.loc[(gdfSel['CUT2018_1'].isnull()) & (gdfSel['CUT2018_2'].isnull()) & (gdfSel['CUT2018_3'].isnull()), 'Coincidencia2018'] = 'A'
gdfSel.loc[(gdfSel['CUT2018_1'].notnull()) & (gdfSel['CUT2018_2'].isnull()) & (gdfSel['CUT2018_3'].isnull()), 'CUT2018'] = gdfSel['CUT2018_1']
gdfSel.loc[(gdfSel['CUT2018_1'].notnull()) & (gdfSel['CUT2018_2'].isnull()) & (gdfSel['CUT2018_3'].isnull()), 'Coincidencia2018'] = 'BB'
gdfSel.loc[(gdfSel['CUT2018_1'].isnull()) & (gdfSel['CUT2018_2'].notnull()) & (gdfSel['CUT2018_3'].isnull()), 'CUT2018'] = gdfSel['CUT2018_2']
gdfSel.loc[(gdfSel['CUT2018_1'].isnull()) & (gdfSel['CUT2018_2'].notnull()) & (gdfSel['CUT2018_3'].isnull()), 'Coincidencia2018'] = 'CC'
gdfSel.loc[(gdfSel['CUT2018_1'].isnull()) & (gdfSel['CUT2018_2'].isnull()) & (gdfSel['CUT2018_3'].notnull()), 'CUT2018'] = gdfSel['CUT2018_3']
gdfSel.loc[(gdfSel['CUT2018_1'].isnull()) & (gdfSel['CUT2018_2'].isnull()) & (gdfSel['CUT2018_3'].notnull()), 'Coincidencia2018'] = 'HH'
gdfSel.loc[(gdfSel['CUT2018_1'] == gdfSel['CUT2018_2']) & (gdfSel['CUT2018_3'] == gdfSel['CUT2018_2']) & (gdfSel['CUT2018_1'] == gdfSel['CUT2018_3']) & (gdfSel['CUT2018_1'].notnull()) & (gdfSel['CUT2018_2'].notnull()) & (gdfSel['CUT2018_3'].notnull()), 'CUT2018'] = gdfSel['CUT2018_1']
gdfSel.loc[(gdfSel['CUT2018_1'] == gdfSel['CUT2018_2']) & (gdfSel['CUT2018_3'] == gdfSel['CUT2018_2']) & (gdfSel['CUT2018_1'] == gdfSel['CUT2018_3']) & (gdfSel['CUT2018_1'].notnull()) & (gdfSel['CUT2018_2'].notnull()) & (gdfSel['CUT2018_3'].notnull()), 'Coincidencia2018'] = 'E'
gdfSel.loc[(gdfSel['CUT2018_1'] != gdfSel['CUT2018_2']) & (gdfSel['CUT2018_2'] == gdfSel['CUT2018_3']) & (gdfSel['CUT2018_1'].notnull()) & (gdfSel['CUT2018_2'].notnull()) & (gdfSel['CUT2018_3'].notnull()), 'CUT2018'] = gdfSel['CUT2018_2']
gdfSel.loc[(gdfSel['CUT2018_1'] != gdfSel['CUT2018_2']) & (gdfSel['CUT2018_2'] == gdfSel['CUT2018_3']) & (gdfSel['CUT2018_1'].notnull()) & (gdfSel['CUT2018_2'].notnull()) & (gdfSel['CUT2018_3'].notnull()), 'Coincidencia2018'] = 'B'
gdfSel.loc[(gdfSel['CUT2018_1'] == gdfSel['CUT2018_2']) & (gdfSel['CUT2018_2'] != gdfSel['CUT2018_3']) & (gdfSel['CUT2018_1'].notnull()) & (gdfSel['CUT2018_2'].notnull()) & (gdfSel['CUT2018_3'].notnull()), 'CUT2018'] = gdfSel['CUT2018_1']
gdfSel.loc[(gdfSel['CUT2018_1'] == gdfSel['CUT2018_2']) & (gdfSel['CUT2018_2'] != gdfSel['CUT2018_3']) & (gdfSel['CUT2018_1'].notnull()) & (gdfSel['CUT2018_2'].notnull()) & (gdfSel['CUT2018_3'].notnull()), 'Coincidencia2018'] = 'C'
gdfSel.loc[(gdfSel['CUT2018_1'] == gdfSel['CUT2018_3']) & (gdfSel['CUT2018_2'] != gdfSel['CUT2018_3']) & (gdfSel['CUT2018_1'].notnull()) & (gdfSel['CUT2018_2'].notnull()) & (gdfSel['CUT2018_3'].notnull()), 'CUT2018'] = gdfSel['CUT2018_1']
gdfSel.loc[(gdfSel['CUT2018_1'] == gdfSel['CUT2018_3']) & (gdfSel['CUT2018_2'] != gdfSel['CUT2018_3']) & (gdfSel['CUT2018_1'].notnull()) & (gdfSel['CUT2018_2'].notnull()) & (gdfSel['CUT2018_3'].notnull()), 'Coincidencia2018'] = 'D'
gdfSel.loc[(gdfSel['CUT2018_1'].isnull()) & (gdfSel['CUT2018_2'] == gdfSel['CUT2018_3']) & (gdfSel['CUT2018_3'].notnull()), 'CUT2018'] = gdfSel['CUT2018_2']
gdfSel.loc[(gdfSel['CUT2018_1'].isnull()) & (gdfSel['CUT2018_2'] == gdfSel['CUT2018_3']) & (gdfSel['CUT2018_3'].notnull()), 'Coincidencia2018'] = 'DD'
gdfSel.loc[(gdfSel['CUT2018_1'].isnull()) & (gdfSel['CUT2018_2'] != gdfSel['CUT2018_3']) & (gdfSel['CUT2018_3'].notnull()), 'CUT2018'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2018_1'].isnull()) & (gdfSel['CUT2018_2'] != gdfSel['CUT2018_3']) & (gdfSel['CUT2018_3'].notnull()), 'Coincidencia2018'] = 'FF'
gdfSel.loc[(gdfSel['CUT2018_1'] != gdfSel['CUT2018_3']) & (gdfSel['CUT2018_2'] != gdfSel['CUT2018_3']) & (gdfSel['CUT2018_1'] != gdfSel['CUT2018_2']) & (gdfSel['CUT2018_1'].notnull()) & (gdfSel['CUT2018_2'].notnull()) & (gdfSel['CUT2018_3'].notnull()), 'CUT2018'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2018_1'] != gdfSel['CUT2018_3']) & (gdfSel['CUT2018_2'] != gdfSel['CUT2018_3']) & (gdfSel['CUT2018_1'] != gdfSel['CUT2018_2']) & (gdfSel['CUT2018_1'].notnull()) & (gdfSel['CUT2018_2'].notnull()) & (gdfSel['CUT2018_3'].notnull()), 'Coincidencia2018'] = 'F'



# %%
# CUT2019
gdfSel.loc[(gdfSel['CUT2019_1'] == gdfSel['CUT2019_2']) & (gdfSel['CUT2019_3'].isnull()), 'CUT2019'] = gdfSel['CUT2019_1']
gdfSel.loc[(gdfSel['CUT2019_1'] == gdfSel['CUT2019_2']) & (gdfSel['CUT2019_3'].isnull()), 'Coincidencia2019'] = 'EA'
gdfSel.loc[(gdfSel['CUT2019_1'] != gdfSel['CUT2019_2']) & (gdfSel['CUT2019_3'].isnull()), 'CUT2019'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2019_1'] != gdfSel['CUT2019_2']) & (gdfSel['CUT2019_3'].isnull()), 'Coincidencia2019'] = 'AA'
gdfSel.loc[(gdfSel['CUT2019_1'].isnull()) & (gdfSel['CUT2019_2'].isnull()) & (gdfSel['CUT2019_3'].isnull()), 'CUT2019'] = np.nan
gdfSel.loc[(gdfSel['CUT2019_1'].isnull()) & (gdfSel['CUT2019_2'].isnull()) & (gdfSel['CUT2019_3'].isnull()), 'Coincidencia2019'] = 'A'
gdfSel.loc[(gdfSel['CUT2019_1'].notnull()) & (gdfSel['CUT2019_2'].isnull()) & (gdfSel['CUT2019_3'].isnull()), 'CUT2019'] = gdfSel['CUT2019_1']
gdfSel.loc[(gdfSel['CUT2019_1'].notnull()) & (gdfSel['CUT2019_2'].isnull()) & (gdfSel['CUT2019_3'].isnull()), 'Coincidencia2019'] = 'BB'
gdfSel.loc[(gdfSel['CUT2019_1'].isnull()) & (gdfSel['CUT2019_2'].notnull()) & (gdfSel['CUT2019_3'].isnull()), 'CUT2019'] = gdfSel['CUT2019_2']
gdfSel.loc[(gdfSel['CUT2019_1'].isnull()) & (gdfSel['CUT2019_2'].notnull()) & (gdfSel['CUT2019_3'].isnull()), 'Coincidencia2019'] = 'CC'
gdfSel.loc[(gdfSel['CUT2019_1'].isnull()) & (gdfSel['CUT2019_2'].isnull()) & (gdfSel['CUT2019_3'].notnull()), 'CUT2019'] = gdfSel['CUT2019_3']
gdfSel.loc[(gdfSel['CUT2019_1'].isnull()) & (gdfSel['CUT2019_2'].isnull()) & (gdfSel['CUT2019_3'].notnull()), 'Coincidencia2019'] = 'HH'
gdfSel.loc[(gdfSel['CUT2019_1'] == gdfSel['CUT2019_2']) & (gdfSel['CUT2019_3'] == gdfSel['CUT2019_2']) & (gdfSel['CUT2019_1'] == gdfSel['CUT2019_3']) & (gdfSel['CUT2019_1'].notnull()) & (gdfSel['CUT2019_2'].notnull()) & (gdfSel['CUT2019_3'].notnull()), 'CUT2019'] = gdfSel['CUT2019_1']
gdfSel.loc[(gdfSel['CUT2019_1'] == gdfSel['CUT2019_2']) & (gdfSel['CUT2019_3'] == gdfSel['CUT2019_2']) & (gdfSel['CUT2019_1'] == gdfSel['CUT2019_3']) & (gdfSel['CUT2019_1'].notnull()) & (gdfSel['CUT2019_2'].notnull()) & (gdfSel['CUT2019_3'].notnull()), 'Coincidencia2019'] = 'E'
gdfSel.loc[(gdfSel['CUT2019_1'] != gdfSel['CUT2019_2']) & (gdfSel['CUT2019_2'] == gdfSel['CUT2019_3']) & (gdfSel['CUT2019_1'].notnull()) & (gdfSel['CUT2019_2'].notnull()) & (gdfSel['CUT2019_3'].notnull()), 'CUT2019'] = gdfSel['CUT2019_2']
gdfSel.loc[(gdfSel['CUT2019_1'] != gdfSel['CUT2019_2']) & (gdfSel['CUT2019_2'] == gdfSel['CUT2019_3']) & (gdfSel['CUT2019_1'].notnull()) & (gdfSel['CUT2019_2'].notnull()) & (gdfSel['CUT2019_3'].notnull()), 'Coincidencia2019'] = 'B'
gdfSel.loc[(gdfSel['CUT2019_1'] == gdfSel['CUT2019_2']) & (gdfSel['CUT2019_2'] != gdfSel['CUT2019_3']) & (gdfSel['CUT2019_1'].notnull()) & (gdfSel['CUT2019_2'].notnull()) & (gdfSel['CUT2019_3'].notnull()), 'CUT2019'] = gdfSel['CUT2019_1']
gdfSel.loc[(gdfSel['CUT2019_1'] == gdfSel['CUT2019_2']) & (gdfSel['CUT2019_2'] != gdfSel['CUT2019_3']) & (gdfSel['CUT2019_1'].notnull()) & (gdfSel['CUT2019_2'].notnull()) & (gdfSel['CUT2019_3'].notnull()), 'Coincidencia2019'] = 'C'
gdfSel.loc[(gdfSel['CUT2019_1'] == gdfSel['CUT2019_3']) & (gdfSel['CUT2019_2'] != gdfSel['CUT2019_3']) & (gdfSel['CUT2019_1'].notnull()) & (gdfSel['CUT2019_2'].notnull()) & (gdfSel['CUT2019_3'].notnull()), 'CUT2019'] = gdfSel['CUT2019_1']
gdfSel.loc[(gdfSel['CUT2019_1'] == gdfSel['CUT2019_3']) & (gdfSel['CUT2019_2'] != gdfSel['CUT2019_3']) & (gdfSel['CUT2019_1'].notnull()) & (gdfSel['CUT2019_2'].notnull()) & (gdfSel['CUT2019_3'].notnull()), 'Coincidencia2019'] = 'D'
gdfSel.loc[(gdfSel['CUT2019_1'].isnull()) & (gdfSel['CUT2019_2'] == gdfSel['CUT2019_3']) & (gdfSel['CUT2019_3'].notnull()), 'CUT2019'] = gdfSel['CUT2019_2']
gdfSel.loc[(gdfSel['CUT2019_1'].isnull()) & (gdfSel['CUT2019_2'] == gdfSel['CUT2019_3']) & (gdfSel['CUT2019_3'].notnull()), 'Coincidencia2019'] = 'DD'
gdfSel.loc[(gdfSel['CUT2019_1'].isnull()) & (gdfSel['CUT2019_2'] != gdfSel['CUT2019_3']) & (gdfSel['CUT2019_3'].notnull()), 'CUT2019'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2019_1'].isnull()) & (gdfSel['CUT2019_2'] != gdfSel['CUT2019_3']) & (gdfSel['CUT2019_3'].notnull()), 'Coincidencia2019'] = 'FF'
gdfSel.loc[(gdfSel['CUT2019_1'] != gdfSel['CUT2019_3']) & (gdfSel['CUT2019_2'] != gdfSel['CUT2019_3']) & (gdfSel['CUT2019_1'] != gdfSel['CUT2019_2']) & (gdfSel['CUT2019_1'].notnull()) & (gdfSel['CUT2019_2'].notnull()) & (gdfSel['CUT2019_3'].notnull()), 'CUT2019'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2019_1'] != gdfSel['CUT2019_3']) & (gdfSel['CUT2019_2'] != gdfSel['CUT2019_3']) & (gdfSel['CUT2019_1'] != gdfSel['CUT2019_2']) & (gdfSel['CUT2019_1'].notnull()) & (gdfSel['CUT2019_2'].notnull()) & (gdfSel['CUT2019_3'].notnull()), 'Coincidencia2019'] = 'F'



# %%
# CUT2020
gdfSel.loc[(gdfSel['CUT2020_1'] == gdfSel['CUT2020_2']) & (gdfSel['CUT2020_3'].isnull()), 'CUT2020'] = gdfSel['CUT2020_1']
gdfSel.loc[(gdfSel['CUT2020_1'] == gdfSel['CUT2020_2']) & (gdfSel['CUT2020_3'].isnull()), 'Coincidencia2020'] = 'EA'
gdfSel.loc[(gdfSel['CUT2020_1'] != gdfSel['CUT2020_2']) & (gdfSel['CUT2020_3'].isnull()), 'CUT2020'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2020_1'] != gdfSel['CUT2020_2']) & (gdfSel['CUT2020_3'].isnull()), 'Coincidencia2020'] = 'AA'
gdfSel.loc[(gdfSel['CUT2020_1'].isnull()) & (gdfSel['CUT2020_2'].isnull()) & (gdfSel['CUT2020_3'].isnull()), 'CUT2020'] = np.nan
gdfSel.loc[(gdfSel['CUT2020_1'].isnull()) & (gdfSel['CUT2020_2'].isnull()) & (gdfSel['CUT2020_3'].isnull()), 'Coincidencia2020'] = 'A'
gdfSel.loc[(gdfSel['CUT2020_1'].notnull()) & (gdfSel['CUT2020_2'].isnull()) & (gdfSel['CUT2020_3'].isnull()), 'CUT2020'] = gdfSel['CUT2020_1']
gdfSel.loc[(gdfSel['CUT2020_1'].notnull()) & (gdfSel['CUT2020_2'].isnull()) & (gdfSel['CUT2020_3'].isnull()), 'Coincidencia2020'] = 'BB'
gdfSel.loc[(gdfSel['CUT2020_1'].isnull()) & (gdfSel['CUT2020_2'].notnull()) & (gdfSel['CUT2020_3'].isnull()), 'CUT2020'] = gdfSel['CUT2020_2']
gdfSel.loc[(gdfSel['CUT2020_1'].isnull()) & (gdfSel['CUT2020_2'].notnull()) & (gdfSel['CUT2020_3'].isnull()), 'Coincidencia2020'] = 'CC'
gdfSel.loc[(gdfSel['CUT2020_1'].isnull()) & (gdfSel['CUT2020_2'].isnull()) & (gdfSel['CUT2020_3'].notnull()), 'CUT2020'] = gdfSel['CUT2020_3']
gdfSel.loc[(gdfSel['CUT2020_1'].isnull()) & (gdfSel['CUT2020_2'].isnull()) & (gdfSel['CUT2020_3'].notnull()), 'Coincidencia2020'] = 'HH'
gdfSel.loc[(gdfSel['CUT2020_1'] == gdfSel['CUT2020_2']) & (gdfSel['CUT2020_3'] == gdfSel['CUT2020_2']) & (gdfSel['CUT2020_1'] == gdfSel['CUT2020_3']) & (gdfSel['CUT2020_1'].notnull()) & (gdfSel['CUT2020_2'].notnull()) & (gdfSel['CUT2020_3'].notnull()), 'CUT2020'] = gdfSel['CUT2020_1']
gdfSel.loc[(gdfSel['CUT2020_1'] == gdfSel['CUT2020_2']) & (gdfSel['CUT2020_3'] == gdfSel['CUT2020_2']) & (gdfSel['CUT2020_1'] == gdfSel['CUT2020_3']) & (gdfSel['CUT2020_1'].notnull()) & (gdfSel['CUT2020_2'].notnull()) & (gdfSel['CUT2020_3'].notnull()), 'Coincidencia2020'] = 'E'
gdfSel.loc[(gdfSel['CUT2020_1'] != gdfSel['CUT2020_2']) & (gdfSel['CUT2020_2'] == gdfSel['CUT2020_3']) & (gdfSel['CUT2020_1'].notnull()) & (gdfSel['CUT2020_2'].notnull()) & (gdfSel['CUT2020_3'].notnull()), 'CUT2020'] = gdfSel['CUT2020_2']
gdfSel.loc[(gdfSel['CUT2020_1'] != gdfSel['CUT2020_2']) & (gdfSel['CUT2020_2'] == gdfSel['CUT2020_3']) & (gdfSel['CUT2020_1'].notnull()) & (gdfSel['CUT2020_2'].notnull()) & (gdfSel['CUT2020_3'].notnull()), 'Coincidencia2020'] = 'B'
gdfSel.loc[(gdfSel['CUT2020_1'] == gdfSel['CUT2020_2']) & (gdfSel['CUT2020_2'] != gdfSel['CUT2020_3']) & (gdfSel['CUT2020_1'].notnull()) & (gdfSel['CUT2020_2'].notnull()) & (gdfSel['CUT2020_3'].notnull()), 'CUT2020'] = gdfSel['CUT2020_1']
gdfSel.loc[(gdfSel['CUT2020_1'] == gdfSel['CUT2020_2']) & (gdfSel['CUT2020_2'] != gdfSel['CUT2020_3']) & (gdfSel['CUT2020_1'].notnull()) & (gdfSel['CUT2020_2'].notnull()) & (gdfSel['CUT2020_3'].notnull()), 'Coincidencia2020'] = 'C'
gdfSel.loc[(gdfSel['CUT2020_1'] == gdfSel['CUT2020_3']) & (gdfSel['CUT2020_2'] != gdfSel['CUT2020_3']) & (gdfSel['CUT2020_1'].notnull()) & (gdfSel['CUT2020_2'].notnull()) & (gdfSel['CUT2020_3'].notnull()), 'CUT2020'] = gdfSel['CUT2020_1']
gdfSel.loc[(gdfSel['CUT2020_1'] == gdfSel['CUT2020_3']) & (gdfSel['CUT2020_2'] != gdfSel['CUT2020_3']) & (gdfSel['CUT2020_1'].notnull()) & (gdfSel['CUT2020_2'].notnull()) & (gdfSel['CUT2020_3'].notnull()), 'Coincidencia2020'] = 'D'
gdfSel.loc[(gdfSel['CUT2020_1'].isnull()) & (gdfSel['CUT2020_2'] == gdfSel['CUT2020_3']) & (gdfSel['CUT2020_3'].notnull()), 'CUT2020'] = gdfSel['CUT2020_2']
gdfSel.loc[(gdfSel['CUT2020_1'].isnull()) & (gdfSel['CUT2020_2'] == gdfSel['CUT2020_3']) & (gdfSel['CUT2020_3'].notnull()), 'Coincidencia2020'] = 'DD'
gdfSel.loc[(gdfSel['CUT2020_1'].isnull()) & (gdfSel['CUT2020_2'] != gdfSel['CUT2020_3']) & (gdfSel['CUT2020_3'].notnull()), 'CUT2020'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2020_1'].isnull()) & (gdfSel['CUT2020_2'] != gdfSel['CUT2020_3']) & (gdfSel['CUT2020_3'].notnull()), 'Coincidencia2020'] = 'FF'
gdfSel.loc[(gdfSel['CUT2020_1'] != gdfSel['CUT2020_3']) & (gdfSel['CUT2020_2'] != gdfSel['CUT2020_3']) & (gdfSel['CUT2020_1'] != gdfSel['CUT2020_2']) & (gdfSel['CUT2020_1'].notnull()) & (gdfSel['CUT2020_2'].notnull()) & (gdfSel['CUT2020_3'].notnull()), 'CUT2020'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2020_1'] != gdfSel['CUT2020_3']) & (gdfSel['CUT2020_2'] != gdfSel['CUT2020_3']) & (gdfSel['CUT2020_1'] != gdfSel['CUT2020_2']) & (gdfSel['CUT2020_1'].notnull()) & (gdfSel['CUT2020_2'].notnull()) & (gdfSel['CUT2020_3'].notnull()), 'Coincidencia2020'] = 'F'



# %%
# CUT2021
gdfSel.loc[(gdfSel['CUT2021_1'] == gdfSel['CUT2021_2']) & (gdfSel['CUT2021_3'].isnull()), 'CUT2021'] = gdfSel['CUT2021_1']
gdfSel.loc[(gdfSel['CUT2021_1'] == gdfSel['CUT2021_2']) & (gdfSel['CUT2021_3'].isnull()), 'Coincidencia2021'] = 'EA'
gdfSel.loc[(gdfSel['CUT2021_1'] != gdfSel['CUT2021_2']) & (gdfSel['CUT2021_3'].isnull()), 'CUT2021'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2021_1'] != gdfSel['CUT2021_2']) & (gdfSel['CUT2021_3'].isnull()), 'Coincidencia2021'] = 'AA'
gdfSel.loc[(gdfSel['CUT2021_1'].isnull()) & (gdfSel['CUT2021_2'].isnull()) & (gdfSel['CUT2021_3'].isnull()), 'CUT2021'] = np.nan
gdfSel.loc[(gdfSel['CUT2021_1'].isnull()) & (gdfSel['CUT2021_2'].isnull()) & (gdfSel['CUT2021_3'].isnull()), 'Coincidencia2021'] = 'A'
gdfSel.loc[(gdfSel['CUT2021_1'].notnull()) & (gdfSel['CUT2021_2'].isnull()) & (gdfSel['CUT2021_3'].isnull()), 'CUT2021'] = gdfSel['CUT2021_1']
gdfSel.loc[(gdfSel['CUT2021_1'].notnull()) & (gdfSel['CUT2021_2'].isnull()) & (gdfSel['CUT2021_3'].isnull()), 'Coincidencia2021'] = 'BB'
gdfSel.loc[(gdfSel['CUT2021_1'].isnull()) & (gdfSel['CUT2021_2'].notnull()) & (gdfSel['CUT2021_3'].isnull()), 'CUT2021'] = gdfSel['CUT2021_2']
gdfSel.loc[(gdfSel['CUT2021_1'].isnull()) & (gdfSel['CUT2021_2'].notnull()) & (gdfSel['CUT2021_3'].isnull()), 'Coincidencia2021'] = 'CC'
gdfSel.loc[(gdfSel['CUT2021_1'].isnull()) & (gdfSel['CUT2021_2'].isnull()) & (gdfSel['CUT2021_3'].notnull()), 'CUT2021'] = gdfSel['CUT2021_3']
gdfSel.loc[(gdfSel['CUT2021_1'].isnull()) & (gdfSel['CUT2021_2'].isnull()) & (gdfSel['CUT2021_3'].notnull()), 'Coincidencia2021'] = 'HH'
gdfSel.loc[(gdfSel['CUT2021_1'] == gdfSel['CUT2021_2']) & (gdfSel['CUT2021_3'] == gdfSel['CUT2021_2']) & (gdfSel['CUT2021_1'] == gdfSel['CUT2021_3']) & (gdfSel['CUT2021_1'].notnull()) & (gdfSel['CUT2021_2'].notnull()) & (gdfSel['CUT2021_3'].notnull()), 'CUT2021'] = gdfSel['CUT2021_1']
gdfSel.loc[(gdfSel['CUT2021_1'] == gdfSel['CUT2021_2']) & (gdfSel['CUT2021_3'] == gdfSel['CUT2021_2']) & (gdfSel['CUT2021_1'] == gdfSel['CUT2021_3']) & (gdfSel['CUT2021_1'].notnull()) & (gdfSel['CUT2021_2'].notnull()) & (gdfSel['CUT2021_3'].notnull()), 'Coincidencia2021'] = 'E'
gdfSel.loc[(gdfSel['CUT2021_1'] != gdfSel['CUT2021_2']) & (gdfSel['CUT2021_2'] == gdfSel['CUT2021_3']) & (gdfSel['CUT2021_1'].notnull()) & (gdfSel['CUT2021_2'].notnull()) & (gdfSel['CUT2021_3'].notnull()), 'CUT2021'] = gdfSel['CUT2021_2']
gdfSel.loc[(gdfSel['CUT2021_1'] != gdfSel['CUT2021_2']) & (gdfSel['CUT2021_2'] == gdfSel['CUT2021_3']) & (gdfSel['CUT2021_1'].notnull()) & (gdfSel['CUT2021_2'].notnull()) & (gdfSel['CUT2021_3'].notnull()), 'Coincidencia2021'] = 'B'
gdfSel.loc[(gdfSel['CUT2021_1'] == gdfSel['CUT2021_2']) & (gdfSel['CUT2021_2'] != gdfSel['CUT2021_3']) & (gdfSel['CUT2021_1'].notnull()) & (gdfSel['CUT2021_2'].notnull()) & (gdfSel['CUT2021_3'].notnull()), 'CUT2021'] = gdfSel['CUT2021_1']
gdfSel.loc[(gdfSel['CUT2021_1'] == gdfSel['CUT2021_2']) & (gdfSel['CUT2021_2'] != gdfSel['CUT2021_3']) & (gdfSel['CUT2021_1'].notnull()) & (gdfSel['CUT2021_2'].notnull()) & (gdfSel['CUT2021_3'].notnull()), 'Coincidencia2021'] = 'C'
gdfSel.loc[(gdfSel['CUT2021_1'] == gdfSel['CUT2021_3']) & (gdfSel['CUT2021_2'] != gdfSel['CUT2021_3']) & (gdfSel['CUT2021_1'].notnull()) & (gdfSel['CUT2021_2'].notnull()) & (gdfSel['CUT2021_3'].notnull()), 'CUT2021'] = gdfSel['CUT2021_1']
gdfSel.loc[(gdfSel['CUT2021_1'] == gdfSel['CUT2021_3']) & (gdfSel['CUT2021_2'] != gdfSel['CUT2021_3']) & (gdfSel['CUT2021_1'].notnull()) & (gdfSel['CUT2021_2'].notnull()) & (gdfSel['CUT2021_3'].notnull()), 'Coincidencia2021'] = 'D'
gdfSel.loc[(gdfSel['CUT2021_1'].isnull()) & (gdfSel['CUT2021_2'] == gdfSel['CUT2021_3']) & (gdfSel['CUT2021_3'].notnull()), 'CUT2021'] = gdfSel['CUT2021_2']
gdfSel.loc[(gdfSel['CUT2021_1'].isnull()) & (gdfSel['CUT2021_2'] == gdfSel['CUT2021_3']) & (gdfSel['CUT2021_3'].notnull()), 'Coincidencia2021'] = 'DD'
gdfSel.loc[(gdfSel['CUT2021_1'].isnull()) & (gdfSel['CUT2021_2'] != gdfSel['CUT2021_3']) & (gdfSel['CUT2021_3'].notnull()), 'CUT2021'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2021_1'].isnull()) & (gdfSel['CUT2021_2'] != gdfSel['CUT2021_3']) & (gdfSel['CUT2021_3'].notnull()), 'Coincidencia2021'] = 'FF'
gdfSel.loc[(gdfSel['CUT2021_1'] != gdfSel['CUT2021_3']) & (gdfSel['CUT2021_2'] != gdfSel['CUT2021_3']) & (gdfSel['CUT2021_1'] != gdfSel['CUT2021_2']) & (gdfSel['CUT2021_1'].notnull()) & (gdfSel['CUT2021_2'].notnull()) & (gdfSel['CUT2021_3'].notnull()), 'CUT2021'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2021_1'] != gdfSel['CUT2021_3']) & (gdfSel['CUT2021_2'] != gdfSel['CUT2021_3']) & (gdfSel['CUT2021_1'] != gdfSel['CUT2021_2']) & (gdfSel['CUT2021_1'].notnull()) & (gdfSel['CUT2021_2'].notnull()) & (gdfSel['CUT2021_3'].notnull()), 'Coincidencia2021'] = 'F'

# %%
#CUT2022

gdfSel.loc[(gdfSel['CUT2022_1'] == gdfSel['CUT2022_2']) & (gdfSel['CUT2022_3'].isnull()), 'CUT2022'] = gdfSel['CUT2022_1']
gdfSel.loc[(gdfSel['CUT2022_1'] == gdfSel['CUT2022_2']) & (gdfSel['CUT2022_3'].isnull()), 'Coincidencia2022'] = 'EA'
gdfSel.loc[(gdfSel['CUT2022_1'] != gdfSel['CUT2022_2']) & (gdfSel['CUT2022_3'].isnull()), 'CUT2022'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2022_1'] != gdfSel['CUT2022_2']) & (gdfSel['CUT2022_3'].isnull()), 'Coincidencia2022'] = 'AA'
gdfSel.loc[(gdfSel['CUT2022_1'].isnull()) & (gdfSel['CUT2022_2'].isnull()) & (gdfSel['CUT2022_3'].isnull()), 'CUT2022'] = np.nan
gdfSel.loc[(gdfSel['CUT2022_1'].isnull()) & (gdfSel['CUT2022_2'].isnull()) & (gdfSel['CUT2022_3'].isnull()), 'Coincidencia2022'] = 'A'
gdfSel.loc[(gdfSel['CUT2022_1'].notnull()) & (gdfSel['CUT2022_2'].isnull()) & (gdfSel['CUT2022_3'].isnull()), 'CUT2022'] = gdfSel['CUT2022_1']
gdfSel.loc[(gdfSel['CUT2022_1'].notnull()) & (gdfSel['CUT2022_2'].isnull()) & (gdfSel['CUT2022_3'].isnull()), 'Coincidencia2022'] = 'BB'
gdfSel.loc[(gdfSel['CUT2022_1'].isnull()) & (gdfSel['CUT2022_2'].notnull()) & (gdfSel['CUT2022_3'].isnull()), 'CUT2022'] = gdfSel['CUT2022_2']
gdfSel.loc[(gdfSel['CUT2022_1'].isnull()) & (gdfSel['CUT2022_2'].notnull()) & (gdfSel['CUT2022_3'].isnull()), 'Coincidencia2022'] = 'CC'
gdfSel.loc[(gdfSel['CUT2022_1'].isnull()) & (gdfSel['CUT2022_2'].isnull()) & (gdfSel['CUT2022_3'].notnull()), 'CUT2022'] = gdfSel['CUT2022_3']
gdfSel.loc[(gdfSel['CUT2022_1'].isnull()) & (gdfSel['CUT2022_2'].isnull()) & (gdfSel['CUT2022_3'].notnull()), 'Coincidencia2022'] = 'HH'
gdfSel.loc[(gdfSel['CUT2022_1'] == gdfSel['CUT2022_2']) & (gdfSel['CUT2022_3'] == gdfSel['CUT2022_2']) & (gdfSel['CUT2022_1'] == gdfSel['CUT2022_3']) & (gdfSel['CUT2022_1'].notnull()) & (gdfSel['CUT2022_2'].notnull()) & (gdfSel['CUT2022_3'].notnull()), 'CUT2022'] = gdfSel['CUT2022_1']
gdfSel.loc[(gdfSel['CUT2022_1'] == gdfSel['CUT2022_2']) & (gdfSel['CUT2022_3'] == gdfSel['CUT2022_2']) & (gdfSel['CUT2022_1'] == gdfSel['CUT2022_3']) & (gdfSel['CUT2022_1'].notnull()) & (gdfSel['CUT2022_2'].notnull()) & (gdfSel['CUT2022_3'].notnull()), 'Coincidencia2022'] = 'E'
gdfSel.loc[(gdfSel['CUT2022_1'] != gdfSel['CUT2022_2']) & (gdfSel['CUT2022_2'] == gdfSel['CUT2022_3']) & (gdfSel['CUT2022_1'].notnull()) & (gdfSel['CUT2022_2'].notnull()) & (gdfSel['CUT2022_3'].notnull()), 'CUT2022'] = gdfSel['CUT2022_2']
gdfSel.loc[(gdfSel['CUT2022_1'] != gdfSel['CUT2022_2']) & (gdfSel['CUT2022_2'] == gdfSel['CUT2022_3']) & (gdfSel['CUT2022_1'].notnull()) & (gdfSel['CUT2022_2'].notnull()) & (gdfSel['CUT2022_3'].notnull()), 'Coincidencia2022'] = 'B'
gdfSel.loc[(gdfSel['CUT2022_1'] == gdfSel['CUT2022_2']) & (gdfSel['CUT2022_2'] != gdfSel['CUT2022_3']) & (gdfSel['CUT2022_1'].notnull()) & (gdfSel['CUT2022_2'].notnull()) & (gdfSel['CUT2022_3'].notnull()), 'CUT2022'] = gdfSel['CUT2022_1']
gdfSel.loc[(gdfSel['CUT2022_1'] == gdfSel['CUT2022_2']) & (gdfSel['CUT2022_2'] != gdfSel['CUT2022_3']) & (gdfSel['CUT2022_1'].notnull()) & (gdfSel['CUT2022_2'].notnull()) & (gdfSel['CUT2022_3'].notnull()), 'Coincidencia2022'] = 'C'
gdfSel.loc[(gdfSel['CUT2022_1'] == gdfSel['CUT2022_3']) & (gdfSel['CUT2022_2'] != gdfSel['CUT2022_3']) & (gdfSel['CUT2022_1'].notnull()) & (gdfSel['CUT2022_2'].notnull()) & (gdfSel['CUT2022_3'].notnull()), 'CUT2022'] = gdfSel['CUT2022_1']
gdfSel.loc[(gdfSel['CUT2022_1'] == gdfSel['CUT2022_3']) & (gdfSel['CUT2022_2'] != gdfSel['CUT2022_3']) & (gdfSel['CUT2022_1'].notnull()) & (gdfSel['CUT2022_2'].notnull()) & (gdfSel['CUT2022_3'].notnull()), 'Coincidencia2022'] = 'D'
gdfSel.loc[(gdfSel['CUT2022_1'].isnull()) & (gdfSel['CUT2022_2'] == gdfSel['CUT2022_3']) & (gdfSel['CUT2022_3'].notnull()), 'CUT2022'] = gdfSel['CUT2022_2']
gdfSel.loc[(gdfSel['CUT2022_1'].isnull()) & (gdfSel['CUT2022_2'] == gdfSel['CUT2022_3']) & (gdfSel['CUT2022_3'].notnull()), 'Coincidencia2022'] = 'DD'
gdfSel.loc[(gdfSel['CUT2022_1'].isnull()) & (gdfSel['CUT2022_2'] != gdfSel['CUT2022_3']) & (gdfSel['CUT2022_3'].notnull()), 'CUT2022'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2022_1'].isnull()) & (gdfSel['CUT2022_2'] != gdfSel['CUT2022_3']) & (gdfSel['CUT2022_3'].notnull()), 'Coincidencia2022'] = 'FF'
gdfSel.loc[(gdfSel['CUT2022_1'] != gdfSel['CUT2022_3']) & (gdfSel['CUT2022_2'] != gdfSel['CUT2022_3']) & (gdfSel['CUT2022_1'] != gdfSel['CUT2022_2']) & (gdfSel['CUT2022_1'].notnull()) & (gdfSel['CUT2022_2'].notnull()) & (gdfSel['CUT2022_3'].notnull()), 'CUT2022'] = 'Evaluar'
gdfSel.loc[(gdfSel['CUT2022_1'] != gdfSel['CUT2022_3']) & (gdfSel['CUT2022_2'] != gdfSel['CUT2022_3']) & (gdfSel['CUT2022_1'] != gdfSel['CUT2022_2']) & (gdfSel['CUT2022_1'].notnull()) & (gdfSel['CUT2022_2'].notnull()) & (gdfSel['CUT2022_3'].notnull()), 'Coincidencia2022'] = 'F'





#%%


print("Tipos de coincidencia 2000: ", gdfSel['Coincidencia2000'].value_counts())
print("Tipos de coincidencia 2008: ", gdfSel['Coincidencia2008'].value_counts())
print("Tipos de coincidencia 2012: ", gdfSel['Coincidencia2012'].value_counts())
print("Tipos de coincidencia 2013: ", gdfSel['Coincidencia2013'].value_counts())
print("Tipos de coincidencia 2014: ", gdfSel['Coincidencia2014'].value_counts())
print("Tipos de coincidencia 2015: ", gdfSel['Coincidencia2015'].value_counts())
print("Tipos de coincidencia 2016: ", gdfSel['Coincidencia2016'].value_counts())
print("Tipos de coincidencia 2017: ", gdfSel['Coincidencia2017'].value_counts())
print("Tipos de coincidencia 2018: ", gdfSel['Coincidencia2018'].value_counts())
print("Tipos de coincidencia 2019: ", gdfSel['Coincidencia2019'].value_counts())
print("Tipos de coincidencia 2020: ", gdfSel['Coincidencia2020'].value_counts())
print("Tipos de coincidencia 2021: ", gdfSel['Coincidencia2021'].value_counts())
print("Tipos de coincidencia 2022: ", gdfSel['Coincidencia2022'].value_counts())
# %%
gdfchange = gdfSel[["plotid", "sampleid", "lon", "lat", "geometry", "pl_id", "pl_cluster", "pl_monimages", "email1", "email2", "email3", 'CUT2000', 'Coincidencia2000', 'CUT2008', 'Coincidencia2008', 'CUT2012', 'Coincidencia2012', 'CUT2013', 'Coincidencia2013', 'CUT2014', 'Coincidencia2014', 'CUT2015', 'Coincidencia2015', 'CUT2016', 'Coincidencia2016', 'CUT2017', 'Coincidencia2017', 'CUT2018', 'Coincidencia2018', 'CUT2019', 'Coincidencia2019', 'CUT2020', 'Coincidencia2020', 'CUT2021', 'Coincidencia2021', 'CUT2022', 'Coincidencia2022']]
#aggregation_functions = {'plotid': 'first', 'lon': 'first', 'lat': 'first', 'geometry': 'first', 'pl_id': 'first', 'pl_cluster': 'first', 'email1': 'first', 'email2': 'first','email3': 'first','CUT2000': 'first', 'Coincidencia2000': 'first', 'CUT2008': 'first', 'Coincidencia2008': 'first', 'CUT2012': 'first', 'Coincidencia2012': 'first', 'CUT2013': 'first', 'Coincidencia2013': 'first', 'CUT2014': 'first', 'Coincidencia2014': 'first', 'CUT2015': 'first', 'Coincidencia2015': 'first', 'CUT2016': 'first', 'Coincidencia2016': 'first', 'CUT2017': 'first', 'Coincidencia2017': 'first', 'CUT2018': 'first', 'Coincidencia2018': 'first', 'CUT2019': 'first', 'Coincidencia2019': 'first', 'CUT2020': 'first', 'Coincidencia2020': 'first', 'CUT2021': 'first', 'Coincidencia2021': 'first', 'CUT2022': 'first', 'Coincidencia2022': 'first'}
#gdfchangeN = gdfchange.groupby(gdfchange['plotid']).aggregate(aggregation_functions)
gdfchangeN = gdfchange.copy()
# %%
# %%
print("Tipos de coincidencia 2000: ", gdfchangeN['Coincidencia2000'].value_counts())
print("Tipos de coincidencia 2008: ", gdfchangeN['Coincidencia2008'].value_counts())
print("Tipos de coincidencia 2012: ", gdfchangeN['Coincidencia2012'].value_counts())
print("Tipos de coincidencia 2013: ", gdfchangeN['Coincidencia2013'].value_counts())
print("Tipos de coincidencia 2014: ", gdfchangeN['Coincidencia2014'].value_counts())
print("Tipos de coincidencia 2015: ", gdfchangeN['Coincidencia2015'].value_counts())
print("Tipos de coincidencia 2016: ", gdfchangeN['Coincidencia2016'].value_counts())
print("Tipos de coincidencia 2017: ", gdfchangeN['Coincidencia2017'].value_counts())
print("Tipos de coincidencia 2018: ", gdfchangeN['Coincidencia2018'].value_counts())
print("Tipos de coincidencia 2019: ", gdfchangeN['Coincidencia2019'].value_counts())
print("Tipos de coincidencia 2020: ", gdfchangeN['Coincidencia2020'].value_counts())
print("Tipos de coincidencia 2021: ", gdfchangeN['Coincidencia2021'].value_counts())
print("Tipos de coincidencia 2022: ", gdfchangeN['Coincidencia2022'].value_counts())
# %%
print("Numero de parcelas por especialistas: ", gdfchangeN['email1'].value_counts())
print("Numero de parcelas por Juniors1: ", gdfchangeN['email2'].value_counts())
print("Numero de parcelas por Juniors2: ", gdfchangeN['email3'].value_counts())
# %%
print("Clases CUT 2000: ", gdfchangeN['CUT2000'].value_counts())
print("Clases CUT 2008: ", gdfchangeN['CUT2008'].value_counts())
print("Clases CUT 2012: ", gdfchangeN['CUT2012'].value_counts())
print("Clases CUT 2013: ", gdfchangeN['CUT2013'].value_counts())
print("Clases CUT 2014: ", gdfchangeN['CUT2014'].value_counts())
print("Clases CUT 2015: ", gdfchangeN['CUT2015'].value_counts())
print("Clases CUT 2016: ", gdfchangeN['CUT2016'].value_counts())
print("Clases CUT 2017: ", gdfchangeN['CUT2017'].value_counts())
print("Clases CUT 2018: ", gdfchangeN['CUT2018'].value_counts())
print("Clases CUT 2019: ", gdfchangeN['CUT2019'].value_counts())
print("Clases CUT 2020: ", gdfchangeN['CUT2020'].value_counts())
print("Clases CUT 2021: ", gdfchangeN['CUT2021'].value_counts())
print("Clases CUT 2022: ", gdfchangeN['CUT2022'].value_counts())

# %%
# save as csv
gdfchangeN.to_csv("./Datos/Ecuador/BSVTBA/ResultadosCUT_BSVTBA_02102023.csv")
print("The CSV file has been saved!")