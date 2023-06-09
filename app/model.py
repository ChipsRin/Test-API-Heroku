# -*- coding: UTF-8 -*-
import pickle
import gzip

# 載入Model
with gzip.open('app/model/xgboost.pgz', 'r') as f:
    xgboostModel = pickle.load(f)


def predict(input):
    pred=xgboostModel.predict(input)[0]
    print(pred)
    return pred