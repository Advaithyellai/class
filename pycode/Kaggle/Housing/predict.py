import preprocess
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from tensorflow import keras
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, root_mean_squared_log_error
# from datetime import datetime

# import sys
# f = open('results.txt', 'a')
# sys.stdout = f

# start_time = datetime.now()
ALGS = ['Linear', 'Ridge', 'Lasso', 'K Neighbors', 'Decision Tree', 
         'Random Forest', 'Gradient Boosting', 'Adaboost'] # 'Neural Network', 'all'
ALG = 'None'
NEURONS = [9, 71, 355, 71, 9, 1]
DROPOUT = 0.15
ACTIVATION = "relu"
EPOCHS = 100
NN_VALIDATION = 0
DROP_WEAK = 0.1
VERBOSE = 0

def evaluate(model, x_test, y_test):
    y_pred = model.predict(x_test)
    y_pred = y_pred.reshape((len(y_pred),))
    
    rmsle = 1
    if ((y_pred>-1).all() and (y_test>-1).all()):
        rmsle = root_mean_squared_log_error(y_test, y_pred)
    r2score = r2_score(y_test, y_pred)

    if VERBOSE == 1:
        print("RMSLE: ", rmsle)
        print("R2 Score: ", r2score)
        print('-'*50, end='\n\n')
    return rmsle, r2score

def algorithms(alg, x_train, y_train):
    if VERBOSE == 1:
        print('-'*50)
        print("Algorithm:", alg, end='\n\n')
    if alg == 'Linear':
        model = LinearRegression()
    elif alg == 'Ridge':
        model = Ridge()
    elif alg == 'Lasso':
        model = Lasso()
    elif alg == 'K Neighbors':
        model = KNeighborsRegressor()
    elif alg == 'Decision Tree':
        model = DecisionTreeRegressor(min_samples_leaf=3, min_samples_split=3, max_depth=7)
    elif alg == 'Random Forest':
        model = RandomForestRegressor(n_estimators=250, min_samples_split=3, min_samples_leaf=1, max_depth=7)
    elif alg == 'Gradient Boosting':
        model = GradientBoostingRegressor(n_estimators=250, min_samples_split=4, min_samples_leaf=1, max_depth=4, learning_rate=0.0733)
    elif alg == 'Adaboost':
        model = AdaBoostRegressor()
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
    
    model.add(keras.layers.Dense(NEURONS[-1], activation="relu"))

    model.compile(loss='mean_squared_error', optimizer="Adam")
    model.fit(x_train, y_train, epochs=EPOCHS, batch_size=16, validation_split=NN_VALIDATION, verbose=0)
    return model

def main():
    print('-'*50)
    print("Drop Strength:", DROP_WEAK, '\n')

    df, dpred = preprocess.main(DROP_WEAK)

    FEATS = df.columns.to_list()
    FEATS.remove("Id")
    FEATS.remove("SalePrice")

    # x_train, y_train = df[FEATS], df["SalePrice"]
    # x_test = dpred[FEATS]
    df = train_test_split(df, test_size=0.15, random_state=42)
    dtrain, dtest = df[0], df[1]
    x_train = dtrain[FEATS]
    y_train = dtrain["SalePrice"]
    x_test = dtest[FEATS]
    y_test = dtest["SalePrice"]
    
    if ALG == 'all':
        if VERBOSE == 1:
            print('-'*50)
            print("All Algorithms\n")
        
        model = neural_network(x_train, y_train)
        rmse, r2 = evaluate(model, x_test, y_test)
        bmod = ['Neural Network', rmse, r2]

        for alg in ALGS:
            model = algorithms(alg, x_train, y_train)
            rmse, r2 = evaluate(model, x_test, y_test)
            if rmse < bmod[1]:
                bmod = [alg, rmse, r2]
        
        print('-'*50)
        print("The Best Algorithm:", bmod[0], end='\n\n')
        print("RMSE:", bmod[1])
        print("R2 Score:", bmod[2])
        print('-'*50, end='\n\n')
    elif ALG == 'Neural Network':
        model = neural_network(x_train, y_train)
        evaluate(model, x_test, y_test)
    else:
        model = algorithms(ALG, x_train, y_train)
        evaluate(model, x_test, y_test)
    
    # y_pred = pd.DataFrame(dpred["Id"])
    # y_pred["SalePrice"] = model.predict(x_test)
    # y_pred.to_csv("predictions.csv", index=False)

# main()


# end_time = datetime.now()
# time = end_time-start_time
# print("Time taken:", time.total_seconds(), "seconds")
# print('-'*50, '\n')