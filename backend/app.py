from flask import Flask, render_template, redirect
from service import line_bot, kintone


app = Flask(__name__, static_folder="../frontend/static", template_folder="../frontend/templates")


@app.route("/", methods=["GET"])
def init():
    return redirect("/shop")


@app.route("/shop", methods=["GET"])
def shop_list():
    # kintoneからselect
    # line_bot.send_ticket('sample')
    return render_template("shop/list.html")


@app.route("/shop/<shop_id>", methods=["GET"])
def shop_details(shop_id):
    # kintoneからselect id = shop_id
    return render_template("shop/details.html")


@app.route("/coupon", methods=["GET"])
def ticket_list():
    # kintoneからselect
    return render_template("coupon/list.html")


@app.route("/coupon/<coupon_id>", methods=["GET"])
def ticket_details(ticket_id):
    # kintoneからselect id = ticket_id
    return render_template("coupon/details.html")


if __name__ == "__main__":
    app.run(debug=True, port="5000")
