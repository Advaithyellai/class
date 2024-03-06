import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import pandas as pd
from tensorflow import keras
from sklearn import metrics, preprocessing, model_selection, svm, tree, linear_model, neighbors, ensemble, discriminant_analysis, naive_bayes
import numpy as np
from datetime import datetime
# Note: tensorflow version greater than 2.10.1 is incompatible with windows

def preprocess(df):
    if PROCESS == 1:
        for var in ['Embarked', 'Title']:
            df = pd.concat([df, pd.get_dummies(df[var], prefix=var)], axis=1)

        scaler = preprocessing.StandardScaler()
        for var in ['Age', 'Parch', 'SibSp', "Pclass", "Family", "Fare"]:
            df[var] = df[var].astype('float64')
            df[var] = scaler.fit_transform(df[var].values.reshape(-1, 1))
    elif PROCESS == 2:
        relation_emb = {"C": 0, "Q": 1, "S": 2}
        relation_tit = {'Mr': 0, 'Miss': 1, 'Mrs': 2, 'Master': 3, 'Royalty': 4, 'Officer': 5}

        df["Embarked_N"] = df.Embarked.map(relation_emb)
        df["Title_N"] = df.Title.map(relation_tit)
    elif PROCESS == 3:
        df["Age"] = pd.cut(df.Age, bins=[0, 12, 20, 40, 120], labels=[0, 1, 2, 3])
        df["Fare"] = pd.cut(df.Fare, bins=[0, 7.91, 14.45, 31, 120], labels=[0, 1, 2, 3])
        for var in ['Embarked', 'Title', "Age", "Fare"]:
            df = pd.concat([df, pd.get_dummies(df[var], prefix=var)], axis=1)

    df.drop(['Cabin', 'Name', 'Ticket', 'Sex', "Embarked", "Title"], axis=1, inplace=True)
    return df

start = datetime.now()
# possible activations are:
# ACTIVATIONS = ["tanh", "softsign", "selu", "elu", "relu", "sigmoid", "softplus", "softmax"]
ACTIVATION = "tanh"
ALGORITHMS = ["naive_bayes", "decision_tree", "k_nearest_neighbor",\
    "support_vector_machine", "linear_discriminant_analysis",\
    "logistic", "random_forest", "gradient_boosting"] #"neural_network", "all"
NUMBER_OF_ALGORITHMS = len(ALGORITHMS)+1
ALGORITHM = "neural_network"
NEURONS = [9, 54, 432, 108, 9, 1]
EPOCHS = 100
DROPOUT = 0.12
REAL_PREDS = False
PROCESS = 1
NN_VALIDATION = 0.2

data = pd.read_csv("train.csv")
data = preprocess(data)

if REAL_PREDS:
    test2 = pd.read_csv("test.csv")
    test2 = preprocess(test2)
    train = data
    train_nn, test_nn = model_selection.train_test_split(data, test_size=0.2)
else:
    train, test2 = model_selection.train_test_split(data, test_size=0.15)
    train_nn, test_nn = model_selection.train_test_split(train, test_size=0.2)

ALL_FEATURES = data.columns.tolist()
ALL_FEATURES.remove("PassengerId")
ALL_FEATURES.remove("Survived")

class titanic:
    def __init__(self, feats):
        FEATURES = feats
        self.feats = feats
        print("\n------------------------------------------")
        print("{} Features: {}".format(len(self.feats), self.feats))

        self.x_train_nn, self.y_train_nn = train_nn[FEATURES], train_nn["Survived"]
        self.x_test_nn, self.y_test_nn = test_nn[FEATURES], test_nn["Survived"]
        self.x_test2 = test2[FEATURES]
        self.x_train, self.y_train = train[FEATURES], train["Survived"]

        if not REAL_PREDS: self.y_test2 = test2["Survived"]

        if ALGORITHM == "neural_network":
            model, hist = self.neural_network()
            self.accuracy(model, ALGORITHM, hist=hist)
        elif ALGORITHM == "all":
            model, hist = self.neural_network()
            fs, preds = self.accuracy(model, "neural_network", hist)
            fscores = {"neural_network": fs}
            
            for algs in ALGORITHMS:
                model = self.other(algs)
                fs, pred = self.accuracy(model, algs)
                fscores[algs] = fs
                preds += pred
            
            self.pred(preds/NUMBER_OF_ALGORITHMS, fscores=fscores)
        else:
            model = self.other(ALGORITHM)
            self.accuracy(model, ALGORITHM)

    def neural_network(self):
        print("\n------------------------------------------")
        print("Algorithm: neural_network")
        print("Activation function:", ACTIVATION)

        model = keras.models.Sequential()

        model.add(keras.layers.Dense(NEURONS[0], input_shape=(len(self.feats),), activation=ACTIVATION))
        model.add(keras.layers.Dropout(DROPOUT))
        
        for neuron in NEURONS[1:-1]:
            model.add(keras.layers.Dense(neuron, activation=ACTIVATION))
            model.add(keras.layers.Dropout(DROPOUT))
        
        model.add(keras.layers.Dense(NEURONS[-1], activation="sigmoid"))

        model.compile(loss='binary_crossentropy', optimizer="Adam", metrics=['accuracy'])
        hist = model.fit(np.array(self.x_train_nn), np.array(self.y_train_nn), epochs=EPOCHS, batch_size=16, verbose=0, validation_split=NN_VALIDATION)
        return model, hist.history

    def other(self, alg):
        print("\n------------------------------------------")
        print("Algorithm: ", alg)

        if alg == "naive_bayes":
            model = naive_bayes.GaussianNB()
        elif alg == "decision_tree":
            model = tree.DecisionTreeClassifier(max_depth=5, criterion="gini", max_features="sqrt", min_samples_leaf=2, min_samples_split=3)
        elif alg == "k_nearest_neighbor":
            model = neighbors.KNeighborsClassifier(weights="uniform", algorithm="auto", n_neighbors=5, leaf_size=5)
        elif alg == "logistic":
            model = linear_model.LogisticRegression(C=1, fit_intercept=True, multi_class="auto", solver="lbfgs", tol=0.0001, warm_start=True)
        elif alg == "random_forest":
            model = ensemble.RandomForestClassifier(max_depth=5, n_estimators=10, min_samples_leaf=2, min_samples_split=3)
        elif alg == "support_vector_machine":
            model = svm.SVC(C=50, gamma=0.01, kernel="rbf")
        elif alg == "linear_discriminant_analysis":
            model = discriminant_analysis.LinearDiscriminantAnalysis(solver="lsqr", tol=0.0001)
        elif alg == "gradient_boosting":
            model = ensemble.GradientBoostingClassifier(loss="deviance", learning_rate=0.4, min_samples_leaf=100, n_estimators=400, max_features=0.3, max_depth=28)
        else:
            raise NameError("\n\n\nInvalid algorithm passed. Algorithm passed is {}\nThe possible algorithms are {}".format(alg, ALGORITHMS+["neural_network"+"all"]))

        model.fit(np.array(self.x_train), np.array(self.y_train))
        return model

    def accuracy(self, model, alg, hist=None):
        y_predicted = model.predict(np.array(self.x_test2))

        predict = pd.DataFrame()
        predict["PassengerId"] = test2["PassengerId"]
        predict["Survived"] = y_predicted.round().astype(int)
        
        if alg == "neural_network":
            score = model.evaluate(np.array(self.x_test_nn), np.array(self.y_test_nn), verbose=0)
            loss = round(score[0]*100, 2)
            acc = round(score[1]*100, 2)

            print("Loss: {}%".format(loss))
            print("Accuracy: {}%\n".format(acc))

            for key, val in hist.items():
                print("{}: {:.2%}".format(key, sum(val)/len(val)))
            
            print("\n")

        if not REAL_PREDS:
            predict["Survived Floats"] = y_predicted.round(3)
            predict["Survived Actual"] = self.y_test2

            check = []
            for row in predict.iloc:
                if row["Survived Actual"] == row["Survived"]:
                    check.append(1)
                else:
                    check.append(0)

            predict["Correct"] = check
            fscore = round(100*metrics.f1_score(self.y_test2, predict.Survived, average="weighted"), 2)
            print("F-score: {}%".format(fscore))
            print("Accuracy: {:.2%}".format(metrics.accuracy_score(self.y_test2, predict.Survived)))
            print("Tested Accuracy: {:.0%}".format(sum(check)/len(check)))
            if alg != "neural_network": print("Score: {:.2%}".format(model_selection.cross_val_score(model, data[ALL_FEATURES], data["Survived"], cv=5).mean()))
            if ALGORITHM == "all": return (fscore, predict["Survived"])
        
        if ALGORITHM != "all":
            predict.to_csv("pred4.csv".format(ALGORITHM), index=False)

        return predict["Survived"]

    def pred(self, predictions, fscores=None):
        print("\n------------------------------------------")

        predict = pd.DataFrame()
        predict["PassengerId"] = test2["PassengerId"]
        predict["Survived"] = predictions.round().astype(int)
        
        if not REAL_PREDS:
            predict["Survived Floats"] = predictions
            predict["Survived Actual"] = self.y_test2

            check = []
            for row in predict.iloc:
                if row["Survived Actual"] == row["Survived"]:
                    check.append(1)
                else:
                    check.append(0)

            predict["Correct"] = check
            print("Overall Tested Accuracy: {:.0%}".format(sum(check)/len(check)))
            best = max(zip(fscores.values(), fscores.keys()))
            print("Best F1-score is {}% with {}".format(best[0], best[1]))
            print("All test scores: {}".format({key: val for key, val in sorted(fscores.items(), key = lambda ele: ele[1], reverse = True)}))
            
        predict.to_csv("pred4.csv", index=False)

titanic(ALL_FEATURES)

end = datetime.now()
time = end-start
print("Time taken:", time.total_seconds(), "seconds")
print("------------------------------------------")