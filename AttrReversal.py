class AttrReversal(object):
    def __init__(self,attr,hay):
        self.attr = attr
        self.hay = hay
        self.reversedString = hay.replace(attr["name"],"{{name}}")
        # classreversed = reversed.replace(attr.name,"{{name}}")