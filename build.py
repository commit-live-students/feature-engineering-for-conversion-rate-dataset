import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
#df=pd.read_csv(filepath)
def csv_to_dataframe(filepath):
    try:
        df=pd.read_csv(filepath)
        return df
    except:
        print("exception occured")


def dtype_category(dataframe, column_list):
    try:
        for col in column_list:
            dataframe[col]=dataframe[col].astype("category")
        return dataframe
    except KeyError:
        print("exception occured")
        raise



def centre_and_scale(dataframe,column_list):
    try:
        for col in column_list:
            dataframe[col]= preprocessing.scale(dataframe[col])
        return dataframe
    except KeyError:
        print("exception occured")
        raise



def label_encoder(dataframe,column_list):
    try:
        for col in column_list:
            lb_make = LabelEncoder()
            dataframe[col] = lb_make.fit_transform(dataframe[col])
        return dataframe
    except KeyError:
        print("exception occured")



def one_hot_encoder(dataframe, column_list):
    return pd.get_dummies(dataframe, columns = column_list)

def skewness(dataframe,column_list):
    try:
        for col in column_list:
            list1=[]
            dataframe[col] = dataframe[col].astype("int64")
        list1.append(dataframe.skew())
        return list1
    except KeyError:
        print("exception occured")



def sqrt_transform(dataframe, column_list):
    sqrt_data = []
    for column in column_list:
        if column not in dataframe.columns:
            raise KeyError
    for column in column_list:
         sqrt_data.append(np.sqrt(dataframe[column]))
    return sqrt_data




def plots(dataframe,list_of_columns):
    for col in list_of_columns:
        Transformed = preprocessing.scale(np.sqrt(dataframe[col]))
        Original = dataframe[col]

        #We draw the histograms
        figure = plt.figure(figsize=(12,12))

        figure.add_subplot(221)
        plt.hist(Transformed,facecolor='red',alpha=0.75)
        plt.title("Transformed "+col+" Histogram (sqrt transform)")

        figure.add_subplot(222)
        plt.hist(Original,facecolor='blue',alpha=0.75)
        plt.title("Original "+col+" Histogram - Right Skewed")

        figure.add_subplot(223)
        plt.boxplot(Transformed)
        plt.title("Transformed "+col+" Distribution")

        figure.add_subplot(224)
        plt.boxplot(Original)
        plt.title("The "+col+" Original Distribution")

        plt.show()
