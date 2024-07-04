FROM python:3.10.12

# MySQLクライアントをインストール
RUN apt-get update && apt-get install -y default-mysql-client

# コンテナ内で必要なファイルやスクリプトをコピー
COPY ./api.py /api.py
COPY ./requirements.txt /requirements.txt

CMD ["bash", "-c", "pip install -r requirements.txt && uvicorn api:app --reload --port 8000 --host 0.0.0.0"]

EXPOSE 8001