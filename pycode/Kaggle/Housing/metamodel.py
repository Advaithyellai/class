import preprocess
from predict import algorithms, neural_network
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import KFold

ALGS = ['Linear', 'Ridge', 'Lasso', 'K Neighbors', 'Decision Tree', 
         'Random Forest', 'Gradient Boosting', 'Adaboost']
DROP_WEAK = 0
df, dpred = preprocess.main(DROP_WEAK)

FEATS = df.columns.to_list()
FEATS.remove("Id")
FEATS.remove("SalePrice")

x_final = dpred[FEATS]
x_df, y_df = df[FEATS], df["SalePrice"]

metadata = pd.DataFrame()

kf = KFold(5, shuffle=True, random_state=42)
for train, test in kf.split(x_df, y_df):
    y_test = pd.DataFrame()
    x_train, y_train = x_df.iloc[train], y_df.iloc[train]
    x_test, y_test["SalePrice"] = x_df.iloc[test], y_df.iloc[test]
    
    model = neural_network(x_train, y_train)
    y_test["Neural Network"] = model.predict(x_test).reshape((len(y_test)))
    
    for alg in ALGS:
        model = algorithms(alg, x_train, y_train)
        y_test[alg] = model.predict(x_test)
    metadata = pd.concat((metadata, y_test), ignore_index=True)

metadata = metadata.astype(int)
metax, metay = metadata.drop("SalePrice", axis=1), metadata["SalePrice"]
metamodel = GradientBoostingRegressor(n_estimators=250, min_samples_split=4, min_samples_leaf=1, max_depth=4, learning_rate=0.0733)
metamodel.fit(metax, metay)

x_pred = pd.DataFrame()
model = neural_network(x_df, y_df)
x_pred["Neural Network"] = model.predict(x_final).reshape((len(x_final)))

for alg in ALGS:
    model = algorithms(alg, x_df, y_df)
    x_pred[alg] = model.predict(x_final)

finalpred = pd.DataFrame()
finalpred["Id"] = dpred["Id"]
finalpred["SalePrice"] = metamodel.predict(x_pred)
finalpred.to_csv("predictions.csv", index=False)