# %%
import pandas as pd
import geopandas as gpd
import os

# %% reading csv with clusters
globalpath1 = '/Users/erith/Dropbox/Comun/FAO_LAC/2023/Nicaragua/eSBAE/example1'
file1 = 'samples_BSVAPM_C3.csv'
path1 = os.path.join(globalpath1, file1)
data1 = pd.read_csv(path1, sep=';')
print("Data 1 ", data1.head())

# reading gpkg
globalpath2 = '/Users/erith/Dropbox/Comun/FAO_LAC/2023/Nicaragua/eSBAE/example1'
file1 = 'samples_BSVAPM_C3.csv'
path1 = os.path.join(globalpath1, file1)
data1 = pd.read_csv(path1, sep=';')
print("Data 1 ", data1.head())

