# サブタスク作る君

github cliを使って指定したissue番号の下にサブタスクを作る

## 使い方

1. issue.txt に作成したいタスクを書く

2. github cliをインストール

3. 認証を済ます

4. issueを作成したリポジトリに移動する

5. コマンドを実行する

```
python /path/to/main.py [issue番号]
```

## テスト

githubの認証がうまく言っているか確認するスクリプト

```
python /path/to/test_github.py
```

## やりたい

* setup.pyでパス指定しなくても動くようにしたい
* コマンドライン引数を使いやすくする

