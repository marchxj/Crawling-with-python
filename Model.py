import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
import xgboost as xgb
from sklearn.preprocessing import StandardScaler


data = pd.read_csv('data_clean.csv')
df = data.drop['movie_id','actor_names','synopsis','Studio','Directed By','Box Office','Written By','month','day'],axis=1)

train_set, test_set = train_test_split(a, test_size=0.2, random_state=42)
train = train_set.drop("target_value", axis=1) # drop labels for training set
train_labels = train_set["target_value"].copy()
test = test_set.drop("target_value", axis=1)
test_labels = test_set["target_value"].copy()

# scaler test and train
scaler = StandardScaler()
scaler.fit(train) 
X_train = scaler.transform(train)  
X_test = scaler.transform(test)

# model 
lin_reg = LinearRegression()
tree_reg = DecisionTreeRegressor(random_state=42)
forest_reg = RandomForestRegressor(random_state=42)
svm_reg = SVR(kernel="linear")
xgb_reg = xgb.XGBRegressor()
nn_reg = MLPRegressor()

#=======================================================================================

lin_reg.fit(X_train, train_labels)
tree_reg.fit(X_train, train_labels)
forest_reg.fit(X_train, train_labels)
svm_reg.fit(X_train, train_labels)
xgb_reg.fit(X_train, train_labels)
nn_reg.fit(X_train, train_labels)

#=======================================================================================

pred_lin =lin_reg.predict(X_test)
pred_t = tree_reg.predict(X_test)
pred_for = forest_reg.fit(X_test)
pred_svm = clf.predict(X_test)
pred_xgb = model.predict(X_test)
pred_nn = nn_reg.predict(X_test)

#=======================================================================================
print('LinearRegression mse: %.2f' 
      % mean_squared_error(test_labels, pred_lin))
print('DecisionTreeRegressor mse: %.2f' 
      % mean_squared_error(test_labels, pred_t))
print('RandomForestRegressor mse: %.2f' 
      % mean_squared_error(test_labels, pred_for))
print('SVM mse: %.2f' 
      % mean_squared_error(test_labels, pred_svm))
print('XGBRegressor mse: %.2f' 
      % mean_squared_error(test_labels, pred_xgb))
print('neural_network: %.2f' 
      % mean_squared_error(test_labels, pred_nn))









