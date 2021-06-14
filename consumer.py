from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "new_user_data",
        bootstrap_servers=['127.0.0.1:9092'],
        auto_offset_reset="earliest",
        group_id="consumer-group-b"
    )
    print("consumer started")
    for msg in consumer:
        print("New User Created! {}".format(json.loads(msg.value)))