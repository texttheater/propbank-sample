#!/usr/bin/env python3


import random
import sys


import nltk
from nltk.corpus import propbank


def print_roleset(roleset):
   print(roleset.attrib['id'])
   roles = roleset.find('roles')
   for role in roles.findall('role'):
       print(f'ARG{role.attrib["n"]} {role.attrib["descr"]}')
   print()


if __name__ == '__main__':
    nltk.download('propbank')
    if len(sys.argv) > 1:
        roleset = propbank.roleset(sys.argv[1])
        print_roleset(roleset)
    else:
        rolesets = tuple(propbank.rolesets())
        for roleset in random.sample(rolesets, 10):
            print_roleset(roleset)
