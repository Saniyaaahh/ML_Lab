#!/usr/bin/env python
# coding: utf-8

# #### a. Reading the CSV file using pandas:

# In[42]:


# Read the CSV file
import pandas as pd
df=pd.read_csv('enjoysport.csv')
df


# #### b. Showing the total number of training instances:

# In[43]:


# Calculate total number of training instances
def total_training_instances(df):
    return len(df)
# Example usage:
total_instances = total_training_instances(df)
print("The total number of training instances are:", total_instances)


# #### c. Displaying the initial hypothesis:

# In[44]:


# Initialize the initial hypothesis
def initial_hypothesis(df):
    return ['0'] * (len(df.columns) - 1)
# Example usage:
init_hypothesis = initial_hypothesis(df)
print("The initial hypothesis are:", init_hypothesis)


# #### d. Displaying the hypothesis for each training instance:

# In[45]:


# Calculate hypothesis for each training instance
def hypothesis_for_instances(df):
    hypotheses = []
    specific_hypothesis = initial_hypothesis(df)
    for index, row in df.iterrows():
        if row['enjoy_sport'] == 'yes':  # Adjusted column name to 'enjoy_sport'
            for i in range(len(df.columns) - 1):
                if specific_hypothesis[i] == '0':
                    specific_hypothesis[i] = row[i]
                elif specific_hypothesis[i] != row[i]:
                    specific_hypothesis[i] = '?'
            hypotheses.append(specific_hypothesis.copy())
    return hypotheses

# Example usage:
hypotheses = hypothesis_for_instances(df)
for idx, h in enumerate(hypotheses, start=1):
    print(f"The hypothesis for the training instance {idx} is:")
    print(h)


# #### e. Displaying the Maximally specific hypothesis:

# In[46]:


import pandas as pd

# Function to read the initial hypothesis from the dataframe
def initial_hypothesis(df):
    return ['0'] * (len(df.columns) - 1)

# Define the find_s_algorithm function
def find_s_algorithm(df):
    specific_hypothesis = initial_hypothesis(df)
    for index, row in df.iterrows():
        if row['enjoy_sport'] == 'yes':  # Ensure the column name matches
            for i in range(len(df.columns) - 1):
                if specific_hypothesis[i] == '0':
                    specific_hypothesis[i] = row[i]
                elif specific_hypothesis[i] != row[i]:
                    specific_hypothesis[i] = '?'
    return specific_hypothesis

# Define the maximally_specific_hypothesis function
def maximally_specific_hypothesis(df):
    return find_s_algorithm(df)

# Example usage:
# Reading the CSV file
df = pd.read_csv('enjoysport.csv')

# Getting the maximally specific hypothesis
max_specific_hypothesis = maximally_specific_hypothesis(df)

# Printing the result
print("The Maximally specific hypothesis for the training instance is:\n", max_specific_hypothesis)

