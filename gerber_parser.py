#!/usr/bin/env python3

import os
import re
import sys

curPath = sys.argv[1] if len(sys.argv) >= 2 else os.curdir
# Constant
TREASH = ["Altium",
          "Designer",
          "Software"]

REG1 = '(' + '|'.join(i + '|' + i.lower() + '|' + i.upper() for i in TREASH) + ')'
TreashPatt = re.compile(REG1)

EXTENSIONS = ["BRD",
              "DRL",
              "GB*",
              "GT*"]

REG2 = '(' + '|'.join(f'{i.replace("*","[A-Z]")}|{i.replace("*","[A-Z]").lower()}' for i in EXTENSIONS) + ')'
ExtPatt = re.compile(REG2)


def file_validator(name: str) -> bool:
    if not os.path.isdir(os.path.join(os.curdir, name)):
        if len(ExtPatt.findall(name.split('.')[-1])):
            return True
    return False


files = [os.path.join(os.curdir, i)
         for i in os.listdir(os.curdir) if file_validator(i)]

os.mkdir(os.path.join(os.curdir, "BACK"))
for name in files:
    back = os.path.join(os.path.split(name)[0], "BACK", os.path.split(name)[1])
    os.rename(name, back)
    with open(name, 'w') as targ:
        with open(back, 'r') as src:
            for s in src.readlines():
                if len(TreashPatt.findall(s)) == 0:
                    targ.write(s)
                else:
                    print(f"Finded {TreashPatt.findall(s)[0]} in string {s}")
