import os
import sys
import github as gh

# settings
SCRIPT_PATH = os.path.dirname(__file__)
ISSUES_LIST_FILENAME = 'issues.txt'
LABEL='question'
DRY=False

if __name__ == '__main__':

    # arguments
    PARENT = dict(enumerate(sys.argv)).get(1, '')
    BODY=f'- #{PARENT}'
    
    # create subtask
    with open(f'{SCRIPT_PATH}/{ISSUES_LIST_FILENAME}', 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
    
    numbers = []
    for line in lines:
        number = gh.create_issue(
            title=line,
            body=BODY,
            label=LABEL,
            dry=DRY
        )
        numbers.append(number)

    # edit parent task
    gh.add_subtasks_to_parent_issue(
        issue=PARENT,
        child_issues=numbers,
        dry=DRY,
    )

    