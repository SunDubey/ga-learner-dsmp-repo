# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
sb.barplot(data['Loan_Status'].values,data['Loan_Status'].index)


#Code starts here


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area','Loan_Status'])
property_and_loan = property_and_loan.size().unstack()
property_and_loan.plot(kind='bar',stacked='False')
plt.xlabel("Property Area")
plt.xlabel("Loan Status")
plt.xticks(rotation=45)
plt.show()



# --------------
#Code starts here
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status'])
education_and_loan = education_and_loan.size().unstack()
education_and_loan.plot(kind='bar',stacked='False')
plt.xlabel("Education Status")
plt.xlabel("Loan Status")
plt.xticks(rotation=45)
plt.show()



# --------------
#Code starts here
graduate = data[data['Education']=='Graduate']
not_graduate = data[data['Education']=='Not Graduate']
graduate['LoanAmount'].plot(kind='density',label='Graduate')
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')













#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=[12,12])
plt.subplot(3,1,1)
plt.scatter(data['ApplicantIncome'],data['LoanAmount'])
plt.title("Applicant Income")
plt.subplot(3,1,2)
plt.scatter(data['CoapplicantIncome'],data['LoanAmount'])
plt.title("CoApplicant Income")
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
plt.subplot(3,1,3)
plt.scatter(data['TotalIncome'],data['LoanAmount'])
plt.title("Total Income")
plt.show()



