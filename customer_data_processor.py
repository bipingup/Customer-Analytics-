from confluent_kafka import Consumer
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import json
from datetime import datetime
import logging
import os
from dotenv import load_dotenv

load_dotenv()



conf = {
    'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS'),
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': os.getenv('KAFKA_API_KEY'),
    'sasl.password': os.getenv('KAFKA_SECRET'),
    "group.id": "streamlit_analytics_group",
    "auto.offset.reset": "earliest"
}

KAFKA_TOPIC = "customer_click_data"

# MongoDB connection
uri = os.getenv("MONGO_URI")

def connect_mongo():
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client

def process_messages():
    consumer = Consumer(conf)
    consumer.subscribe([KAFKA_TOPIC])
    mongo_client = connect_mongo()
    db = mongo_client["customer_click_behavior"]
    event_collection = db["click_data"]

    try:
        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                logging.error(f"Consumer error: {msg.error()}")
                continue

            value = json.loads(msg.value().decode('utf-8'))
            value["kafka_metadata"] = {
                "topic": msg.topic(),
                "partition": msg.partition(),
                "offset": msg.offset(),
                "timestamp": datetime.now().isoformat()
            }

            result=event_collection.insert_one(value)
            print(result)

    except KeyboardInterrupt:
        print("Stopping consumer...")

    finally:
        consumer.close()
        mongo_client.close()

            
if __name__ == "__main__":
    process_messages()
