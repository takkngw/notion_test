import os
from notion_client import Client
import requests
from keys import notion_keys

NOTION_API_KEY = notion_keys.NOTION_API_KEY

url = f"https://api.notion.com/v1/search"

headers = {
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "Authorization": f"Bearer {NOTION_API_KEY}"
}

json_data = {
    # タイトルを検索できる
    #"query": "ブログ",
    # 絞り込み(データベースだけに絞るなど)
    #"filter": {
    #    "value": "database",
    #    "property": "object"
    #},
    # ソート順
    "sort": {
        "direction": "ascending",
        "timestamp": "last_edited_time"
    }
}

response = requests.post(url, json=json_data, headers=headers)
print(response.text)