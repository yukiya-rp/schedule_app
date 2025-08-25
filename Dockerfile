# ベースイメージ
FROM python:3.11-slim

# 作業ディレクトリ
WORKDIR /app

# 依存関係を先にコピーしてインストール（キャッシュ効率化）
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# アプリコードをコピー
COPY . .

# 開発サーバーを起動
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]