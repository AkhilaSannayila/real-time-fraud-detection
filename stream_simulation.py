
import pickle
import pandas as pd
import time

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

print("Model loaded... Starting real-time simulation\n")

# Load dataset
df = pd.read_csv("data/creditcard.csv")

# Remove target column
df = df.drop("Class", axis=1)

# Simulate streaming
for i in range(10):   # change 10 → 100 later
    transaction = df.iloc[i:i+1]

    prediction = model.predict(transaction)

    if prediction[0] == 0:
        print(f"Transaction {i+1}: Normal")
    else:
        print(f"Transaction {i+1}: FRAUD ALERT 🚨")

    time.sleep(1)  # 1 second delay (simulates real-time)