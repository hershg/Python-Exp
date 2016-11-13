class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i-1]
    def __len__(self):
        return 1 + len(self.rest)
    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))

def remove_duplicates(lnk):
    if lnk == Link.empty or lnk.rest == Link.empty:
        return
    elif lnk.first == lnk.rest.first:
        lnk.rest = lnk.rest.rest
        remove_duplicates(lnk)
    else:
        remove_duplicates(lnk.rest)








class Tree:
    """A tree with root as its root value."""
    def __init__(self, root, branches=[]):
        self.root = root
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.root, branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self, k=0):
        indented = []
        for b in self.branches:
            for line in b.indented(k + 1):
                indented.append('  ' + line)
        return [str(self.root)] + indented

    def is_leaf(self):
        return not self.branches


def redundant_map_mutate(t, f):
    t.root = f(t.root)
    new_f = lambda x: f(f(x))
    t.branches = [redundant_map_mutate(branch, new_f) for branch in t.branches]
    return t

def redundant_map_new(t, f):
    new_root = f(t.root)
    new_f = lambda x: f(f(x))
    new_branches = [redundant_map_new(branch, new_f) for branch in t.branches]
    return Tree(new_root, new_branches)











class BTree(Tree):
    empty = Tree(None)

    def __init__(self, root, left=empty, right=empty):
        Tree.__init__(self, root, (left, right))

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]


def find_min(bst):
    if bst.left == BTree.empty:
        return bst.root
    return find_min(bst.left)


