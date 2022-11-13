import os
import fire
import src.github as gh


SCRIPT_PATH = os.path.dirname(__file__)


def main(
    issue,
    label,
    dry=False,
    issue_file='issues.txt',
):
    # debug
    print(f'issue={issue}')
    print(f'label={label}')
    print(f'dry={dry}')

    # convert type
    issue = str(issue)
    label = str(label)

    # create subtask
    child_body = f'- #{issue}'
    with open(f'{SCRIPT_PATH}/{issue_file}', 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
    numbers = []
    for line in lines:
        number = gh.create_issue(
            title=line,
            body=child_body,
            label=label,
            dry=dry
        )
        numbers.append(number)

    # edit parent task
    gh.add_subtasks_to_parent_issue(
        issue=issue,
        child_issues=numbers,
        dry=dry,
    )

def entry():
    fire.Fire(main)

if __name__ == '__main__':
    fire.Fire(main)
