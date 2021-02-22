import matplotlib.pyplot as plt
import pandas as pd 
from scipy.stats import norm
import statistics as stc 

plt.style.use('bmh')
df = pd.read_csv('diabetes.csv')

# age glucose BMI
x = df['Age']
y = df['Glucose']
z = df['BMI']

# convert to list
age = x.to_list()
glucose = y.to_list()
bmi = z.to_list()

data = glucose
data2 = bmi

# calculate parameters
sample_mean = stc.mean(data)
sample_std = stc.stdev(data)
print('Mean=%.3f, Standard Deviation=%.3f' % (sample_mean, sample_std))

sample_mean2 = stc.mean(data2)
sample_std2 = stc.stdev(data2)

# define the distribution
dist = norm(sample_mean, sample_std)
dist2 = norm(sample_mean2, sample_std2)

# sample probabilities for a range of outcomes
values = [value for value in range(30, 200)]
probabilities = [dist.pdf(value) for value in values]

values2 = [value2 for value2 in range(0, 70)]
probabilities2 = [dist2.pdf(value2) for value2 in values2]

fig, ax = plt.subplots(1, 2)
fig.suptitle('Probability Density Function')

# plot the histogram and pdf
ax[0].hist(data, bins=10, density=True)
ax[0].plot(values, probabilities)
ax[0].set_xlabel('Glucose (mmol/L)')
ax[0].set_ylabel('Probability')

ax[1].hist(data2, bins=10, density=True)
ax[1].plot(values2, probabilities2)
ax[1].set_xlabel('BMI ((kg/height)^2)')
ax[1].set_ylabel('Probability')

plt.show()