from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "7f1ed54dae81edef1fa42b40"

def fetch_conversion_factor(source_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{source_currency}"
    response = requests.get(url)
    data = response.json()
    return data.get('conversion_rates', {}).get(target_currency, None)

@app.route("/", methods=["POST"])
def index():
    try:
        data = request.get_json()
        print("Incoming JSON:", data)

        parameters = data.get('queryResult', {}).get('parameters', {})

        # Extract from your JSON (unit-currency and currency-name)
        unit_currency = parameters.get('unit-currency', {})
        source_currency = unit_currency.get('currency')
        amount = unit_currency.get('amount')

        currency_name_list = parameters.get('currency-name', [])
        target_currency = currency_name_list[0] if currency_name_list else None

        # Convert to uppercase to make it case-insensitive
        if source_currency:
            source_currency = source_currency.upper()
        if target_currency:
            target_currency = target_currency.upper()

        # Validate
        if not source_currency or amount is None or not target_currency:
            return jsonify({
                "fulfillmentText": f"Missing parameters. Raw parameters: {parameters}"
            })

        # Fetch rate
        cf = fetch_conversion_factor(source_currency, target_currency)
        if cf is None:
            return jsonify({
                "fulfillmentText": f"Conversion rate from {source_currency} to {target_currency} not found."
            })

        # Calculate
        final_amount = amount * cf
        return jsonify({
            "fulfillmentText": f"{amount} {source_currency} is {final_amount:.2f} {target_currency}"
        })

    except Exception as e:
        return jsonify({"fulfillmentText": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
