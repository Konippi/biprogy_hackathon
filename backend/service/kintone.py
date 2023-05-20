import os
import requests
from dotenv import load_dotenv


load_dotenv()
BASE_URL = os.environ.get("KINTONE_BASE_URL")
BASE_URL_ALL = os.environ.get("KINTONE_BASE_URL_ALL")
API_TOKEN_SHOP = os.environ.get("KINTONE_SHOP_ACCESS_TOKEN")
API_TOKEN_COUPON = os.environ.get("KINTONE_COUPON_ACCESS_TOKEN")


def get_kintone_shop(id):
    params = {
        "app": 1,
        "id": id,
    }
    headers = {"X-Cybozu-API-Token": API_TOKEN_SHOP}
    resp = requests.get(BASE_URL, headers=headers, params=params)
    return resp


def get_kintone_shop_all():
    headers = {"X-Cybozu-API-Token": API_TOKEN_SHOP}
    url = BASE_URL_ALL + "?app=1"
    resp = requests.get(url, headers=headers)
    return resp


def get_kintone_coupon(id):
    params = {
        "app": 2,
        "id": id,
    }
    headers = {"X-Cybozu-API-Token": API_TOKEN_COUPON}
    resp = requests.get(BASE_URL, headers=headers, params=params)
    return resp


def get_kintone_coupon_all():
    headers = {"X-Cybozu-API-Token": API_TOKEN_COUPON}
    url = BASE_URL_ALL + "?app=2"
    resp = requests.get(url, headers=headers)
    return resp


if __name__ == "__main__":
    # RESP = get_kintone_shop(2)
    # RESP = get_kintone_shop_all()
    # RESP = get_kintone_coupon(1)
    RESP = get_kintone_coupon_all()
    print(RESP.text)
