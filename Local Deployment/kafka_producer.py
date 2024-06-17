from kafka import KafkaProducer
import json
import time
import random

# Generating sample sensor data
def generate_sensor_data():
    return {
        "sensor_id": random.randint(1, 10),
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 50.0), 2),
        "timestamp": int(time.time())
    }

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Generate and send data to Kafka topic
try:
    while True:
        sensor_data = generate_sensor_data()
        producer.send('sensor_data', sensor_data)
        print(f"Sent: {sensor_data}")
        time.sleep(1)  # Send data every second
except KeyboardInterrupt:
    print("Stopped sending data.")
finally:
    producer.close()
