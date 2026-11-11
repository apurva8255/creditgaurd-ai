import pandas as pd
from xgboost import XGBClassifier
import pickle

data = pd.read_csv("transactions.csv")

X = data.drop(["customer_id", "default_risk"], axis=1)
y = data["default_risk"]

model = XGBClassifier()
model.fit(X, y)

with open("risk_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved.")
