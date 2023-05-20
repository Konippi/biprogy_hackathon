from pykintone import pykintone

# # kintoneの設定 
# account = pykintone.account('your_domain atode', 'your_api_token atode')
# app_kintone = account.app('app_id atode')

# yaml形式もある (こっちの方が早い)
account = pykintone.load('account.yaml')
app_kintone = account.app('app_id atode')

"""yaml
domain: your_domain
apitoken: your_api_token
"""
# という形式


records = app.select().all()

# データのレコードを表示
for record in records:
    print(record)