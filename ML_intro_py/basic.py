
# check the version
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