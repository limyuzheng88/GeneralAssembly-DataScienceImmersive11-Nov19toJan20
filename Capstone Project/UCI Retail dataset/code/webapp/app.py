# app.py
from flask import Flask, request, jsonify, render_template, url_for
import pickle
import pandas as pd
import numpy as np


app = Flask(__name__, static_url_path='', 
            static_folder='templates',
            template_folder='templates')

data_rec = pickle.load(open('./static/pickle_files/data_rec.pkl', 'rb'))
lookup_urls_price = pickle.load(open('./static/pickle_files/lookup_urls_price.pkl', 'rb'))
recs = pickle.load(open('./static/pickle_files/recs.pkl', 'rb'))
mba_associations = pickle.load(open('./static/pickle_files/mba_associations.pkl', 'rb'))

@app.route("/product", methods=["GET"])
def product():
    stockcode = request.args.get('stockcode') #takes in inputted value of stockcode, to show its image
    lup = lookup_urls_price #table containing all 3 info
    return render_template("product.html",stockcode=stockcode,lookup_urls_price=lup)

@app.route("/cid", methods=["POST"])
def customer():
    customer_id = int(request.form['customer_id']) #takes in inputted value of customer id, to show recommendations for him/her
    customer_recs = recs.iloc[customer_id] #recommendations for customer
    n_customers = len(recs)
    lup = lookup_urls_price #table containing all 3 info
    return render_template("customer.html",customer_id=customer_id,customer_recs=customer_recs,n_customers=n_customers,lookup_urls_price=lup)


@app.route("/cart", methods=["GET"])
def cart():
    stockcode = request.args.get('stockcode') #takes in inputted value of stockcode, to show its image
    lup = lookup_urls_price #table containing all 3 info
    assoc = mba_associations
    return render_template("cart.html",stockcode=stockcode,lookup_urls_price=lup, mba_associations = assoc)


@app.route('/')
def index():
    n_customers = len(recs)
    return render_template("index.html",n_customers=n_customers)


if __name__ == '__main__':
    app.run(debug=True, port=5000)