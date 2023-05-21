from flask import Flask, render_template, redirect, request
from service import line_bot, kintone


app = Flask(__name__, static_folder="../frontend/static", template_folder="../frontend/templates")
# line_bot.send_coupon('sample')


@app.route("/", methods=["GET"])
def init():
    return redirect("/shop")


@app.route("/shop", methods=["GET"])
def shop_list():
    shops = [
        kintone.get_kintone_shop_all()
        if request.args.get("search") in [None, all]
        else kintone.get_kintone_shop_search(request.args.get("search"))
    ]

    return render_template("shop/list.html", shops=shops)


@app.route("/shop/<shop_id>", methods=["GET"])
def shop_details(shop_id):
    shop = kintone.get_kintone_shop(shop_id)
    return render_template("shop/details.html", shop=shop)


@app.route("/coupon", methods=["GET"])
def coupon_list(tag=None):
    if tag:
        coupons = kintone.get_kintone_coupon_search(tag)
        return render_template("coupon/list.html", coupons=coupons)
    else:
        coupons = kintone.get_kintone_coupon_all()
        return render_template("coupon/list.html", coupons=coupons)


@app.route("/coupon/<coupon_id>", methods=["GET"])
def coupon_details(coupon_id):
    coupon = kintone.get_kintone_coupon(coupon_id)
    shop_name = coupon["record"]["coupom_store_name"]["value"]
    shop_detail = kintone.get_kintone_shop_search_name(shop_name)
    return render_template("coupon/details.html", coupon=coupon, shop_detail=shop_detail)


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True, port="5000")
