from typing import Union,Optional,Annotated
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

from io import BytesIO # メモリ上でバイナリデータを扱うためのモジュール
import matplotlib.pyplot as plt
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
async def create_upload_file(img: UploadFile):
    memory = await img.read()
    image = plt.imread(BytesIO(memory), format = img.filename.split('.')[-1])
    plt.imshow(image)
    plt.show() # Docker環境内だと表示されない。
    return {"filename": img.filename}

#
# エンドポイント
#
@app.post("/cam/search")
async def search_cam(cap : UploadFile):
    # ここにカメラ画像検索処理を記述
    memory = await cap.read()
    image = plt.imread(BytesIO(memory), format = cap.filename.split('.')[-1]) # image ･･･ 画像インスタンス。これをモデルの入力として使えるか要検証
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