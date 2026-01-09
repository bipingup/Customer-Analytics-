import json
import streamlit as st
import time 
from confluent_kafka import Producer
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
producer = Producer(conf)

st.title("Euron Big DATA Customer Click Analytics")
user_id = st.number_input("user id",min_value=1,max_value=100000,step=1)
activity = st.selectbox("activity",["view_product","add_to_cart","checkout","search","whishlist","purchase"])
product = st.selectbox("product",["laptop","mobile","tablet","desktop","accessories","smartwatch","headphones","camera"])
def send_event():
    event = {
    "user_id": user_id,
    "activity": activity,
    "product": product,
    "timestamp": int(time.time())
    }
    producer.produce(KAFKA_TOPIC,key=str(user_id),value=json.dumps(event))
    producer.flush()
    st.success(f"Event sent to Kafka topic!: {event}")

if st.button("send data"):
    send_event()