from sklearn import preprocessing as pp
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
'''
WRITE A FUNTION TO CONVERT GIVEN CSV FILE TO DATAFRAME
Define function with name csv_to_dataframe which should accept filepath as a parameter.
Function should return a dataframe.
As we require a dataframe, type of return variable should be pandas dataframe.
In case if we pass filepath which does not exist, function should raise FileNotFoundError.
'''
def csv_to_dataframe(filepath):
    try:
        df = pd.read_csv(filepath)
    except IOError:
        raise 'File Path not found'
    return df

'''
WRITE A FUNCTION TO CONVERT DATATYPE OF GIVEN VARIABLES TO "CATEGORY"
Define function with name dtype_category which should accept dataframe and list of columns as parameters.
Function should return a dataframe with type of given columns changed to "category".
As we require a dataframe, type of return variable should be pandas dataframe.
In case if we pass column name which does not exist, function should raise KeyError
'''
def dtype_category(dataframe, column_list):
    try:
        for cols in column_list:
            dataframe[cols] = dataframe[cols].astype('category')
    except KeyError:
        raise 'Column does not exist'
    return dataframe

'''
WRITE A FUNCTION TO TO CENTER AND SCALE NUMERICAL VARIABLES.
Define function with name centre_and_scale which should accept dataframe and column_list as parameters.
Function should return a dataframe given columns of numerical variables being centred and scaled.
As we require a dataframe, type of return variable should be pandas dataframe.
In case if we pass column name which does not exist, function should raise KeyError
'''
def centre_and_scale(dataframe, column_list):
    try:
        for cols in column_list:
            dataframe[cols] = pp.scale(dataframe[cols], copy=False)
    except KeyError:
        raise 'Column does not exist'
    return dataframe

'''
WRITE A FUNCTION TO ENCODE ALL NOMINAL CATEGORICAL VARIABLES USING LABEL ENCODING
Define function with name label_encoder which should accept dataframe, column_list (of variables to be encoded) as parameters.
Function should return dataframe with encoded variables.
As we require dataframe, type of return variable should be pandas dataframe.
In case if we pass column name which does not exist or is not categorical type, function should raise KeyError
'''
def label_encoder(dataframe, column_list):
    try:
        for cols in column_list:
            le = pp.LabelEncoder()
            dataframe[cols] = le.fit_transform(dataframe[cols])
    except KeyError:
        raise 'Column does not exist or column in not categorical'
    return dataframe

'''
WRITE A FUNCTION TO ENCODE NOMINAL CATEGORICAL VARIABLES USING ONE HOT ENCODING
Define function with name one_hot_encoder which should accept dataframe, column_list (of variables to be encoded) as parameters.
Function should return dataframe with encoded variables.
As we require dataframe, type of return variable should be pandas dataframe.
In case if we pass column name which does not exist or is not categorical type, function should raise KeyError
'''
def one_hot_encoder(dataframe, column_list):
    try:
        return pd.get_dummies(dataframe, columns = column_list)
    except KeyError:
        raise 'Column does not exist or column in not categorical'

'''
Define function with name skewness which should accept dataframe, column_list (of variables whose skewness is to be determined) as parameters.
Function should return list of skewness of given columns
As we require list of values, type of return variable should be list
In case if we pass column name which does not exist or is categorical type, function should raise KeyError
'''
def skewness(dataframe, column_list):
    try:
        list_of_skew = []
        for cols in column_list:
            skew_data = dataframe[cols].skew()
            list_of_skew.append(skew_data)
    except KeyError:
            raise 'Column does not exist or column in not categorical'
    return list_of_skew

'''
Define function with name sqrt_transform which should accept dataframe, column_list (of variables which are to be sqrt transformed) as parameters.
Function should return dataframe of sqrt transformed columns of given columns
As we require list of values, type of return variable should be list
In case if we pass column name which does not exist or is categorical type, function should raise KeyError
'''

def sqrt_transform(dataframe, column_list):
    list_of_sqrt = []
    try:
        for cols in column_list:
            sqrt_num = np.sqrt(dataframe[cols])
            list_of_sqrt.append(sqrt_num)
    except KeyError:
        raise 'Column does not exist or column in not categorical'
    return list_of_sqrt
'''
WRITE A FUNCTION TO PLOT HISTOGRAM AND BOX PLOT OF TRANSFORMED VS ORIGINAL NUMERICAL VARIABLES:
Define function with name plots which should accept dataframe, column_list (of variables to be plotted) as parameters.
Function should return subplots of histogram and boxplots for the numeric variables.
As we require plot, type of return variable should be matplotlib object.
In case if we pass column name which does not exist, function should raise KeyError
'''
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
