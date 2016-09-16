import json

import logic
import NounReversal
import sys




def reversal(hay,nouns):
    reversedString = hay
    for noun in nouns:
        nounReversal = NounReversal.NounReversal(noun,reversedString)
        reversedString = nounReversal.reversedString
    return reversedString



def main():
    print("main")
    argvs = sys.argv
    argc = len(argvs)
    if (argc != 3):
        print 'Usage: # python %s target_file_path noun_file_path' % argvs[0]
        quit()

    file = open(argvs[1])

    hay = file.read()
    nounFile = open(argvs[2])
    # @todo convention

    nouns = json.load(nounFile)


    reversedString = reversal(hay,nouns)
    print reversedString

main()
