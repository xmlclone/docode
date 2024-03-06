import ast
import astpretty
from robot.api.parsing import get_model

model = get_model('example.robot')
# print(model.name)
# for attr in dir(model):
#     print(f"{attr}: {getattr(model, attr)}")
# print(ast.dump(model, include_attributes=True))
# print('-' * 72)
# astpretty.pprint(model)