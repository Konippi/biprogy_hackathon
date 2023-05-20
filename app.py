import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# URL = "https://7hsj87vfpdhh.cybozu.com/k/v1/record.json?app=1&id=2"
# API_TOKEN = "t4O70FRaVB3sD9UdOWCH1xKlaGiBAjziGBYkm37x"

# def get_kintone(url, api_token):
#     """kintoneのレコードを1件取得する関数"""
#     headers = {"X-Cybozu-API-Token": api_token}
#     resp = requests.get(url, headers=headers)
#     return resp

@app.route('/shop', methods=['GET'])
def shop_list():
    # kintoneからselect
    return render_template('shop/list.html')

@app.route('/shop/details', methods=['GET'])
def shop_details():
    return render_template('shop/details.html')

@app.route('/ticket', methods=['GET'])
def ticket_list():
    return render_template('ticket/list.html')

@app.route('/ticket/details', methods=['GET'])
def ticket_details():
    return render_template('ticket/details.html')


if __name__ == '__main__':
    app.run(debug=True, port="5000")