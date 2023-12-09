import os
from notion_client import Client
import requests
from keys import notion_keys

NOTION_API_KEY = notion_keys.NOTION_API_KEY
DATABASE_ID = notion_keys.DATABASE_ID


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