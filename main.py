#!/usr/bin/env python

import json
import os
import sys

from reversal import reversal


def getVerbbase():
    for k, v in os.environ.items():
        # print k;
        if k == "VERBBASE":
            return v
    return None

def main():

    # print("main")
    argvs = sys.argv
    argv_length = len(argvs)


    file = open(argvs[1])

    hay = file.read()
    nounFile = open(argvs[2])
    # @todo convention

    verbbase = getVerbbase()

    nouns = json.load(nounFile)

    reversedString = reversal(hay, nouns)

    print reversedString
    # to_verbname

main()

