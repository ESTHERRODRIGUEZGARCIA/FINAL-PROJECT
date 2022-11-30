# load the data present on file `creditcardmarketing.xlsx` for `credit_card_classification`. Fill the notebook with the Python code needed to answer each question. This last file must be delivered.
#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')
from scipy import stats
from scipy.stats import pearsonr
#1.  Select all the data from table `credit_card_data` to check if the data was imported correctly.
ccm = pd.read_excel('creditcardmarketing.xlsx')

#2.  Select all the data from the table to verify if the command worked. Limit your returned results to 10.
print(ccm.head(10))

#3.  Use code to find how many rows of data you have.
print(ccm.shape)

#4.  Now find the unique values in some of columns: `Offer Accepted`, `Reward`, `Mailer Type`, `# Credit Cards Held`, `household_size`
print(ccm['Offer Accepted'].unique())
print(ccm['Reward'].unique())
print(ccm['Mailer Type'].unique())
print(ccm['# Credit Cards Held'].unique())
print(ccm['Household Size'].unique())

#5.  Arrange the data in decreasing order by the `average_balance`. Return only the `customer_number` of the top 10 customers with the highest `average_balances` in your data.
print(ccm.sort_values(by='Average Balance', ascending=False).head(10)['Customer Number'])

#6.  What is the average of `Average Balance` of all the customers in your data?
print(ccm['Average Balance'].mean())

#7. In this exercise use  `groupby` to check the properties of some of the categorical variables in our data. Note wherever `average_balance` is asked in the questions below, please take the average of the column `average_balance`. Show the results in a data frame and a plot. 
#What is the average balance of the customers grouped by `Income Level`? The returned result should have only two columns, `Income` and `Average Balance` of the customers. 

total = ccm.groupby('Income Level')['Average Balance'].mean()
total
plt.figure(figsize=(7,5))
sns.barplot(x='Income Level', y='Average Balance', data=ccm)

#What is the average balance of the customers grouped by `number_of_bank_accounts_open`? The returned result should have only two columns, `number_of_bank_aaccounts_open` and `Average Balance` of the customers. 
total = ccm.groupby('# Bank Accounts Open')['Average Balance'].mean()
total
plt.figure(figsize=(7,5))
sns.barplot(x='# Bank Accounts Open', y='Average Balance', data=ccm)

#What is the average number of credit cards held by customers for each of the credit card ratings? The returned result should have only two columns, `rating` and `average number of credit cards`.
total = ccm.groupby('Credit Rating')['# Credit Cards Held'].mean()
total
plt.figure(figsize=(7,5))
sns.barplot(x='Credit Rating', y='# Credit Cards Held', data=ccm)

#Is there any correlation between the columns `credit_cards_held` and `number_of_bank_accounts_open`? You can analyze this by grouping the data by one of the variables and then aggregating the results of the other column. Visually check if there is a positive correlation or negative correlation or no correlation between the variables.
#group the data by `credit_cards_held` and then aggregate the results of `number_of_bank_accounts_open`
ccm['# Credit Cards Held'].corr(ccm​​['# Bank Accounts Open']))
plt.figure(figsize=(15, 10))

sns.set(style='white')

mask=np.triu(np.ones_like(ccm.corr(), dtype=bool))

cmap=sns.diverging_palette(0, 10, as_cmap=True)


sns.heatmap(ccm.corr(),
           mask=mask,
          cmap=cmap,
          center=0,
          square=True,
          annot=True,
          linewidths=0.5,
          cbar_kws={'shrink': 0.5});

# - Check the number of customers in each category (ie number of credit cards held) to assess if that category is well represented in the dataset to include it in your analysis. For eg. If the category is under-represented as compared to other categories, ignore that category in this analysis
#numero de clientes por categoria
for i in ['Offer Accepted','Reward','Mailer Type','Income Level','# Bank Accounts Open','Overdraft Protection','Credit Rating','# Credit Cards Held','# Homes Owned','Household Size','Own Your Home','Average Balance' ]:
  print('--------->CATEGORY: ',i)
  print(ccm[i].value_counts())


# Search only for custtomers with credit ratign medium or high, credit card held 2 or less, owns their own home, household size 3 or more
rating = ccm[(ccm['Credit Rating'] == 'Medium') | (ccm['Credit Rating'] == 'High')]
cards = ccm[(ccm['# Credit Cards Held'] <= 2)]
Hhold = ccm[(ccm['Household Size'] >= 3)]
House = ccm[(ccm['Own Your Home'] == 'Yes')]
