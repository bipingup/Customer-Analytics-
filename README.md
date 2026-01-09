# 📊 Euron Big DATA: Real-Time Customer Behavior Analytics

This project is a complete end-to-end Data Engineering pipeline that captures real-time customer interactions (clicks, views, purchases) and visualizes them on a live dashboard.

## 🔗 Live Project Links
- **Producer App:** [https://customerpro.streamlit.app/](https://customerpro.streamlit.app/)
- **Analytics Dashboard:** [https://customeranalytic.streamlit.app/](https://customeranalytic.streamlit.app/)

## 🚀 The Architecture (How it Works)

The pipeline is built using the **K-M-S Stack** (Kafka, MongoDB, Streamlit):

1. **Producer (Data Generation):** - A dedicated Streamlit interface where users can simulate customer actions (e.g., viewing a laptop, adding a smartwatch to the cart).
   - Every "send data" click triggers a message sent to a **Confluent Kafka Cloud** topic.
   
2. **Processor (Data Ingestion):**
   - A Python-based Kafka Consumer (Processor) runs in the background.
   - It listens for incoming events on the Kafka topic and stores them in a **MongoDB Atlas** NoSQL database for persistence.

3. **Analytics Dashboard (Visualization):**
   - Another Streamlit application that acts as the frontend.
   - It fetches real-time data from MongoDB and displays Key Metrics (Total Users, Activities) and Charts (Activity Timelines, Product Distribution).

## 🛠️ Tech Stack
- **Language:** Python 3.11
- **Message Broker:** Confluent Kafka (Cloud-native)
- **Database:** MongoDB Atlas
- **Visualization:** Plotly Express & Streamlit
- **Security:** Managed via Streamlit Secrets (for Cloud) and `.env` (for Local)

## 📂 File Structure
- `customer_data_producer.py`: The data entry UI (Producer).
- `customer_data_processor.py`: The bridge between Kafka and MongoDB.
- `customer_analytics.py`: The main analytics dashboard.
- `requirements.txt`: Python dependencies (including `dnspython` for MongoDB SRV support).

## ⚙️ Local Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/bipingup/Customer-Analytics-.git](https://github.com/bipingup/Customer-Analytics-.git)
