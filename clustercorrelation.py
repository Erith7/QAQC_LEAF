# %%
import pandas as pd

#%%
# Data reading
file = pd.read_csv("./Datos/Ecuador/BSVTBA/ResultadosCambios_BSVTBA_02102023.csv")
#%%
print(file['Cambio2122'].unique())
file['Cambio']=''
file.loc[(file['Cambio2122'] == 'No Bosque Estable'), 'Cambio'] = 1
file.loc[(file['Cambio2122'] == 'Bosque Estable'), 'Cambio'] = 2
file.loc[(file['Cambio2122'] == 'Perturbación'), 'Cambio'] = 3
file.loc[(file['Cambio2122'] == 'Deforestación'), 'Cambio'] = 4

#%%
confusion_matrix = pd.crosstab(file['pl_cluster'], file['Cambio'], rownames=['clusters'], colnames=['cambios'])
print (confusion_matrix)