# aws-architecture-icon-quiz-app

[AWS Architecture Icons](https://aws.amazon.com/architecture/icons/?nc1=h_ls)から取得したアイコンを元に作成したクイズアプリです。

## 動作前提

- Dockerがインストール済みであること

## 動作方法

### 1. アプリ起動

```sh
$ docker build -t aws-architecture-icon-quiz-app .
4 docker run -p 5000:5000 aws-architecture-icon-quiz-app
```

### 2. アプリアクセス

`http://localhost:5000`にアクセス

## アプリ動作イメージ

![app-image](/images/app-image.png)

## アプリ機能

初期値は文字列の70%を*で置換して表示。

### Hint

解答をランダムで3文字表示。

### Show Answer

解答の表示。

### Next Quiz

次のクイズを表示。
