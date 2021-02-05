import statistics as stc 
import matplotlib.pyplot as plt
import pandas as pd 

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

def mean(data):
    print(stc.mean(data))

def mode(data):
    print(stc.multimode(data))

def median(data):
    print(stc.median(data))

# mean
# age_mean = stc.mean(age)
# print(age_mean)

# glucose_mean = stc.mean(glucose)
# print(glucose_mean)

#mode
# age_mode = stc.multimode(age)
# print(age_mode)

# glucose_mode = stc.mode(glucose)
# print(glucose_mode)

# median
# age_median = stc.median(age)
# print(age_median)

# glucose_median = stc.median(glucose)
# print(glucose_median)

# Sample standard deviation
# age_ssd = stc.stdev(age)
# print(age_ssd)

# glucose_ssd = stc.stdev(glucose)
# print(glucose_ssd)


# class my_plot:

#     def hist()

# histogram

plt.xlabel('Age')
# plt.ylabel('Interval')
# plt.title('Age')
plt.hist(age, bins=10)
plt.show()

# fig, ax = plt.subplots(2)

# ax[0].set_title('Age (years)')
# ax[0].hist(age)

# ax[1].set_title('Glucose')
# ax[1].hist(glucose)

# plt.show()

# box plot
# fig, ax = plt.subplots(2)
# ax[0].set_title('Age')
# ax[0].boxplot(age, vert=False)

# ax[1].set_title('Glucose')
# ax[1].boxplot(glucose, vert=False)

# plt.show()

# stem and leave
# ls = [i for i in range(1,10)]
# print(ls)
# fig, ax = plt.subplots(2)
# ax[0].set_title('Age')
# ax[0].stem(age, ls)

# ax[1].set_title('Glucose')
# ax[1].stem(glucose)

# plt.show()

# import stemgraphic

# fig, ax = stemgraphic.stem_graphic(df['Age'])

# plt.show()

# scatter
# fig, ax = plt.subplots(2)
# ax[0].set_title('Age')
# ax[0].scatter(x, y)


# ax[1].set_title('Glucose')
# ax[1].scatter(x, y)

# plt.show()