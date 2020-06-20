# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 22:46:44 2018
learnpython2org.py
@author: santi
"""
# NUMPY ARRAYS
# Numpy arrays are great alternatives to Python Lists. Some of the key advantages 
# of Numpy arrays are that they are fast, easy to work with, and give users the 
# opportunity to perform calculations across entire arrays.

# In the following example, you will first create two Python lists. Then, you 
# will import the numpy package and create numpy arrays out of the newly 
# created lists.
#%%
# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

# Print out the type of np_height
print(type(np_height))

# Element-wise calculations
# Now we can perform element-wise calculations on height and weight. For example, 
# you could take all 6 of the height and weight observations above, and calculate 
# the BMI for each observation with a single equation. These operations are very
# fast and computationally efficient. They are particularly helpful when you 
# have 1000s of observations in your data.

# Calculate bmi
bmi = np_weight / np_height ** 2
print(type(bmi))
# Print the result
print(bmi)

# Subsetting
# Another great feature of Numpy arrays is the ability to subset. For instance, 
# if you wanted to know which observations in our BMI array are above 23, we 
# could quickly subset it to find out.

# For a boolean response
bmi > 23

# Print only those observations above 23
bmi[bmi > 23]
#%%
# Exercise
# First, convert the list of weights from a list to a Numpy array. Then, 
# convert all of the weights from kilograms to pounds. Use the scalar conversion 
# of 2.2 lbs per kilogram to make your conversion. Lastly, print the 
# resulting array of weights in pounds.

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)
print(np_weight_kg)
# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2

# Print out np_weight_lbs
print(np_weight_lbs)

#%%

# PANDAS BASICS

# Pandas DataFrames
# Pandas is a high-level data manipulation tool developed by Wes McKinney. 
# It is built on the Numpy package and its key data structure is called the 
# DataFrame. DataFrames allow you to store and manipulate tabular data in 
# rows of observations and columns of variables.

# There are several ways to create a DataFrame. One way way is to use a 
# dictionary. For example:

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

# As you can see with the new brics DataFrame, Pandas has assigned a key 
# for each country as the numerical values 0 through 4. If you would like to 
# have different index values, say, the two letter country code, you can do 
# that easily as well.

# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)

#%%
# Another way to create a DataFrame is by importing a csv file using Pandas. 
# Now, the csv cars.csv is stored and can be imported using pd.read_csv:

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)
#%%

# Indexing DataFrames
# There are several ways to index a Pandas DataFrame. One of the easiest ways
# to do this is by using square bracket notation.

# In the example below, you can use square brackets to select one column of 
# the cars DataFrame. You can either use a single bracket or a double bracket. 
# The single bracket with output a Pandas Series, while a double bracket will 
# output a Pandas DataFrame.

# Import pandas and cars.csv
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['cars_per_cap'])

# Print out country column as Pandas DataFrame
print(cars[['cars_per_cap']])

# Print out DataFrame with country and drives_right columns
print(cars[['cars_per_cap', 'country']])

#%%
##################################
print("\n# 7 - Dictionary to DataFrame (1):")
# https://repl.it/@andris1990/DataCamp-Intermediate-2-Dictionaries-and-Pandas
##################################
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {
    "country":names,
    "drives_right":dr,
    "cars_per_cap":cpc
}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)
# Print out first 3 observations
#print(cars[0:3])
# Print out fourth, fifth and sixth observation
#print(cars[3:6])
# Print out country column as Pandas Series
print(cars['country'])
# Print out country column as Pandas DataFrame
print(cars[['country']])
# Print out DataFrame with country and drives_right columns
print(cars[['country','drives_right']])

#Square brackets can also be used to access observations (rows) from a 
#DataFrame. For example:
# Print out first 3 observations
print(cars[0:3])
# Print out fourth, fifth and sixth observation
print(cars[3:6])

# You can also use loc and iloc to perform just about any data selection 
# operation. loc is label-based, which means that you have to specify rows 
# and columns based on their row and column labels. iloc is integer index 
# based, so you have to specify rows and columns by their integer index like 
# you did in the previous exercise.
# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)
# Print out observation for Japan
print(cars.loc['JAP'])
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS','EG']])
print(cars.iloc([[1,-1]]))

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU','MOR'],['country','drives_right']])

#%%
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)
# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:,['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap','drives_right']])

#%%




