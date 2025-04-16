from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual API URL for exchange rates
API_URL = "https://api.exchangerate-api.com/v4/latest/"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['GET'])
def convert_currency():
    # Retrieve query parameters for currency conversion
    from_currency = request.args.get('from_currency').upper()
    to_currency = request.args.get('to_currency').upper()
    amount = float(request.args.get('amount'))

    # Validate the currencies
    if not from_currency or not to_currency:
        return jsonify({"error": "Invalid currency codes!"})

    try:
        # Fetch exchange rates from the API
        response = requests.get(f"{API_URL}{from_currency}")
        data = response.json()

        if response.status_code != 200 or 'rates' not in data:
            return jsonify({"error": "Failed to fetch exchange rates"})

        # Get the exchange rate for the requested target currency
        exchange_rate = data['rates'].get(to_currency)

        if not exchange_rate:
            return jsonify({"error": f"Exchange rate for {to_currency} not found."})

        # Perform the conversion
        converted_amount = amount * exchange_rate

        # Return the conversion result as a JSON response
        return jsonify({
            "from_currency": from_currency,
            "to_currency": to_currency,
            "amount": amount,
            "converted_amount": round(converted_amount, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
