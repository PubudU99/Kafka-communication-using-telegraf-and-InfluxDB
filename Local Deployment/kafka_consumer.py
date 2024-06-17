from kafka import KafkaConsumer
import json

# Creating a Kafka consumer
consumer = KafkaConsumer(
    'sensor_data', # Topic name
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='sensor_data_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Consume and print data from Kafka topic
try:
    for message in consumer:
        sensor_data = message.value
        print(f"Received: {sensor_data}")
except KeyboardInterrupt:
    print("Stopped consuming data.")
finally:
    consumer.close()
