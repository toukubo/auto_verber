import NounReversal


def reversal(hay,nouns):
    reversedString = hay
    for noun in nouns:
        nounReversal = NounReversal.NounReversal(noun,reversedString)
        reversedString = nounReversal.reversedString
    return reversedString