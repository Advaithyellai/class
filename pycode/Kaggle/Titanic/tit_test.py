import pandas as pd
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import model_selection

def algorithms(alg):
    if alg == "all":
        
        bestscore = ["", 0]
        for a in ALGORITHMS:
            if VERBOSE != 0:
                print()
                print()
                print("-----------------")
                print("Algorithm:", a)
                print()

            score = algorithms(a)
            
            if score > bestscore[1]:
                bestscore = [a, score]
        
        print()
        print("-----------------")
        print("Best Algorithm: ", bestscore[0])
        print("Accuracy of: {:.2%}".format(bestscore[1]))
        print("-----------------")
        print()

        return
    elif alg == "logistic_regression":
        model = LogisticRegression()
    elif alg == "linear_discriminant_analysis":
        model = LinearDiscriminantAnalysis()
    elif alg == "decision_tree":
        model = DecisionTreeClassifier()
    elif alg == "naive_bayes":
        model = GaussianNB()
    elif alg == "gradient_boosting":
        model = GradientBoostingClassifier()
    elif alg == "random_forest":
        model = RandomForestClassifier()
    elif alg == "support_vector_machine":
        model = SVC()
    elif alg == "k_nearest_neighbors":
        model = KNeighborsClassifier()
    else:
        raise NameError("Algorithm '{}' not found.".format(alg))

    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    return evaluate(y_test, y_pred)

def evaluate(y_true, y_pred):
    score1 = accuracy_score(y_true, y_pred)
    score2 = precision_recall_fscore_support(y_true, y_pred, average="binary")

    if VERBOSE == 0 and ALGORITHM == "all": return score1

    print("Accuracy: {:.2%}".format(score1))
    for t, s in zip(["Precision", "Recall", "F1 Score", ""], score2):
        if t == "": break
        print("{}: {:.2%}".format(t, s))

    print("-----------------")
    return score1

ALGORITHMS = ["decision_tree", "logistic_regression", "linear_discriminant_analysis",\
              "naive_bayes", "gradient_boosting", "random_forest", "support_vector_machine",\
              "k_nearest_neighbors"] # "all"
ALGORITHM = "all"
FEATS = ["Gender", "Pclass", "Age", "Family"]
VERBOSE = 1

db = pd.read_csv("train.csv")

X = db[FEATS]
X.dropna()
Y = db["Survived"]

x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.3)

print()
print("-----------------")
print("Algorithm:", ALGORITHM)
print()

algorithms(ALGORITHM)