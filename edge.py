class Edge:
    def __init__(self,to,From,w=0):
        self.__to = to
        self.__from = From
        self.__w = w
    def From(self):
        return self.__from
    def To(self):
        return self.__to
    def W(self):
        return self.__w