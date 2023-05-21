from flask import Flask, render_template, redirect, request
from service import line_bot, kintone


app = Flask(__name__, static_folder="../frontend/static", template_folder="../frontend/templates")
# line_bot.send_coupon('sample')


@app.route("/", methods=["GET"])
def init():
    return redirect("/shop")


@app.route("/shop", methods=["GET"])
def shop_list():
    shops = (
        kintone.get_kintone_shop_all()
        if request.args.get("search") in [None, "all"]
        else kintone.get_kintone_shop_search(request.args.get("search"))
    )

    return render_template("shop/list.html", shops=shops)


@app.route("/shop/<shop_id>", methods=["GET"])
def shop_details(shop_id):
    shop = kintone.get_kintone_shop(shop_id)
    print(shop)

    return render_template("shop/details.html", shop=shop)


@app.route("/coupon", methods=["GET"])
def coupon_list():
    coupons = (
        kintone.get_kintone_coupon_all()
        if request.args.get("search") in [None, "all"]
        else kintone.get_kintone_coupon_search(request.args.get("search"))
    )

    return render_template("coupon/list.html", coupons=coupons)


@app.route("/coupon/<coupon_id>", methods=["GET"])
def coupon_details(coupon_id):
    coupon = kintone.get_kintone_coupon(coupon_id)
    shop_detail = kintone.get_kintone_coupon(coupon_id)

    return render_template("coupon/details.html", coupon=coupon, shop_detail=shop_detail)


@app.route("/form", methods=["GET"])
def admin_form():
    return render_template("form/form.html")


@app.route("/coupon/new", methods=["POST"])
def admin_new_coupon():
    store_name = request.form.get("name")
    due_date = request.form.get("due-date")
    description = request.form.get("description")
    store_info = kintone.get_kintone_shop_search_name(store_name)
    params = {
        "coupon_store_name": {"value": store_name},
        "detail_coupon": {"value": description},
        "due_date": {"value": due_date},
        "coupon_image_url": {"value": store_info["image_url"]["value"]},
        "coupon_tag": {"value": store_info["tag"]["value"]},
    }
    kintone.post_kintone_coupon(params)

    return redirect("/coupon")


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True, port="5000")
