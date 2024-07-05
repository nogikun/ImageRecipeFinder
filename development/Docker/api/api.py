from typing import Union,Optional,Annotated
from fastapi import FastAPI, File, UploadFile
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
    n: int
    about: Optional[str] = None

class Resipe(BaseModel):
    name: str
    items: list[Item]

class cart(BaseModel):
    #userid : Optional[int] = None # テスト用に追加
    items: list[Item]

app = FastAPI()

#
# 機能検証用エンドポイント /test
#
@app.get("/test/get")
async def read_root():
    return {"message":"Test OK"}

@app.post("/test/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

#
# エンドポイント
#
@app.post("/cam/search")
async def search_cam(cap : UploadFile):
    # ここにカメラ画像検索処理を記述
    return {"item_list":[{"name":"item1","id":1,"price":1000,"amount":1,"about":"item1"},{"name":"item2","id":2,"price":2000,"amount":1,"about":"item2"}]}

@app.post("/resipe/search")
async def search_resipe(resipe: Item):
    # ここにレシピ検索処理を記述
    return {"resipe_list":[{"name":"resipe1","items":[{"name":"item1","id":1,"price":1000,"amount":1,"about":"item1"},{"name":"item2","id":2,"price":2000,"amount":1,"about":"item2"}]}]}

@app.post("/cart/sum")
async def sum_cart(cart: cart):
    total = 0
    for item in cart.items:
        total += item.price * item.n # 価格×個数を加算
    return {"total":total}