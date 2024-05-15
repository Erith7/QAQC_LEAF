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
fullfile = pd.read_csv("./MAATE2023/Resultados2/10_NBE/ResultadosInterpretacion_NBE_04112024.csv")
print(fullfile.head(10))
fullfile['geometry'] = fullfile['geometry'].apply(wkt.loads)
gdf = gpd.GeoDataFrame(fullfile, crs="EPSG:4326")
# %%
# Selection of changes columns and deleting the previous dataframes
#gdfSel = gdf[["plotid", "sampleid", "lon", "lat", "geometry", "pl_id", "pl_cluster", "pl_mon_images", "email1", "email2", "email3", "Cambio0008_1", "Cambio0008_2", "Cambio0008_3", "Cambio0812_1", "Cambio0812_2", "Cambio0812_3", "Cambio1213_1", "Cambio1213_2", "Cambio1213_3", "Cambio1314_1", "Cambio1314_2", "Cambio1314_3", "Cambio1415_1", "Cambio1415_2", "Cambio1415_3", "Cambio1516_1", "Cambio1516_2", "Cambio1516_3", "Cambio1617_1", "Cambio1617_2", "Cambio1617_3", "Cambio1718_1", "Cambio1718_2", "Cambio1718_3", "Cambio1819_1", "Cambio1819_2", "Cambio1819_3", "Cambio1920_1", "Cambio1920_2", "Cambio1920_3", "Cambio2021_1", "Cambio2021_2", "Cambio2021_3", "Cambio2122_1", "Cambio2122_2", "Cambio2122_3"]]
# for id columns
gdfSel = gdf[["plotid", "sampleid", "lon", "lat", "geometry", "pl_cluster", "pl_mon_images", "email1", "email2", "email3", "Cambio0008_1", "Cambio0008_2", "Cambio0008_3", "Cambio0812_1", "Cambio0812_2", "Cambio0812_3", "Cambio1213_1", "Cambio1213_2", "Cambio1213_3", "Cambio1314_1", "Cambio1314_2", "Cambio1314_3", "Cambio1415_1", "Cambio1415_2", "Cambio1415_3", "Cambio1516_1", "Cambio1516_2", "Cambio1516_3", "Cambio1617_1", "Cambio1617_2", "Cambio1617_3", "Cambio1718_1", "Cambio1718_2", "Cambio1718_3", "Cambio1819_1", "Cambio1819_2", "Cambio1819_3", "Cambio1920_1", "Cambio1920_2", "Cambio1920_3", "Cambio2021_1", "Cambio2021_2", "Cambio2021_3", "Cambio2122_1", "Cambio2122_2", "Cambio2122_3"]]

del gdf
del fullfile

# %%
# Cambios 2000-2008
gdfSel.loc[(gdfSel['Cambio0008_1'] == gdfSel['Cambio0008_2']) & (gdfSel['Cambio0008_3'].isnull()), 'Cambio0008'] = gdfSel['Cambio0008_1']
gdfSel.loc[(gdfSel['Cambio0008_1'] == gdfSel['Cambio0008_2']) & (gdfSel['Cambio0008_3'].isnull()), 'Coincidencia0008'] = 'EA'
gdfSel.loc[(gdfSel['Cambio0008_1'] != gdfSel['Cambio0008_2']) & (gdfSel['Cambio0008_3'].isnull()), 'Cambio0008'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio0008_1'] != gdfSel['Cambio0008_2']) & (gdfSel['Cambio0008_3'].isnull()), 'Coincidencia0008'] = 'AA'
gdfSel.loc[(gdfSel['Cambio0008_1'].isnull()) & (gdfSel['Cambio0008_2'].isnull()) & (gdfSel['Cambio0008_3'].isnull()), 'Cambio0008'] = np.nan
gdfSel.loc[(gdfSel['Cambio0008_1'].isnull()) & (gdfSel['Cambio0008_2'].isnull()) & (gdfSel['Cambio0008_3'].isnull()), 'Coincidencia0008'] = 'A'
gdfSel.loc[(gdfSel['Cambio0008_1'].notnull()) & (gdfSel['Cambio0008_2'].isnull()) & (gdfSel['Cambio0008_3'].isnull()), 'Cambio0008'] = gdfSel['Cambio0008_1']
gdfSel.loc[(gdfSel['Cambio0008_1'].notnull()) & (gdfSel['Cambio0008_2'].isnull()) & (gdfSel['Cambio0008_3'].isnull()), 'Coincidencia0008'] = 'BB'
gdfSel.loc[(gdfSel['Cambio0008_1'].isnull()) & (gdfSel['Cambio0008_2'].notnull()) & (gdfSel['Cambio0008_3'].isnull()), 'Cambio0008'] = gdfSel['Cambio0008_2']
gdfSel.loc[(gdfSel['Cambio0008_1'].isnull()) & (gdfSel['Cambio0008_2'].notnull()) & (gdfSel['Cambio0008_3'].isnull()), 'Coincidencia0008'] = 'CC'
gdfSel.loc[(gdfSel['Cambio0008_1'].isnull()) & (gdfSel['Cambio0008_2'].isnull()) & (gdfSel['Cambio0008_3'].notnull()), 'Cambio0008'] = gdfSel['Cambio0008_3']
gdfSel.loc[(gdfSel['Cambio0008_1'].isnull()) & (gdfSel['Cambio0008_2'].isnull()) & (gdfSel['Cambio0008_3'].notnull()), 'Coincidencia0008'] = 'HH'
gdfSel.loc[(gdfSel['Cambio0008_1'] == gdfSel['Cambio0008_2']) & (gdfSel['Cambio0008_3'] == gdfSel['Cambio0008_2']) & (gdfSel['Cambio0008_1'] == gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_1'].notnull()) & (gdfSel['Cambio0008_2'].notnull()) & (gdfSel['Cambio0008_3'].notnull()), 'Cambio0008'] = gdfSel['Cambio0008_1']
gdfSel.loc[(gdfSel['Cambio0008_1'] == gdfSel['Cambio0008_2']) & (gdfSel['Cambio0008_3'] == gdfSel['Cambio0008_2']) & (gdfSel['Cambio0008_1'] == gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_1'].notnull()) & (gdfSel['Cambio0008_2'].notnull()) & (gdfSel['Cambio0008_3'].notnull()), 'Coincidencia0008'] = 'E'
gdfSel.loc[(gdfSel['Cambio0008_1'] != gdfSel['Cambio0008_2']) & (gdfSel['Cambio0008_2'] == gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_1'].notnull()) & (gdfSel['Cambio0008_2'].notnull()) & (gdfSel['Cambio0008_3'].notnull()), 'Cambio0008'] = gdfSel['Cambio0008_2']
gdfSel.loc[(gdfSel['Cambio0008_1'] != gdfSel['Cambio0008_2']) & (gdfSel['Cambio0008_2'] == gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_1'].notnull()) & (gdfSel['Cambio0008_2'].notnull()) & (gdfSel['Cambio0008_3'].notnull()), 'Coincidencia0008'] = 'B'
gdfSel.loc[(gdfSel['Cambio0008_1'] == gdfSel['Cambio0008_2']) & (gdfSel['Cambio0008_2'] != gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_1'].notnull()) & (gdfSel['Cambio0008_2'].notnull()) & (gdfSel['Cambio0008_3'].notnull()), 'Cambio0008'] = gdfSel['Cambio0008_1']
gdfSel.loc[(gdfSel['Cambio0008_1'] == gdfSel['Cambio0008_2']) & (gdfSel['Cambio0008_2'] != gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_1'].notnull()) & (gdfSel['Cambio0008_2'].notnull()) & (gdfSel['Cambio0008_3'].notnull()), 'Coincidencia0008'] = 'C'
gdfSel.loc[(gdfSel['Cambio0008_1'] == gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_2'] != gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_1'].notnull()) & (gdfSel['Cambio0008_2'].notnull()) & (gdfSel['Cambio0008_3'].notnull()), 'Cambio0008'] = gdfSel['Cambio0008_1']
gdfSel.loc[(gdfSel['Cambio0008_1'] == gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_2'] != gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_1'].notnull()) & (gdfSel['Cambio0008_2'].notnull()) & (gdfSel['Cambio0008_3'].notnull()), 'Coincidencia0008'] = 'D'
gdfSel.loc[(gdfSel['Cambio0008_1'].isnull()) & (gdfSel['Cambio0008_2'] == gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_3'].notnull()), 'Cambio0008'] = gdfSel['Cambio0008_2']
gdfSel.loc[(gdfSel['Cambio0008_1'].isnull()) & (gdfSel['Cambio0008_2'] == gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_3'].notnull()), 'Coincidencia0008'] = 'DD'
gdfSel.loc[(gdfSel['Cambio0008_1'].isnull()) & (gdfSel['Cambio0008_2'] != gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_3'].notnull()), 'Cambio0008'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio0008_1'].isnull()) & (gdfSel['Cambio0008_2'] != gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_3'].notnull()), 'Coincidencia0008'] = 'FF'
gdfSel.loc[(gdfSel['Cambio0008_1'] != gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_2'] != gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_1'] != gdfSel['Cambio0008_2']) & (gdfSel['Cambio0008_1'].notnull()) & (gdfSel['Cambio0008_2'].notnull()) & (gdfSel['Cambio0008_3'].notnull()), 'Cambio0008'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio0008_1'] != gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_2'] != gdfSel['Cambio0008_3']) & (gdfSel['Cambio0008_1'] != gdfSel['Cambio0008_2']) & (gdfSel['Cambio0008_1'].notnull()) & (gdfSel['Cambio0008_2'].notnull()) & (gdfSel['Cambio0008_3'].notnull()), 'Coincidencia0008'] = 'F'

# %%
# cambios 2008-2012
gdfSel.loc[(gdfSel['Cambio0812_1'] == gdfSel['Cambio0812_2']) & (gdfSel['Cambio0812_3'].isnull()), 'Cambio0812'] = gdfSel['Cambio0812_1']
gdfSel.loc[(gdfSel['Cambio0812_1'] == gdfSel['Cambio0812_2']) & (gdfSel['Cambio0812_3'].isnull()), 'Coincidencia0812'] = 'EA'
gdfSel.loc[(gdfSel['Cambio0812_1'] != gdfSel['Cambio0812_2']) & (gdfSel['Cambio0812_3'].isnull()), 'Cambio0812'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio0812_1'] != gdfSel['Cambio0812_2']) & (gdfSel['Cambio0812_3'].isnull()), 'Coincidencia0812'] = 'AA'
gdfSel.loc[(gdfSel['Cambio0812_1'].isnull()) & (gdfSel['Cambio0812_2'].isnull()) & (gdfSel['Cambio0812_3'].isnull()), 'Cambio0812'] = np.nan
gdfSel.loc[(gdfSel['Cambio0812_1'].isnull()) & (gdfSel['Cambio0812_2'].isnull()) & (gdfSel['Cambio0812_3'].isnull()), 'Coincidencia0812'] = 'A'
gdfSel.loc[(gdfSel['Cambio0812_1'].notnull()) & (gdfSel['Cambio0812_2'].isnull()) & (gdfSel['Cambio0812_3'].isnull()), 'Cambio0812'] = gdfSel['Cambio0812_1']
gdfSel.loc[(gdfSel['Cambio0812_1'].notnull()) & (gdfSel['Cambio0812_2'].isnull()) & (gdfSel['Cambio0812_3'].isnull()), 'Coincidencia0812'] = 'BB'
gdfSel.loc[(gdfSel['Cambio0812_1'].isnull()) & (gdfSel['Cambio0812_2'].notnull()) & (gdfSel['Cambio0812_3'].isnull()), 'Cambio0812'] = gdfSel['Cambio0812_2']
gdfSel.loc[(gdfSel['Cambio0812_1'].isnull()) & (gdfSel['Cambio0812_2'].notnull()) & (gdfSel['Cambio0812_3'].isnull()), 'Coincidencia0812'] = 'CC'
gdfSel.loc[(gdfSel['Cambio0812_1'].isnull()) & (gdfSel['Cambio0812_2'].isnull()) & (gdfSel['Cambio0812_3'].notnull()), 'Cambio0812'] = gdfSel['Cambio0812_3']
gdfSel.loc[(gdfSel['Cambio0812_1'].isnull()) & (gdfSel['Cambio0812_2'].isnull()) & (gdfSel['Cambio0812_3'].notnull()), 'Coincidencia0812'] = 'HH'
gdfSel.loc[(gdfSel['Cambio0812_1'] == gdfSel['Cambio0812_2']) & (gdfSel['Cambio0812_3'] == gdfSel['Cambio0812_2']) & (gdfSel['Cambio0812_1'] == gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_1'].notnull()) & (gdfSel['Cambio0812_2'].notnull()) & (gdfSel['Cambio0812_3'].notnull()), 'Cambio0812'] = gdfSel['Cambio0812_1']
gdfSel.loc[(gdfSel['Cambio0812_1'] == gdfSel['Cambio0812_2']) & (gdfSel['Cambio0812_3'] == gdfSel['Cambio0812_2']) & (gdfSel['Cambio0812_1'] == gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_1'].notnull()) & (gdfSel['Cambio0812_2'].notnull()) & (gdfSel['Cambio0812_3'].notnull()), 'Coincidencia0812'] = 'E'
gdfSel.loc[(gdfSel['Cambio0812_1'] != gdfSel['Cambio0812_2']) & (gdfSel['Cambio0812_2'] == gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_1'].notnull()) & (gdfSel['Cambio0812_2'].notnull()) & (gdfSel['Cambio0812_3'].notnull()), 'Cambio0812'] = gdfSel['Cambio0812_2']
gdfSel.loc[(gdfSel['Cambio0812_1'] != gdfSel['Cambio0812_2']) & (gdfSel['Cambio0812_2'] == gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_1'].notnull()) & (gdfSel['Cambio0812_2'].notnull()) & (gdfSel['Cambio0812_3'].notnull()), 'Coincidencia0812'] = 'B'
gdfSel.loc[(gdfSel['Cambio0812_1'] == gdfSel['Cambio0812_2']) & (gdfSel['Cambio0812_2'] != gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_1'].notnull()) & (gdfSel['Cambio0812_2'].notnull()) & (gdfSel['Cambio0812_3'].notnull()), 'Cambio0812'] = gdfSel['Cambio0812_1']
gdfSel.loc[(gdfSel['Cambio0812_1'] == gdfSel['Cambio0812_2']) & (gdfSel['Cambio0812_2'] != gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_1'].notnull()) & (gdfSel['Cambio0812_2'].notnull()) & (gdfSel['Cambio0812_3'].notnull()), 'Coincidencia0812'] = 'C'
gdfSel.loc[(gdfSel['Cambio0812_1'] == gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_2'] != gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_1'].notnull()) & (gdfSel['Cambio0812_2'].notnull()) & (gdfSel['Cambio0812_3'].notnull()), 'Cambio0812'] = gdfSel['Cambio0812_1']
gdfSel.loc[(gdfSel['Cambio0812_1'] == gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_2'] != gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_1'].notnull()) & (gdfSel['Cambio0812_2'].notnull()) & (gdfSel['Cambio0812_3'].notnull()), 'Coincidencia0812'] = 'D'
gdfSel.loc[(gdfSel['Cambio0812_1'].isnull()) & (gdfSel['Cambio0812_2'] == gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_3'].notnull()), 'Cambio0812'] = gdfSel['Cambio0812_2']
gdfSel.loc[(gdfSel['Cambio0812_1'].isnull()) & (gdfSel['Cambio0812_2'] == gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_3'].notnull()), 'Coincidencia0812'] = 'DD'
gdfSel.loc[(gdfSel['Cambio0812_1'].isnull()) & (gdfSel['Cambio0812_2'] != gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_3'].notnull()), 'Cambio0812'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio0812_1'].isnull()) & (gdfSel['Cambio0812_2'] != gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_3'].notnull()), 'Coincidencia0812'] = 'FF'
gdfSel.loc[(gdfSel['Cambio0812_1'] != gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_2'] != gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_1'] != gdfSel['Cambio0812_2']) & (gdfSel['Cambio0812_1'].notnull()) & (gdfSel['Cambio0812_2'].notnull()) & (gdfSel['Cambio0812_3'].notnull()), 'Cambio0812'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio0812_1'] != gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_2'] != gdfSel['Cambio0812_3']) & (gdfSel['Cambio0812_1'] != gdfSel['Cambio0812_2']) & (gdfSel['Cambio0812_1'].notnull()) & (gdfSel['Cambio0812_2'].notnull()) & (gdfSel['Cambio0812_3'].notnull()), 'Coincidencia0812'] = 'F'


# %%
# Cambios 2012-2013
gdfSel.loc[(gdfSel['Cambio1213_1'] == gdfSel['Cambio1213_2']) & (gdfSel['Cambio1213_3'].isnull()), 'Cambio1213'] = gdfSel['Cambio1213_1']
gdfSel.loc[(gdfSel['Cambio1213_1'] == gdfSel['Cambio1213_2']) & (gdfSel['Cambio1213_3'].isnull()), 'Coincidencia1213'] = 'EA'
gdfSel.loc[(gdfSel['Cambio1213_1'] != gdfSel['Cambio1213_2']) & (gdfSel['Cambio1213_3'].isnull()), 'Cambio1213'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1213_1'] != gdfSel['Cambio1213_2']) & (gdfSel['Cambio1213_3'].isnull()), 'Coincidencia1213'] = 'AA'
gdfSel.loc[(gdfSel['Cambio1213_1'].isnull()) & (gdfSel['Cambio1213_2'].isnull()) & (gdfSel['Cambio1213_3'].isnull()), 'Cambio1213'] = np.nan
gdfSel.loc[(gdfSel['Cambio1213_1'].isnull()) & (gdfSel['Cambio1213_2'].isnull()) & (gdfSel['Cambio1213_3'].isnull()), 'Coincidencia1213'] = 'A'
gdfSel.loc[(gdfSel['Cambio1213_1'].notnull()) & (gdfSel['Cambio1213_2'].isnull()) & (gdfSel['Cambio1213_3'].isnull()), 'Cambio1213'] = gdfSel['Cambio1213_1']
gdfSel.loc[(gdfSel['Cambio1213_1'].notnull()) & (gdfSel['Cambio1213_2'].isnull()) & (gdfSel['Cambio1213_3'].isnull()), 'Coincidencia1213'] = 'BB'
gdfSel.loc[(gdfSel['Cambio1213_1'].isnull()) & (gdfSel['Cambio1213_2'].notnull()) & (gdfSel['Cambio1213_3'].isnull()), 'Cambio1213'] = gdfSel['Cambio1213_2']
gdfSel.loc[(gdfSel['Cambio1213_1'].isnull()) & (gdfSel['Cambio1213_2'].notnull()) & (gdfSel['Cambio1213_3'].isnull()), 'Coincidencia1213'] = 'CC'
gdfSel.loc[(gdfSel['Cambio1213_1'].isnull()) & (gdfSel['Cambio1213_2'].isnull()) & (gdfSel['Cambio1213_3'].notnull()), 'Cambio1213'] = gdfSel['Cambio1213_3']
gdfSel.loc[(gdfSel['Cambio1213_1'].isnull()) & (gdfSel['Cambio1213_2'].isnull()) & (gdfSel['Cambio1213_3'].notnull()), 'Coincidencia1213'] = 'HH'
gdfSel.loc[(gdfSel['Cambio1213_1'] == gdfSel['Cambio1213_2']) & (gdfSel['Cambio1213_3'] == gdfSel['Cambio1213_2']) & (gdfSel['Cambio1213_1'] == gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_1'].notnull()) & (gdfSel['Cambio1213_2'].notnull()) & (gdfSel['Cambio1213_3'].notnull()), 'Cambio1213'] = gdfSel['Cambio1213_1']
gdfSel.loc[(gdfSel['Cambio1213_1'] == gdfSel['Cambio1213_2']) & (gdfSel['Cambio1213_3'] == gdfSel['Cambio1213_2']) & (gdfSel['Cambio1213_1'] == gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_1'].notnull()) & (gdfSel['Cambio1213_2'].notnull()) & (gdfSel['Cambio1213_3'].notnull()), 'Coincidencia1213'] = 'E'
gdfSel.loc[(gdfSel['Cambio1213_1'] != gdfSel['Cambio1213_2']) & (gdfSel['Cambio1213_2'] == gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_1'].notnull()) & (gdfSel['Cambio1213_2'].notnull()) & (gdfSel['Cambio1213_3'].notnull()), 'Cambio1213'] = gdfSel['Cambio1213_2']
gdfSel.loc[(gdfSel['Cambio1213_1'] != gdfSel['Cambio1213_2']) & (gdfSel['Cambio1213_2'] == gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_1'].notnull()) & (gdfSel['Cambio1213_2'].notnull()) & (gdfSel['Cambio1213_3'].notnull()), 'Coincidencia1213'] = 'B'
gdfSel.loc[(gdfSel['Cambio1213_1'] == gdfSel['Cambio1213_2']) & (gdfSel['Cambio1213_2'] != gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_1'].notnull()) & (gdfSel['Cambio1213_2'].notnull()) & (gdfSel['Cambio1213_3'].notnull()), 'Cambio1213'] = gdfSel['Cambio1213_1']
gdfSel.loc[(gdfSel['Cambio1213_1'] == gdfSel['Cambio1213_2']) & (gdfSel['Cambio1213_2'] != gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_1'].notnull()) & (gdfSel['Cambio1213_2'].notnull()) & (gdfSel['Cambio1213_3'].notnull()), 'Coincidencia1213'] = 'C'
gdfSel.loc[(gdfSel['Cambio1213_1'] == gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_2'] != gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_1'].notnull()) & (gdfSel['Cambio1213_2'].notnull()) & (gdfSel['Cambio1213_3'].notnull()), 'Cambio1213'] = gdfSel['Cambio1213_1']
gdfSel.loc[(gdfSel['Cambio1213_1'] == gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_2'] != gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_1'].notnull()) & (gdfSel['Cambio1213_2'].notnull()) & (gdfSel['Cambio1213_3'].notnull()), 'Coincidencia1213'] = 'D'
gdfSel.loc[(gdfSel['Cambio1213_1'].isnull()) & (gdfSel['Cambio1213_2'] == gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_3'].notnull()), 'Cambio1213'] = gdfSel['Cambio1213_2']
gdfSel.loc[(gdfSel['Cambio1213_1'].isnull()) & (gdfSel['Cambio1213_2'] == gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_3'].notnull()), 'Coincidencia1213'] = 'DD'
gdfSel.loc[(gdfSel['Cambio1213_1'].isnull()) & (gdfSel['Cambio1213_2'] != gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_3'].notnull()), 'Cambio1213'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1213_1'].isnull()) & (gdfSel['Cambio1213_2'] != gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_3'].notnull()), 'Coincidencia1213'] = 'FF'
gdfSel.loc[(gdfSel['Cambio1213_1'] != gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_2'] != gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_1'] != gdfSel['Cambio1213_2']) & (gdfSel['Cambio1213_1'].notnull()) & (gdfSel['Cambio1213_2'].notnull()) & (gdfSel['Cambio1213_3'].notnull()), 'Cambio1213'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1213_1'] != gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_2'] != gdfSel['Cambio1213_3']) & (gdfSel['Cambio1213_1'] != gdfSel['Cambio1213_2']) & (gdfSel['Cambio1213_1'].notnull()) & (gdfSel['Cambio1213_2'].notnull()) & (gdfSel['Cambio1213_3'].notnull()), 'Coincidencia1213'] = 'F'


# %%
#Cambios 2013-2014
gdfSel.loc[(gdfSel['Cambio1314_1'] == gdfSel['Cambio1314_2']) & (gdfSel['Cambio1314_3'].isnull()), 'Cambio1314'] = gdfSel['Cambio1314_1']
gdfSel.loc[(gdfSel['Cambio1314_1'] == gdfSel['Cambio1314_2']) & (gdfSel['Cambio1314_3'].isnull()), 'Coincidencia1314'] = 'EA'
gdfSel.loc[(gdfSel['Cambio1314_1'] != gdfSel['Cambio1314_2']) & (gdfSel['Cambio1314_3'].isnull()), 'Cambio1314'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1314_1'] != gdfSel['Cambio1314_2']) & (gdfSel['Cambio1314_3'].isnull()), 'Coincidencia1314'] = 'AA'
gdfSel.loc[(gdfSel['Cambio1314_1'].isnull()) & (gdfSel['Cambio1314_2'].isnull()) & (gdfSel['Cambio1314_3'].isnull()), 'Cambio1314'] = np.nan
gdfSel.loc[(gdfSel['Cambio1314_1'].isnull()) & (gdfSel['Cambio1314_2'].isnull()) & (gdfSel['Cambio1314_3'].isnull()), 'Coincidencia1314'] = 'A'
gdfSel.loc[(gdfSel['Cambio1314_1'].notnull()) & (gdfSel['Cambio1314_2'].isnull()) & (gdfSel['Cambio1314_3'].isnull()), 'Cambio1314'] = gdfSel['Cambio1314_1']
gdfSel.loc[(gdfSel['Cambio1314_1'].notnull()) & (gdfSel['Cambio1314_2'].isnull()) & (gdfSel['Cambio1314_3'].isnull()), 'Coincidencia1314'] = 'BB'
gdfSel.loc[(gdfSel['Cambio1314_1'].isnull()) & (gdfSel['Cambio1314_2'].notnull()) & (gdfSel['Cambio1314_3'].isnull()), 'Cambio1314'] = gdfSel['Cambio1314_2']
gdfSel.loc[(gdfSel['Cambio1314_1'].isnull()) & (gdfSel['Cambio1314_2'].notnull()) & (gdfSel['Cambio1314_3'].isnull()), 'Coincidencia1314'] = 'CC'
gdfSel.loc[(gdfSel['Cambio1314_1'].isnull()) & (gdfSel['Cambio1314_2'].isnull()) & (gdfSel['Cambio1314_3'].notnull()), 'Cambio1314'] = gdfSel['Cambio1314_3']
gdfSel.loc[(gdfSel['Cambio1314_1'].isnull()) & (gdfSel['Cambio1314_2'].isnull()) & (gdfSel['Cambio1314_3'].notnull()), 'Coincidencia1314'] = 'HH'
gdfSel.loc[(gdfSel['Cambio1314_1'] == gdfSel['Cambio1314_2']) & (gdfSel['Cambio1314_3'] == gdfSel['Cambio1314_2']) & (gdfSel['Cambio1314_1'] == gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_1'].notnull()) & (gdfSel['Cambio1314_2'].notnull()) & (gdfSel['Cambio1314_3'].notnull()), 'Cambio1314'] = gdfSel['Cambio1314_1']
gdfSel.loc[(gdfSel['Cambio1314_1'] == gdfSel['Cambio1314_2']) & (gdfSel['Cambio1314_3'] == gdfSel['Cambio1314_2']) & (gdfSel['Cambio1314_1'] == gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_1'].notnull()) & (gdfSel['Cambio1314_2'].notnull()) & (gdfSel['Cambio1314_3'].notnull()), 'Coincidencia1314'] = 'E'
gdfSel.loc[(gdfSel['Cambio1314_1'] != gdfSel['Cambio1314_2']) & (gdfSel['Cambio1314_2'] == gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_1'].notnull()) & (gdfSel['Cambio1314_2'].notnull()) & (gdfSel['Cambio1314_3'].notnull()), 'Cambio1314'] = gdfSel['Cambio1314_2']
gdfSel.loc[(gdfSel['Cambio1314_1'] != gdfSel['Cambio1314_2']) & (gdfSel['Cambio1314_2'] == gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_1'].notnull()) & (gdfSel['Cambio1314_2'].notnull()) & (gdfSel['Cambio1314_3'].notnull()), 'Coincidencia1314'] = 'B'
gdfSel.loc[(gdfSel['Cambio1314_1'] == gdfSel['Cambio1314_2']) & (gdfSel['Cambio1314_2'] != gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_1'].notnull()) & (gdfSel['Cambio1314_2'].notnull()) & (gdfSel['Cambio1314_3'].notnull()), 'Cambio1314'] = gdfSel['Cambio1314_1']
gdfSel.loc[(gdfSel['Cambio1314_1'] == gdfSel['Cambio1314_2']) & (gdfSel['Cambio1314_2'] != gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_1'].notnull()) & (gdfSel['Cambio1314_2'].notnull()) & (gdfSel['Cambio1314_3'].notnull()), 'Coincidencia1314'] = 'C'
gdfSel.loc[(gdfSel['Cambio1314_1'] == gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_2'] != gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_1'].notnull()) & (gdfSel['Cambio1314_2'].notnull()) & (gdfSel['Cambio1314_3'].notnull()), 'Cambio1314'] = gdfSel['Cambio1314_1']
gdfSel.loc[(gdfSel['Cambio1314_1'] == gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_2'] != gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_1'].notnull()) & (gdfSel['Cambio1314_2'].notnull()) & (gdfSel['Cambio1314_3'].notnull()), 'Coincidencia1314'] = 'D'
gdfSel.loc[(gdfSel['Cambio1314_1'].isnull()) & (gdfSel['Cambio1314_2'] == gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_3'].notnull()), 'Cambio1314'] = gdfSel['Cambio1314_2']
gdfSel.loc[(gdfSel['Cambio1314_1'].isnull()) & (gdfSel['Cambio1314_2'] == gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_3'].notnull()), 'Coincidencia1314'] = 'DD'
gdfSel.loc[(gdfSel['Cambio1314_1'].isnull()) & (gdfSel['Cambio1314_2'] != gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_3'].notnull()), 'Cambio1314'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1314_1'].isnull()) & (gdfSel['Cambio1314_2'] != gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_3'].notnull()), 'Coincidencia1314'] = 'FF'
gdfSel.loc[(gdfSel['Cambio1314_1'] != gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_2'] != gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_1'] != gdfSel['Cambio1314_2']) & (gdfSel['Cambio1314_1'].notnull()) & (gdfSel['Cambio1314_2'].notnull()) & (gdfSel['Cambio1314_3'].notnull()), 'Cambio1314'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1314_1'] != gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_2'] != gdfSel['Cambio1314_3']) & (gdfSel['Cambio1314_1'] != gdfSel['Cambio1314_2']) & (gdfSel['Cambio1314_1'].notnull()) & (gdfSel['Cambio1314_2'].notnull()) & (gdfSel['Cambio1314_3'].notnull()), 'Coincidencia1314'] = 'F'



# %%
# Cambios 2014-2015
gdfSel.loc[(gdfSel['Cambio1415_1'] == gdfSel['Cambio1415_2']) & (gdfSel['Cambio1415_3'].isnull()), 'Cambio1415'] = gdfSel['Cambio1415_1']
gdfSel.loc[(gdfSel['Cambio1415_1'] == gdfSel['Cambio1415_2']) & (gdfSel['Cambio1415_3'].isnull()), 'Coincidencia1415'] = 'EA'
gdfSel.loc[(gdfSel['Cambio1415_1'] != gdfSel['Cambio1415_2']) & (gdfSel['Cambio1415_3'].isnull()), 'Cambio1415'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1415_1'] != gdfSel['Cambio1415_2']) & (gdfSel['Cambio1415_3'].isnull()), 'Coincidencia1415'] = 'AA'
gdfSel.loc[(gdfSel['Cambio1415_1'].isnull()) & (gdfSel['Cambio1415_2'].isnull()) & (gdfSel['Cambio1415_3'].isnull()), 'Cambio1415'] = np.nan
gdfSel.loc[(gdfSel['Cambio1415_1'].isnull()) & (gdfSel['Cambio1415_2'].isnull()) & (gdfSel['Cambio1415_3'].isnull()), 'Coincidencia1415'] = 'A'
gdfSel.loc[(gdfSel['Cambio1415_1'].notnull()) & (gdfSel['Cambio1415_2'].isnull()) & (gdfSel['Cambio1415_3'].isnull()), 'Cambio1415'] = gdfSel['Cambio1415_1']
gdfSel.loc[(gdfSel['Cambio1415_1'].notnull()) & (gdfSel['Cambio1415_2'].isnull()) & (gdfSel['Cambio1415_3'].isnull()), 'Coincidencia1415'] = 'BB'
gdfSel.loc[(gdfSel['Cambio1415_1'].isnull()) & (gdfSel['Cambio1415_2'].notnull()) & (gdfSel['Cambio1415_3'].isnull()), 'Cambio1415'] = gdfSel['Cambio1415_2']
gdfSel.loc[(gdfSel['Cambio1415_1'].isnull()) & (gdfSel['Cambio1415_2'].notnull()) & (gdfSel['Cambio1415_3'].isnull()), 'Coincidencia1415'] = 'CC'
gdfSel.loc[(gdfSel['Cambio1415_1'].isnull()) & (gdfSel['Cambio1415_2'].isnull()) & (gdfSel['Cambio1415_3'].notnull()), 'Cambio1415'] = gdfSel['Cambio1415_3']
gdfSel.loc[(gdfSel['Cambio1415_1'].isnull()) & (gdfSel['Cambio1415_2'].isnull()) & (gdfSel['Cambio1415_3'].notnull()), 'Coincidencia1415'] = 'HH'
gdfSel.loc[(gdfSel['Cambio1415_1'] == gdfSel['Cambio1415_2']) & (gdfSel['Cambio1415_3'] == gdfSel['Cambio1415_2']) & (gdfSel['Cambio1415_1'] == gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_1'].notnull()) & (gdfSel['Cambio1415_2'].notnull()) & (gdfSel['Cambio1415_3'].notnull()), 'Cambio1415'] = gdfSel['Cambio1415_1']
gdfSel.loc[(gdfSel['Cambio1415_1'] == gdfSel['Cambio1415_2']) & (gdfSel['Cambio1415_3'] == gdfSel['Cambio1415_2']) & (gdfSel['Cambio1415_1'] == gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_1'].notnull()) & (gdfSel['Cambio1415_2'].notnull()) & (gdfSel['Cambio1415_3'].notnull()), 'Coincidencia1415'] = 'E'
gdfSel.loc[(gdfSel['Cambio1415_1'] != gdfSel['Cambio1415_2']) & (gdfSel['Cambio1415_2'] == gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_1'].notnull()) & (gdfSel['Cambio1415_2'].notnull()) & (gdfSel['Cambio1415_3'].notnull()), 'Cambio1415'] = gdfSel['Cambio1415_2']
gdfSel.loc[(gdfSel['Cambio1415_1'] != gdfSel['Cambio1415_2']) & (gdfSel['Cambio1415_2'] == gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_1'].notnull()) & (gdfSel['Cambio1415_2'].notnull()) & (gdfSel['Cambio1415_3'].notnull()), 'Coincidencia1415'] = 'B'
gdfSel.loc[(gdfSel['Cambio1415_1'] == gdfSel['Cambio1415_2']) & (gdfSel['Cambio1415_2'] != gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_1'].notnull()) & (gdfSel['Cambio1415_2'].notnull()) & (gdfSel['Cambio1415_3'].notnull()), 'Cambio1415'] = gdfSel['Cambio1415_1']
gdfSel.loc[(gdfSel['Cambio1415_1'] == gdfSel['Cambio1415_2']) & (gdfSel['Cambio1415_2'] != gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_1'].notnull()) & (gdfSel['Cambio1415_2'].notnull()) & (gdfSel['Cambio1415_3'].notnull()), 'Coincidencia1415'] = 'C'
gdfSel.loc[(gdfSel['Cambio1415_1'] == gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_2'] != gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_1'].notnull()) & (gdfSel['Cambio1415_2'].notnull()) & (gdfSel['Cambio1415_3'].notnull()), 'Cambio1415'] = gdfSel['Cambio1415_1']
gdfSel.loc[(gdfSel['Cambio1415_1'] == gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_2'] != gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_1'].notnull()) & (gdfSel['Cambio1415_2'].notnull()) & (gdfSel['Cambio1415_3'].notnull()), 'Coincidencia1415'] = 'D'
gdfSel.loc[(gdfSel['Cambio1415_1'].isnull()) & (gdfSel['Cambio1415_2'] == gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_3'].notnull()), 'Cambio1415'] = gdfSel['Cambio1415_2']
gdfSel.loc[(gdfSel['Cambio1415_1'].isnull()) & (gdfSel['Cambio1415_2'] == gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_3'].notnull()), 'Coincidencia1415'] = 'DD'
gdfSel.loc[(gdfSel['Cambio1415_1'].isnull()) & (gdfSel['Cambio1415_2'] != gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_3'].notnull()), 'Cambio1415'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1415_1'].isnull()) & (gdfSel['Cambio1415_2'] != gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_3'].notnull()), 'Coincidencia1415'] = 'FF'
gdfSel.loc[(gdfSel['Cambio1415_1'] != gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_2'] != gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_1'] != gdfSel['Cambio1415_2']) & (gdfSel['Cambio1415_1'].notnull()) & (gdfSel['Cambio1415_2'].notnull()) & (gdfSel['Cambio1415_3'].notnull()), 'Cambio1415'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1415_1'] != gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_2'] != gdfSel['Cambio1415_3']) & (gdfSel['Cambio1415_1'] != gdfSel['Cambio1415_2']) & (gdfSel['Cambio1415_1'].notnull()) & (gdfSel['Cambio1415_2'].notnull()) & (gdfSel['Cambio1415_3'].notnull()), 'Coincidencia1415'] = 'F'



# %%
# Cambios 2015-2016
gdfSel.loc[(gdfSel['Cambio1516_1'] == gdfSel['Cambio1516_2']) & (gdfSel['Cambio1516_3'].isnull()), 'Cambio1516'] = gdfSel['Cambio1516_1']
gdfSel.loc[(gdfSel['Cambio1516_1'] == gdfSel['Cambio1516_2']) & (gdfSel['Cambio1516_3'].isnull()), 'Coincidencia1516'] = 'EA'
gdfSel.loc[(gdfSel['Cambio1516_1'] != gdfSel['Cambio1516_2']) & (gdfSel['Cambio1516_3'].isnull()), 'Cambio1516'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1516_1'] != gdfSel['Cambio1516_2']) & (gdfSel['Cambio1516_3'].isnull()), 'Coincidencia1516'] = 'AA'
gdfSel.loc[(gdfSel['Cambio1516_1'].isnull()) & (gdfSel['Cambio1516_2'].isnull()) & (gdfSel['Cambio1516_3'].isnull()), 'Cambio1516'] = np.nan
gdfSel.loc[(gdfSel['Cambio1516_1'].isnull()) & (gdfSel['Cambio1516_2'].isnull()) & (gdfSel['Cambio1516_3'].isnull()), 'Coincidencia1516'] = 'A'
gdfSel.loc[(gdfSel['Cambio1516_1'].notnull()) & (gdfSel['Cambio1516_2'].isnull()) & (gdfSel['Cambio1516_3'].isnull()), 'Cambio1516'] = gdfSel['Cambio1516_1']
gdfSel.loc[(gdfSel['Cambio1516_1'].notnull()) & (gdfSel['Cambio1516_2'].isnull()) & (gdfSel['Cambio1516_3'].isnull()), 'Coincidencia1516'] = 'BB'
gdfSel.loc[(gdfSel['Cambio1516_1'].isnull()) & (gdfSel['Cambio1516_2'].notnull()) & (gdfSel['Cambio1516_3'].isnull()), 'Cambio1516'] = gdfSel['Cambio1516_2']
gdfSel.loc[(gdfSel['Cambio1516_1'].isnull()) & (gdfSel['Cambio1516_2'].notnull()) & (gdfSel['Cambio1516_3'].isnull()), 'Coincidencia1516'] = 'CC'
gdfSel.loc[(gdfSel['Cambio1516_1'].isnull()) & (gdfSel['Cambio1516_2'].isnull()) & (gdfSel['Cambio1516_3'].notnull()), 'Cambio1516'] = gdfSel['Cambio1516_3']
gdfSel.loc[(gdfSel['Cambio1516_1'].isnull()) & (gdfSel['Cambio1516_2'].isnull()) & (gdfSel['Cambio1516_3'].notnull()), 'Coincidencia1516'] = 'HH'
gdfSel.loc[(gdfSel['Cambio1516_1'] == gdfSel['Cambio1516_2']) & (gdfSel['Cambio1516_3'] == gdfSel['Cambio1516_2']) & (gdfSel['Cambio1516_1'] == gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_1'].notnull()) & (gdfSel['Cambio1516_2'].notnull()) & (gdfSel['Cambio1516_3'].notnull()), 'Cambio1516'] = gdfSel['Cambio1516_1']
gdfSel.loc[(gdfSel['Cambio1516_1'] == gdfSel['Cambio1516_2']) & (gdfSel['Cambio1516_3'] == gdfSel['Cambio1516_2']) & (gdfSel['Cambio1516_1'] == gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_1'].notnull()) & (gdfSel['Cambio1516_2'].notnull()) & (gdfSel['Cambio1516_3'].notnull()), 'Coincidencia1516'] = 'E'
gdfSel.loc[(gdfSel['Cambio1516_1'] != gdfSel['Cambio1516_2']) & (gdfSel['Cambio1516_2'] == gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_1'].notnull()) & (gdfSel['Cambio1516_2'].notnull()) & (gdfSel['Cambio1516_3'].notnull()), 'Cambio1516'] = gdfSel['Cambio1516_2']
gdfSel.loc[(gdfSel['Cambio1516_1'] != gdfSel['Cambio1516_2']) & (gdfSel['Cambio1516_2'] == gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_1'].notnull()) & (gdfSel['Cambio1516_2'].notnull()) & (gdfSel['Cambio1516_3'].notnull()), 'Coincidencia1516'] = 'B'
gdfSel.loc[(gdfSel['Cambio1516_1'] == gdfSel['Cambio1516_2']) & (gdfSel['Cambio1516_2'] != gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_1'].notnull()) & (gdfSel['Cambio1516_2'].notnull()) & (gdfSel['Cambio1516_3'].notnull()), 'Cambio1516'] = gdfSel['Cambio1516_1']
gdfSel.loc[(gdfSel['Cambio1516_1'] == gdfSel['Cambio1516_2']) & (gdfSel['Cambio1516_2'] != gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_1'].notnull()) & (gdfSel['Cambio1516_2'].notnull()) & (gdfSel['Cambio1516_3'].notnull()), 'Coincidencia1516'] = 'C'
gdfSel.loc[(gdfSel['Cambio1516_1'] == gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_2'] != gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_1'].notnull()) & (gdfSel['Cambio1516_2'].notnull()) & (gdfSel['Cambio1516_3'].notnull()), 'Cambio1516'] = gdfSel['Cambio1516_1']
gdfSel.loc[(gdfSel['Cambio1516_1'] == gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_2'] != gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_1'].notnull()) & (gdfSel['Cambio1516_2'].notnull()) & (gdfSel['Cambio1516_3'].notnull()), 'Coincidencia1516'] = 'D'
gdfSel.loc[(gdfSel['Cambio1516_1'].isnull()) & (gdfSel['Cambio1516_2'] == gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_3'].notnull()), 'Cambio1516'] = gdfSel['Cambio1516_2']
gdfSel.loc[(gdfSel['Cambio1516_1'].isnull()) & (gdfSel['Cambio1516_2'] == gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_3'].notnull()), 'Coincidencia1516'] = 'DD'
gdfSel.loc[(gdfSel['Cambio1516_1'].isnull()) & (gdfSel['Cambio1516_2'] != gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_3'].notnull()), 'Cambio1516'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1516_1'].isnull()) & (gdfSel['Cambio1516_2'] != gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_3'].notnull()), 'Coincidencia1516'] = 'FF'
gdfSel.loc[(gdfSel['Cambio1516_1'] != gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_2'] != gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_1'] != gdfSel['Cambio1516_2']) & (gdfSel['Cambio1516_1'].notnull()) & (gdfSel['Cambio1516_2'].notnull()) & (gdfSel['Cambio1516_3'].notnull()), 'Cambio1516'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1516_1'] != gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_2'] != gdfSel['Cambio1516_3']) & (gdfSel['Cambio1516_1'] != gdfSel['Cambio1516_2']) & (gdfSel['Cambio1516_1'].notnull()) & (gdfSel['Cambio1516_2'].notnull()) & (gdfSel['Cambio1516_3'].notnull()), 'Coincidencia1516'] = 'F'



# %%
# Cambios 2016-2017
gdfSel.loc[(gdfSel['Cambio1617_1'] == gdfSel['Cambio1617_2']) & (gdfSel['Cambio1617_3'].isnull()), 'Cambio1617'] = gdfSel['Cambio1617_1']
gdfSel.loc[(gdfSel['Cambio1617_1'] == gdfSel['Cambio1617_2']) & (gdfSel['Cambio1617_3'].isnull()), 'Coincidencia1617'] = 'EA'
gdfSel.loc[(gdfSel['Cambio1617_1'] != gdfSel['Cambio1617_2']) & (gdfSel['Cambio1617_3'].isnull()), 'Cambio1617'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1617_1'] != gdfSel['Cambio1617_2']) & (gdfSel['Cambio1617_3'].isnull()), 'Coincidencia1617'] = 'AA'
gdfSel.loc[(gdfSel['Cambio1617_1'].isnull()) & (gdfSel['Cambio1617_2'].isnull()) & (gdfSel['Cambio1617_3'].isnull()), 'Cambio1617'] = np.nan
gdfSel.loc[(gdfSel['Cambio1617_1'].isnull()) & (gdfSel['Cambio1617_2'].isnull()) & (gdfSel['Cambio1617_3'].isnull()), 'Coincidencia1617'] = 'A'
gdfSel.loc[(gdfSel['Cambio1617_1'].notnull()) & (gdfSel['Cambio1617_2'].isnull()) & (gdfSel['Cambio1617_3'].isnull()), 'Cambio1617'] = gdfSel['Cambio1617_1']
gdfSel.loc[(gdfSel['Cambio1617_1'].notnull()) & (gdfSel['Cambio1617_2'].isnull()) & (gdfSel['Cambio1617_3'].isnull()), 'Coincidencia1617'] = 'BB'
gdfSel.loc[(gdfSel['Cambio1617_1'].isnull()) & (gdfSel['Cambio1617_2'].notnull()) & (gdfSel['Cambio1617_3'].isnull()), 'Cambio1617'] = gdfSel['Cambio1617_2']
gdfSel.loc[(gdfSel['Cambio1617_1'].isnull()) & (gdfSel['Cambio1617_2'].notnull()) & (gdfSel['Cambio1617_3'].isnull()), 'Coincidencia1617'] = 'CC'
gdfSel.loc[(gdfSel['Cambio1617_1'].isnull()) & (gdfSel['Cambio1617_2'].isnull()) & (gdfSel['Cambio1617_3'].notnull()), 'Cambio1617'] = gdfSel['Cambio1617_3']
gdfSel.loc[(gdfSel['Cambio1617_1'].isnull()) & (gdfSel['Cambio1617_2'].isnull()) & (gdfSel['Cambio1617_3'].notnull()), 'Coincidencia1617'] = 'HH'
gdfSel.loc[(gdfSel['Cambio1617_1'] == gdfSel['Cambio1617_2']) & (gdfSel['Cambio1617_3'] == gdfSel['Cambio1617_2']) & (gdfSel['Cambio1617_1'] == gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_1'].notnull()) & (gdfSel['Cambio1617_2'].notnull()) & (gdfSel['Cambio1617_3'].notnull()), 'Cambio1617'] = gdfSel['Cambio1617_1']
gdfSel.loc[(gdfSel['Cambio1617_1'] == gdfSel['Cambio1617_2']) & (gdfSel['Cambio1617_3'] == gdfSel['Cambio1617_2']) & (gdfSel['Cambio1617_1'] == gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_1'].notnull()) & (gdfSel['Cambio1617_2'].notnull()) & (gdfSel['Cambio1617_3'].notnull()), 'Coincidencia1617'] = 'E'
gdfSel.loc[(gdfSel['Cambio1617_1'] != gdfSel['Cambio1617_2']) & (gdfSel['Cambio1617_2'] == gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_1'].notnull()) & (gdfSel['Cambio1617_2'].notnull()) & (gdfSel['Cambio1617_3'].notnull()), 'Cambio1617'] = gdfSel['Cambio1617_2']
gdfSel.loc[(gdfSel['Cambio1617_1'] != gdfSel['Cambio1617_2']) & (gdfSel['Cambio1617_2'] == gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_1'].notnull()) & (gdfSel['Cambio1617_2'].notnull()) & (gdfSel['Cambio1617_3'].notnull()), 'Coincidencia1617'] = 'B'
gdfSel.loc[(gdfSel['Cambio1617_1'] == gdfSel['Cambio1617_2']) & (gdfSel['Cambio1617_2'] != gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_1'].notnull()) & (gdfSel['Cambio1617_2'].notnull()) & (gdfSel['Cambio1617_3'].notnull()), 'Cambio1617'] = gdfSel['Cambio1617_1']
gdfSel.loc[(gdfSel['Cambio1617_1'] == gdfSel['Cambio1617_2']) & (gdfSel['Cambio1617_2'] != gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_1'].notnull()) & (gdfSel['Cambio1617_2'].notnull()) & (gdfSel['Cambio1617_3'].notnull()), 'Coincidencia1617'] = 'C'
gdfSel.loc[(gdfSel['Cambio1617_1'] == gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_2'] != gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_1'].notnull()) & (gdfSel['Cambio1617_2'].notnull()) & (gdfSel['Cambio1617_3'].notnull()), 'Cambio1617'] = gdfSel['Cambio1617_1']
gdfSel.loc[(gdfSel['Cambio1617_1'] == gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_2'] != gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_1'].notnull()) & (gdfSel['Cambio1617_2'].notnull()) & (gdfSel['Cambio1617_3'].notnull()), 'Coincidencia1617'] = 'D'
gdfSel.loc[(gdfSel['Cambio1617_1'].isnull()) & (gdfSel['Cambio1617_2'] == gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_3'].notnull()), 'Cambio1617'] = gdfSel['Cambio1617_2']
gdfSel.loc[(gdfSel['Cambio1617_1'].isnull()) & (gdfSel['Cambio1617_2'] == gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_3'].notnull()), 'Coincidencia1617'] = 'DD'
gdfSel.loc[(gdfSel['Cambio1617_1'].isnull()) & (gdfSel['Cambio1617_2'] != gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_3'].notnull()), 'Cambio1617'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1617_1'].isnull()) & (gdfSel['Cambio1617_2'] != gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_3'].notnull()), 'Coincidencia1617'] = 'FF'
gdfSel.loc[(gdfSel['Cambio1617_1'] != gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_2'] != gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_1'] != gdfSel['Cambio1617_2']) & (gdfSel['Cambio1617_1'].notnull()) & (gdfSel['Cambio1617_2'].notnull()) & (gdfSel['Cambio1617_3'].notnull()), 'Cambio1617'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1617_1'] != gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_2'] != gdfSel['Cambio1617_3']) & (gdfSel['Cambio1617_1'] != gdfSel['Cambio1617_2']) & (gdfSel['Cambio1617_1'].notnull()) & (gdfSel['Cambio1617_2'].notnull()) & (gdfSel['Cambio1617_3'].notnull()), 'Coincidencia1617'] = 'F'


# %%
# Cambios 2017-2018
gdfSel.loc[(gdfSel['Cambio1718_1'] == gdfSel['Cambio1718_2']) & (gdfSel['Cambio1718_3'].isnull()), 'Cambio1718'] = gdfSel['Cambio1718_1']
gdfSel.loc[(gdfSel['Cambio1718_1'] == gdfSel['Cambio1718_2']) & (gdfSel['Cambio1718_3'].isnull()), 'Coincidencia1718'] = 'EA'
gdfSel.loc[(gdfSel['Cambio1718_1'] != gdfSel['Cambio1718_2']) & (gdfSel['Cambio1718_3'].isnull()), 'Cambio1718'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1718_1'] != gdfSel['Cambio1718_2']) & (gdfSel['Cambio1718_3'].isnull()), 'Coincidencia1718'] = 'AA'
gdfSel.loc[(gdfSel['Cambio1718_1'].isnull()) & (gdfSel['Cambio1718_2'].isnull()) & (gdfSel['Cambio1718_3'].isnull()), 'Cambio1718'] = np.nan
gdfSel.loc[(gdfSel['Cambio1718_1'].isnull()) & (gdfSel['Cambio1718_2'].isnull()) & (gdfSel['Cambio1718_3'].isnull()), 'Coincidencia1718'] = 'A'
gdfSel.loc[(gdfSel['Cambio1718_1'].notnull()) & (gdfSel['Cambio1718_2'].isnull()) & (gdfSel['Cambio1718_3'].isnull()), 'Cambio1718'] = gdfSel['Cambio1718_1']
gdfSel.loc[(gdfSel['Cambio1718_1'].notnull()) & (gdfSel['Cambio1718_2'].isnull()) & (gdfSel['Cambio1718_3'].isnull()), 'Coincidencia1718'] = 'BB'
gdfSel.loc[(gdfSel['Cambio1718_1'].isnull()) & (gdfSel['Cambio1718_2'].notnull()) & (gdfSel['Cambio1718_3'].isnull()), 'Cambio1718'] = gdfSel['Cambio1718_2']
gdfSel.loc[(gdfSel['Cambio1718_1'].isnull()) & (gdfSel['Cambio1718_2'].notnull()) & (gdfSel['Cambio1718_3'].isnull()), 'Coincidencia1718'] = 'CC'
gdfSel.loc[(gdfSel['Cambio1718_1'].isnull()) & (gdfSel['Cambio1718_2'].isnull()) & (gdfSel['Cambio1718_3'].notnull()), 'Cambio1718'] = gdfSel['Cambio1718_3']
gdfSel.loc[(gdfSel['Cambio1718_1'].isnull()) & (gdfSel['Cambio1718_2'].isnull()) & (gdfSel['Cambio1718_3'].notnull()), 'Coincidencia1718'] = 'HH'
gdfSel.loc[(gdfSel['Cambio1718_1'] == gdfSel['Cambio1718_2']) & (gdfSel['Cambio1718_3'] == gdfSel['Cambio1718_2']) & (gdfSel['Cambio1718_1'] == gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_1'].notnull()) & (gdfSel['Cambio1718_2'].notnull()) & (gdfSel['Cambio1718_3'].notnull()), 'Cambio1718'] = gdfSel['Cambio1718_1']
gdfSel.loc[(gdfSel['Cambio1718_1'] == gdfSel['Cambio1718_2']) & (gdfSel['Cambio1718_3'] == gdfSel['Cambio1718_2']) & (gdfSel['Cambio1718_1'] == gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_1'].notnull()) & (gdfSel['Cambio1718_2'].notnull()) & (gdfSel['Cambio1718_3'].notnull()), 'Coincidencia1718'] = 'E'
gdfSel.loc[(gdfSel['Cambio1718_1'] != gdfSel['Cambio1718_2']) & (gdfSel['Cambio1718_2'] == gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_1'].notnull()) & (gdfSel['Cambio1718_2'].notnull()) & (gdfSel['Cambio1718_3'].notnull()), 'Cambio1718'] = gdfSel['Cambio1718_2']
gdfSel.loc[(gdfSel['Cambio1718_1'] != gdfSel['Cambio1718_2']) & (gdfSel['Cambio1718_2'] == gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_1'].notnull()) & (gdfSel['Cambio1718_2'].notnull()) & (gdfSel['Cambio1718_3'].notnull()), 'Coincidencia1718'] = 'B'
gdfSel.loc[(gdfSel['Cambio1718_1'] == gdfSel['Cambio1718_2']) & (gdfSel['Cambio1718_2'] != gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_1'].notnull()) & (gdfSel['Cambio1718_2'].notnull()) & (gdfSel['Cambio1718_3'].notnull()), 'Cambio1718'] = gdfSel['Cambio1718_1']
gdfSel.loc[(gdfSel['Cambio1718_1'] == gdfSel['Cambio1718_2']) & (gdfSel['Cambio1718_2'] != gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_1'].notnull()) & (gdfSel['Cambio1718_2'].notnull()) & (gdfSel['Cambio1718_3'].notnull()), 'Coincidencia1718'] = 'C'
gdfSel.loc[(gdfSel['Cambio1718_1'] == gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_2'] != gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_1'].notnull()) & (gdfSel['Cambio1718_2'].notnull()) & (gdfSel['Cambio1718_3'].notnull()), 'Cambio1718'] = gdfSel['Cambio1718_1']
gdfSel.loc[(gdfSel['Cambio1718_1'] == gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_2'] != gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_1'].notnull()) & (gdfSel['Cambio1718_2'].notnull()) & (gdfSel['Cambio1718_3'].notnull()), 'Coincidencia1718'] = 'D'
gdfSel.loc[(gdfSel['Cambio1718_1'].isnull()) & (gdfSel['Cambio1718_2'] == gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_3'].notnull()), 'Cambio1718'] = gdfSel['Cambio1718_2']
gdfSel.loc[(gdfSel['Cambio1718_1'].isnull()) & (gdfSel['Cambio1718_2'] == gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_3'].notnull()), 'Coincidencia1718'] = 'DD'
gdfSel.loc[(gdfSel['Cambio1718_1'].isnull()) & (gdfSel['Cambio1718_2'] != gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_3'].notnull()), 'Cambio1718'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1718_1'].isnull()) & (gdfSel['Cambio1718_2'] != gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_3'].notnull()), 'Coincidencia1718'] = 'FF'
gdfSel.loc[(gdfSel['Cambio1718_1'] != gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_2'] != gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_1'] != gdfSel['Cambio1718_2']) & (gdfSel['Cambio1718_1'].notnull()) & (gdfSel['Cambio1718_2'].notnull()) & (gdfSel['Cambio1718_3'].notnull()), 'Cambio1718'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1718_1'] != gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_2'] != gdfSel['Cambio1718_3']) & (gdfSel['Cambio1718_1'] != gdfSel['Cambio1718_2']) & (gdfSel['Cambio1718_1'].notnull()) & (gdfSel['Cambio1718_2'].notnull()) & (gdfSel['Cambio1718_3'].notnull()), 'Coincidencia1718'] = 'F'



# %%
# Cambios 2018-2019
gdfSel.loc[(gdfSel['Cambio1819_1'] == gdfSel['Cambio1819_2']) & (gdfSel['Cambio1819_3'].isnull()), 'Cambio1819'] = gdfSel['Cambio1819_1']
gdfSel.loc[(gdfSel['Cambio1819_1'] == gdfSel['Cambio1819_2']) & (gdfSel['Cambio1819_3'].isnull()), 'Coincidencia1819'] = 'EA'
gdfSel.loc[(gdfSel['Cambio1819_1'] != gdfSel['Cambio1819_2']) & (gdfSel['Cambio1819_3'].isnull()), 'Cambio1819'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1819_1'] != gdfSel['Cambio1819_2']) & (gdfSel['Cambio1819_3'].isnull()), 'Coincidencia1819'] = 'AA'
gdfSel.loc[(gdfSel['Cambio1819_1'].isnull()) & (gdfSel['Cambio1819_2'].isnull()) & (gdfSel['Cambio1819_3'].isnull()), 'Cambio1819'] = np.nan
gdfSel.loc[(gdfSel['Cambio1819_1'].isnull()) & (gdfSel['Cambio1819_2'].isnull()) & (gdfSel['Cambio1819_3'].isnull()), 'Coincidencia1819'] = 'A'
gdfSel.loc[(gdfSel['Cambio1819_1'].notnull()) & (gdfSel['Cambio1819_2'].isnull()) & (gdfSel['Cambio1819_3'].isnull()), 'Cambio1819'] = gdfSel['Cambio1819_1']
gdfSel.loc[(gdfSel['Cambio1819_1'].notnull()) & (gdfSel['Cambio1819_2'].isnull()) & (gdfSel['Cambio1819_3'].isnull()), 'Coincidencia1819'] = 'BB'
gdfSel.loc[(gdfSel['Cambio1819_1'].isnull()) & (gdfSel['Cambio1819_2'].notnull()) & (gdfSel['Cambio1819_3'].isnull()), 'Cambio1819'] = gdfSel['Cambio1819_2']
gdfSel.loc[(gdfSel['Cambio1819_1'].isnull()) & (gdfSel['Cambio1819_2'].notnull()) & (gdfSel['Cambio1819_3'].isnull()), 'Coincidencia1819'] = 'CC'
gdfSel.loc[(gdfSel['Cambio1819_1'].isnull()) & (gdfSel['Cambio1819_2'].isnull()) & (gdfSel['Cambio1819_3'].notnull()), 'Cambio1819'] = gdfSel['Cambio1819_3']
gdfSel.loc[(gdfSel['Cambio1819_1'].isnull()) & (gdfSel['Cambio1819_2'].isnull()) & (gdfSel['Cambio1819_3'].notnull()), 'Coincidencia1819'] = 'HH'
gdfSel.loc[(gdfSel['Cambio1819_1'] == gdfSel['Cambio1819_2']) & (gdfSel['Cambio1819_3'] == gdfSel['Cambio1819_2']) & (gdfSel['Cambio1819_1'] == gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_1'].notnull()) & (gdfSel['Cambio1819_2'].notnull()) & (gdfSel['Cambio1819_3'].notnull()), 'Cambio1819'] = gdfSel['Cambio1819_1']
gdfSel.loc[(gdfSel['Cambio1819_1'] == gdfSel['Cambio1819_2']) & (gdfSel['Cambio1819_3'] == gdfSel['Cambio1819_2']) & (gdfSel['Cambio1819_1'] == gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_1'].notnull()) & (gdfSel['Cambio1819_2'].notnull()) & (gdfSel['Cambio1819_3'].notnull()), 'Coincidencia1819'] = 'E'
gdfSel.loc[(gdfSel['Cambio1819_1'] != gdfSel['Cambio1819_2']) & (gdfSel['Cambio1819_2'] == gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_1'].notnull()) & (gdfSel['Cambio1819_2'].notnull()) & (gdfSel['Cambio1819_3'].notnull()), 'Cambio1819'] = gdfSel['Cambio1819_2']
gdfSel.loc[(gdfSel['Cambio1819_1'] != gdfSel['Cambio1819_2']) & (gdfSel['Cambio1819_2'] == gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_1'].notnull()) & (gdfSel['Cambio1819_2'].notnull()) & (gdfSel['Cambio1819_3'].notnull()), 'Coincidencia1819'] = 'B'
gdfSel.loc[(gdfSel['Cambio1819_1'] == gdfSel['Cambio1819_2']) & (gdfSel['Cambio1819_2'] != gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_1'].notnull()) & (gdfSel['Cambio1819_2'].notnull()) & (gdfSel['Cambio1819_3'].notnull()), 'Cambio1819'] = gdfSel['Cambio1819_1']
gdfSel.loc[(gdfSel['Cambio1819_1'] == gdfSel['Cambio1819_2']) & (gdfSel['Cambio1819_2'] != gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_1'].notnull()) & (gdfSel['Cambio1819_2'].notnull()) & (gdfSel['Cambio1819_3'].notnull()), 'Coincidencia1819'] = 'C'
gdfSel.loc[(gdfSel['Cambio1819_1'] == gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_2'] != gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_1'].notnull()) & (gdfSel['Cambio1819_2'].notnull()) & (gdfSel['Cambio1819_3'].notnull()), 'Cambio1819'] = gdfSel['Cambio1819_1']
gdfSel.loc[(gdfSel['Cambio1819_1'] == gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_2'] != gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_1'].notnull()) & (gdfSel['Cambio1819_2'].notnull()) & (gdfSel['Cambio1819_3'].notnull()), 'Coincidencia1819'] = 'D'
gdfSel.loc[(gdfSel['Cambio1819_1'].isnull()) & (gdfSel['Cambio1819_2'] == gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_3'].notnull()), 'Cambio1819'] = gdfSel['Cambio1819_2']
gdfSel.loc[(gdfSel['Cambio1819_1'].isnull()) & (gdfSel['Cambio1819_2'] == gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_3'].notnull()), 'Coincidencia1819'] = 'DD'
gdfSel.loc[(gdfSel['Cambio1819_1'].isnull()) & (gdfSel['Cambio1819_2'] != gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_3'].notnull()), 'Cambio1819'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1819_1'].isnull()) & (gdfSel['Cambio1819_2'] != gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_3'].notnull()), 'Coincidencia1819'] = 'FF'
gdfSel.loc[(gdfSel['Cambio1819_1'] != gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_2'] != gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_1'] != gdfSel['Cambio1819_2']) & (gdfSel['Cambio1819_1'].notnull()) & (gdfSel['Cambio1819_2'].notnull()) & (gdfSel['Cambio1819_3'].notnull()), 'Cambio1819'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1819_1'] != gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_2'] != gdfSel['Cambio1819_3']) & (gdfSel['Cambio1819_1'] != gdfSel['Cambio1819_2']) & (gdfSel['Cambio1819_1'].notnull()) & (gdfSel['Cambio1819_2'].notnull()) & (gdfSel['Cambio1819_3'].notnull()), 'Coincidencia1819'] = 'F'



# %%
# Cambios 2019-2020
gdfSel.loc[(gdfSel['Cambio1920_1'] == gdfSel['Cambio1920_2']) & (gdfSel['Cambio1920_3'].isnull()), 'Cambio1920'] = gdfSel['Cambio1920_1']
gdfSel.loc[(gdfSel['Cambio1920_1'] == gdfSel['Cambio1920_2']) & (gdfSel['Cambio1920_3'].isnull()), 'Coincidencia1920'] = 'EA'
gdfSel.loc[(gdfSel['Cambio1920_1'] != gdfSel['Cambio1920_2']) & (gdfSel['Cambio1920_3'].isnull()), 'Cambio1920'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1920_1'] != gdfSel['Cambio1920_2']) & (gdfSel['Cambio1920_3'].isnull()), 'Coincidencia1920'] = 'AA'
gdfSel.loc[(gdfSel['Cambio1920_1'].isnull()) & (gdfSel['Cambio1920_2'].isnull()) & (gdfSel['Cambio1920_3'].isnull()), 'Cambio1920'] = np.nan
gdfSel.loc[(gdfSel['Cambio1920_1'].isnull()) & (gdfSel['Cambio1920_2'].isnull()) & (gdfSel['Cambio1920_3'].isnull()), 'Coincidencia1920'] = 'A'
gdfSel.loc[(gdfSel['Cambio1920_1'].notnull()) & (gdfSel['Cambio1920_2'].isnull()) & (gdfSel['Cambio1920_3'].isnull()), 'Cambio1920'] = gdfSel['Cambio1920_1']
gdfSel.loc[(gdfSel['Cambio1920_1'].notnull()) & (gdfSel['Cambio1920_2'].isnull()) & (gdfSel['Cambio1920_3'].isnull()), 'Coincidencia1920'] = 'BB'
gdfSel.loc[(gdfSel['Cambio1920_1'].isnull()) & (gdfSel['Cambio1920_2'].notnull()) & (gdfSel['Cambio1920_3'].isnull()), 'Cambio1920'] = gdfSel['Cambio1920_2']
gdfSel.loc[(gdfSel['Cambio1920_1'].isnull()) & (gdfSel['Cambio1920_2'].notnull()) & (gdfSel['Cambio1920_3'].isnull()), 'Coincidencia1920'] = 'CC'
gdfSel.loc[(gdfSel['Cambio1920_1'].isnull()) & (gdfSel['Cambio1920_2'].isnull()) & (gdfSel['Cambio1920_3'].notnull()), 'Cambio1920'] = gdfSel['Cambio1920_3']
gdfSel.loc[(gdfSel['Cambio1920_1'].isnull()) & (gdfSel['Cambio1920_2'].isnull()) & (gdfSel['Cambio1920_3'].notnull()), 'Coincidencia1920'] = 'HH'
gdfSel.loc[(gdfSel['Cambio1920_1'] == gdfSel['Cambio1920_2']) & (gdfSel['Cambio1920_3'] == gdfSel['Cambio1920_2']) & (gdfSel['Cambio1920_1'] == gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_1'].notnull()) & (gdfSel['Cambio1920_2'].notnull()) & (gdfSel['Cambio1920_3'].notnull()), 'Cambio1920'] = gdfSel['Cambio1920_1']
gdfSel.loc[(gdfSel['Cambio1920_1'] == gdfSel['Cambio1920_2']) & (gdfSel['Cambio1920_3'] == gdfSel['Cambio1920_2']) & (gdfSel['Cambio1920_1'] == gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_1'].notnull()) & (gdfSel['Cambio1920_2'].notnull()) & (gdfSel['Cambio1920_3'].notnull()), 'Coincidencia1920'] = 'E'
gdfSel.loc[(gdfSel['Cambio1920_1'] != gdfSel['Cambio1920_2']) & (gdfSel['Cambio1920_2'] == gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_1'].notnull()) & (gdfSel['Cambio1920_2'].notnull()) & (gdfSel['Cambio1920_3'].notnull()), 'Cambio1920'] = gdfSel['Cambio1920_2']
gdfSel.loc[(gdfSel['Cambio1920_1'] != gdfSel['Cambio1920_2']) & (gdfSel['Cambio1920_2'] == gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_1'].notnull()) & (gdfSel['Cambio1920_2'].notnull()) & (gdfSel['Cambio1920_3'].notnull()), 'Coincidencia1920'] = 'B'
gdfSel.loc[(gdfSel['Cambio1920_1'] == gdfSel['Cambio1920_2']) & (gdfSel['Cambio1920_2'] != gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_1'].notnull()) & (gdfSel['Cambio1920_2'].notnull()) & (gdfSel['Cambio1920_3'].notnull()), 'Cambio1920'] = gdfSel['Cambio1920_1']
gdfSel.loc[(gdfSel['Cambio1920_1'] == gdfSel['Cambio1920_2']) & (gdfSel['Cambio1920_2'] != gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_1'].notnull()) & (gdfSel['Cambio1920_2'].notnull()) & (gdfSel['Cambio1920_3'].notnull()), 'Coincidencia1920'] = 'C'
gdfSel.loc[(gdfSel['Cambio1920_1'] == gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_2'] != gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_1'].notnull()) & (gdfSel['Cambio1920_2'].notnull()) & (gdfSel['Cambio1920_3'].notnull()), 'Cambio1920'] = gdfSel['Cambio1920_1']
gdfSel.loc[(gdfSel['Cambio1920_1'] == gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_2'] != gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_1'].notnull()) & (gdfSel['Cambio1920_2'].notnull()) & (gdfSel['Cambio1920_3'].notnull()), 'Coincidencia1920'] = 'D'
gdfSel.loc[(gdfSel['Cambio1920_1'].isnull()) & (gdfSel['Cambio1920_2'] == gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_3'].notnull()), 'Cambio1920'] = gdfSel['Cambio1920_2']
gdfSel.loc[(gdfSel['Cambio1920_1'].isnull()) & (gdfSel['Cambio1920_2'] == gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_3'].notnull()), 'Coincidencia1920'] = 'DD'
gdfSel.loc[(gdfSel['Cambio1920_1'].isnull()) & (gdfSel['Cambio1920_2'] != gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_3'].notnull()), 'Cambio1920'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1920_1'].isnull()) & (gdfSel['Cambio1920_2'] != gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_3'].notnull()), 'Coincidencia1920'] = 'FF'
gdfSel.loc[(gdfSel['Cambio1920_1'] != gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_2'] != gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_1'] != gdfSel['Cambio1920_2']) & (gdfSel['Cambio1920_1'].notnull()) & (gdfSel['Cambio1920_2'].notnull()) & (gdfSel['Cambio1920_3'].notnull()), 'Cambio1920'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio1920_1'] != gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_2'] != gdfSel['Cambio1920_3']) & (gdfSel['Cambio1920_1'] != gdfSel['Cambio1920_2']) & (gdfSel['Cambio1920_1'].notnull()) & (gdfSel['Cambio1920_2'].notnull()) & (gdfSel['Cambio1920_3'].notnull()), 'Coincidencia1920'] = 'F'



# %%
# Cambios 2020-2021
gdfSel.loc[(gdfSel['Cambio2021_1'] == gdfSel['Cambio2021_2']) & (gdfSel['Cambio2021_3'].isnull()), 'Cambio2021'] = gdfSel['Cambio2021_1']
gdfSel.loc[(gdfSel['Cambio2021_1'] == gdfSel['Cambio2021_2']) & (gdfSel['Cambio2021_3'].isnull()), 'Coincidencia2021'] = 'EA'
gdfSel.loc[(gdfSel['Cambio2021_1'] != gdfSel['Cambio2021_2']) & (gdfSel['Cambio2021_3'].isnull()), 'Cambio2021'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio2021_1'] != gdfSel['Cambio2021_2']) & (gdfSel['Cambio2021_3'].isnull()), 'Coincidencia2021'] = 'AA'
gdfSel.loc[(gdfSel['Cambio2021_1'].isnull()) & (gdfSel['Cambio2021_2'].isnull()) & (gdfSel['Cambio2021_3'].isnull()), 'Cambio2021'] = np.nan
gdfSel.loc[(gdfSel['Cambio2021_1'].isnull()) & (gdfSel['Cambio2021_2'].isnull()) & (gdfSel['Cambio2021_3'].isnull()), 'Coincidencia2021'] = 'A'
gdfSel.loc[(gdfSel['Cambio2021_1'].notnull()) & (gdfSel['Cambio2021_2'].isnull()) & (gdfSel['Cambio2021_3'].isnull()), 'Cambio2021'] = gdfSel['Cambio2021_1']
gdfSel.loc[(gdfSel['Cambio2021_1'].notnull()) & (gdfSel['Cambio2021_2'].isnull()) & (gdfSel['Cambio2021_3'].isnull()), 'Coincidencia2021'] = 'BB'
gdfSel.loc[(gdfSel['Cambio2021_1'].isnull()) & (gdfSel['Cambio2021_2'].notnull()) & (gdfSel['Cambio2021_3'].isnull()), 'Cambio2021'] = gdfSel['Cambio2021_2']
gdfSel.loc[(gdfSel['Cambio2021_1'].isnull()) & (gdfSel['Cambio2021_2'].notnull()) & (gdfSel['Cambio2021_3'].isnull()), 'Coincidencia2021'] = 'CC'
gdfSel.loc[(gdfSel['Cambio2021_1'].isnull()) & (gdfSel['Cambio2021_2'].isnull()) & (gdfSel['Cambio2021_3'].notnull()), 'Cambio2021'] = gdfSel['Cambio2021_3']
gdfSel.loc[(gdfSel['Cambio2021_1'].isnull()) & (gdfSel['Cambio2021_2'].isnull()) & (gdfSel['Cambio2021_3'].notnull()), 'Coincidencia2021'] = 'HH'
gdfSel.loc[(gdfSel['Cambio2021_1'] == gdfSel['Cambio2021_2']) & (gdfSel['Cambio2021_3'] == gdfSel['Cambio2021_2']) & (gdfSel['Cambio2021_1'] == gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_1'].notnull()) & (gdfSel['Cambio2021_2'].notnull()) & (gdfSel['Cambio2021_3'].notnull()), 'Cambio2021'] = gdfSel['Cambio2021_1']
gdfSel.loc[(gdfSel['Cambio2021_1'] == gdfSel['Cambio2021_2']) & (gdfSel['Cambio2021_3'] == gdfSel['Cambio2021_2']) & (gdfSel['Cambio2021_1'] == gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_1'].notnull()) & (gdfSel['Cambio2021_2'].notnull()) & (gdfSel['Cambio2021_3'].notnull()), 'Coincidencia2021'] = 'E'
gdfSel.loc[(gdfSel['Cambio2021_1'] != gdfSel['Cambio2021_2']) & (gdfSel['Cambio2021_2'] == gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_1'].notnull()) & (gdfSel['Cambio2021_2'].notnull()) & (gdfSel['Cambio2021_3'].notnull()), 'Cambio2021'] = gdfSel['Cambio2021_2']
gdfSel.loc[(gdfSel['Cambio2021_1'] != gdfSel['Cambio2021_2']) & (gdfSel['Cambio2021_2'] == gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_1'].notnull()) & (gdfSel['Cambio2021_2'].notnull()) & (gdfSel['Cambio2021_3'].notnull()), 'Coincidencia2021'] = 'B'
gdfSel.loc[(gdfSel['Cambio2021_1'] == gdfSel['Cambio2021_2']) & (gdfSel['Cambio2021_2'] != gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_1'].notnull()) & (gdfSel['Cambio2021_2'].notnull()) & (gdfSel['Cambio2021_3'].notnull()), 'Cambio2021'] = gdfSel['Cambio2021_1']
gdfSel.loc[(gdfSel['Cambio2021_1'] == gdfSel['Cambio2021_2']) & (gdfSel['Cambio2021_2'] != gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_1'].notnull()) & (gdfSel['Cambio2021_2'].notnull()) & (gdfSel['Cambio2021_3'].notnull()), 'Coincidencia2021'] = 'C'
gdfSel.loc[(gdfSel['Cambio2021_1'] == gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_2'] != gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_1'].notnull()) & (gdfSel['Cambio2021_2'].notnull()) & (gdfSel['Cambio2021_3'].notnull()), 'Cambio2021'] = gdfSel['Cambio2021_1']
gdfSel.loc[(gdfSel['Cambio2021_1'] == gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_2'] != gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_1'].notnull()) & (gdfSel['Cambio2021_2'].notnull()) & (gdfSel['Cambio2021_3'].notnull()), 'Coincidencia2021'] = 'D'
gdfSel.loc[(gdfSel['Cambio2021_1'].isnull()) & (gdfSel['Cambio2021_2'] == gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_3'].notnull()), 'Cambio2021'] = gdfSel['Cambio2021_2']
gdfSel.loc[(gdfSel['Cambio2021_1'].isnull()) & (gdfSel['Cambio2021_2'] == gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_3'].notnull()), 'Coincidencia2021'] = 'DD'
gdfSel.loc[(gdfSel['Cambio2021_1'].isnull()) & (gdfSel['Cambio2021_2'] != gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_3'].notnull()), 'Cambio2021'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio2021_1'].isnull()) & (gdfSel['Cambio2021_2'] != gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_3'].notnull()), 'Coincidencia2021'] = 'FF'
gdfSel.loc[(gdfSel['Cambio2021_1'] != gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_2'] != gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_1'] != gdfSel['Cambio2021_2']) & (gdfSel['Cambio2021_1'].notnull()) & (gdfSel['Cambio2021_2'].notnull()) & (gdfSel['Cambio2021_3'].notnull()), 'Cambio2021'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio2021_1'] != gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_2'] != gdfSel['Cambio2021_3']) & (gdfSel['Cambio2021_1'] != gdfSel['Cambio2021_2']) & (gdfSel['Cambio2021_1'].notnull()) & (gdfSel['Cambio2021_2'].notnull()) & (gdfSel['Cambio2021_3'].notnull()), 'Coincidencia2021'] = 'F'



# %%
# Cambios 2021-2022
gdfSel.loc[(gdfSel['Cambio2122_1'] == gdfSel['Cambio2122_2']) & (gdfSel['Cambio2122_3'].isnull()), 'Cambio2122'] = gdfSel['Cambio2122_1']
gdfSel.loc[(gdfSel['Cambio2122_1'] == gdfSel['Cambio2122_2']) & (gdfSel['Cambio2122_3'].isnull()), 'Coincidencia2122'] = 'EA'
gdfSel.loc[(gdfSel['Cambio2122_1'] != gdfSel['Cambio2122_2']) & (gdfSel['Cambio2122_3'].isnull()), 'Cambio2122'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio2122_1'] != gdfSel['Cambio2122_2']) & (gdfSel['Cambio2122_3'].isnull()), 'Coincidencia2122'] = 'AA'
gdfSel.loc[(gdfSel['Cambio2122_1'].isnull()) & (gdfSel['Cambio2122_2'].isnull()) & (gdfSel['Cambio2122_3'].isnull()), 'Cambio2122'] = np.nan
gdfSel.loc[(gdfSel['Cambio2122_1'].isnull()) & (gdfSel['Cambio2122_2'].isnull()) & (gdfSel['Cambio2122_3'].isnull()), 'Coincidencia2122'] = 'A'
gdfSel.loc[(gdfSel['Cambio2122_1'].notnull()) & (gdfSel['Cambio2122_2'].isnull()) & (gdfSel['Cambio2122_3'].isnull()), 'Cambio2122'] = gdfSel['Cambio2122_1']
gdfSel.loc[(gdfSel['Cambio2122_1'].notnull()) & (gdfSel['Cambio2122_2'].isnull()) & (gdfSel['Cambio2122_3'].isnull()), 'Coincidencia2122'] = 'BB'
gdfSel.loc[(gdfSel['Cambio2122_1'].isnull()) & (gdfSel['Cambio2122_2'].notnull()) & (gdfSel['Cambio2122_3'].isnull()), 'Cambio2122'] = gdfSel['Cambio2122_2']
gdfSel.loc[(gdfSel['Cambio2122_1'].isnull()) & (gdfSel['Cambio2122_2'].notnull()) & (gdfSel['Cambio2122_3'].isnull()), 'Coincidencia2122'] = 'CC'
gdfSel.loc[(gdfSel['Cambio2122_1'].isnull()) & (gdfSel['Cambio2122_2'].isnull()) & (gdfSel['Cambio2122_3'].notnull()), 'Cambio2122'] = gdfSel['Cambio2122_3']
gdfSel.loc[(gdfSel['Cambio2122_1'].isnull()) & (gdfSel['Cambio2122_2'].isnull()) & (gdfSel['Cambio2122_3'].notnull()), 'Coincidencia2122'] = 'HH'
gdfSel.loc[(gdfSel['Cambio2122_1'] == gdfSel['Cambio2122_2']) & (gdfSel['Cambio2122_3'] == gdfSel['Cambio2122_2']) & (gdfSel['Cambio2122_1'] == gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_1'].notnull()) & (gdfSel['Cambio2122_2'].notnull()) & (gdfSel['Cambio2122_3'].notnull()), 'Cambio2122'] = gdfSel['Cambio2122_1']
gdfSel.loc[(gdfSel['Cambio2122_1'] == gdfSel['Cambio2122_2']) & (gdfSel['Cambio2122_3'] == gdfSel['Cambio2122_2']) & (gdfSel['Cambio2122_1'] == gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_1'].notnull()) & (gdfSel['Cambio2122_2'].notnull()) & (gdfSel['Cambio2122_3'].notnull()), 'Coincidencia2122'] = 'E'
gdfSel.loc[(gdfSel['Cambio2122_1'] != gdfSel['Cambio2122_2']) & (gdfSel['Cambio2122_2'] == gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_1'].notnull()) & (gdfSel['Cambio2122_2'].notnull()) & (gdfSel['Cambio2122_3'].notnull()), 'Cambio2122'] = gdfSel['Cambio2122_2']
gdfSel.loc[(gdfSel['Cambio2122_1'] != gdfSel['Cambio2122_2']) & (gdfSel['Cambio2122_2'] == gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_1'].notnull()) & (gdfSel['Cambio2122_2'].notnull()) & (gdfSel['Cambio2122_3'].notnull()), 'Coincidencia2122'] = 'B'
gdfSel.loc[(gdfSel['Cambio2122_1'] == gdfSel['Cambio2122_2']) & (gdfSel['Cambio2122_2'] != gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_1'].notnull()) & (gdfSel['Cambio2122_2'].notnull()) & (gdfSel['Cambio2122_3'].notnull()), 'Cambio2122'] = gdfSel['Cambio2122_1']
gdfSel.loc[(gdfSel['Cambio2122_1'] == gdfSel['Cambio2122_2']) & (gdfSel['Cambio2122_2'] != gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_1'].notnull()) & (gdfSel['Cambio2122_2'].notnull()) & (gdfSel['Cambio2122_3'].notnull()), 'Coincidencia2122'] = 'C'
gdfSel.loc[(gdfSel['Cambio2122_1'] == gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_2'] != gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_1'].notnull()) & (gdfSel['Cambio2122_2'].notnull()) & (gdfSel['Cambio2122_3'].notnull()), 'Cambio2122'] = gdfSel['Cambio2122_1']
gdfSel.loc[(gdfSel['Cambio2122_1'] == gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_2'] != gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_1'].notnull()) & (gdfSel['Cambio2122_2'].notnull()) & (gdfSel['Cambio2122_3'].notnull()), 'Coincidencia2122'] = 'D'
gdfSel.loc[(gdfSel['Cambio2122_1'].isnull()) & (gdfSel['Cambio2122_2'] == gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_3'].notnull()), 'Cambio2122'] = gdfSel['Cambio2122_2']
gdfSel.loc[(gdfSel['Cambio2122_1'].isnull()) & (gdfSel['Cambio2122_2'] == gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_3'].notnull()), 'Coincidencia2122'] = 'DD'
gdfSel.loc[(gdfSel['Cambio2122_1'].isnull()) & (gdfSel['Cambio2122_2'] != gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_3'].notnull()), 'Cambio2122'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio2122_1'].isnull()) & (gdfSel['Cambio2122_2'] != gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_3'].notnull()), 'Coincidencia2122'] = 'FF'
gdfSel.loc[(gdfSel['Cambio2122_1'] != gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_2'] != gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_1'] != gdfSel['Cambio2122_2']) & (gdfSel['Cambio2122_1'].notnull()) & (gdfSel['Cambio2122_2'].notnull()) & (gdfSel['Cambio2122_3'].notnull()), 'Cambio2122'] = 'Evaluar'
gdfSel.loc[(gdfSel['Cambio2122_1'] != gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_2'] != gdfSel['Cambio2122_3']) & (gdfSel['Cambio2122_1'] != gdfSel['Cambio2122_2']) & (gdfSel['Cambio2122_1'].notnull()) & (gdfSel['Cambio2122_2'].notnull()) & (gdfSel['Cambio2122_3'].notnull()), 'Coincidencia2122'] = 'F'



#%%


print("Tipos de coincidencia 0008: ", gdfSel['Coincidencia0008'].value_counts())
print("Tipos de coincidencia 0812: ", gdfSel['Coincidencia0812'].value_counts())
print("Tipos de coincidencia 1213: ", gdfSel['Coincidencia1213'].value_counts())
print("Tipos de coincidencia 1314: ", gdfSel['Coincidencia1314'].value_counts())
print("Tipos de coincidencia 1415: ", gdfSel['Coincidencia1415'].value_counts())
print("Tipos de coincidencia 1516: ", gdfSel['Coincidencia1516'].value_counts())
print("Tipos de coincidencia 1617: ", gdfSel['Coincidencia1617'].value_counts())
print("Tipos de coincidencia 1819: ", gdfSel['Coincidencia1819'].value_counts())
print("Tipos de coincidencia 1920: ", gdfSel['Coincidencia1920'].value_counts())
print("Tipos de coincidencia 2021: ", gdfSel['Coincidencia2021'].value_counts())
print("Tipos de coincidencia 2122: ", gdfSel['Coincidencia2122'].value_counts())
# %%
#gdfchange = gdfSel[["plotid", "sampleid", "lon", "lat", "geometry", "pl_id", "pl_cluster", "pl_mon_images", "email1", "email2", "email3", 'Cambio0008', 'Coincidencia0008', 'Cambio0812', 'Coincidencia0812', 'Cambio1213', 'Coincidencia1213', 'Cambio1314', 'Coincidencia1314', 'Cambio1415', 'Coincidencia1415', 'Cambio1516', 'Coincidencia1516', 'Cambio1617', 'Coincidencia1617', 'Cambio1718', 'Coincidencia1718', 'Cambio1819', 'Coincidencia1819', 'Cambio1920', 'Coincidencia1920', 'Cambio2021', 'Coincidencia2021', 'Cambio2122', 'Coincidencia2122']]
#aggregation_functions = {'plotid': 'first', 'lon': 'first', 'lat': 'first', 'geometry': 'first', 'pl_id': 'first', 'pl_cluster': 'first', 'email1': 'first', 'email2': 'first','email3': 'first','Cambio0008': 'first', 'Coincidencia0008': 'first', 'Cambio0812': 'first', 'Coincidencia0812': 'first', 'Cambio1213': 'first', 'Coincidencia1213': 'first', 'Cambio1314': 'first', 'Coincidencia1314': 'first', 'Cambio1415': 'first', 'Coincidencia1415': 'first', 'Cambio1516': 'first', 'Coincidencia1516': 'first', 'Cambio1617': 'first', 'Coincidencia1617': 'first', 'Cambio1718': 'first', 'Coincidencia1718': 'first', 'Cambio1819': 'first', 'Coincidencia1819': 'first', 'Cambio1920': 'first', 'Coincidencia1920': 'first', 'Cambio2021': 'first', 'Coincidencia2021': 'first', 'Cambio2122': 'first', 'Coincidencia2122': 'first'}
# id columns
gdfchange = gdfSel[["plotid", "sampleid", "lon", "lat", "geometry", "pl_cluster", "pl_mon_images", "email1", "email2", "email3", 'Cambio0008', 'Coincidencia0008', 'Cambio0812', 'Coincidencia0812', 'Cambio1213', 'Coincidencia1213', 'Cambio1314', 'Coincidencia1314', 'Cambio1415', 'Coincidencia1415', 'Cambio1516', 'Coincidencia1516', 'Cambio1617', 'Coincidencia1617', 'Cambio1718', 'Coincidencia1718', 'Cambio1819', 'Coincidencia1819', 'Cambio1920', 'Coincidencia1920', 'Cambio2021', 'Coincidencia2021', 'Cambio2122', 'Coincidencia2122']]
aggregation_functions = {'plotid': 'first', 'lon': 'first', 'lat': 'first', 'geometry': 'first', 'pl_cluster': 'first', 'email1': 'first', 'email2': 'first','email3': 'first','Cambio0008': 'first', 'Coincidencia0008': 'first', 'Cambio0812': 'first', 'Coincidencia0812': 'first', 'Cambio1213': 'first', 'Coincidencia1213': 'first', 'Cambio1314': 'first', 'Coincidencia1314': 'first', 'Cambio1415': 'first', 'Coincidencia1415': 'first', 'Cambio1516': 'first', 'Coincidencia1516': 'first', 'Cambio1617': 'first', 'Coincidencia1617': 'first', 'Cambio1718': 'first', 'Coincidencia1718': 'first', 'Cambio1819': 'first', 'Coincidencia1819': 'first', 'Cambio1920': 'first', 'Coincidencia1920': 'first', 'Cambio2021': 'first', 'Coincidencia2021': 'first', 'Cambio2122': 'first', 'Coincidencia2122': 'first'}

gdfchangeN = gdfchange.groupby(gdfchange['plotid']).aggregate(aggregation_functions)

# %%
# %%
print("Tipos de coincidencia 0008: ", gdfchangeN['Coincidencia0008'].value_counts())
print("Tipos de coincidencia 0812: ", gdfchangeN['Coincidencia0812'].value_counts())
print("Tipos de coincidencia 1213: ", gdfchangeN['Coincidencia1213'].value_counts())
print("Tipos de coincidencia 1314: ", gdfchangeN['Coincidencia1314'].value_counts())
print("Tipos de coincidencia 1415: ", gdfchangeN['Coincidencia1415'].value_counts())
print("Tipos de coincidencia 1516: ", gdfchangeN['Coincidencia1516'].value_counts())
print("Tipos de coincidencia 1617: ", gdfchangeN['Coincidencia1617'].value_counts())
print("Tipos de coincidencia 1819: ", gdfchangeN['Coincidencia1819'].value_counts())
print("Tipos de coincidencia 1920: ", gdfchangeN['Coincidencia1920'].value_counts())
print("Tipos de coincidencia 2021: ", gdfchangeN['Coincidencia2021'].value_counts())
print("Tipos de coincidencia 2022: ", gdfchangeN['Coincidencia2122'].value_counts())
# %%
print("Numero de parcelas por especialistas: ", gdfchangeN['email1'].value_counts())
print("Numero de parcelas por Juniors1: ", gdfchangeN['email2'].value_counts())
print("Numero de parcelas por Juniors2: ", gdfchangeN['email3'].value_counts())
# %%
print("Clases de cambio 2000-2008: ", gdfchangeN['Cambio0008'].value_counts())
print("Clases de cambio 2008-2012: ", gdfchangeN['Cambio0812'].value_counts())
print("Clases de cambio 2012-2013: ", gdfchangeN['Cambio1213'].value_counts())
print("Clases de cambio 2013-2014: ", gdfchangeN['Cambio1314'].value_counts())
print("Clases de cambio 2014-2015: ", gdfchangeN['Cambio1415'].value_counts())
print("Clases de cambio 2015-2016: ", gdfchangeN['Cambio1516'].value_counts())
print("Clases de cambio 2016-2017: ", gdfchangeN['Cambio1617'].value_counts())
print("Clases de cambio 2017-2018: ", gdfchangeN['Cambio1718'].value_counts())
print("Clases de cambio 2018-2019: ", gdfchangeN['Cambio1819'].value_counts())
print("Clases de cambio 2019-2020: ", gdfchangeN['Cambio1920'].value_counts())
print("Clases de cambio 2020-2021: ", gdfchangeN['Cambio2021'].value_counts())
print("Clases de cambio 2021-2022: ", gdfchangeN['Cambio2122'].value_counts())

# %%
# save as csv
gdfchangeN.to_csv("./MAATE2023/Resultados2/10_NBE/ResultadosCambios_NBE_11042024.csv")
print("The CSV file has been saved")