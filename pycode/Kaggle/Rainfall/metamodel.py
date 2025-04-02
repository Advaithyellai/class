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

# import sys
# f = open('results.txt', 'a')
# sys.stdout = f

ALGS = ['Linear', 'Random Forest', 'Gradient Boosting', 'Adaboost', 'SVR', 'K Neighbors', 'Decision Tree', 'Naive Bayes']
# 'Neural Network', 'all'
PREDICT = True
ALG = 'Linear'
NEURONS = [11, 132, 66, 22, 11, 1]
DROPOUT = 0.15
ACTIVATION = "sigmoid"
EPOCHS = 100
NN_VALIDATION = 0
VERBOSE = 1
trainad = "metatrain.csv"
testad = "metatest.csv"

def process():
    dtrain = pd.read_csv(trainad)

    if PREDICT:
        dtest = pd.read_csv(testad)
    else:
        dtrain, dtest = train_test_split(dtrain, test_size=0.15, random_state=42)
    
    return dtrain, dtest

def algorithms(alg, x_train, y_train):
    if VERBOSE == 1:
        print('-'*50)
        print("Algorithm:", alg, end='\n\n')
    if alg == 'Linear':
        model = LinearRegression()
    elif alg == 'K Neighbors':
        model = KNeighborsRegressor()
    elif alg == 'Decision Tree':
        model = DecisionTreeRegressor()
    elif alg == 'Random Forest':
        model = RandomForestRegressor()
    elif alg == 'Gradient Boosting':
        model = GradientBoostingRegressor()
    elif alg == 'Adaboost':
        model = AdaBoostRegressor()
    elif alg == 'Naive Bayes':
        model = GaussianNB()
    elif alg == 'SVR':
        model = SVR()
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
    model.fit(x_train, y_train, epochs=EPOCHS, batch_size=16, validation_split=NN_VALIDATION, verbose=0)
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
    dtrain, dtest = process()

    FEATS = dtrain.columns.to_list()
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
        pred[pred>1] = 1
        pred[pred<0] = 0
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