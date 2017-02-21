import numpy as np
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn import metrics

X = np.load('Data/Kno1517.npy')
y = np.load('Data/Pre1517.npy')

# X_test = np.load('Data/Pre1617test.npy')
# X_test = X_test[170:190]
# print X_test
# y_test = np.load('Data/Res1617test.npy')
# y_test = y_test[170:190]

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state = 33,test_size = 0.15)

# rfr = RandomForestRegressor()
# rfr.fit(X_train, y_train)

# etr = ExtraTreesRegressor()
# etr.fit(X_train, y_train)

# gbr = GradientBoostingRegressor()
# gbr.fit(X_train, y_train) 

# y_predict_rfr = rfr.predict(X_test)
# y_predict_etr = etr.predict(X_test)
# y_predict_gbr = gbr.predict(X_test)

Lasso = linear_model.Lasso(alpha = 0.1)
Lasso.fit(X_train, y_train)
y_predict_lasso = Lasso.predict(X_test)

# linreg = LinearRegression()
# linreg.fit(X_train, y_train)
# y_predict_lin  = linreg.predict(X_test)

print y_predict_lasso
print y_test
#print np.sqrt(metrics.mean_squared_error(y_test, y_predict_lasso))

################ PLOT #################

import matplotlib.pyplot as plt  
stock = range(0,len(y_test))
smaLabel1 = 'Real'
smaLabel2 = 'Predict'
plt.plot(stock, y_test, 'r',label=smaLabel1)
plt.plot(stock, y_predict_lasso, 'b*',label=smaLabel2)
plt.xlabel('years(+2000)')
plt.ylabel('housing average price(*2000 yuan)')
plt.ylim(0, 30)
plt.xlim(-1,9)
plt.title('real Price & predict Price')
plt.legend()
plt.show()