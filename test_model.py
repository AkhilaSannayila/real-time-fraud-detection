
import pickle
import pandas as pd

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

print("Model loaded successfully")

# Load dataset
df = pd.read_csv("data/creditcard.csv")

# Take one sample transaction
sample = df.drop("Class", axis=1).iloc[0:1]

# Predict
prediction = model.predict(sample)

if prediction[0] == 0:
    print("Prediction: Normal Transaction")
else:
    print("Prediction: Fraud Transaction")