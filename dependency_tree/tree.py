from pathlib import Path
from .node import node

class tree:
    def __init__(self, entry: str, src: dict[str, Path]) -> None:

        if not entry in src:
            print("entry  point not found!")
            exit()

        self.entry = entry
        self.src = src
        self.root = None

    def grow(self):
        self.root = node(self.entry, self)
        self.root.grow()

    def get_leaves(self) -> list[node]:
        if self.root == None:
            return []
        
        return self.root.get_leaves()
            
    
    def cull(self, node: node):
        if node == self.root:
            self.root = None
            return

        self.root.cull(node)