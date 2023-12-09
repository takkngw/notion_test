import os
from notion_client import Client
import requests
from keys import notion_keys



# toke : インテグレーションのシークレット情報
token = notion_keys.NOTION_API_KEY
client = Client(auth=token)

def read_notion_database(database_id):
    response = client.databases.query(
        **{
            "database_id": database_id,
        }
    )
    return response

a = read_notion_database('notion_keys.DATABASE_ID')
print(a)