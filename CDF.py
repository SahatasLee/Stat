import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('diabetes.csv')

# read data
x = df['Age']
y = df['Glucose']
z = df['BMI']


# to list
age = x.to_list()
glucose = y.to_list()
bmi = z.to_list()

data = np.array(bmi)
data.sort()

# https://www.youtube.com/watch?v=fQ0Iy0Sew_U

# yvals = np.zeros(len(data))
# for i in range(len(data)):
#     yvals[i] = (i+1)/len(yvals)
# plt.plot(data, yvals, 'k')

# https://stackoverflow.com/questions/24788200/calculate-the-cumulative-distribution-function-cdf-in-python

p = 1. * np.arange(len(data)) / (len(data) - 1)
plt.plot(data, p)


plt.show()