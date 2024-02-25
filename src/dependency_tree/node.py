import utils
import logging


class node:
    def __init__(self, name: str, base) -> None:
        self.name = name
        self.path = base.data.src[name]
        self.deps = None

        self.base = base
        logging.info("<< created node for dependency '" + name + "'")

    def __eq__(self, __value: object) -> bool:
        if __value is None:
            return False

        eq = self.name == __value.name\
            and self.path == __value.path
        return eq

    def __hash__(self) -> int:
        return hash(("name", self.name,
                     "path", self.path))

    def grow(self):
        logging.info("growing " + self.name)
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

    def remove(self, node):
        logging.info("culling " + node.name + " from " + self.name)
        # remove from this node
        self.deps = list(filter(lambda n: n != node, self.deps))
        for d in self.deps:  # remove from children
            d.remove(node)
        pass
