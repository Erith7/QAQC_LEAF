import pandas as pd
import numpy as np

def annual_data_extraction(dataframe, email, coincidence):
    extraction = dataframe.groupby(email)[coincidence].value_counts()
    extraction = extraction.to_frame()
    extraction = extraction.sort_values([email, coincidence])
    return extraction


def set_order(dataframe, coincidence):
    #dataframe2['temporal'] = ''
    print(dataframe.shape)
    dataframe.loc[(dataframe[coincidence] == 'B'), coincidence] = 1
    dataframe.loc[(dataframe[coincidence] == 'C'), coincidence] = 2
    dataframe.loc[(dataframe[coincidence] == 'D'), coincidence] = 3
    dataframe.loc[(dataframe[coincidence] == 'E'), coincidence] = 4
    dataframe.loc[(dataframe[coincidence] == 'F'), coincidence] = 5
    #dataframe2 = dataframe2.drop([coincidence], axis=1)
    #dataframe2 = dataframe2.rename(columns={"temporal": coincidence})
    print(dataframe.shape)
    dataframe = dataframe.groupby(dataframe[coincidence].diff().lt(1)
    .cumsum()).apply(lambda x: x.set_index(coincidence)
    .reindex(range(1, 6))).reset_index(level=0, drop=True).reset_index()
    return dataframe


def nan_filler(dataframe, email, coincidence, count):
    dataframe.loc[(dataframe[email].isna()) & (dataframe[coincidence] > 1), email] = dataframe[email].shift(+1)
    dataframe.loc[(dataframe[email].isna()) & (dataframe[coincidence] == 1), email] = dataframe[email].shift(-1)
    dataframe.loc[(dataframe[count].isna()), count] = 0
    dataframe.loc[(dataframe[coincidence] == 1), coincidence] = 'B'
    dataframe.loc[(dataframe[coincidence] == 2), coincidence] = 'C'
    dataframe.loc[(dataframe[coincidence] == 3), coincidence] = 'D'
    dataframe.loc[(dataframe[coincidence] == 4), coincidence] = 'E'
    dataframe.loc[(dataframe[coincidence] == 5), coincidence] = 'F'
    dataframe = dataframe[[email, coincidence, count]]
    return dataframe
