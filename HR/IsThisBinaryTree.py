LEFT_LIMIT = -float('inf')
RIGHT_LIMIT = float('inf')

class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

def isBinaryTree(root, left_limit = LEFT_LIMIT, right_limit = RIGHT_LIMIT):
    '''
    For a give binary tree, limit for a branch tree changes as follows:
                             6 (-inf < x < +inf)
                           /  \
                         /     \
         (-inf < x < 6) 3       ----------------------
                       / \                            \
                     /    \                            9 (6 < x < +inf)
     (-inf < x < 3) 1      4 (3 < x < 6)             /  \
                                                    /    \
                                       (6 < x < 9) 7      10 (9 < x < +inf)
    '''
    # check left branches
    # This is end condition, i.e. there is no number in left branch of current
    # node
        if root.left is None:
        # this is end condition. If we have reached to the leaf node, it means
        # all above nodes satisfied the condition. So, left branches that are
        # traversed have
        left_node = True
    # if there is number at left, it has to be lesser than the root.
    # Also, as the progression down the branch continues, the limit between which
    # the number has to fall starts to change.

    # when moving down left branch, we can see above that, left limit remains same
    # and right limit changes.
    elif ((root.data > root.left.data) and
            (right_limit > root.left.data > left_limit)
            ):
        left_node = isBinaryTree(root.left,
                                 left_limit=left_limit,
                                 right_limit=root.data)
    else:
        return False

    # check right branches
    if left_node:
        if root.right is None:
            right_node = True
        elif ((root.data < root.right.data) and
              (left_limit < root.right.data < right_limit)):
            right_node = isBinaryTree(root.right,
                                      left_limit=root.data,
                                      right_limit=right_limit)
        else:
            return False
    else:
        return False
    
    return left_node and right_node


def check_binary_search_tree_(root):
    if root.left is None:
        left_node = True
    elif root.left.data < root.data:
        left_node = check_binary_search_tree_(root.left)
    elif not(root.left.data < root.data):
        return False

    if not left_node:
        return False
    else:
        if root.right is None:
            right_node = True
        elif root.right.data > root.data:
            right_node = check_binary_search_tree_(root.right)
        elif not(root.right.data > root.data):
            return False
    if left_node and right_node:
        return True
