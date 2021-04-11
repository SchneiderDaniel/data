from os import walk

_, _, filenames = next(walk('./Dashapps/world'))

class_list = []

for file in filenames:
    to_Add = file.split('.')[0]
    if to_Add[0].isupper(): class_list.append(to_Add)

__all__ = class_list