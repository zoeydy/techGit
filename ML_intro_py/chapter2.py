
import sys
import matplotlib.pyplot as plt
import numpy as np

# sys.path.append('/Users/zoeydy/opt/anaconda3/lib/python3.9/site-packages/mglearn')
import mglearn
import graphviz


# 1.e.g.
# generate dataset
X, y = mglearn.datasets.make_forge()

# plot dataset
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.legend(["Class 0", "Class 1"], loc=4) 
plt.xlabel("First feature") 
plt.ylabel("Second feature")
plt.show()

print("X.shape: {}".format(X.shape))




# 2.e.g. Plot of the wave dataset
X, y = mglearn.datasets.make_wave(n_samples=40)
plt.plot(X, y, 'o')
plt.ylim(-3, 3)
plt.xlabel("Feature")
plt.ylabel("Target")
plt.show()



# 3.e.g.cancer
from sklearn.datasets import load_breast_cancer 
cancer = load_breast_cancer() 
print("cancer.keys(): \n{}".format(cancer.keys()))

print("the shape of cancer data: {}".format(cancer.data.shape))
print("sample counts per class: \n{}".format({
    n:v for n,v in zip(cancer.target_names, np.bincount(cancer.target))
}))
print("Feature names: \n{}".format(cancer.feature_names))



# 4.e.g.house price
from sklearn.datasets import load_boston
boston = load_boston()
print("Data shape: {}".format(boston.data.shape))
# load the derived data (feature engineering)
X, y = mglearn.datasets.load_extended_boston()
print("X.shape: {}".format(X.shape))