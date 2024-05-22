# Pythonのベースイメージを使用
FROM python:3.9-slim

# 作業ディレクトリの設定
WORKDIR /usr/django

# 環境変数を設定（Pythonがpycファイルやディスクキャッシュを生成しないようにする）
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 依存関係のインストール
# requirements.txtをコンテナ内にコピー
COPY requirements.txt /usr/django/
# requirements.txtに記載されたパッケージをインストール
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# # プロジェクトのファイルをコンテナ内の作業ディレクトリにコピー
# COPY . /app/

# gunicornを使ってDjangoアプリケーションを実行するコマンド
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project.wsgi:application"]
