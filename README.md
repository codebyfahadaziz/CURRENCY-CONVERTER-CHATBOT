# CURRENCY-CONVERTER-CHATBOT
💱 Flask Currency Converter Webhook for Dialogflow
📌 Overview
This project is a Flask-based webhook that connects Dialogflow to a real-time currency exchange API.
It listens to POST requests from Dialogflow, extracts the source currency, target currency, and amount,
and responds with the converted value using the ExchangeRate-API.

Perfect for building a voice assistant or chatbot that can instantly answer currency conversion queries like:

"Convert 500 GBP to INR"
"How much is 100 USD in EUR?"

✨ Features
🔹 Real-time exchange rates from ExchangeRate-API.

🔹 Case-insensitive currency handling (usd, USD, Usd all work).

🔹 Handles Dialogflow’s unit-currency and currency-name entities directly.

🔹 Graceful error messages for missing or invalid parameters.

🔹 Simple and easy-to-deploy Flask app.

🛠 Requirements
Python 3.7+

Flask

Requests

📥 Installation
1️⃣ Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/currency-converter-webhook.git
cd currency-converter-webhook
🖼 Flow Diagram.
flowchart TD
    A[User Input in Chatbot/Dialogflow] --> B[Dialogflow Extracts Parameters]
    B --> C[Dialogflow Sends JSON Request to Flask Webhook]
    C --> D[Flask Parses Amount, Source, Target]
    D --> E[Flask Calls ExchangeRate-API for Conversion Rate]
    E --> F[API Returns Conversion Rate]
    F --> G[Flask Calculates Converted Amount]
    G --> H[Flask Sends JSON Response to Dialogflow]
    H --> I[Dialogflow Displays Result to User]
