FROM postgres:16.1

# rootユーザーのパスワードを設定
ENV POSTGRES_PASSWORD=rootpass

# set timezone
ENV TZ Asia/Tokyo

# 必要なパッケージのインストールとロケールの設定
RUN apt-get update

# タイムゾーンの設定
RUN apt-get install -y tzdata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

EXPOSE 5432