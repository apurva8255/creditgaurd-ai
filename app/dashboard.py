import streamlit as st
from predict import predict_risk, intervention_action

st.title("CreditGuard AI – Risk Dashboard")

salary_delay = st.slider("Salary Delay (days)", 0, 15, 2)
savings_decline = st.slider("Savings Decline (%)", 0, 50, 10)
utility_delay = st.slider("Utility Payment Delay (days)", 0, 20, 3)
loan_apps = st.slider("Loan App Transactions", 0, 10, 1)
atm_withdrawals = st.slider("ATM Withdrawals", 0, 15, 2)

if st.button("Predict Risk"):
    customer = {
        "salary_delay_days": salary_delay,
        "savings_decline_pct": savings_decline,
        "utility_delay_days": utility_delay,
        "loan_app_txn_count": loan_apps,
        "atm_withdrawals": atm_withdrawals
    }

    score = predict_risk(customer)
    action = intervention_action(score)

    st.subheader(f"Risk Score: {score}")
    st.subheader(f"Recommended Action: {action}")
