from robot.api.parsing import get_tokens

path = 'example.robot'

for token in get_tokens(path):
    print(repr(token))