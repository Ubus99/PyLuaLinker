from . import utils

class node:
    def __init__(self, name:str, base) -> None:
        self.name = name
        self.path = base.src[name]
        self.deps = None

        self.base = base

    def grow(self):
        deps = utils.scan_file(self.path)
        buff = []

        for ln in deps:
            name = deps[ln]
            child = node(name, self.base)
            child.grow()
            buff.append(child)

        self.deps = buff

    def get_leaves(self) -> list:
        if len(self.deps) == 0:
            return [self]
        
        buff = []
        for n in self.deps:
            buff += n.get_leaves()

        return buff
    
    def cull(self, node):
        self.deps = [n in n for n in self.deps if not n == node]
        pass