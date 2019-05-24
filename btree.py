from btnode import Field
from btnode import BTNode


class BTree:
    """An link-based binary tree implementation."""
    def __init__(self, field_width):
        self._root = BTNode(Field(field_width))

    def build(self):
        self._root.build_children(True)
        self._root.calc_rating(True)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._root = None
        self._size = 0
