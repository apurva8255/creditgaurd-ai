import pickle
import pandas as pd

model = pickle.load(open("risk_model.pkl", "rb"))

def predict_risk(customer_data):
    df = pd.DataFrame([customer_data])
    risk_prob = model.predict_proba(df)[0][1]
    return round(risk_prob * 100, 2)
def intervention_action(score):
    if score < 30:
        return "No action required"
    elif score < 70:
        return "Send EMI reminder"
    else:
        return "Offer payment holiday or restructuring"
