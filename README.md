# Conversion Rate Dataset

We have data about users who hit our site: whether they converted or not as well as some of their characteristics such as their country, the marketing channel, their age, whether they are repeat users and the number of pages visited during that session (as a proxy for site activity/time spent on site).

**Goal:**
* Predict conversion rate
* Come up with recommendations for the product team and the marketing team to improve conversion rate


**Data:** Present under data/conversion_data.csv

**Table: "conversion_data" - information about signed-in users during one session. Each row is a user session.**

* country : user country based on the IP address
* age : user age. Self-reported at sign-in step
* new_user : whether the user created the account during this session or had already an account and simply came back to the site
* source : marketing channel source
    * Ads: came to the site by clicking on an advertisement
    * Seo: came to the site by clicking on search results
    * Direct: came to the site by directly typing the URL on the browser
* total_pages_visited: number of total pages visited during the session.
    * This is a proxy for time spent on site and engagement during the session.
* converted: this is our label. 1 means they converted within the session, 0 means they left without buying anything.
    * The company goal is to increase conversion rate: # conversions / total sessions.


### Question 1

#### Write a funtion to convert given CSV file to Dataframe

* Define function with name `csv_to_dataframe` which should accept `filepath` as a parameter.
* Function should return a dataframe.
* As we require a dataframe, type of return variable should be pandas dataframe.
* In case if we pass `filepath` which does not exist, function should raise FileNotFoundError.

### Question 2

#### Write a function to convert datatype of given variables to "category"

* Define function with name `dtype_category` which should accept `dataframe` and `list of columns` as parameters.
* Function should return a dataframe with type of given columns changed to "category".
* As we require a dataframe, type of return variable should be `pandas dataframe`.
* In case if we pass column name which does not exist, function should raise KeyError

### Question 3

#### Write a function to to center and scale numerical variables.

* Define function with name `centre_and_scale` which should accept `dataframe` and `column_list` as parameters.
* Function should return a dataframe given columns of numerical variables being centred and scaled.
* As we require a dataframe, type of return variable should be `pandas dataframe`.
* In case if we pass column name which does not exist, function should raise KeyError

### Question 4

#### Write a function to encode all nominal categorical variables using label encoding

* Define function with name `label_encoder` which should accept `dataframe`, `column_list` (of variables to be encoded) as parameters.
* Function should return dataframe with encoded variables.
* As we require dataframe, type of return variable should be pandas dataframe.
* In case if we pass column name which does not exist or is not categorical type, function should raise KeyError

### Question 5

#### Write a function to encode nominal categorical variables using one hot encoding

* Define function with name `one_hot_encoder` which should accept `dataframe`, `column_list` (of variables to be encoded) as parameters.
* Function should return dataframe with encoded variables.
* As we require dataframe, type of return variable should be pandas dataframe.
* In case if we pass column name which does not exist or is not categorical type, function should raise KeyError

### Question 6

#### Write a function to return skewness of numerical variables:

* Define function with name `skewness` which should accept `dataframe`, `column_list` (of variables whose skewness is to be determined) as parameters.
* Function should return list of skewness of given columns
* As we require list of values, type of return variable should be list
* In case if we pass column name which does not exist or is categorical type, function should raise KeyError

### Question 7

#### Write a function to return sqrt transform of numerical variables

* Define function with name `sqrt_transform` which should accept `dataframe`, `column_list` (of variables which are to be sqrt transformed) as parameters.
* Function should return dataframe of sqrt transformed columns of given columns
* As we require list of values, type of return variable should be list
* In case if we pass column name which does not exist or is categorical type, function should raise KeyError

### Question 8

#### Write a function to plot  histogram and box plot of transformed  vs original numerical variables:

* Define function with name `plots` which should accept `dataframe`, `column_list` (of variables to be plotted) as parameters.
* Function should return subplots of histogram and boxplots for the numeric variables.
* As we require plot, type of return variable should be matplotlib object.
* In case if we pass column name which does not exist, function should raise KeyError