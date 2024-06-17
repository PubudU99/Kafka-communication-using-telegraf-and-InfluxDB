import time
import json
import random
from kafka import KafkaProducer


def random_temp_cels():
    return round(random.uniform(-10, 50), 1)

def random_humidity():
    return round(random.uniform(0, 100), 1)

def random_voltage():
    return round(random.uniform(110, 240), 1)

def random_current():
    return round(random.uniform(0, 30), 1)

def get_json_data():
    data = {}

    data["temperature"] = random_temp_cels()
    data["humidity"] = random_humidity()
    data["voltage"] = random_voltage()
    data["current"] = random_current()

    return json.dumps(data) 

def main():
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

    for _ in range(20000):
        json_data = get_json_data()
        producer.send('smart_city_sensor_data', bytes(f'{json_data}', 'UTF-8'))
        print(f"Sensor data is sent: {json_data}")
        time.sleep(5)


if __name__ == "__main__":
    main()

