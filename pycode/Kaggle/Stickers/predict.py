import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_percentage_error, root_mean_squared_error
from sklearn.model_selection import train_test_split
import keras
import pandas as pd
from datetime import datetime

# import sys
# f = open('results.txt', 'a')
# sys.stdout = f

start_time = datetime.now()
ALGS = ['Linear', 'Random Forest', 'Gradient Boosting', 'Naive Bayes', 'Decision Tree', 'Adaboost', 'K Neighbors', 'Ridge', 'Lasso']
# 'Neural Network', 'all', 'Decision Tree', 'Naive Bayes'
PREDICT = True
ALG = 'Random Forest'
DROP = 0.01
NEURONS = [9, 18, 9, 1]
DROPOUT = 0.15
ACTIVATION = "relu"
EPOCHS = 10
NN_VALIDATION = 0.1
VERBOSE = 1

def transform_data(ad):
    df = pd.read_csv(ad)
    df = df.dropna()
    
    df['date'] = pd.to_datetime(df['date']) 
    df['year'] = df['date'].dt.year.astype('float')
    df['quarter'] = df['date'].dt.quarter.astype('float')
    df['month'] = df['date'].dt.month.astype('float')
    df['day'] = df['date'].dt.day.astype('float')
    df['day_of_week'] = df['date'].dt.dayofweek.astype('float')
    df['week_of_year'] = df['date'].dt.isocalendar().week.astype('float')
    
    df['day_sin'] = np.sin(2 * np.pi * df['day'] / 365.0).round(2)
    df['day_cos'] = np.cos(2 * np.pi * df['day'] / 365.0).round(2)
    df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12.0).round(2)
    df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12.0).round(2)
    df['year_sin'] = np.sin(2 * np.pi * df['year'] / 7.0).round(2)
    df['year_cos'] = np.cos(2 * np.pi * df['year'] / 7.0).round(2)
    
    df['Group'] = (df['year'] - 2010) * 48 + df['month'] * 4 + df['day'] // 7

    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].factorize()[0]
        df[col] = df[col].astype('int')
    
    return df

def process():
    df = transform_data("train.csv")
    dropcols = df.corrwith(df['num_sold'])[df.corrwith(df['num_sold']).abs()<DROP]
    dropcols = dropcols.index
    df = df.drop(dropcols, axis=1)
    
    if PREDICT:
        dtest = transform_data("test.csv")
        dtest = dtest.drop(dropcols, axis=1)
    
    else:
        df, dtest = train_test_split(df, test_size=0.15, shuffle=False)#, random_state=42)
    
    return df, dtest

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
    elif alg == 'Lasso':
        model = Lasso()
    elif alg == 'Ridge':
        model = Ridge()
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

    mape = mean_absolute_percentage_error(y_test, y_pred)
    rmse = root_mean_squared_error(y_test, y_pred)

    if VERBOSE == 1:
        print("MAPE: ", mape)
        print("RMSE: ", rmse)
        print('-'*50, end='\n\n')
    return mape, rmse

def main():
    print('-'*50)
    print("Drop Strength:", DROP, '\n')

    dtrain, dtest = process()
    
    FEATS = dtrain.columns
    FEATS = FEATS.drop(['num_sold', 'date', 'id'])

    if PREDICT:
        x_train, y_train = dtrain[FEATS], dtrain["num_sold"]
        x_test = dtest[FEATS]
        
        if ALG == 'Neural Network':
            model = neural_network(x_train, y_train)
        else:
            model = algorithms(ALG, x_train, y_train)
        
        y_pred = pd.DataFrame(dtest["id"])
        pred = model.predict(x_test)
        y_pred["num_sold"] = pred
        y_pred.to_csv("predictions.csv", index=False)
    else:
        x_train = dtrain[FEATS]
        y_train = dtrain["num_sold"]
        x_test = dtest[FEATS]
        y_test = dtest["num_sold"]
        
        if ALG == 'all':
            if VERBOSE == 1:
                print('-'*50)
                print("All Algorithms\n")
            
            model = neural_network(x_train, y_train)
            mape, rmse = evaluate(model, x_test, y_test)
            bmod = ['Neural Network', mape, rmse]

            for alg in ALGS:
                model = algorithms(alg, x_train, y_train)
                mape, rmse = evaluate(model, x_test, y_test)
                if mape < bmod[1]:
                    bmod = [alg, mape, rmse]
            
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

end_time = datetime.now()
time = end_time-start_time
print("Time taken:", time.total_seconds(), "seconds")
print('-'*50, '\n')