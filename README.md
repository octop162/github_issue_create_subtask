# サブタスク作る君

github cliを使って指定したissue番号の下にサブタスクを作る

## install

```
pip install -e .
```

## uninstall

```
pip uninstall gh-subtask
```

## 使い方

1. github cliをインストール
1. 認証を済ます
1. issueを作成したリポジトリに移動する
1. 作成する
1. コマンドを実行する

```
gh-subtask --issue [issue番号] --label subtask --issue_file issue.txt

# dry mode
gh-subtask --issue [issue番号] --label subtask --issue_file issue.txt --dry --debug
```

