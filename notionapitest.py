import os
from notion_client import Client
import requests

# notion notionapitestのシークレット情報
# 'secret_HidOWMHEF8usYbCphDuuHOFM1aGxiWsOICaTTWcJWuZ'
# journalデータベースにコネクト

# journalのURL
# https://www.notion.so/goldenriver/journal-c6ea4378335f4280b4b92f576fd6e3ec?pvs=4
# journalのデータベースID


# toke : インテグレーションのシークレット情報
token = "secret_HidOWMHEF8usYbCphDuuHOFM1aGxiWsOICaTTWcJWuZ"
client = Client(auth=token)

def read_notion_database(database_id):
    response = client.databases.query(
        **{
            "database_id": database_id,
        }
    )
    return response

a = read_notion_database('ede808c9-e27a-47a3-aa2f-ae6a2a03fa57')
print(a)