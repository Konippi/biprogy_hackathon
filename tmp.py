import os
from pykintone import pykintone

if __name__ == '__main__':
    # kintoneの設定
    # domain_name = os.environ['DB_DOMAIN_NAME']
    # api_token = os.environ['DB_STORE_ACCESS_TOKEN']
    # app_id = os.environ['DB_STORE_APP_ID']
    domain_name = "7hsj87vfpdhh.cybozu.com"
    api_token = "t4O70FRaVB3sD9UdOWCH1xKlaGiBAjziGBYkm37x"
    app_id = "1"

    # pykintone設定
    account = pykintone.account(domain_name, api_token)
    app_kintone = account.app(app_id)

    # # yaml形式もある (こっちの方が早い)
    # account = pykintone.load('account.yaml')
    # app_kintone = account.app('app_id atode')

    # """yaml
    # domain: your_domain
    # apitoken: your_api_token
    # """
    # # という形式


    records = app.select().all()

    # データのレコードを表示
    for record in records:
        print(record)