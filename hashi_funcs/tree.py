class Tree:
    class Node:
        content = None
        children = []
        parent = None

        def __init__(self, val, par=None):
            self.content = val
            self.children = []
            self.parent = par

        def add_child(self, val):
            child = Tree.Node(val)
            child.parent = self
            self.children.append(child)
            return child

        def path(self):
            current=self
            path_list = []           
            while current.parent :
                path_list.append(current.content.board)
                current=current.parent
            path_list.reverse()
            return path_list

    root = None

    def __init__(self, val):
        self.root = Tree.Node(val)
