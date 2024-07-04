from typing import Union,Optional
from fastapi import FastAPI
from pydantic import BaseModel
#import mysql.connector
#import datetime

# データベース接続設定
#config = {
#  'user': 'root',     # ここにユーザー名を入れます
#  'password': 'rootpass', # ここにパスワードを入れます
#  'host': 'mysql-db',    # ここにホストを入れます（mysql-db）
#  'database': 'test', # ここにデータベース名を入れます
#  'raise_on_warnings': True
#}

#
# データ形式の指定
#
class Item(BaseModel):
    name: str
    id: int # DB内に保存されるID
    price: float
    amount: int
    about: Optional[str] = None

class Resipe(BaseModel):
    name: str
    items: list[Item]

class cart(BaseModel):
    userid : Optional[int] = None # テスト用に追加
    items: list[Item]

app = FastAPI()

@app.get("/test/get")
async def read_root():
    return {"message":"Test Pass"}

@app.post("/cart/sum")
async def sum_cart(cart: cart):
    total = 0
    for item in cart.items:
        total += item.price * item.amount
    return {"total":total}

@app.post('/cam/search') # test
async def search_cam():
    return {"item_list":[{"name":"item1","id":1,"price":1000,"amount":1,"about":"item1"},{"name":"item2","id":2,"price":2000,"amount":1,"about":"item2"}]} # テスト用に追加
