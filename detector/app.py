from kafka import KafkaConsumer, KafkaProducer

import json
import os


def is_suspicious(transaction: dict) -> bool:
    return transaction["amount"] >= 900


KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")

LEGIT_TOPIC = os.environ.get("LEGIT_TOPIC")
FRAUD_TOPIC = os.environ.get("FRAUD_TOPIC")

if __name__ == "__main__":
    consumer = KafkaConsumer(
        TRANSACTIONS_TOPIC,
        bootstrap_servers=KAFKA_BROKER_URL,
        value_deserializer=lambda value: json.loads(value), # TODO https://github.com/mallory-jpg/kafka-fraud/issues/1 'no brokers available' -- api version? 
    )
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        api_version=(1, 3, 5),
        value_serializer=lambda value: json.dumps(value).encode()
    )
    for message in consumer:
        transaction: dict = message.value
        topic = FRAUD_TOPIC if is_suspicious(transaction) else LEGIT_TOPIC
        producer.send(topic, value=transaction)
        print(topic, transaction)
