# 画像分類モデルを用いたレシピ検索アプリケーション(仮)

### 1. 実行方法
本レポジトリのルートからターミナルを開き、下記コマンドを入力する事でシステムが起動します。
```bash
cd development/Docker
docker-compose up
```
サーバーの起動後、[localhost:80](localhost) にアクセスする事でWebアプリケーションにアクセスする事ができます。

### 2. ポートについて
|port|詳細|
|:-:|:-|
|80|Webアプリケーション用ポート|
|443|ssl用ポート|
|3000|API(FastAPI)を提供する<br>`{$host}:3000/docs` によりAPIをテストすることができます。|
|5050|pgadmin4用ポート|

### 3. Demo
https://github.com/user-attachments/assets/2dbd776a-cd2d-48ed-84e5-c85a32d3fa15
<!-- https://github.com/user-attachments/assets/91bd7f7f-20fc-4cab-b2ef-f0d378406384 -->
<!-- https://github.com/user-attachments/assets/9c6599d7-28fd-4a60-87cf-3ead214f424f -->

