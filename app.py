from flask import Flask, render_template, request, redirect, url_for
# from pykintone import pykintone

app = Flask(__name__)

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