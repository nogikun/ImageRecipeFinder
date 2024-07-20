FROM python:3.10.12

RUN apt-get update

# コンテナ内で必要なファイルやスクリプトをコピー
#COPY ./api.py /api.py
#COPY ./requirements.txt /requirements.txt

CMD ["bash", "-c", "pip install --upgrade pip && pip install -r requirements.txt && uvicorn api:app --reload --port 3000 --host 0.0.0.0"]

EXPOSE 3000