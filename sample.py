#!/usr/bin/env python3


import random


import nltk
from nltk.corpus import propbank


if __name__ == '__main__':
    nltk.download('propbank')
    rolesets = list(propbank.rolesets())
    for roleset in random.sample(rolesets, 10):
        print(roleset.attrib['id'])
        roles = roleset.find('roles')
        for role in roles.findall('role'):
            print(f'ARG{role.attrib["n"]} {role.attrib["descr"]}')
        print()
