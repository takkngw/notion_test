import requests
import datetime

dt_now = datetime.datetime.now()
print(dt_now.strftime('%Y-%m-%d-T%H:%M:%SZ'))

url = "https://api.notion.com/v1/pages"

NOTION_API_KEY = 'secret_HidOWMHEF8usYbCphDuuHOFM1aGxiWsOICaTTWcJWuZ'
DATABASE_ID = 'ede808c9e27a47a3aa2fae6a2a03fa57'

headers = {
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "Authorization": f"Bearer {NOTION_API_KEY}"
}

json_data = {
    # アイコンやカバーも設定可能
    "icon": {
        "type": "emoji",
        "emoji": "📅"
    },
    "parent": {
        "type": "database_id",
        "database_id": f"{DATABASE_ID}"
    },
    # プロパティ
    "properties": {
        # タイトル
        "title": {
            "title": [
                {
                    "text": {
                        "content": "予定"
                    }                
                }
            ]
        },
    "日付": {
        "date": {
            "start": f"{dt_now.strftime('%Y-%m-%dT%H:%M:%SZ')}",
            "end": None,
        },
     },
    },
    # 本文
    "children": [
        # ブロック
        # リンク
        {
            "object": "block",
            "paragraph": {
                "rich_text": [
                    {
                        "text": {
                            "content": "カレンダーを開く",
                            "link": {
                                "url": "https://calendar.google.com/calendar/u/0/r"
                            }
                        },
                        "href": "https://calendar.google.com/calendar/u/0/r"
                    }
                ],
                "color": "default"
            }
        }
    ]
}

response = requests.post(url, json=json_data, headers=headers)
print(response.text)