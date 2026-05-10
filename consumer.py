import csv

file = open("results.csv", "a", newline="")
writer = csv.writer(file)

from kafka import KafkaConsumer
import json
import pickle
import pandas as pd

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

print("Model loaded. Waiting for data...\n")

# Create Kafka consumer
consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Read messages
for message in consumer:
    data = message.value

    # Convert to DataFrame
    df = pd.DataFrame([data])

    # Predict
    prediction = model.predict(df)

    if prediction[0] == 0:
     print("Normal Transaction")
     writer.writerow(["Normal"])
     file.flush()  
else:
    print("🚨 FRAUD DETECTED 🚨")
    writer.writerow(["Fraud"])
    file.flush()   