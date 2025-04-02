from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR
import predict
from datetime import datetime

start = datetime.now()
dtrain, dtest = predict.process("train.csv", 0.075, "test.csv")
FEATS = dtrain.columns.to_list()
FEATS.remove("id")
FEATS.remove("rainfall")

x_train = dtrain[FEATS]
y_train = dtrain["rainfall"]

model = SVR()
param_grid = {'kernel':['linear', 'poly', 'rbf', 'sigmoid'], 'degree':[1, 2, 3, 4, 5], 'gamma':['scale', 'auto']}

random_search = GridSearchCV(model, param_grid, cv=5, verbose=1)
random_search.fit(x_train, y_train)

print("Best Hyperparameters:", random_search.best_params_)
print("Best Score:", random_search.best_score_)

end = datetime.now()
print("Time Taken: {} seconds".format((end-start).total_seconds()))
# LinearRegressor: {'copy_X': [True,False], 'fit_intercept': [True,False], 'positive': [True,False]}
# KNeighborsRegressor: {'n_neighbors' : [5,7,9,11,13,15], 'weights' : ['uniform','distance'], 'metric' : ['minkowski','euclidean','manhattan']}
# DecisionTreeRegressor: {'criterion': ['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],'max_depth': range(2, 5),'min_samples_split': range(2, 5),'min_samples_leaf': range(2, 5), 'max_features': ['auto', 'sqrt', 'log2']}
# RandomForestRegressor: {'n_estimators':[50, 75, 100, 125, 150],'max_features': ['sqrt', 'log2'], 'criterion': ['squared_error', 'friedman_mse', 'absolute_error', 'poisson'], 'max_depth': range(2, 10),'min_samples_split': range(2, 5),'min_samples_leaf': range(2, 5)}
# GradientBoostingRegressor: {'loss': ['squared_error', 'absolute_error', 'huber', 'quantile'], 'learning_rate':[0.01, 0.05, 1, 1.5, 2], 'n_estimators':[50, 75, 100, 125, 150], 'criterion':['friedman_mse', 'squared_error'], 'min_samples_split':range(2, 5), 'min_samples_leaf':range(2, 5), 'max_depth':[None, 2, 3, 4], 'max_features':['auto', 'sqrt', 'log2']}
# AdaBoostRegressor: {'n_estimators':[10, 25, 50, 75, 90], 'loss':['linear', 'square', 'exponential']}
# GaussianNB: {}
# SVR: {'kernel':['linear', 'poly', 'rbf', 'sigmoid'], 'degree':[1, 2, 3, 4, 5], 'gamma':['scale', 'auto']}