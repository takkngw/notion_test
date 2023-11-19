import os
from notion_client import Client
import requests

NOTION_API_KEY = 'secret_HidOWMHEF8usYbCphDuuHOFM1aGxiWsOICaTTWcJWuZ'
DATABASE_ID = 'ede808c9-e27a-47a3-aa2f-ae6a2a03fa57'

url = 'https://api.notion.com/v1/pages'

headers =  {
    'Notion-Version': '2022-06-28',
    'Authorization': 'Bearer ' + NOTION_API_KEY,
    'Content-Type': 'application/json',
}

json_data = {
    'parent': { 'database_id': DATABASE_ID },
    'properties': {
        '名前': {
            'title': [
                {
                    'text': {
                        'content': 'Pythonで追加'
                    }
                }
            ]
        },
				'タグ': {
            'multi_select': [
                {
                'name': 'Python'
                }
            ]
        },
    },
}

response = requests.post(url, headers=headers, json=json_data)
print(response)