from sklearn import preprocessing
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

def csv_to_dataframe(filepath):
    try:
        df = pd.read_csv(filepath)

    except:
        raise IOError('Please provide valid file path')
# df=csv_to_dataframe('/home/nikita/conversion_data.csv')
    return df
def dtype_category(df, list_col):
    try:
        for col in list_col:
            df[col]=df[col].astype("category")
        return df
    except:
        raise KeyError('enter valid column_name')

def centre_and_scale(df,column_list):
    try:
        for col in column_list:
            df[col]=preprocessing.scale(df[col])
        return df
    except:
        raise KeyError('enter valid column_name')

def label_encoder(df, column_list):
    for column in column_list:
        if column not in df.columns:
            raise KeyError
    le = preprocessing.LabelEncoder()
    return df[column_list].apply(le.fit_transform)



def one_hot_encoder(df,column_list):
    try:
        return pd.get_dummies(df, columns = column_list)
    except:
        raise KeyError('enter valid column_name')


def skewness(df,column_list):
    try:
        lst1=[]
        for col in column_list:
            df[col]= df[col].astype("int64")
            lst1.append(df.skew())

    except:
        raise KeyError('enter valid column_name')
    return lst1

def sqrt_transform(dataframe, column_list):
    sqrt_data = []
    for column in column_list:
        if column not in dataframe.columns:
            raise KeyError
    for column in column_list:
         sqrt_data.append(np.sqrt(dataframe[column]))
    return sqrt_data


def plots(df,column_list):
    try:
        for col in column_list:
            var_trans = preprocessing.scale(np.sqrt(df[col]))
            var_Orig = preprocessing.scale(df[col])

            figure = plt.figure(figsize=(12,12))

            figure.add_subplot(221)
            plt.hist(var_trans,facecolor='red',alpha=0.75)
            plt.title("Transformed variable Histogram (sqrt transform)")


            figure.add_subplot(222)
            plt.hist(var_Orig,facecolor='blue',alpha=0.75)
            plt.title("Original variable Histogram - Right Skewed")


            figure.add_subplot(223)
            plt.boxplot(var_Orig)
            plt.title("Transformed variable Distribution")

            figure.add_subplot(224)
            plt.boxplot(var_trans)
            plt.title("Transformed variable Distribution")
    except:
        raise KeyError('enter valid column_name')
