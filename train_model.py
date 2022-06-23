import pandas as pd
import numpy as np

import pickle

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR


if __name__ == "__main__":
    # データのロード
    df = pd.read_csv("./data/property_price_chuo-line.csv")
    # 説明変数
    x = df.loc[:, ["years", "minutes", "sqrm", "distance", "renovate", "express", "rooms"]]
    # 目的変数
    y = df["price"]

    # ダミー変数化
    x = pd.get_dummies(x)

    # hold-outで7:3分割
    x_train, x_valid, y_train, y_valid = train_test_split(x, y, train_size=0.3, random_state=0)
    print(f"training data: {x_train.shape} {y_train.shape}")
    print(f"test data    : {x_valid.shape} {y_valid.shape}")

    # モデルの学習
    model = RandomForestRegressor()
    model.fit(x_train, y_train)

    train_score = model.score(x_train, y_train)
    valid_score = model.score(x_valid, y_valid)

    print(f"train score: {train_score}")
    print(f"valid score: {valid_score}")

    # models = {
    #     "Linear": LinearRegression(),
    #     "Logistic": LogisticRegression(),
    #     "RF": RandomForestRegressor(),
    #     "SVM": SVR(),
    # }
    #
    # for name, model in models.items():
    #     print("-" * 10)
    #     print(name)
    #
    #     model.fit(x_train, y_train)
    #     train_score = model.score(x_train, y_train)
    #     valid_score = model.score(x_valid, y_valid)
    #
    #     print(f"train score: {train_score}")
    #     print(f"valid score: {valid_score}")
    #
    #     print("-" * 10)

    # 特徴量の重要度
    print("-" * 10)
    print("Feature importance")
    for name, importance in zip(model.feature_names_in_, model.feature_importances_):
        print(f"{name} : {importance}")

    # 推論
    predict = model.predict(x)
    results = pd.concat([df, pd.DataFrame({"predict": predict})], axis=1)
    results.to_csv("./data/prediction_property_price_chuo-line.csv", index=False)

    # モデルの保存
    pickle.dump(model, open("./data/property_price_model.sav", "wb"))

