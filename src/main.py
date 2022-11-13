import os
import fire
import src.github as gh


def command(
    issue,
    label,
    issue_file,
    dry=False,
    debug=False,
):
    # test gh command
    gh.test_github()
    
    # debug
    if debug:
        print('## auguments')
        print(f'issue={issue}')
        print(f'label={label}')
        print(f'issue_file={issue_file}')
        print(f'debug={debug}')
        print(f'dry={dry}')
        print('')

    # convert type
    if debug:
        print('## convert type')
    issue = str(issue)
    label = str(label)
    issue_file = str(issue_file)

    # check parent issue
    if debug:
        print('## check parent issue')
    gh.check_parent_issue(issue)

    # create subtask
    if debug:
        print('## create subtask')
    child_body = f'## 親Issue\n- #{issue}'
    with open(f'{issue_file}', 'r') as f:
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

    # edit parent issue 
    if debug:
        print('## edit parent issue')
    gh.add_subtasks_to_parent_issue(
        issue=issue,
        child_issues=numbers,
        dry=dry,
    )

def main():
    fire.Fire(command)

if __name__ == '__main__':
    main()
