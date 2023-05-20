from flask import Flask, render_template, redirect
from service import line_bot
from service.kintone import get_kintone_shop, get_kintone_shop_all, get_kintone_coupon, get_kintone_coupon_all


app = Flask(__name__, static_folder="../frontend/static", template_folder="../frontend/templates")


@app.route("/", methods=["GET"])
def init():
    return redirect("/shop")


@app.route("/shop", methods=["GET"])
def shop_list():
    # kintoneからselect
    # line_bot.send_coupon('sample')
    shops = get_kintone_shop_all()
    return render_template("shop/list.html", shops=shops)


@app.route("/shop/<shop_id>", methods=["GET"])
def shop_details(shop_id):
    # kintoneからselect id = shop_id
    shop = get_kintone_shop(shop_id)
    return render_template("shop/details.html", shop=shop)


@app.route("/coupon", methods=["GET"])
def coupon_list():
    # kintoneからselect
    coupons = get_kintone_coupon_all()
    return render_template("coupon/list.html", coupons=coupons)


@app.route("/coupon/<coupon_id>", methods=["GET"])
def coupon_details(coupon_id):
    # kintoneからselect id = coupon_id
    coupon = get_kintone_shop(coupon_id)
    return render_template("coupon/details.html", coupon=coupon)


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True, port="5000")
