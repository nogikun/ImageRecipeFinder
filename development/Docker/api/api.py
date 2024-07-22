from typing import Union,Optional,Annotated
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from io import BytesIO # メモリ上でバイナリデータを扱うためのモジュール
import matplotlib.pyplot as plt
import psycopg2
import json

# local import
from components.Rakuten_recipe_api import req_recipe

# データベース接続設定
connection = psycopg2.connect(
    "host=db dbname=postgres user=postgres password=rootpass"
    )
#
# データ形式の指定
#
class Item(BaseModel):
    name: str
    id: str # DB内に保存されるID
    price: float
    amount: int
    about: Optional[str] = None

class Resipe(BaseModel):
    name: str
    items: list[Item]

class cart(BaseModel):
    #userid : Optional[int] = None # テスト用に追加
    items: list[Item]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

    # 画像の形式を加工
    image = image.transpose(2,0,1) # モデルの入力形式に変換
    image = image[:3] # 4チャンネル目を削除（すべて1.0のデータのため無効）
    image = image.transpose(1,2,0) # 元の形式に戻す
    
    # 画像を受け取ったことを確認
    print('画像を受付けました')
    print("image shape:",image.shape) # 480 x 640 x 3 (width x height x color channel) の形式である事を想定

    # 
    # ここに画像検索処理を記述
    #
    results = ["lettuce","carrot"] # 仮の結果

    # 検索結果を返す
    res = {"item_list":[]}
    for result in results:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM items WHERE label = %s", (result,))
        item = cursor.fetchone()
        cursor.close()
        item = Item(id=item[0], name=item[1], price=item[3], about=item[4], amount=1)
        res["item_list"].append(item.dict())

    #return {"item_list":[{"name":"item1","id":1,"price":1000,"amount":1,"about":"item1"},{"name":"item2","id":2,"price":2000,"amount":1,"about":"item2"}]}
    return res

@app.post("/resipe/search")
async def search_resipe(Material: Item,
                        cols = ['recipeTitle','recipeMaterial'],
                        keys = ['name','items']):
    r = req_recipe('1031564129861406174')

    res = r(Material.name) # レシピ検索 : 第一引数に素材を指定

    Response = []
    for i in range(len(res)):
        Response.append({key: res[i][col] for col, key in zip(cols,keys)})

    
    for i, res in enumerate(Response):
        items = []
        for item in res['items']:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM items WHERE name = %s", (item,))
            item_detail = cursor.fetchone()
            cursor.close()
            if item_detail is None:
                # 商品が見つからなかった場合
                item = Item(id="0", name=item, price=0, about="not found", amount=1)
            else:
                # 商品が見つかった場合
                item = Item(id=item_detail[0], name=item_detail[1], price=item_detail[2], about=item_detail[3], amount=1)
            items.append(item)
        Response[i]['items'] = items # DBに基づく商品情報に変換
    
    # ここにレシピ検索処理を記述
    return {"resipe_list":Response}
    #return {"resipe_list":[{"name":"resipe1","items":[{"name":"item1","id":1,"price":1000,"amount":1,"about":"item1"},{"name":"item2","id":2,"price":2000,"amount":1,"about":"item2"}]}]}

@app.post("/cart/sum")
async def sum_cart(cart: cart):
    total = 0
    for item in cart.items:
        total += item.price * item.n # 価格×個数を加算
    return {"total":total}