class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        visited = []

        visited.append(root)

        while visited:
            cur = visited.pop()

            if cur is None:
                continue

            res.append(cur.val)

            visited.append(cur.right)
            visited.append(cur.left)

        return res