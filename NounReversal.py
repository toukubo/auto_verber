from AttrReversal import AttrReversal


class NounReversal:
    def __init__(self,noun,hay):
        self.hay = hay
        for attr in noun["attrs"]:
            attrReversal = AttrReversal(attr, hay)
            self.reversedString = attrReversal.reversedString
        self.reversedString = self.reversedString.replace(noun["name"],"{{noun.name}}")
