# サブタスク作る君

github cliを使って指定したissue番号の下にサブタスクを作る

## install

```
pip install -e .
```

## 使い方

1. issue.txt に作成したいタスクを書く

2. github cliをインストール

3. 認証を済ます

4. issueを作成したリポジトリに移動する

5. コマンドを実行する

```
python /path/to/main.py --issue [issue番号] --label subtask

# dry mode
python /path/to/main.py --issue [issue番号] --label subtask --dry
```

## テスト

githubの認証がうまく言っているか確認するスクリプト

```
python /path/to/test_github.py
```

## やりたい
* issue存在チェック
* エラー時に止める

