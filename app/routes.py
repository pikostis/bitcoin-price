from app import app
from coinbase.wallet.client import Client
import json
from flask import render_template, jsonify

@app.route('/')
def price():
	client = Client('api-user-name', 'api-key')
	price = client.get_spot_price(currency_pair = 'BTC-USD')
	result = price['amount']
	print(result)
	return render_template('index.html', price = result)
	#return jsonify(price)

@app.route('/ajax')
def ajax():
	client = Client('api-user-name', 'api-key')
	price = client.get_spot_price(currency_pair = 'BTC-USD')
	print(price)
	return jsonify(price)