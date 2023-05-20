import requests

URL = "https://7hsj87vfpdhh.cybozu.com/k/v1/record.json?app=1&id=2"
API_TOKEN = "t4O70FRaVB3sD9UdOWCH1xKlaGiBAjziGBYkm37x"


def get_kintone(url, api_token):
    """kintoneのレコードを1件取得する関数"""
    headers = {"X-Cybozu-API-Token": api_token}
    resp = requests.get(url, headers=headers)
    return resp


if __name__ == "__main__":
    RESP = get_kintone(URL, API_TOKEN)

    print(RESP.text)