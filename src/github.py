import subprocess
import json


def test_github():
    '''githubコマンド使えるかテスト'''
    command = ["gh", "issue", "view", "1", "--json", "body"]
    result = subprocess.run(command, capture_output=True)
    __check_gh_command(result, echo=False)


def check_parent_issue(issue: str):
    '''親チケットの存在チェック'''
    command = ["gh", "issue", "view", issue, "--json", "body"]
    result = subprocess.run(command, capture_output=True)
    __check_gh_command(result, echo=False)


def create_issue(
    title='',
    body='',
    label='',
    dry=False,
):
    '''issueを作成'''
    command = ["gh", "issue", "create", "-t", title, "-b", body, "-l", label]
    print(" ".join(command))
    if not dry:
        result = subprocess.run(command, capture_output=True)
        __check_gh_command(result)
        # 結果からissue番号を返却
        return result.stdout.decode('ascii').split('/')[-1].strip()
    else:
        return "0"


def add_subtasks_to_parent_issue(
    issue='',
    child_issues='',
    dry=False,
):
    '''親issueを修正'''
    current_body = __get_issue_body(issue) 
    body = current_body 
    body += '\n\n## Subtasks\n'
    body += "\n".join(map(lambda issue: f"- #{issue}", child_issues))
    command = ["gh", "issue", "edit", issue, "-b", body]
    print(" ".join(command))
    if not dry:
        result = subprocess.run(command, capture_output=True)
        __check_gh_command(result)


def __get_issue_body(
    issue='',
):
    '''issueの説明欄を見る'''
    command = ["gh", "issue", "view", issue, "--json", "body"]
    result = subprocess.run(command, capture_output=True)
    if result.stderr:
        return False
    return json.loads(result.stdout.decode('utf-8')).get('body')


def __check_gh_command(result: subprocess.CompletedProcess, echo=True):
    '''ghコマンドの結果を確認してエラーならエラー終了'''
    if echo:
        print(result.stdout.decode('utf-8'))
    print(result.stderr.decode('utf-8'))
    try:
        result.check_returncode()
    except subprocess.CalledProcessError:
        print(f'github cliの実行に失敗しました')
        exit(1)
