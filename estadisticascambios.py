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
# parcelas de no cambio
parcelasestables = gdf.loc[(gdf['Cambio0008'] == gdf['Cambio0812']) & (gdf['Cambio0812'] == gdf['Cambio1213']) & (gdf['Cambio1213'] == gdf['Cambio1314']) & (gdf['Cambio1314'] == gdf['Cambio1415']) & (gdf['Cambio1415'] == gdf['Cambio1516']) & (gdf['Cambio1516'] == gdf['Cambio1617']) & (gdf['Cambio1617'] == gdf['Cambio1718']) & (gdf['Cambio1718'] == gdf['Cambio1819']) & (gdf['Cambio1819'] == gdf['Cambio1920']) & (gdf['Cambio1920'] == gdf['Cambio2021']) & (gdf['Cambio2021'] == gdf['Cambio2122'])]
print('Parcelas de no cambio:',parcelasestables.shape)
# parcelas de cambio preliminar
parcelascambio = pd.concat([gdf, parcelasestables]).drop_duplicates(subset = ['plotid'], keep=False)
print('Parcelas de cambio, incluyendo SINF y Eva:', parcelascambio.shape)
 # parcelas de cambio sin "evaluar"
parcelascambioF = parcelascambio.loc[(parcelascambio['Cambio0008'] == "Evaluar") | (parcelascambio['Cambio0812'] == "Evaluar") | (parcelascambio['Cambio1213'] == "Evaluar") | (parcelascambio['Cambio1314'] == "Evaluar") | (parcelascambio['Cambio1415'] == "Evaluar") | (parcelascambio['Cambio1516'] == "Evaluar") | (parcelascambio['Cambio1617'] == "Evaluar") | (parcelascambio['Cambio1718'] == "Evaluar") | (parcelascambio['Cambio1819'] == "Evaluar") | (parcelascambio['Cambio1920'] == "Evaluar") | (parcelascambio['Cambio2021'] == "Evaluar") | (parcelascambio['Cambio2122'] == "Evaluar")]
parcelascambioReal = pd.concat([parcelascambio, parcelascambioF]).drop_duplicates(subset = ['plotid'], keep=False)
print('Parcelas por Evaluar:', parcelascambioF.shape)
print('Parcelas de cambio incluyendo SINF:', parcelascambioReal.shape)
# parcelas con deforestación
parcelascambioSF = parcelascambioReal.loc[(parcelascambioReal['Cambio0008'] == "Sin Información") | (parcelascambioReal['Cambio0812'] == "Sin Información") | (parcelascambioReal['Cambio1213'] == "Sin Información") | (parcelascambioReal['Cambio1314'] == "Sin Información") | (parcelascambioReal['Cambio1415'] == "Sin Información") | (parcelascambioReal['Cambio1516'] == "Sin Información") | (parcelascambioReal['Cambio1617'] == "Sin Información") | (parcelascambioReal['Cambio1718'] == "Sin Información") | (parcelascambioReal['Cambio1819'] == "Sin Información") | (parcelascambioReal['Cambio1920'] == "Sin Información") | (parcelascambioReal['Cambio2021'] == "Sin Información") | (parcelascambioReal['Cambio2122'] == "Sin Información")]
parcelascambioLast = pd.concat([parcelascambioReal, parcelascambioSF]).drop_duplicates(subset = ['plotid'], keep=False)
print('Parcelas SINF:', parcelascambioSF.shape)
parcelascambioSF['Estado'] = 'SINF'
print('Parcelas de cambio:', parcelascambioLast.shape)
parcelascambioLast['Estado'] = parcelascambioLast['Cambio2122']

# %%
# parcelas bosque estable
parBE = parcelasestables.loc[(parcelasestables['Cambio0008'] == 'Bosque Estable') & (parcelasestables['Cambio2122'] == 'Bosque Estable')]
print('Parcelas de bosque estable: ',parBE.shape)
parBE['Estado'] = 'BE'

# parcelas No Bosque Estable
parNBE = parcelasestables.loc[(parcelasestables['Cambio0008'] == 'No Bosque Estable') & (parcelasestables['Cambio2122'] == 'No Bosque Estable')]
print('Parcelas de No bosque estable: ',parNBE.shape)
parNBE['Estado'] = 'NBE'
