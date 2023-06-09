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
    jdata = requests.get(BASE_URL, headers=headers, params=params).json()
    return jdata["record"]


def get_kintone_shop_all():
    headers = {"X-Cybozu-API-Token": API_TOKEN_SHOP}
    url = BASE_URL_ALL + "?app=1"
    jdata = requests.get(url, headers=headers).json()
    return jdata["records"]


def get_kintone_shop_search(tag):
    # tag = "foods", "clothes", "leisure"
    query = f'tag="{tag}"'
    params = {
        "app": 1,
        "query": query,
    }
    headers = {"X-Cybozu-API-Token": API_TOKEN_SHOP}
    jdata = requests.get(BASE_URL_ALL, headers=headers, params=params).json()
    return jdata["records"]


def get_kintone_shop_search_name(store_name):
    # tag = "foods", "clothes", "leisure"
    query = f'store_name="{store_name}"'
    params = {
        "app": 1,
        "query": query,
    }
    headers = {"X-Cybozu-API-Token": API_TOKEN_SHOP}
    jdata = requests.get(BASE_URL_ALL, headers=headers, params=params).json()
    return jdata["records"][0]


def get_kintone_coupon(id):
    params = {
        "app": 2,
        "id": id,
    }
    headers = {"X-Cybozu-API-Token": API_TOKEN_COUPON}
    jdata = requests.get(BASE_URL, headers=headers, params=params).json()
    return jdata["record"]


def get_kintone_coupon_all():
    headers = {"X-Cybozu-API-Token": API_TOKEN_COUPON}
    url = BASE_URL_ALL + "?app=2"
    jdata = requests.get(url, headers=headers).json()
    return jdata["records"]


def get_kintone_coupon_search(tag):
    headers = {"X-Cybozu-API-Token": API_TOKEN_COUPON}
    query = f'tag="{tag}"'
    params = {
        "app": 2,
        "query": query,
    }
    jdata = requests.get(BASE_URL_ALL, headers=headers, params=params).json()
    return jdata["records"]


def post_kintone_coupon(params):
    headers = {"X-Cybozu-API-Token": API_TOKEN_COUPON, "Content-Type": "application/json"}
    body = {"app": 2, "record": params}
    requests.post(BASE_URL, json=body, headers=headers)
