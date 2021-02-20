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

# calculate parameters
sample_mean = stc.mean(data)
sample_std = stc.stdev(data)
print('Mean=%.3f, Standard Deviation=%.3f' % (sample_mean, sample_std))

# define the distribution
dist = norm(sample_mean, sample_std)

# sample probabilities for a range of outcomes
values = [value for value in range(30, 200)]
probabilities = [dist.pdf(value) for value in values]

# plot the histogram and pdf
plt.hist(data, bins=10, density=True)
plt.plot(values, probabilities)

plt.xlabel('Glucose (mmol/L)')
plt.ylabel('Quality')
plt.show()