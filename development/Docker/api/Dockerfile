FROM python:3.10.12

WORKDIR /usr/src/app

RUN apt-get update && \
apt-get install -y \
libgl1-mesa-glx \
libglib2.0-0 \
&& apt-get clean
# コンテナ内で必要なファイルやスクリプトをコピー
#COPY ./api.py /api.py
COPY requirements.txt ./requirements.txt

# モデルのダウンロード
RUN mkdir -p /usr/src/app/models && \
wget https://huggingface.co/nogikun/IPUT_Models/resolve/main/yolo/yolov5/yolov5s_20240723.pt \
-O ./models/yolov5s_20240723.pt
COPY ./models /usr/src/app/models

RUN pip install --upgrade pip && \
pip install --no-cache-dir -r requirements.txt && \
pip install --no-cache-dir -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt

# エントリーポイントとしてsupervisordを指定
#CMD ["/usr/bin/supervisord"]
CMD ["bash", "-c", "uvicorn api:app --reload --port 3000 --host 0.0.0.0"]

EXPOSE 3000