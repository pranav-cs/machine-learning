# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
# y = dataset.iloc[:, 2].values
y = dataset.iloc[:, 2:3].values

# feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)
#  The number "-1" for rows commands your Python compiler to pick up such number of rows for the available entries  that a matrix with one column will be formed.
# 2-d array with one column
# y = y.reshape(-1, 1)
#y = np.ravel(sc_y.fit_transform(y.reshape(-1, 1)))

# Fitting the Regression Model to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)

# Predicting a new result
# 1. feature scale the 6.5 value
# 2. prediction will be in the scaled range
# 3. So, to get prediction in original scale perform inverse transform on it
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))

# Visualising the Regression results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1)) # from vector to matrix
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Regression Model) higher resolution')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
