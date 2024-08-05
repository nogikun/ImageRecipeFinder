# 画像分類モデルを用いたレシピ検索アプリケーション(仮)
このレポジトリは私の通う大学内のグループワークで作成したものであり、その他で運用する事を目的としていません。

### 1. システム構成
![image](https://github.com/user-attachments/assets/46686b26-9a80-4606-baf1-6e9e9d1aa6f3)


### 2. 実行方法
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/nogikun/IPUT3_AIDev_case3)

本レポジトリのルートからターミナルを開き、下記コマンドを入力する事でシステムが起動します。
```bash
cd development/Docker
docker-compose up
```
サーバーの起動後、[localhost:80](localhost) にアクセスする事でWebアプリケーションにアクセスする事ができます。<br>
ローカルネットワーク内からアクセスする場合、ホストにサーバーのIPv4アドレスを入力してください。

### 3. ポートについて
|port|詳細|
|:-:|:-|
|80|Webアプリケーション用ポート|
|443|ssl用ポート|
|3000|API(FastAPI)を提供する<br>`{$host}:3000/docs` によりAPIをテストすることができます。|
|5050|pgadmin4用ポート|

### 4. Demo
https://github.com/user-attachments/assets/2dbd776a-cd2d-48ed-84e5-c85a32d3fa15
<!-- https://github.com/user-attachments/assets/91bd7f7f-20fc-4cab-b2ef-f0d378406384 -->
<!-- https://github.com/user-attachments/assets/9c6599d7-28fd-4a60-87cf-3ead214f424f -->

