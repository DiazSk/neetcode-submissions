class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            if node is None:
                return True

            if not (min_val < node.val < max_val):
                return False

            is_left_valid = validate(node.left, min_val, node.val)
            is_right_valid = validate(node.right, node.val, max_val)

            return is_left_valid and is_right_valid

        return validate(root, float('-inf'), float('inf'))