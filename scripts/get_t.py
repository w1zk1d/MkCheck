#!/usr/bin/env python3
import time

with open('files/tiks.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('files/tiks1.txt', 'w') as fout:
    fout.writelines(data[1:])

time.sleep(3)

fp = open("files/tiks1.txt")
content = fp.readline()
print(content)
