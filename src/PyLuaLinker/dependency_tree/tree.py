import logging

from .node import node
from ..build_data import build_data


class tree:
    def __init__(self, data: build_data) -> None:
        logging.info("creating dependency-tree for " +
                     data.entry_point + ":")

        self.data = data

        self.grow()
        logging.info("dependency-tree for " +
                     data.entry_point + " is complete")

    def grow(self):
        logging.info("> growing tree for " + self.data.entry_point)
        self.root = node(self.data.entry_point, self)
        self.root.grow()

    def get_leaves(self) -> list[node]:
        if self.root == None:
            return []

        leaves = self.root.get_leaves()
        leaves = list(set(leaves))  # remove duplicates

        return leaves

    def cull(self, node: node):
        if node == self.root:
            self.root = None
            return

        self.root.remove(node)
