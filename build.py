from sklearn import preprocessing as pp
import pandas as pd
import numpy as np

def csv_to_dataframe(filepath):
    try:
        dataframe = pd.read_csv(filepath)
    except IOError:
        raise 'File Path not found'
    return dataframe

def dtype_category(dataframe, column_list):
    try:
        for col in column_list:
            dataframe[col] = dataframe[col].astype('category')
    except KeyError:
        raise 'Column does not exist'
    return dataframe

def centre_and_scale(dataframe, column_list):
    try:
        for col in column_list:
            dataframe[col] = pp.scale(dataframe[col], copy=False)
    except KeyError:
        raise 'Column does not exist'
    return dataframe

def label_encoder(dataframe, column_list):
    try:
        for col in column_list[0:4:2]:
            le = pp.LabelEncoder()
            dataframe[col] = le.fit_transform(dataframe[col])
        #     df[col].apply(le.fit_transform)
    except KeyError:
        raise 'Column does not exist or column in not categorical'
    return dataframe

def one_hot_encoder(dataframe, column_list):
    try:
        return pd.get_dummies(dataframe, columns = column_list)
    except KeyError:
        raise 'Column does not exist or column in not categorical'

def skewness(dataframe, column_list):
    try:
        list_of_skew = []
        for col in column_list:
            skew_data = dataframe[col].skew()
            list_of_skew.append(skew_data)
    except KeyError:
        raise 'Column does not exist or column in not categorical'
    return list_of_skew

def sqrt_transform(dataframe, column_list):
    try:
        list_of_sqrt = []
        for col in column_list:
            sqrt_num = np.sqrt(dataframe[col])
            list_of_sqrt.append(sqrt_num)
    except KeyError:
        raise 'Column does not exist or column in not categorical'
    return list_of_sqrt

def plots(dataframe, column_list):
    pass
