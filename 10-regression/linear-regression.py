import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn import datasets
import statsmodels.api as sm

import seaborn as sns; sns.set()

# We generate our data
# Then apply our transfrom of X and X transpose to the data
# If you think X2 may be a term, you need to include it in the terms you try

# plot line
# We know what the parameters are Beta0 is 1, Beta1 is 0.5
line = np.array([1, 0.5])
xlin = -10.0 + 20.0 * np.random.random(100)
ylin = line[0]+(line[1]*xlin)+np.random.randn(100)
plt.plot(xlin,ylin,'ro',markersize=4)
plt.show()

# plot quadratic
# There are ways to explore your data so you can decide what parameters to try
quad = np.array([1, 3, 0.5])
xquad = -10.0 + 20.0 * np.random.random(100)
# Calling it xquad is a little misleading
# How did you know if was X2? That's where being a data scientist comes in
yquad = quad[0]+(quad[1]*xquad)+(quad[2]*xquad*xquad)+np.random.randn(100)
plt.plot(xquad,yquad,'ro',markersize=4)
plt.show()

# plot log
# You can see that shape is clearly logarithmic so you need to include a log term
# If we get negative points, then our model would bbe clearly wrong and it wasn't actually log
# If you repeat this many times, you expect on average you will get the true values you had generated
log = np.array([1, 4])
xlog = 10.0 * np.random.random(100)
ylog = log[0]+log[1]*np.log(xlog)+np.random.randn(100)
plt.plot(xlog,ylog,'ro',markersize=4)
plt.show()

# plot line through first plot
line = np.array([1, 0.5])
xlin = -10.0 + 20.0 * np.random.random(100)
ylin = line[0]+(line[1]*xlin)+np.random.randn(100)
plt.plot(xlin,ylin,'ro',markersize=4)
plt.plot(xlin,line[0]+line[1]*xlin,'b-')
plt.text(-9,3,r'$y = \beta_0 + \beta_1x$',size=20)
plt.show()

# Least square estimate through first plot
m = np.shape(xlin)[0]
X = np.array([np.ones(m),xlin]).T
beta = np.linalg.inv(X.T @ X) @ X.T @ ylin

xplot = np.linspace(-10,10,50)
yestplot = beta[0]+beta[1]*xplot
plt.plot(xplot,yestplot,'b-',lw=2)
plt.plot(xlin,ylin,'ro',markersize=4)
plt.show()
print(beta)

# Least square estimate through second plot
m = np.shape(xquad)[0]
X = np.array([np.ones(m),xquad,xquad**2]).T
beta = np.linalg.inv(X.T @ X) @ X.T @ yquad

xplot = np.linspace(-10,10,50)
yestplot = beta[0]+beta[1]*xplot+beta[2]*xplot**2
plt.plot(xplot,yestplot,'b-',lw=2)
plt.plot(xquad,yquad,'ro',markersize=4)
plt.show()
print(beta)

# Least square estimate through third plot
m = np.shape(xlog)[0]
X = np.array([np.ones(m),np.log(xlog)]).T
beta = np.linalg.inv(X.T @ X) @ X.T @ ylog

xplot = np.linspace(-10,10,50)
yestplot = beta[0]+beta[1]*np.log(xplot)
plt.plot(xplot,yestplot,'b-',lw=2)
plt.plot(xlog,ylog,'ro',markersize=4)
plt.show()
print(beta)

# using libraries
# There are libraries to do this for you
# We can plot this in 3D (pycharm showed it flat, but there may be a way to manipulate it)
X, y = datasets.make_regression(n_samples=100, n_features=2, n_informative=5, noise=30, random_state=1)
X = sm.add_constant(X)
ax = plt.axes(projection='3d')
ax.scatter3D(X.T[1], X.T[2], y, cmap='ro')
plt.show()

model = sm.OLS(y, X)
results = model.fit()

ax = plt.axes(projection='3d')
ax.scatter3D(X.T[1], X.T[2], y)

x1, x2 = np.meshgrid(np.arange(min(X.T[1]), max(X.T[1]), .5), np.arange(min(X.T[2]), max(X.T[2]), .5))
exog = pd.core.frame.DataFrame({'x0': np.ones(len(x1.ravel())).ravel(), 'x1': x1.ravel(), 'x2':x2.ravel()})
print(exog)
out = results.predict(exog=exog)
ax.plot_surface(x1, x2, out.values.reshape(x1.shape), color='Green', alpha=.2)
plt.show()

# Evaluating the Modal
print(results.summary())
