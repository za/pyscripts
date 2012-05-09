#!/usr/bin/python

from sys import argv
from collections import Counter

if __name__ == "__main__":
    with open(argv[1]) as f:
        c = Counter(i.partition("-")[0] for i in f)

    for k,v in c.most_common(5):
        print '{:>4} {}'.format(v,k)
