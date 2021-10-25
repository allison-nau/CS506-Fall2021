import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn import datasets
import statsmodels.api as sm
import seaborn as sns; sns.set()

# Logisitc regression is a little more complicated

df = pd.read_csv('ats-admissions.csv') 
print(df.head(10))

print()

# Describe dataset using pandas library:
# Get average GRE
# Most students get rejected
# Quantile for 50% is 0, so at least 50% get's rejected
print("DESCRIBE")
print(df.describe())
# If you see an increase in GRE by 1 what is the increase in log-odds... need to apply logit-inverse to get probability
# GPA looks more important than GRE, BUT GPA range is less
# Resolve some issues of scale through normalization
# The way you interpret these coefficients is different than it would be in lienar regression


# Can see histogram distributions

df.hist()
plt.show()

df['intercept'] = 1.0
train_cols = df.columns[1:]
train_cols
logit = sm.Logit(df['admit'], df[train_cols])
 
# fit the model
result = logit.fit()

print()
print("SUMMARY")
print(result.summary())
