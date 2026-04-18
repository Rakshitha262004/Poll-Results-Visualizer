import pandas as pd
import numpy as np

def generate_data(file_path="data/poll_data.csv"):
    np.random.seed(42)
    n = 500

    data = pd.DataFrame({
        "Respondent_ID": range(1, n+1),
        "Region": np.random.choice(["North", "South", "East", "West"], n),
        "Age_Group": np.random.choice(["18-25", "26-35", "36-50"], n),
        "Option": np.random.choice(["Product A", "Product B", "Product C"], n),
        "Date": pd.date_range(start="2024-01-01", periods=n, freq='D')
    })

    data.to_csv(file_path, index=False)
    print("✅ Dataset generated!")