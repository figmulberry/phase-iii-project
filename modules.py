# Importing the required modules: They will be imported as needed
import numpy as np # Useful for Numerical operations and Arrays in Python
import pandas as pd # Useful for Manipulation of Data
# Useful for Data Visualizations (Data Engineering) on Matplotlib in Python
import seaborn as sns 
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import sys
import datetime
import tabulate
from tabulate import tabulate

from datetime import datetime
import warnings # Ignore all warnings
warnings.filterwarnings('ignore')

import random

# from sklearn.linear_model import LinearRegression
# #     Assumption of Independence: sensitive to Multicoliniality
# #     Outliers can have a significant impact on the results
# #     Sensitive to Scaling and Units: (scale data before training)
# #     Missing Data

# # Incase we have multicolinearity
# from sklearn.linear_model import Ridge
# #   Ridge Regression: Handles multicoliniality well by distributing the weight among correlated features.

# from sklearn.linear_model import Lasso
# #   Lasso Regression: Preferred when you suspect that only a subset of features are relevant and you want to perform feature selection.
# #   Too many columns without knowing which to drop

# # Decision Trees
# from sklearn.tree import DecisionTreeRegressor
# #   potential issues:
# #   Overfitting: soln(pre-pruning post pruning)
# #   Sensitive to Outliers
# #   Difficulty in Handling Irrelevant Features(minimize input columns to only important features)

# # KNN Regressor
# from sklearn.neighbors import KNeighborsRegressor
# #   The choice of 'k' have a significant impact on the performance of the model.(check online how to)
# #   Computationally Intensive:(Not suited for big datasets)
# #   Sensitivity to Noise and Outliers:
# #   Sensitive to Imbalanced Data
# #   Need for Standardization:


