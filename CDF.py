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
data2 = np.array(glucose)
data.sort()
data2.sort()

# https://www.youtube.com/watch?v=fQ0Iy0Sew_U

# yvals = np.zeros(len(data))
# for i in range(len(data)):
#     yvals[i] = (i+1)/len(yvals)
# plt.plot(data, yvals, 'k')

# https://stackoverflow.com/questions/24788200/calculate-the-cumulative-distribution-function-cdf-in-python

p = 1. * np.arange(len(data)) / (len(data) - 1)
p2 = 1. * np.arange(len(data2)) / (len(data) - 1)

fig, ax = plt.subplots(1, 2)
fig.suptitle('Cumulative Probability Function')

ax[0].plot(data, p)
ax[0].set_title('BMI')
ax[0].set_xlabel('BMI ((kg/height)^2)')
ax[0].set_ylabel('Probability')

ax[1].plot(data2, p2)
ax[1].set_title('Glucose')
ax[1].set_xlabel('Glucose (mmol/L)')
ax[1].set_ylabel('Probability')


plt.show()