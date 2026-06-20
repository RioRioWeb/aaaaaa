# test-drive-reservation
## Installation
```bash
# リポジトリをクローン
git clone https://github.com/〇〇/〇〇.git
# 仮想環境を作成
python3.13.3 -m venv .venv
# 仮想環境を有効化
source .venv/bin/activate
# ライブラリをインストール
pip install -r requirements.txt
```

## Usage
```bash
# サーバを起動
python app.py
```
http://127.0.0.1:5000/ からWebサイトにアクセス<br>
CTRL+Cでサーバを終了

## ディレクトリ構成
```text
reservation_app/
├── app.py                  # アプリの起動エントリーポイント（Blueprintの登録など）
├── config.py               # DB接続設定（環境変数など）
├── extensions.py           # SQLAlchemyインスタンスの初期化（循環インポート防止）
│
├── models/                 # 【Model】データベースの定義・ビジネスロジック
│   └── reservation.py      # 予約テーブル・車種テーブルの定義
│
├── views/                  # 【Controller】ルーティングと交通整理（Blueprint）
│   ├── booking.py          # 新規予約・Top用のBlueprint
│   └── enquiry.py          # 照会・変更・キャンセル用のBlueprint
│
└── templates/              # 【View】画面テンプレート（HTML / UI層）
    ├── base.html           # 全画面共通のベースレイアウト（店名表示など）
    ├── booking/            # 新規予約系の画面（0〜4）
    │   ├── top.html        # 0
    │   ├── select_car_datetime.html # 1
    │   ├── input_customer.html # 2
    │   ├── confirm.html    # 3
    │   └── complete.html   # 4
    └── enquiry/            # 照会・変更・キャンセル系の画面（5〜7）
        ├── auth.html       # 5
        ├── detail.html     # 6
        └── cancel_confirm.html # 7
'''

## 〇〇