# 中央線沿線のマンション価格ダッシュボード

「Tableauで始めるデータサイエンス」の「東京23区のマンション価格を推論してみよう!」で作成したダッシュボード

## ディレクトリ構造

```
.
├── JR_JC_line_symbol.svg.png
├── README.md
├── chuo-line-property-price.tfl
├── chuo-line-property-price.twb
├── data
│   ├── 13101_20161_20214.csv
│   ├── 13102_20161_20214.csv
│   ├── 13104_20161_20214.csv
│   ├── 13113_20161_20214.csv
│   ├── 13114_20161_20214.csv
│   ├── 13115_20161_20214.csv
│   ├── 13202_20161_20214.csv
│   ├── 13203_20161_20214.csv
│   ├── 13210_20161_20214.csv
│   ├── 13214_20161_20214.csv
│   └── 中央線-UTF8+Express.csv
├── deploy_tabpy.py
├── full_to_half.py
├── tabpy_log.log
└── train_model.py

```


## データソース

- [国土交通省 不動産取引価格情報ダウンロード](https://www.land.mlit.go.jp/webland/download.html)
    - 2016年第1四半期から2021年第4四半期まで
    - 中央区、千代田区、新宿区、渋谷区、中野区、杉並区、武蔵野市、小金井市、国分寺市、立川市
- [秀和システム](https://www.shuwasystem.co.jp/support/7980html/6025.html)
    - Tableau_sample.zipの中の「3.2.東京マンション」の`中央線-UTF8+Express.csv`
