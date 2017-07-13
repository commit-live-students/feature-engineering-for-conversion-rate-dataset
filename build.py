from sklearn import preprocessing
import pandas as pd
import numpy as np


def csv_to_dataframe(filepath):
    try:
        df = pd.read_csv(filepath)
    except IOError:
        raise 'File Path not found'
    return df


def dtype_category(dataframe, column_list):

    try:
        for col in column_list:
            dataframe[col] = dataframe[col].astype('category')
    except keyerror:
        raise 'Column does not exist'

    return dataframe


def centre_and_scale(dataframe, column_list):
    try:
        for col in column_list:
            dataframe[col] = preprocessing.scale(dataframe[col])
    except KeyError:
        raise 'Column does not exist'
    return dataframe


def label_encoder(dataframe, column_list):
    try:
        for cols in column_list:
            le_make = preprocessing.LabelEncoder()
            dataframe[cols] = le_make.fit_transform(dataframe[cols])
    except KeyError:
        raise 'Column does not exist or column in not categorical'
    return dataframe


def one_hot_encoder(dataframe, column_list):
    try:
        return pd.get_dummies(dataframe, columns = column_list)
    except KeyError:
        raise 'Column does not exist or column in not categorical'

def skewness(dataframe, column_list):
    ls_skew = []

    try:
        for col in column_list:
            skew_data = dataframe[col].skew()
            ls_skew.append(skew_data)
    except KeyError:
        raise 'Column does not exist or column in not categorical'

    return ls_skew


def sqrt_transform(dataframe, column_list):
    ls_sqrt = []

    try:
        for col in column_list:
            sqrt_data = np.sqrt(dataframe[col])
            ls_sqrt.append(sqrt_data)
    except KeyError:
        raise 'Column does not exist or column in not categorical'

    return ls_sqrt

def plots(dataframe, column_list):
    try:
        original_sub = dataframe.loc[:,column_list]
        df = centre_and_scale(dataframe,column_list)
        df_sub = df.loc[:,column_list]
        sub_cols = list(df_sub.columns)
        cols = list(original_sub.columns)
        col_length = len(sub_cols)
        for i in range(0,col_length):
            figure = plt.figure(figsize=(30,10))

            plt.subplot(221)
            plt.boxplot(original_sub.iloc[:,i],0,'rs',0)
            plt.title("Original " + cols[i])
            plt.xlabel("Value")
            plt.ylabel(cols[i])

            plt.subplot(222)
            plt.boxplot(df_sub.iloc[:,i], 0, 'rs', 0)
            plt.title("Transformed "+sub_cols[i])
            plt.xlabel("Value")
            plt.ylabel(sub_cols[i])

            plt.subplot(223)
            plt.hist(original_sub.iloc[:,i], bins=10)
            plt.title("Original "+cols[i])
            plt.xlabel("Value")
            plt.ylabel(cols[i])
            plt.show()

            plt.subplot(224)
            plt.hist(df_sub.iloc[:,i], bins=10)
            plt.title("Transformed "+sub_cols[i])
            plt.xlabel("Value")
            plt.ylabel(sub_cols[i])
            plt.show()

    except KeyError:
        raise 'Column does not exist or column in not categorical'
