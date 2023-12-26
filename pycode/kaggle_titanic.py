import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import pandas as pd
from tensorflow import keras
from sklearn import model_selection, svm, tree, linear_model, neighbors, ensemble, discriminant_analysis, naive_bayes
import numpy as np
from datetime import datetime

start = datetime.now()
# possible activations are:
# ACTIVATIONS = ["tanh", "softsign", "selu", "elu", "relu", "sigmoid", "softplus", "softmax"]
ACTIVATION = "tanh"
ALGORITHMS = ["naive_bayes", "decision_tree", "k_nearest_neighbor",\
    "support_vector_machine", "linear_discriminant_analysis",\
    "logistic", "random_forest", "gradient_boosting"] #"neural_network", "all"
NUMBER_OF_ALGORITHMS = len(ALGORITHMS)+1
ALGORITHM = "all"
NEURONS = [60, 30, 10, 5, 2, 1]
EPOCHS = 16
DROPOUT = 0.13

data = pd.read_csv("titanic_data/train2.csv")
# test2 = pd.read_csv("titanic_data/test2.csv")
train_nn, test_nn = model_selection.train_test_split(data[:791], test_size=0.2)
train = data[:791]
test2 = data[791:]
ALL_FEATURES = ["Gender", "Pclass", "SibSp", "Parch"]

class titanic:
    def __init__(self, feats):
        FEATURES = feats
        self.feats = feats
        print("\n------------------------------------------")
        print("Features: {}".format(self.feats))

        self.x_train_nn, self.y_train_nn = train_nn[FEATURES], train_nn["Survived"]
        self.x_test_nn, self.y_test_nn = test_nn[FEATURES], test_nn["Survived"]
        self.x_test2, self.y_test2 = test2[FEATURES], test2["Survived"]
        self.x_train, self.y_train = train[FEATURES], train["Survived"]

        if ALGORITHM == "neural_network":
            model = self.neural_network()
            self.accuracy(model, ALGORITHM)
        elif ALGORITHM == "all":
            model = self.neural_network()
            preds = self.accuracy(model, "neural_network")
            
            for algs in ALGORITHMS:
                model = self.other(algs)
                preds += self.accuracy(model, algs)
            
            self.pred(preds/NUMBER_OF_ALGORITHMS)
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
        model.add(keras.layers.Dense(NEURONS[1], activation=ACTIVATION))
        model.add(keras.layers.Dropout(DROPOUT))
        model.add(keras.layers.Dense(NEURONS[2], activation=ACTIVATION))
        model.add(keras.layers.Dropout(DROPOUT))
        model.add(keras.layers.Dense(NEURONS[3], activation=ACTIVATION))
        model.add(keras.layers.Dropout(DROPOUT))
        model.add(keras.layers.Dense(NEURONS[4], activation=ACTIVATION))
        model.add(keras.layers.Dropout(DROPOUT))
        model.add(keras.layers.Dense(NEURONS[5], activation="sigmoid"))

        model.compile(loss="mean_absolute_error", optimizer="adam", metrics=["accuracy"])
        model.fit(np.array(self.x_train_nn), np.array(self.y_train_nn), epochs=EPOCHS)
        return model

    def other(self, alg):
        print("\n------------------------------------------")
        print("Algorithm: ", alg)

        if alg == "naive_bayes":
            model = naive_bayes.GaussianNB()
        elif alg == "decision_tree":
            model = tree.DecisionTreeClassifier()
        elif alg == "k_nearest_neighbor":
            model = neighbors.KNeighborsClassifier()
        elif alg == "logistic":
            model = linear_model.LogisticRegression()
        elif alg == "random_forest":
            model = ensemble.RandomForestClassifier()
        elif alg == "support_vector_machine":
            model = svm.SVC()
        elif alg == "linear_discriminant_analysis":
            model = discriminant_analysis.LinearDiscriminantAnalysis()
        elif alg == "gradient_boosting":
            model = ensemble.GradientBoostingClassifier()
        else:
            raise NameError("\n\n\nInvalid algorithm passed. Algorithm passed is {}\nThe possible algorithms are {}".format(alg, ALGORITHMS+["neural_network"+"all"]))

        model.fit(np.array(self.x_train), np.array(self.y_train))
        return model

    def accuracy(self, model, alg):
        y_predicted = model.predict(np.array(self.x_test2))

        predict = pd.DataFrame()
        predict["PassengerId"] = test2["PassengerId"]
        predict["Survived Actual"] = self.y_test2
        predict["Survived"] = y_predicted.round().astype(int)
        predict["Survived Floats"] = y_predicted.round(3)

        check = []
        for row in predict.iloc:
            if row["Survived Actual"] == row["Survived"]:
                check.append(1)
            else:
                check.append(0)

        predict["Correct"] = check
        
        if alg == "neural_network":
            score = model.evaluate(np.array(self.x_test_nn), np.array(self.y_test_nn))
            loss = round(score[0]*100, 2)
            acc = round(score[1]*100, 2)

            print("Loss: {}%".format(loss))
            print("Accuracy: {}%".format(acc))
        
        if ALGORITHM != "all":
            predict.to_csv("titanic_data/predictions.csv", index=False)
        print("Tested Accuracy: {}%".format(round(100*sum(check)/len(check), 2)))

        return predict["Survived"]

    def pred(self, predictions):
        print("\n------------------------------------------")

        predict = pd.DataFrame()
        predict["PassengerId"] = test2["PassengerId"]
        predict["Survived Actual"] = self.y_test2
        predict["Survived"] = predictions.round().astype(int)
        predict["Survived Floats"] = predictions

        check = []
        for row in predict.iloc:
            if row["Survived Actual"] == row["Survived"]:
                check.append(1)
            else:
                check.append(0)

        predict["Correct"] = check
        
        predict.to_csv("titanic_data/predictions.csv", index=False)
        print("Overall Tested Accuracy: {}%".format(100*sum(check)/len(check)))

titanic(ALL_FEATURES)

end = datetime.now()
time = end-start
print("Time taken:", time.total_seconds(), "seconds")
print("------------------------------------------")