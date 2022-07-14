import re

match = {')': '(', ']': '['}

while True:
    balanced_stack = []
    unbalanced = False
    sentence = input()
    if sentence == '.':
        break

    sentence = re.sub('[^\(\)\[\]]+', '', sentence)
    for bracket in sentence:
        if bracket in {'(', '['}:
            balanced_stack.append(bracket)
        else:
            try:
                if balanced_stack[-1] == match[bracket]:
                    balanced_stack.pop()
                else:
                    raise IndexError
            except IndexError:
                unbalanced = True
                break
    if not(balanced_stack or unbalanced):
        print('yes')
    else:
        print('no')
