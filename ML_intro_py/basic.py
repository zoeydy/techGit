
# check the version
import imp
import sys
sys.version
import pandas as pd
pd.__version__
import matplotlib as plt
plt.__version__
import numpy as np
np.__version__
import scipy as sp
sp.__version__
import IPython
IPython.__version__
import sklearn
sklearn.__version__

# 路径问题
import sys
sys.path.append('/Users/zoeydy/opt/anaconda3/lib/python3.9/site-packages/mglearn')

# 1. the Iris example
from sklearn.datasets import load_iris
iris_dataset = load_iris()
iris_dataset.keys()
print(iris_dataset['DESCR'][:100] + "\n...")
iris_dataset['target_names']
iris_dataset['feature_names']
iris_dataset['data']
iris_dataset['target']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0
)

print("X_train shape: {}".format(X_train.shape))
print("y_train shape: {}".format(y_train.shape))

print("X_test shape: {}".format(X_test.shape)) 
print("y_test shape: {}".format(y_test.shape))

# create dataframe from data in X_train
# label the columns using the strings in iris_dataset.feature_names 
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
# create a scatter matrix from the dataframe, color by y_train

# this block returns the error: NameError: name 'mglearn' is not defined
import mglearn
grr = pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
                            hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
                            

# 2.e.g. the scikit-learn 
from sklearn.neighbors import KNeighborsClassifier 
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)

# 3.e.g. making predictions
X_new = np.array([[5, 2.9, 1, 0.2]]) 
print("X_new.shape: {}".format(X_new.shape))

prediction = knn.predict(X_new) 
print("Prediction: {}".format(prediction)) 
print("Predicted target name: {}".format(
    iris_dataset['target_names'][prediction]))

# 4.e.g. evalusting the model
y_pred = knn.predict(X_test)
print("Test set predictions:\n {}".format(y_pred))

print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))

print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))

# Summary
X_train, X_test, y_train, y_test = train_test_split(
        iris_dataset['data'], iris_dataset['target'], random_state=0)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))

