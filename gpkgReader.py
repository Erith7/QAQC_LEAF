# %%
import pandas as pd
import geopandas as gpd

# %%

gdf = gpd.read_file('./Datos/eSBAE/samplesChiapas2182.shp')
print(gdf.head())
print(gdf.columns)

# %%
gdf['lon'] = gdf['geometry'].x
gdf['lat'] = gdf['geometry'].y
# %%
print(gdf.columns)
gdf.rename(columns = {'ccdc_chang': 'ccdc_change', 'ccdc_magni': 'ccdc_magnitude', 'dw_class_m': 'dw_class_mode', 'dw_tree_pr': 'dw_tree_prob__max', 'dw_tree__1': 'dw_tree_prob__min', 'dw_tree__2': 'dw_tree_prob__stdDev', 'dw_tree__3': 'dw_tree_prob_mean', 'bfast_chan': 'bfast_change', 'bfast_magn': 'bfast_magnitude', 'bfast_mean': 'bfast_means', 'cusum_chan': 'cusum_change', 'cusum_conf': 'cusum_confidence', 'cusum_magn': 'cusum_magnitude', 'bs_slope_m': 'bs_slope_max', 'bs_slope_s': 'bs_slope_sd', 'bs_slope_1': 'bs_slope_min', 'bs_slope_2': 'bs_slope_mean', 'potapov_tr': 'potapov_tree_height'}, inplace = True)
print(gdf.columns)

# %%
#df.to_file('./Datos/eSBAE/sampleChiapas.shp', driver='ESRI Shapefile')
gdf.to_csv('./Datos/eSBAE/sampleChiapas.csv', encoding='utf-8')