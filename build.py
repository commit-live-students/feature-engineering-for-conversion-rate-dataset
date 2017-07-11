import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.preprocessing as pre
import math



def csv_to_dataframe(pth):
    try:
        df = pd.read_csv(pth)
        #print df.head(10)
        return df
    except IOError:
        print "Supposed to raise a FileNotFoundError"


def dtype_category(df,ls):
    for col in ls:
        if col not in set(df.columns.values):
            raise KeyError
        df[col] = df[col].astype('category')
    return df


def centre_and_scale(df,ls):
    for col in ls:
        if col not in set(df.columns.values):
            raise KeyError
        df[col] = pre.scale(df[col])
    #print df.head(10)
    return df


def skewness(df,ls):
    ret_ls = []
    for col in ls:
        if col not in set(df.columns.values):
            raise KeyError
        #print("Skew for column:{} is {}".format(col,df[col].skew()))
        ret_ls.append(df[col].skew())
    return ret_ls


def sqrt_transform(df,ls):
    ret_ls = []
    cols_ls = []
    for col in ls:
        col_sqrt = col+'_sqrt'
        if col not in set(df.columns.values):
            raise KeyError
        df[col_sqrt] = df[col].apply(math.sqrt)
        cols_ls.append(df[col_sqrt].tolist())
    return cols_ls



def label_encoder(df,ls):
    le = pre.LabelEncoder()
    for col in ls:
        if col not in set(df.columns.values):
            raise KeyError
        le.fit(df[col])
        df[col] = le.transform(df[col])
    return df


def one_hot_encoder(df,ls):
    ohe = pre.OneHotEncoder()
    for col in ls:
        if col not in set(df.columns.values):
            raise KeyError
        df = pd.concat([df,pd.get_dummies(df[col])],axis=1)
        #df[col] = ohe.transform(df[col])
    return df


def plots(dataframe, column_list):
    pass
