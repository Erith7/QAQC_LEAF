# %%
# Imports
import pandas as pd
import os
from functions import oa_estimator_inter1
from functions import oa_estimator_inter2
from functions import oa_estimator_inter3

#%%
# path and variables definition
email1= 'email1'
email2= 'email2'
email3= 'email3'
ruta_folder = './MAATE2023/Resultados2/10_NBE/OverallAgreement/'
estrato = '10_NBE'
folder1 = email1
folder2 = email2
folder3 = email3
input1 = os.path.join(ruta_folder, folder1)
input2 = os.path.join(ruta_folder, folder2)
input3 = os.path.join(ruta_folder, folder3)

# %%
# Reading of data for interpreter1
file1_TR = 'resultadosALLYEARS_tecnico1.csv'
allpath1 = os.path.join(input1, file1_TR)
file1 = pd.read_csv(allpath1)
file1['total']=file1.iloc[:,4:14].sum(axis=1)
interpretes1 = pd.DataFrame()
interpretes1['email'] = ''
interpretes1['OA'] = ''
resultado1 = oa_estimator_inter1(file1, interpretes1)
resultado1['Rol']='E'
print(resultado1)

# %%
# Reading of data for interpreter2
file2_TR = 'resultadosALLYEARS_tecnico2.csv'
allpath2 = os.path.join(input2, file2_TR)
file2 = pd.read_csv(allpath2)
file2['total']=file2.iloc[:,4:14].sum(axis=1)
interpretes2 = pd.DataFrame()
interpretes2['email'] = ''
interpretes2['OA'] = ''
resultado2 = oa_estimator_inter2(file2, interpretes2)
resultado2['Rol']='J'
print(resultado2)

# %%
# Reading of data for interpreter3
file3_TR = 'resultadosALLYEARS_tecnico3.csv'
allpath3 = os.path.join(input3, file3_TR)
file3 = pd.read_csv(allpath3)
file3['total']=file3.iloc[:,4:14].sum(axis=1)
interpretes3 = pd.DataFrame()
interpretes3['email'] = ''
interpretes3['OA'] = ''
resultado3 = oa_estimator_inter3(file3, interpretes3)
resultado3['Rol']='J'
print(resultado3)
#%%
# Merging dataframes and exporting CSV
mer1 = pd.concat([resultado1, resultado2], axis=0)
mer2 = pd.concat([mer1, resultado3], axis=0)
mer2_sorted = mer2.sort_values(by=['OA'], ascending=False).reset_index(drop=True)
merged = mer2_sorted.groupby(['email', 'Rol'])['OA'].mean()

#%%
name = estrato+'.csv'
output = os.path.join(ruta_folder, name)
merged.to_csv(output)
merged2 = pd.read_csv(output)
merged3 = merged2[['email', 'OA', 'Rol']]
merged_sorted = merged3.sort_values(by=['OA'], ascending=False).reset_index(drop=True)
merged_sorted.to_csv(output)