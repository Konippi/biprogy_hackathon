import requests
import os

BASE_URL = os.environ.get('KINTONE_BASE_URL')
API_TOKEN1 = os.environ.get('KINTONE_SHOP_ACCESS_TOKEN')
API_TOKEN2 = os.environ.get('KINTONE_COUPON_ACCESS_TOKEN')


def get_kintone_shop(api_token, id):
    params = {
        "app": 1,
        "id": id,
    }
    headers = {"X-Cybozu-API-Token": api_token}
    resp = requests.get(BASE_URL, headers=headers, params=params)
    return resp


def get_kintone_coupon(api_token, id):
    params = {
        "app": 2,
        "id": id,
    }

    headers = {"X-Cybozu-API-Token": api_token}
    resp = requests.get(BASE_URL, headers=headers, params=params)
    return resp


if __name__ == "__main__":
    RESP = get_kintone_shop(API_TOKEN1, 2)