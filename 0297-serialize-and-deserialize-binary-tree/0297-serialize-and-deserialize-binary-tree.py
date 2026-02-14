# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                res.append('null')
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(res)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        val_list = data.split(',')
        self.idx = 0

        def dfs():
            if self.idx >= len(data):
                return

            cur_str = val_list[self.idx]
            self.idx += 1

            if cur_str == 'null':
                return None

            node = TreeNode(str(cur_str))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))