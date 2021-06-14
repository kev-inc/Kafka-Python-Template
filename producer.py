from kafka import KafkaProducer
import json
from data import new_user_created
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers=['127.0.0.1:9092'],
    value_serializer=json_serializer
)

if __name__ == "__main__":
    while True:
        user_data = new_user_created()
        print(user_data)
        producer.send("new_user_data", user_data)
        time.sleep(5)