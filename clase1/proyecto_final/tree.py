
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(data, feature):
    if len(data) == 0:
        return None

    data.sort(key=lambda x: x[feature])
    split_point = len(data) // 2
    root = TreeNode(data[split_point])

    root.left = build_tree(data[:split_point], feature)
    root.right = build_tree(data[split_point + 1:], feature)

    return root


