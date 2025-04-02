import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def cond(row):
    row["Condition_N"] = (row["Condition1"] == "N")+(row["Condition2"] == "N")
    row["Condition_R"] = (row["Condition1"] == "R")+(row["Condition2"] == "R")
    row["Condition_P"] = (row["Condition1"] == "P")+(row["Condition2"] == "P")
    return row

def process(data:pd.DataFrame):
    # print(data.isnull().sum()[data.isnull().sum()!=0]*100/len(data))
    # print("\n\n\n")
    data = data.drop(["Fence", "FireplaceQu", "MiscFeature", "LandContour", "RoofMatl", "Exterior1st", "MasVnrType", "Exterior2nd", "MasVnrArea", "Utilities", "HouseStyle", "BsmtUnfSF", "BsmtFinSF2", "BsmtFinSF1"], axis=1)

    data["PoolQC"] = data["PoolQC"].notnull().astype('int')
    data[["TotalBsmtSF", "BsmtFullBath", "BsmtHalfBath", "GarageArea", "GarageCars"]] = data[["TotalBsmtSF", "BsmtFullBath", "BsmtHalfBath", "GarageArea", "GarageCars"]].fillna(0)
    data["KitchenQual"] = data["KitchenQual"].fillna("Po")
    data["Functional"] = data["Functional"].fillna("Typ")
    data["MSZoning"] = data["MSZoning"].fillna("RL")

    data.loc[data["SaleCondition"] == "AdjLand", "SaleCondition"] = "Alloca"
    data["SaleType"] = data["SaleType"].map({"WD":"W", "CWD":"W", "VWD":"W", "Oth":"O", "New":"N", "COD":"D", "Con":"C", "ConLD":"C", "ConLI":"C", "ConLw":"C"}).fillna("W")

    data["MSSubClass"] = data["MSSubClass"].map({20:1, 30:1, 40:1, 45:1.5, 50:1.5, 60:2, 70:2, 75:2.5, 80:3, 85:3, 90:3, 120:1, 150:1.5, 160:2, 180:3, 190:4})
    data["MSSubClass"] = data["MSSubClass"].astype(int)

    data["Street"] = data["Street"].map({"Grvl":0, "Pave":1})
    data["Alley"] = data["Alley"].fillna("None").map({"None":0, "Grvl":1, "Pave":2})
    data["Strally"] = data["Street"]+data["Alley"]
    data["Strally"] = data["Strally"].astype(int)
    data = data.drop(["Street", "Alley"], axis=1)

    data["LotShape"] = data["LotShape"].map({"Reg":0, "IR1":1, "IR2":2, "IR3":2})
    data["LotShape"] = data["LotShape"].astype(int)

    data["LotConfig"] = data["LotConfig"].map({"Inside":0, "Corner":1, "CulDSac":2, "FR2":3, "FR3":3})
    data["LotConfig"] = data["LotConfig"].astype(int)

    data["LandSlope"] = data["LandSlope"].map({"Gtl":0, "Mod":1, "Sev":1})
    data["LotConfig"] = data["LotConfig"].astype(int)

    data["LotFrontage"] = data["LotFrontage"].fillna(0)

    data["BldgType"] = data["BldgType"].map({"1Fam":1, "Duplex":2, "2fmCon":2, "TwnhsE":3, "Twnhs":3})
    data["BldgType"] = data["BldgType"].astype(int)

    data["RoofStyle"] = data["RoofStyle"].map({"Gable":"G", "Hip":"H", "Flat":"U", "Gambrel":"U", "Mansard":"U", "Shed":"U"})

    data["Condition1"] = data["Condition1"].map({"Artery":"R", "Feedr":"R", "Norm":"N", "RRNn":"R", "RRNe":"R", "RRAn":"R", "RRAe":"R", "PosA":"P", "PosN":"P"})
    data["Condition2"] = data["Condition2"].map({"Artery":"R", "Feedr":"R", "Norm":"N", "RRNn":"R", "RRNe":"R", "RRAn":"R", "RRAe":"R", "PosA":"P", "PosN":"P"})

    data["ExterQual"] = data["ExterQual"].map({"Ex":5, "Gd":4, "TA":3, "Fa":2, "Po":1})
    data["ExterCond"] = data["ExterCond"].map({"Ex":5, "Gd":4, "TA":3, "Fa":2, "Po":1})
    data["ExterCond"] = (data["ExterCond"]+data["ExterQual"])/2
    data["ExterCond"] = data["ExterCond"].astype(int)

    data[["BsmtQual", "BsmtCond", "BsmtExposure", "BsmtFinType1", "BsmtFinType2"]] = data[["BsmtQual", "BsmtCond", "BsmtExposure", "BsmtFinType1", "BsmtFinType2"]].fillna("None")
    data["BsmtQual"] = data["BsmtQual"].map({"Ex":5, "Gd":4, "TA":3, "Fa":2, "Po":1, "None":0})
    data["BsmtCond"] = data["BsmtCond"].map({"Ex":5, "Gd":4, "TA":3, "Fa":2, "Po":1, "None":0})
    data["BsmtExposure"] = data["BsmtExposure"].map({"None":0, "No":1, "Mn":2, "Av":3, "Gd":4})
    data["BsmtFinType1"] = (data["BsmtFinType1"].map({"None":0, "Unf":1, "LwQ":2, "Rec":3, "BLQ":4, "ALQ":5, "GLQ":6})+data["BsmtFinType2"].map({"None":0, "Unf":1, "LwQ":2, "Rec":3, "BLQ":4, "ALQ":5, "GLQ":6}))/2
    data["BsmtCond"] = (data["BsmtCond"]+data["BsmtQual"]+data["BsmtExposure"]+data["BsmtFinType1"])/4
    data["BsmtCond"] = data["BsmtCond"].astype(int)
    data = data.drop(["BsmtQual", "BsmtExposure", "BsmtFinType1", "BsmtFinType2"], axis=1)

    data["Heating"] = data["Heating"].map({"GasA":1})
    data["Heating"] = data["Heating"].fillna(0).astype(int)

    data["HeatingQC"] = data["HeatingQC"].map({"Ex":5, "Gd":4, "TA":3, "Fa":2, "Po":1})
    data["HeatingQC"] = data["HeatingQC"].astype(int)

    data["KitchenQual"] = data["KitchenQual"].map({"Ex":5, "Gd":4, "TA":3, "Fa":2, "Po":1})
    data["KitchenQual"] = data["KitchenQual"].astype(int)

    data["GarageCond"] = data["GarageCond"].map({"Ex":5, "Gd":4, "TA":3, "Fa":2, "Po":1}).fillna(0)
    data["GarageQual"] = data["GarageQual"].map({"Ex":5, "Gd":4, "TA":3, "Fa":2, "Po":1}).fillna(0)
    data["GarageCond"] = (data["GarageCond"]+data["GarageQual"])/2

    data["GarageFinish"] = data["GarageFinish"].map({"Unf":1, "RFn":2, "Fin":3})
    data["GarageFinish"] = data["GarageFinish"].fillna(0).astype(int)

    data["Electrical"] = data["Electrical"].map({"Mix":5, "SBrkr":4, "FuseA":3, "FuseF":2, "FuseP":1})
    data["Electrical"] = data["Electrical"].fillna(3)
    data["Electrical"] = data["Electrical"].astype(int)

    data["OverallCond"] = (data["OverallCond"] + data["OverallQual"])/2
    data["OverallCond"] = data["OverallCond"].astype(int)

    data["CentralAir"] = data["CentralAir"].map({"N":0, "Y":1})
    data["PavedDrive"] = data["PavedDrive"].map({"N":0, "P":1, "Y":2})

    data["Functional"] = data["Functional"].map({"Typ":4, "Min2":3, "Min1":3, "Mod":2, "Maj1":1, "Maj2":1, "Sev":1})
    data["Functional"] = data["Functional"].astype(int)

    data["YearBin"] = pd.qcut(data["YearBuilt"], 10, labels=range(1, 11))
    data["YrSold"] = data["YrSold"]-2008
    data["YearReModBin"] = pd.qcut(data["YearRemodAdd"], 5, labels=range(1, 6))
    data["GarageYrBlt"] = pd.qcut(data["GarageYrBlt"], 5, labels=range(1, 6)).cat.add_categories(7).fillna(7)
    data = data.drop(["YearBuilt", "YearRemodAdd", "OverallQual"], axis=1)

    data["Condition_N"] = [0]*data.shape[0]
    data["Condition_R"] = [0]*data.shape[0]
    data["Condition_P"] = [0]*data.shape[0]
    data.apply(cond, axis=1)
    data = data.drop(["Condition1", "Condition2"], axis=1)

    data["GarageType"] = data["GarageType"].fillna("None")
    oh_columns = ["Neighborhood", "RoofStyle", "Foundation", "GarageType", "MSZoning", "SaleType", "SaleCondition"]
    encoded_features = []
    for feats in oh_columns:
        encoded_feat = OneHotEncoder().fit_transform(data[feats].values.reshape(-1, 1)).toarray()
        n = data[feats].nunique()
        cols = ['{}_{}'.format(feats, n) for n in range(1, n+1)]
        encoded_df = pd.DataFrame(encoded_feat, columns=cols)
        encoded_df.index = data.index
        encoded_features.append(encoded_df)

    data = pd.concat([data.drop(oh_columns, axis=1), *encoded_features], axis=1)

    data["GarageYrBlt"] = data["GarageYrBlt"].cat.add_categories(0)
    data[["LotFrontage", "GarageYrBlt"]].fillna(0)
    
    return data

def main(drop_cor):
    dtrain = process(pd.read_csv("/Users/advaith/Documents/Advaith/class/pycode/Kaggle/Housing/train.csv"))
    dtest = process(pd.read_csv("/Users/advaith/Documents/Advaith/class/pycode/Kaggle/Housing/test.csv"))

    cols = dtrain.dtypes[dtrain.dtypes == 'category'].index
    dtrain[cols] = dtrain[cols].astype('int64')
    dtest[cols] = dtest[cols].astype('int64')

    if drop_cor>0:
        cor = dtrain.corr()["SalePrice"]
        droppedcols = cor[abs(cor) < drop_cor].index.tolist()
        droppedcols.remove("Id")
        dtrain = dtrain.drop(droppedcols, axis=1)
        dtest = dtest.drop(droppedcols, axis=1)
    
    return dtrain, dtest
