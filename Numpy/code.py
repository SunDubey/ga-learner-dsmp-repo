# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
new_record= np.array(new_record)
#Code starts here
data = np.genfromtxt(path,delimiter=",",skip_header=1,dtype='i4')
print(data)
print(type(data))
print(data.shape)
print(data.size)
print(data.dtype)
census = np.concatenate((data,new_record))


# --------------
#Code starts here
age = np.array(census[:,0])
print(age)
max_age = np.max(age)

min_age = np.min(age,axis=0)
age_mean = np.mean(age,axis=0)
age_std = np.std(age,axis=0)



# --------------
#Code starts here
import numpy as np
race_0 = census[(census[:,2]==0)]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

arr = np.array([len_0,len_1,len_2,len_3,len_4])
minority_race = np.argmin(arr)
print(minority_race)


# --------------
#Code starts here
senior_citizens = census[census[:,0] > 60]
working_hours_sum = np.sum(senior_citizens[:,6])
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1] > 10]
low = census[census[:,1] <= 10]
avg_pay_high = np.mean(high[:,7],axis = 0)
avg_pay_low = np.mean(low[:,7],axis = 0)
truth = bool(avg_pay_high>avg_pay_low)
print(truth)




