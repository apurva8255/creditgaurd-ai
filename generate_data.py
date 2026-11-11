import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

data = pd.DataFrame({
    "customer_id": range(n),
    "salary_delay_days": np.random.randint(0, 10, n),
    "savings_decline_pct": np.random.uniform(0, 40, n),
    "utility_delay_days": np.random.randint(0, 15, n),
    "loan_app_txn_count": np.random.randint(0, 5, n),
    "atm_withdrawals": np.random.randint(0, 10, n),
})

# Create risk label
risk_score = (
    data["salary_delay_days"] * 2 +
    data["savings_decline_pct"] * 1.5 +
    data["utility_delay_days"] * 1.8 +
    data["loan_app_txn_count"] * 5 +
    data["atm_withdrawals"] * 2
)

data["default_risk"] = (risk_score > 80).astype(int)

data.to_csv("transactions.csv", index=False)
print("Synthetic data created.")
