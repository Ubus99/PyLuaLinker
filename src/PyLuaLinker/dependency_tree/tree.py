import logging

from .node import Node
from ..builddata import BuildData


class Tree:
    def __init__(self, data: BuildData) -> None:
        self.root = None

        logging.info(
            "creating dependency-tree for " +
            data.entry_point + ":"
        )

        self.data = data

        self.grow()
        logging.info(
            "dependency-tree for " +
            data.entry_point + " is complete"
        )

    def grow(self):
        logging.info("> growing tree for " + self.data.entry_point)
        self.root = Node(self.data.entry_point, self)
        self.root.grow()

    def get_leaves(self) -> list[Node]:
        if self.root is None:
            return []

        leaves = self.root.get_leaves()
        leaves = list(set(leaves))  # remove duplicates

        return leaves

    def cull(self, node: Node):
        if node == self.root:
            self.root = None
            return

        self.root.remove(node)
