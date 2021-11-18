from time import sleep
import os
from transactions import create_random_transaction
import json
from kafka import KafkaProducer #TODO https://github.com/mallory-jpg/kafka-fraud/issues/2 no module found 'kafka'

KAFKA_VERSION = os.environ.get("KAFKA_VERSION")
KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
# float(os.environ.get("TRANSACTIONS_PER_SECOND"))
TRANSACTIONS_PER_SECOND = 1000
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND

if __name__ == "__main__":
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        api_version=KAFKA_VERSION,
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    # infinite loop
    while True:
        transaction: dict = create_random_transaction()
        producer.send(TRANSACTIONS_TOPIC, value=transaction)
        message: str = json.dumps(transaction)
        producer.send(TRANSACTIONS_TOPIC, value=transaction)
        print(transaction) # DEBUG
        sleep(SLEEP_TIME)
    