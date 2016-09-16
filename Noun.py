
class Noun:
    def __init__(self,name,json):
        self.__dict__ = json.loads(json)
        self.name = name
        # self.attrs = []
