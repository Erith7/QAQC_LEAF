#%%
# imports
import numpy as np
import pandas as pd
import geopandas as gpd
import os
import fiona

#%%
# Path definitions
rutageneral = '/Users/erith/Dropbox/Comun/FAO_LAC/2023/Ecuador/08_CSVsInterpretacion'
foldermes = '01_Julio'
folderdia ='31072023'
filenameE='ceo-PROY.-INTERP.-BSVTBA-(19-ESPECIALISTAS-USFQ)-v2-sample-data-2023-08-01.csv'
filenameJ='ceo-PROY.-INTERP.-BSVTBA-(38-TECNICOS-JUNIOR-USFQ)-sample-data-2023-08-01.csv'

#%%
# Reading files for specialists
rutames = os.path.join(rutageneral, foldermes)
rutadia = os.path.join(rutames, folderdia)
rutafileE = os.path.join(rutadia, filenameE)
fileE=pd.read_csv(rutafileE)
gdfE = gpd.GeoDataFrame(fileE, geometry=gpd.points_from_xy(fileE.lon, fileE.lat), crs="EPSG:4326")
print(gdfE.columns)
print('Numero Total de parcelas en interpretes especialistas: ', gdfE.plotid.value_counts())
#gdfE.dropna(subset=['email'], inplace=True)
#print('Numero de parcelas avanzadas en interpretes especialistas: ', gdfE.plotid.value_counts())

# %%
ciclo = 1
if ciclo == 1:
    gdfTemplate = gdfE[["plotid", "sampleid", "lon", "lat", "geometry", "pl_id", "pl_cluster", "pl_monimages"]]
    gdfTemplate['email1'] = ''
    gdfTemplate['email2'] = np.nan
    gdfTemplate['email3'] = ''
    gdfTemplate['collection_time1'] = ''
    gdfTemplate['collection_time2'] = ''
    gdfTemplate['collection_time3'] = ''
    gdfTemplate['analysis_duration1'] = ''
    gdfTemplate['analysis_duration2'] = ''
    gdfTemplate['analysis_duration3'] = ''
    gdfTemplate['imagery_title1'] = ''
    gdfTemplate['imagery_title2'] = ''
    gdfTemplate['imagery_title3'] = ''
    gdfTemplate['CUT2000_1'] = ''
    gdfTemplate['CUT2000_2'] = ''
    gdfTemplate['CUT2000_3'] = ''
    gdfTemplate['insumos2000_1'] = ''
    gdfTemplate['insumos2000_2'] = ''
    gdfTemplate['insumos2000_3'] = ''
    gdfTemplate['CUT2008_1'] = ''
    gdfTemplate['CUT2008_2'] = ''
    gdfTemplate['CUT2008_3'] = ''
    gdfTemplate['insumos2008_1'] = ''
    gdfTemplate['insumos2008_2'] = ''
    gdfTemplate['insumos2008_3'] = ''
    gdfTemplate['Cambio0008_1'] = ''
    gdfTemplate['Cambio0008_2'] = ''
    gdfTemplate['Cambio0008_3'] = ''
    gdfTemplate['CUT2012_1'] = ''
    gdfTemplate['CUT2012_2'] = ''
    gdfTemplate['CUT2012_3'] = ''
    gdfTemplate['insumos2012_1'] = ''
    gdfTemplate['insumos2012_2'] = ''
    gdfTemplate['insumos2012_3'] = ''
    gdfTemplate['Cambio0812_1'] = ''
    gdfTemplate['Cambio0812_2'] = ''
    gdfTemplate['Cambio0812_3'] = ''
    gdfTemplate['CUT2013_1'] = ''
    gdfTemplate['CUT2013_2'] = ''
    gdfTemplate['CUT2013_3'] = ''
    gdfTemplate['insumos2013_1'] = ''
    gdfTemplate['insumos2013_2'] = ''
    gdfTemplate['insumos2013_3'] = ''
    gdfTemplate['Cambio1213_1'] = ''
    gdfTemplate['Cambio1213_2'] = ''
    gdfTemplate['Cambio1213_3'] = ''
    gdfTemplate['CUT2014_1'] = ''
    gdfTemplate['CUT2014_2'] = ''
    gdfTemplate['CUT2014_3'] = ''
    gdfTemplate['insumos2014_1'] = ''
    gdfTemplate['insumos2014_2'] = ''
    gdfTemplate['insumos2014_3'] = ''
    gdfTemplate['Cambio1314_1'] = ''
    gdfTemplate['Cambio1314_2'] = ''
    gdfTemplate['Cambio1314_3'] = ''
    gdfTemplate['CUT2015_1'] = ''
    gdfTemplate['CUT2015_2'] = ''
    gdfTemplate['CUT2015_3'] = ''
    gdfTemplate['insumos2015_1'] = ''
    gdfTemplate['insumos2015_2'] = ''
    gdfTemplate['insumos2015_3'] = ''
    gdfTemplate['Cambio1415_1'] = ''
    gdfTemplate['Cambio1415_2'] = ''
    gdfTemplate['Cambio1415_3'] = ''
    gdfTemplate['CUT2016_1'] = ''
    gdfTemplate['CUT2016_2'] = ''
    gdfTemplate['CUT2016_3'] = ''
    gdfTemplate['insumos2016_1'] = ''
    gdfTemplate['insumos2016_2'] = ''
    gdfTemplate['insumos2016_3'] = ''
    gdfTemplate['Cambio1516_1'] = ''
    gdfTemplate['Cambio1516_2'] = ''
    gdfTemplate['Cambio1516_3'] = ''
    gdfTemplate['CUT2017_1'] = ''
    gdfTemplate['CUT2017_2'] = ''
    gdfTemplate['CUT2017_3'] = ''
    gdfTemplate['insumos2017_1'] = ''
    gdfTemplate['insumos2017_2'] = ''
    gdfTemplate['insumos2017_3'] = ''
    gdfTemplate['Cambio1617_1'] = ''
    gdfTemplate['Cambio1617_2'] = ''
    gdfTemplate['Cambio1617_3'] = ''
    gdfTemplate['CUT2018_1'] = ''
    gdfTemplate['CUT2018_2'] = ''
    gdfTemplate['CUT2018_3'] = ''
    gdfTemplate['insumos2018_1'] = ''
    gdfTemplate['insumos2018_2'] = ''
    gdfTemplate['insumos2018_3'] = ''
    gdfTemplate['Cambio1718_1'] = ''
    gdfTemplate['Cambio1718_2'] = ''
    gdfTemplate['Cambio1718_3'] = ''
    gdfTemplate['CUT2019_1'] = ''
    gdfTemplate['CUT2019_2'] = ''
    gdfTemplate['CUT2019_3'] = ''
    gdfTemplate['insumos2019_1'] = ''
    gdfTemplate['insumos2019_2'] = ''
    gdfTemplate['insumos2019_3'] = ''
    gdfTemplate['Cambio1819_1'] = ''
    gdfTemplate['Cambio1819_2'] = ''
    gdfTemplate['Cambio1819_3'] = ''
    gdfTemplate['CUT2020_1'] = ''
    gdfTemplate['CUT2020_2'] = ''
    gdfTemplate['CUT2020_3'] = ''
    gdfTemplate['insumos2020_1'] = ''
    gdfTemplate['insumos2020_2'] = ''
    gdfTemplate['insumos2020_3'] = ''
    gdfTemplate['Cambio1920_1'] = ''
    gdfTemplate['Cambio1920_2'] = ''
    gdfTemplate['Cambio1920_3'] = ''
    gdfTemplate['CUT2021_1'] = ''
    gdfTemplate['CUT2021_2'] = ''
    gdfTemplate['CUT2021_3'] = ''
    gdfTemplate['insumos2021_1'] = ''
    gdfTemplate['insumos2021_2'] = ''
    gdfTemplate['insumos2021_3'] = ''
    gdfTemplate['Cambio2021_1'] = ''
    gdfTemplate['Cambio2021_2'] = ''
    gdfTemplate['Cambio2021_3'] = ''
    gdfTemplate['CUT2022_1'] = ''
    gdfTemplate['CUT2022_2'] = ''
    gdfTemplate['CUT2022_3'] = ''
    gdfTemplate['insumos2022_1'] = ''
    gdfTemplate['insumos2022_2'] = ''
    gdfTemplate['insumos2022_3'] = ''
    gdfTemplate['Cambio2122_1'] = ''
    gdfTemplate['Cambio2122_2'] = ''
    gdfTemplate['Cambio2122_3'] = ''
    gdfGeneral = gdfTemplate.copy()
    print('Ciclo: ', ciclo)
# %%
rutafileJ = os.path.join(rutadia, filenameJ)
fileJ=pd.read_csv(rutafileJ)
gdfJ = gpd.GeoDataFrame(fileJ, geometry=gpd.points_from_xy(fileJ.lon, fileJ.lat), crs="EPSG:4326")
gdfJ.drop_duplicates(subset=['geometry'], inplace=True)
print(gdfJ.columns)
print('Numero de parcelas en interpretes juniors: ', gdfJ.plotid.value_counts())
gdfJ.dropna(subset=['email'], inplace=True)
#print('Numero de parcelas avanzadas en interpretes juniors: ', gdfJ.plotid.value_counts())

# %%
# lectura de información de interpretes
listainterpretes = pd.read_excel('./Datos/20230719ListadodeTecnicosEspecialistas.xlsx')

# %%
# Lectura de datos de interpretaciones especialistas
gdfE.dropna(subset=['email'], inplace=True)
for index, row in gdfE.iterrows():
    correo = row['email']
    sampleid = row['sampleid']
    plotid = row['plotid']
    datosinterprete = listainterpretes.loc[listainterpretes["CORREO PERSONAL"]==correo]
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid']==sampleid), 'email1'] = correo
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid']==sampleid), 'collection_time1'] = row['collection_time']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'analysis_duration1'] = row['analysis_duration']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'imagery_title1'] = row['imagery_title']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2000_1'] = row['Uso y cobertura 2000']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2000_1'] = row['Insumos 2000']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2008_1'] = row['Uso y cobertura 2008']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2008_1'] = row['Insumos 2008']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio0008_1'] = row['Cambio 2000-2008']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2012_1'] = row['Uso y cobertura 2012']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2012_1'] = row['Insumos 2012']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio0812_1'] = row['Cambio 2008-2012']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2013_1'] = row['Uso y cobertura 2013']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2013_1'] = row['Insumos 2013']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1213_1'] = row['Cambio 2012-2013']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2014_1'] = row['Uso y cobertura 2014']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2014_1'] = row['Insumos 2014']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1314_1'] = row['Cambio 2013-2014']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2015_1'] = row['Uso y cobertura 2015']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2015_1'] = row['Insumos 2015']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1415_1'] = row['Cambio 2014-2015']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2016_1'] = row['Uso y cobertura 2016']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2016_1'] = row['Insumos 2016']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1516_1'] = row['Cambio 2015-2016']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2017_1'] = row['Uso y cobertura 2017']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2017_1'] = row['Insumos 2017']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1617_1'] = row['Cambio 2016-2017']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2018_1'] = row['Uso y cobertura 2018']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2018_1'] = row['Insumos 2018']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1718_1'] = row['Cambio 2017-2018']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2019_1'] = row['Uso y cobertura 2019']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2019_1'] = row['Insumos 2019']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1819_1'] = row['Cambio 2018-2019']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2020_1'] = row['Uso y cobertura 2020']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2020_1'] = row['Insumos 2020']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1920_1'] = row['Cambio 2019-2020']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2021_1'] = row['Uso y cobertura 2021']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2021_1'] = row['Insumos 2021']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio2021_1'] = row['Cambio 2020-2021']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2022_1'] = row['Uso y cobertura 2022']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2022_1'] = row['Insumos 2022']
    gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio2122_1'] = row['Cambio 2021-2022']


# %%
# Lectura de datos de interpretaciones Juniors

for index, row in gdfJ.iterrows():
    correo = row['email']
    sampleid = row['sampleid']
    plotid = row['plotid']
    datosinterprete = listainterpretes.loc[listainterpretes["CORREO PERSONAL"] == correo]
    rowtofill = gdfGeneral.index[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid)].tolist()
    #print(rowtofill[0])
    filaone = gdfGeneral.loc[gdfGeneral.index[rowtofill]]
    #print(filaone['email2'].to_string(index=False))
    #print(filaone['email2'])

    if filaone['email2'].isnull().any():
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'email2'] = correo
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'collection_time2'] = \
            row['collection_time']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'analysis_duration2'] = \
            row['analysis_duration']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'imagery_title2'] = row[
            'imagery_title']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2000_2'] = row[
            'Uso y cobertura 2000']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2000_2'] = row[
            'Insumos 2000']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2008_2'] = row[
            'Uso y cobertura 2008']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2008_2'] = row[
            'Insumos 2008']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio0008_2'] = row[
            'Cambio 2000-2008']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2012_2'] = row[
            'Uso y cobertura 2012']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2012_2'] = row[
            'Insumos 2012']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio0812_2'] = row[
            'Cambio 2008-2012']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2013_2'] = row[
            'Uso y cobertura 2013']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2013_2'] = row[
            'Insumos 2013']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1213_2'] = row[
            'Cambio 2012-2013']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2014_2'] = row[
            'Uso y cobertura 2014']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2014_2'] = row[
            'Insumos 2014']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1314_2'] = row[
            'Cambio 2013-2014']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2015_2'] = row[
            'Uso y cobertura 2015']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2015_2'] = row[
            'Insumos 2015']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1415_2'] = row[
            'Cambio 2014-2015']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2016_2'] = row[
            'Uso y cobertura 2016']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2016_2'] = row[
            'Insumos 2016']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1516_2'] = row[
            'Cambio 2015-2016']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2017_2'] = row[
            'Uso y cobertura 2017']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2017_2'] = row[
            'Insumos 2017']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1617_2'] = row[
            'Cambio 2016-2017']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2018_2'] = row[
            'Uso y cobertura 2018']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2018_2'] = row[
            'Insumos 2018']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1718_2'] = row[
            'Cambio 2017-2018']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2019_2'] = row[
            'Uso y cobertura 2019']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2019_2'] = row[
            'Insumos 2019']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1819_2'] = row[
            'Cambio 2018-2019']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2020_2'] = row[
            'Uso y cobertura 2020']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2020_2'] = row[
            'Insumos 2020']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1920_2'] = row[
            'Cambio 2019-2020']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2021_2'] = row[
            'Uso y cobertura 2021']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2021_2'] = row[
            'Insumos 2021']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio2021_2'] = row[
            'Cambio 2020-2021']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2022_2'] = row[
            'Uso y cobertura 2022']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2022_2'] = row[
            'Insumos 2022']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio2122_2'] = row[
            'Cambio 2021-2022']

    else:
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'email3'] = correo
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'collection_time3'] = \
            row['collection_time']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'analysis_duration3'] = \
            row['analysis_duration']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'imagery_title3'] = row[
            'imagery_title']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2000_3'] = row[
            'Uso y cobertura 2000']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2000_3'] = row[
            'Insumos 2000']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2008_3'] = row[
            'Uso y cobertura 2008']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2008_3'] = row[
            'Insumos 2008']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio0008_3'] = row[
            'Cambio 2000-2008']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2012_3'] = row[
            'Uso y cobertura 2012']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2012_3'] = row[
            'Insumos 2012']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio0812_3'] = row[
            'Cambio 2008-2012']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2013_3'] = row[
            'Uso y cobertura 2013']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2013_3'] = row[
            'Insumos 2013']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1213_3'] = row[
            'Cambio 2012-2013']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2014_3'] = row[
            'Uso y cobertura 2014']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2014_3'] = row[
            'Insumos 2014']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1314_3'] = row[
            'Cambio 2013-2014']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2015_3'] = row[
            'Uso y cobertura 2015']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2015_3'] = row[
            'Insumos 2015']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1415_3'] = row[
            'Cambio 2014-2015']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2016_3'] = row[
            'Uso y cobertura 2016']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2016_3'] = row[
            'Insumos 2016']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1516_3'] = row[
            'Cambio 2015-2016']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2017_3'] = row[
            'Uso y cobertura 2017']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2017_3'] = row[
            'Insumos 2017']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1617_3'] = row[
            'Cambio 2016-2017']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2018_3'] = row[
            'Uso y cobertura 2018']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2018_3'] = row[
            'Insumos 2018']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1718_3'] = row[
            'Cambio 2017-2018']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2019_3'] = row[
            'Uso y cobertura 2019']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2019_3'] = row[
            'Insumos 2019']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1819_3'] = row[
            'Cambio 2018-2019']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2020_3'] = row[
            'Uso y cobertura 2020']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2020_3'] = row[
            'Insumos 2020']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio1920_3'] = row[
            'Cambio 2019-2020']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2021_3'] = row[
            'Uso y cobertura 2021']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2021_3'] = row[
            'Insumos 2021']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio2021_3'] = row[
            'Cambio 2020-2021']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'CUT2022_3'] = row[
            'Uso y cobertura 2022']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'insumos2022_3'] = row[
            'Insumos 2022']
        gdfGeneral.loc[(gdfGeneral['plotid'] == plotid) & (gdfGeneral['sampleid'] == sampleid), 'Cambio2122_3'] = row[
            'Cambio 2021-2022']

# %%
print("Tercera interpretacion: ", gdfGeneral['email2'].value_counts())
# %%
# save as csv
gdfGeneral.to_csv("./Datos/ResultadosInterpretacion_BSVTBA_01082023.csv")
