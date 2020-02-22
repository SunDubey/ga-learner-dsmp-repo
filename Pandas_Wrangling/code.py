# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
# code starts here
bank = pd.read_csv(path)
#print(bank.describe)
#print(bank.info)

categorical_var = bank.select_dtypes(include='object')
print(categorical_var.head(10))

numerical_var = bank.select_dtypes(include='number')
print(numerical_var.head(10))
# code ends here


# --------------
# code starts here
#print(bank.head(10))
banks = bank.drop(['Loan_ID'],axis=1)
#print(banks.head(10))
print(banks.isnull().sum())
bank_mode = banks.mode().iloc[0]
banks.fillna(value = bank_mode,inplace=True)
print(banks.isnull().sum())

#code ends here


# --------------
# Code starts here

avg_loan_amount = banks.pivot_table(index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc=np.mean)
print(avg_loan_amount)


# code ends here



# --------------
# code starts here
loan_approved_se = banks[( banks['Self_Employed']=='Yes' ) & ( banks['Loan_Status']=='Y' ) ]
loan_approved_nse = banks[( banks['Self_Employed']=='No' ) & ( banks['Loan_Status']=='Y' ) ]

percentage_se = (len(loan_approved_se)*100)/614
percentage_nse = (len(loan_approved_nse)*100)/614
print(percentage_se)
print(percentage_nse)

# code ends here


# --------------
# code starts here
banks['Loan_Amount_Term'] = banks['Loan_Amount_Term'].apply(lambda x : int(x/12))
loan_term = banks['Loan_Amount_Term']
big_loan_term = len(banks[banks['Loan_Amount_Term'] >= 25])



# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')
loan_groupby=loan_groupby['ApplicantIncome','Credit_History']
mean_values = loan_groupby.mean()
mean_values


# code ends here


