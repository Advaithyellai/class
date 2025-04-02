from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn.model_selection import train_test_split
import keras
import pandas as pd
# from datetime import datetime

# import sys
# f = open('results.txt', 'a')
# sys.stdout = f

# start_time = datetime.now()
ALGS = ['Linear', 'Random Forest', 'Gradient Boosting', 'Adaboost', 'SVR', 'K Neighbors', 'Decision Tree', 'Naive Bayes']
# 'Neural Network', 'all'
PREDICT = False
ALG = 'all'
DROP = 0.075
NEURONS = [11, 132, 66, 22, 11, 1]
DROPOUT = 0.15
ACTIVATION = "sigmoid"
EPOCHS = 100
NN_VALidATION = 0
VERBOSE = 1

# def plot():
#     import matplotlib.pyplot as plt

#     plt.imshow(abs(data.corr()), cmap='hot')
#     plt.colorbar()
#     plt.xticks(range(len(data.columns)), labels=data.columns, rotation=45, ha="right", rotation_mode="anchor")
#     plt.yticks(range(len(data.columns)), labels=data.columns)
#     plt.show()

#     figure, axis = plt.subplots(2, 3)
#     axis[0, 0].scatter(data["rainfall"], data["humidity"])
#     axis[0, 0].set_title("humidity")
#     axis[0, 1].scatter(data["rainfall"], data["cloud"])
#     axis[0, 1].set_title("cloud")
#     axis[0, 2].scatter(data["rainfall"], data["sunshine"])
#     axis[0, 2].set_title("sunshine")
#     axis[1, 0].scatter(data["rainfall"], data["winddirection"])
#     axis[1, 0].set_title("winddirection")
#     axis[1, 1].scatter(data["rainfall"], data["windspeed"])
#     axis[1, 1].set_title("windspeed")
#     plt.show()

def process(train_ad, drop, test_ad = None):
    df = pd.read_csv(train_ad)
        
    if drop != 0:
        dropcols = df.corrwith(df["rainfall"])[df.corrwith(df["rainfall"]).abs() < drop].drop("id", axis=0).index
        df = df.drop(dropcols, axis=1)
    
    if test_ad == None:
        df, dtest = train_test_split(df, test_size=0.15, random_state=42)
    
    else:
        dtest = pd.read_csv(test_ad)
        if drop != 0: dtest = dtest.drop(dropcols, axis=1)
    
    return df, dtest

def algorithms(alg, x_train, y_train):
    if VERBOSE == 1:
        print('-'*50)
        print("Algorithm:", alg, end='\n\n')
    if alg == 'Linear':
        model = LinearRegression(positive=False, fit_intercept=True, copy_X=True)
    elif alg == 'K Neighbors':
        model = KNeighborsRegressor(weights='distance', n_neighbors=15, metric='manhattan')
    elif alg == 'Decision Tree':
        model = DecisionTreeRegressor(criterion='poisson', max_depth=3, min_samples_leaf=2, min_samples_split=2, max_features='log2')
    elif alg == 'Random Forest':
        model = RandomForestRegressor(n_estimators=125, criterion='poisson', max_features='sqrt', max_depth=4, min_samples_leaf=3, min_samples_split=2)
    elif alg == 'Gradient Boosting':
        model = GradientBoostingRegressor(learning_rate=0.05, loss='squared_error', n_estimators=75, criterion='squared_error', max_depth=2, max_features='log2', min_samples_leaf=3, min_samples_split=4)
    elif alg == 'Adaboost':
        model = AdaBoostRegressor(loss='linear', n_estimators=100)
    elif alg == 'Naive Bayes':
        model = GaussianNB()
    elif alg == 'SVR':
        model = SVR(degree=2, kernel='linear', gamma='scale')
    else:
        raise ValueError("Incorrect model name '{}' passed.".format(alg))

    model.fit(x_train, y_train)
    return model

def neural_network(x_train, y_train):
    if VERBOSE == 1:
        print('-'*50)
        print("Algorithm: Neural Network", end='\n\n')

    model = keras.models.Sequential()

    for neuron in NEURONS[:-1]:
        model.add(keras.layers.Dense(neuron, activation=ACTIVATION))
        model.add(keras.layers.Dropout(DROPOUT))
    
    model.add(keras.layers.Dense(NEURONS[-1], activation=ACTIVATION))

    model.compile(loss='mean_squared_error', optimizer="Adam")
    model.fit(x_train, y_train, epochs=EPOCHS, batch_size=16, validation_split=NN_VALidATION, verbose=0)
    return model

def evaluate(model, x_test, y_test):
    y_pred = model.predict(x_test)
    y_pred = y_pred.reshape((len(y_pred),))

    y_pred[y_pred>1] = 1
    y_pred[y_pred<0] = 0
    auc = roc_auc_score(y_test, y_pred)
    y_pred = y_pred.round()
    roundauc = roc_auc_score(y_test, y_pred)
    acc = accuracy_score(y_test, y_pred)

    if VERBOSE == 1:
        print("AUC: ", auc)
        print("Rounded AUC: ", roundauc)
        print("Accuracy: ", acc)
        print('-'*50, end='\n\n')
    return auc, acc

def main():
    print('-'*50)
    print("Drop Strength:", DROP, '\n')

    if PREDICT: dtrain, dtest = process("train.csv", DROP, test_ad="test.csv")
    else: dtrain, dtest = process("train.csv", DROP)

    FEATS = dtrain.columns.to_list()
    FEATS.remove("id")
    FEATS.remove("rainfall")

    if PREDICT:
        x_train, y_train = dtrain[FEATS], dtrain["rainfall"]
        x_test = dtest[FEATS]
        
        if ALG == 'Neural Network':
            model = neural_network(x_train, y_train)
        else:
            model = algorithms(ALG, x_train, y_train)
        y_pred = pd.DataFrame(dtest["id"])
        pred = model.predict(x_test)
        # pred[pred>1] = 1
        # pred[pred<0] = 0
        y_pred["rainfall"] = pred
        y_pred.to_csv("predictions.csv", index=False)
    else:
        x_train = dtrain[FEATS]
        y_train = dtrain["rainfall"]
        x_test = dtest[FEATS]
        y_test = dtest["rainfall"]
        
        if ALG == 'all':
            if VERBOSE == 1:
                print('-'*50)
                print("All Algorithms\n")
            
            model = neural_network(x_train, y_train)
            auc, acc = evaluate(model, x_test, y_test)
            bmod = ['Neural Network', auc, acc]

            for alg in ALGS:
                model = algorithms(alg, x_train, y_train)
                auc, acc = evaluate(model, x_test, y_test)
                if auc > bmod[1]:
                    bmod = [alg, auc, acc]
            
            print('-'*50)
            print("The Best Algorithm:", bmod[0], end='\n\n')
            print("AUC:", bmod[1])
            print("Accuracy", bmod[2])
            print('-'*50, end='\n\n')
        elif ALG == 'Neural Network':
            model = neural_network(x_train, y_train)
            evaluate(model, x_test, y_test)
        else:
            model = algorithms(ALG, x_train, y_train)
            evaluate(model, x_test, y_test)

main()

# end_time = datetime.now()
# time = end_time-start_time
# print("Time taken:", time.total_seconds(), "seconds")
# print('-'*50, '\n')

# from sklearn.tree import DecisionTreeRegressor
# from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
# from sklearn.linear_model import LinearRegression
# from sklearn.naive_bayes import GaussianNB
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.svm import SVR
# import keras
# import pandas as pd
# import numpy as np

# ALGS = ['Linear', 'Random Forest', 'Gradient Boosting', 'Adaboost', 'SVR', 'K Neighbors', 'Decision Tree', 'Naive Bayes']
# # 'Neural Network', 'all'
# PREDICT = False
# ALG = 'all'
# DROP = 0.075
# NEURONS = [11, 132, 66, 22, 11, 1]
# DROPOUT = 0.15
# ACTIVATION = "sigmoid"
# EPOCHS = 100
# NN_VALidATION = 0
# VERBOSE = 1
# CV = 5

# def algorithms(alg, x_train, y_train):
#     if VERBOSE == 1:
#         print('-'*50)
#         print("Algorithm:", alg, end='\n\n')
#     if alg == 'Linear':
#         model = LinearRegression(positive=False, fit_intercept=True, copy_X=True)
#     elif alg == 'K Neighbors':
#         model = KNeighborsRegressor(weights='distance', n_neighbors=15, metric='manhattan')
#     elif alg == 'Decision Tree':
#         model = DecisionTreeRegressor(criterion='poisson', max_depth=3, min_samples_leaf=2, min_samples_split=2, max_features='log2')
#     elif alg == 'Random Forest':
#         model = RandomForestRegressor(n_estimators=125, criterion='poisson', max_features='sqrt', max_depth=4, min_samples_leaf=3, min_samples_split=2)
#     elif alg == 'Gradient Boosting':
#         model = GradientBoostingRegressor(learning_rate=0.05, loss='squared_error', n_estimators=75, criterion='squared_error', max_depth=2, max_features='log2', min_samples_leaf=3, min_samples_split=4)
#     elif alg == 'Adaboost':
#         model = AdaBoostRegressor(loss='linear', n_estimators=100)
#     elif alg == 'Naive Bayes':
#         model = GaussianNB()
#     elif alg == 'SVR':
#         model = SVR(degree=2, kernel='linear', gamma='scale')
#     else:
#         raise ValueError("Incorrect model name '{}' passed.".format(alg))

#     model.fit(x_train, y_train)
#     return model

# def neural_network(x_train, y_train):
#     if VERBOSE == 1:
#         print('-'*50)
#         print("Algorithm: Neural Network", end='\n\n')

#     model = keras.models.Sequential()

#     for neuron in NEURONS[:-1]:
#         model.add(keras.layers.Dense(neuron, activation=ACTIVATION))
#         model.add(keras.layers.Dropout(DROPOUT))
    
#     model.add(keras.layers.Dense(NEURONS[-1], activation=ACTIVATION))

#     model.compile(loss='mean_squared_error', optimizer="Adam")
#     model.fit(x_train, y_train, epochs=EPOCHS, batch_size=16, validation_split=NN_VALidATION, verbose=0)
#     return model

# def main():
#     print('-'*50)
#     print("Drop Strength:", DROP, '\n')
#     dtrain = pd.read_csv("train.csv")
#     dtest = pd.read_csv("test.csv")
#     dpred = pd.DataFrame(index = dtest.index)
#     dpred["id"] = dtest["id"]

#     FEATS = dtrain.columns.to_list()
#     FEATS.remove("id")
#     FEATS.remove("rainfall")

#     x_train = dtrain[FEATS]
#     y_train = dtrain["rainfall"]
#     x_test = dtest[FEATS]
    
#     if VERBOSE == 1:
#         print('-'*50)
#         print("All Algorithms\n")
    
#     model = neural_network(x_train, y_train)
#     dpred["Neural Network"] = model.predict(x_test).tolist()

#     for alg in ALGS:
#         model = algorithms(alg, x_train, y_train)
#         dpred[alg] = model.predict(x_test).tolist()

#     dpred.to_csv("metatest.csv", index=False)

# main()