import pandas as pd
import pickle
import tabpy_client as tabpy


def predict_property_price(years, minutes, sqrm, distance, renovate, express,
                           rooms_1k, rooms_1ldk, rooms_1r, rooms_2k, rooms_2ldk, rooms_3ldk):
    abs_model_path = "/Users/kobayashisatoshi/Documents/GitHub/chuo-line-property-price/data/property_price_model.sav"
    loaded_model = pickle.load(open(abs_model_path, "rb"))
    x = pd.DataFrame({
        "years": years,
        "minutes": minutes,
        "sqrm": sqrm,
        "distance": distance,
        "renovate": renovate,
        "express": express,
        "rooms_1K": rooms_1k,
        "rooms_1LDK": rooms_1ldk,
        "rooms_1R": rooms_1r,
        "rooms_2K": rooms_2k,
        "rooms_2LDK": rooms_2ldk,
        "rooms_3LDK": rooms_3ldk,
    })

    # 予測
    predict = loaded_model.predict(x)

    return predict.tolist()


if __name__ == "__main__":
    client = tabpy.Client("http://localhost:9004/")

    client.deploy('price_predict', predict_property_price, 'Predict property price', override=True)

    print(client.get_endpoints()['price_predict'])

