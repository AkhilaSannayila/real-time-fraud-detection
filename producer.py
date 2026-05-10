from kafka import KafkaProducer
import pandas as pd
import json
import time

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Kafka Producer started...\n")

# Load dataset
df = pd.read_csv("data/creditcard.csv")

# Remove target column
df = df.drop("Class", axis=1)

# Send transactions
for i in range(20):
    transaction = df.iloc[i].to_dict()

    producer.send('transactions', transaction)
    print(f"Sent transaction {i+1}")

    time.sleep(1)

producer.flush()