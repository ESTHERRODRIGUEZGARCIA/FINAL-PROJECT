import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')


ccm = pd.read_excel('creditcardmarketing.xlsx')
#print(ccm.head(15))
#print(ccm.shape)
print(ccm.info())

plt.figure(figsize=(10,8))
sns.heatmap(ccm.corr(), annot=True, cmap='coolwarm')

#sacar valores unicos de una columna del dataset
print(ccm['Offer Accepted'].unique())
print(ccm['Reward'].unique())
print(ccm['Mailer Type'].unique())
print(ccm['# Credit Cards Held'].unique())
print(ccm['Household Size'].unique())

#Arrange the data in decreasing order by the `average_balance`. Return only the `customer_number` of the top 10 customers with the highest `average_balances` in your data.
print(ccm.sort_values(by='Average Balance', ascending=False).head(10)['Customer Number'])

#What is the average of `Average Balance` of all the customers in your data?
print(ccm['Average Balance'].mean())

#What is the average balance of the customers grouped by `Income Level`? The returned result should have only two columns, `Income` and `Average Balance` of the customers.
#Show the results in a data frame and a plot. 

print(ccm.groupby('Income Level')['Average Balance'].mean())
plt.figure(figsize=(10,8))
sns.barplot(x='Income Level', y='Average Balance', data=ccm)



# Note wherever `average_balance` is asked in the questions below, please take the average of the column `average_balance`. Show the results in a data frame and a plot. 
#What is the average balance of the customers grouped by `number_of_bank_accounts_open`? The returned result should have only two columns, `number_of_bank_aaccounts_open` and `Average Balance` of the customers. 
print(ccm.groupby('# Bank Accounts Open')['Average Balance'].mean())

#What is the average number of credit cards held by customers for each of the credit card ratings? The returned result should have only two columns, `rating` and `average number of credit cards`.
print(ccm.groupby('Credit Rating')['# Credit Cards Held'].mean())

#Is there any correlation between the columns `credit_cards_held` and `number_of_bank_accounts_open`? You can analyze this by grouping the data by one of the variables and then aggregating the results of the other column. Visually check if there is a positive correlation or negative correlation or no correlation between the variables.
print(ccm.groupby('# Bank Accounts Open')['# Credit Cards Held'].mean())

