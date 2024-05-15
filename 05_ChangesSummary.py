# %%
# imports
import pandas as pd
import os
import numpy as np

# %%
main_file = pd.read_csv("./MAATE2023/Resultados2/10_NBE/ResultadosCambios_NBE_11042024.csv")
output = './MAATE2023/Resultados2/10_NBE/'
total_rows = len(main_file)


# %%
# analisis for 2000-2008

change = 'change2122.csv'
target = 'Cambio2122'
target2 = 'Coincidencia2122'
change_classes_2008 = main_file[[target, target2]].value_counts()
file = os.path.join(output, change)
change_classes_2008.to_csv(file)
clases = pd.read_csv(file)
resumen = clases.groupby([target], as_index=False).sum()

PERcheck = resumen[resumen[target].str.contains('Perturbación')]
NBEcheck = resumen[resumen[target].str.contains('No Bosque Estable')]
BEcheck = resumen[resumen[target].str.contains('Bosque Estable')]
DEFcheck = resumen[resumen[target].str.contains('Deforestación')]
SINcheck = resumen[resumen[target].str.contains('Sin Información')]

if NBEcheck.empty:
    NBE = 0
else:
    NBE = resumen.loc[resumen[target]=='No Bosque Estable', 'count'].values[0]

if BEcheck.empty:
    BE = 0
else:
    BE = resumen.loc[resumen[target]=='Bosque Estable', 'count'].values[0]

if DEFcheck.empty:
    DEF = 0
else:
    DEF = resumen.loc[resumen[target]=='Deforestación', 'count'].values[0]

if SINcheck.empty:
    SIN = 0
else:
    SIN = resumen.loc[resumen[target]=='Sin Información', 'count'].values[0]

if PERcheck.empty:
    PER = 0
else:
    PER = resumen.loc[resumen[target]=='Perturbación', 'count'].values[0]

filterNBE = clases.loc[(clases[target] == 'No Bosque Estable') & (clases[target2] == 'E'), 'count'].values[0]
NBE_3C = (filterNBE/NBE)*100
NBE_2C = 100-NBE_3C

filterBE = clases.loc[(clases[target] == 'Bosque Estable') & (clases[target2] == 'E'), 'count'].values[0]
BE_3C = (filterBE/BE)*100
BE_2C = 100-BE_3C

if DEF != 0:
    if clases.loc[(clases[target] == 'Deforestación') & (clases[target2] == 'E'), 'count'].empty:
        DEF_3C = 0
        DEF_2C = 100

    else:
        filterDEF = clases.loc[(clases[target] == 'Deforestación') & (clases[target2] == 'E'), 'count'].values[0]
        DEF_3C = (filterDEF/DEF)*100
        DEF_2C = 100-DEF_3C
else:
    DEF_3C = 0
    DEF_2C = 0

if SIN != 0:

    if clases.loc[(clases[target] == 'Sin Información') & (clases[target2] == 'E'), 'count'].empty:
        SIN_3C = 0
        SIN_2C = 100
    else:
        filterSIN = clases.loc[(clases[target] == 'Sin Información') & (clases[target2] == 'E'), 'count'].values[0]
        SIN_3C = (filterSIN/SIN)*100
        SIN_2C = 100-SIN_3C
else:
    SIN_3C = 0
    SIN_2C = 0

if PER != 0:
    if clases.loc[(clases[target] == 'Perturbación') & (clases[target2] == 'E'), 'count'].empty:
        PER_3C = 0
        PER_2C = 100
    else:
        filterPER = clases.loc[(clases[target] == 'Perturbación') & (clases[target2] == 'E'), 'count'].values[0]
        PER_3C = (filterPER/PER)*100
        PER_2C = 100-PER_3C
else:
    PER_3C = 0
    PER_2C = 0

porcentaTotal3C =(NBE_3C*NBE+BE_3C*BE+DEF_3C*DEF+PER_3C*PER+SIN_3C*SIN)/total_rows
porcentaTotal2C =(NBE_2C*NBE+BE_2C*BE+DEF_2C*DEF+PER_2C*PER+SIN_2C*SIN)/total_rows
# %%
print('Cambio:',target)
print('Total BE',BE)
print('BE_3C', BE_3C)
print('BE_2C', BE_2C)
print('Total NBE',NBE)
print('NBE_3C', NBE_3C)
print('NBE_2C', NBE_2C)
print('Total PER',PER)
print('PER_3C', PER_3C)
print('PER_2C', PER_2C)
print('Total DEF',DEF)
print('DEF_3C', DEF_3C)
print('DEF_2C', DEF_2C)
print('Total SIN',SIN)
print('SIN_3C', SIN_3C)
print('SIN_2C', SIN_2C)
print('Total Muestras', total_rows)
print('Porcentaje 3C', porcentaTotal3C)
print('Porcentaje 2C', porcentaTotal2C)