import requests
import json

# 送信先のURL
url = 'http://172.34.0.7:8080/select-tables/'  # 実際のURLに置き換えてください

# 送信するJSONデータ
data = {
    "room": "101"
}

# POSTリクエストの送信
response = requests.post(url, json=data)

# レスポンスの表示
print("ステータスコード:", response.status_code)
print("response:", response.text)
# print("レスポンス本文:", response.text)
