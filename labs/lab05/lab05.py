"""Lab 5: Trees."""


from __future__ import annotations
from tree import Tree, is_leaf


def sprout_leaves[T](t: Tree[T], leaves: list[T]) -> Tree[T]:
  """Sprout new leaves containing the labels in leaves at each leaf of
  the original tree t and return the resulting tree.

  >>> t = Tree(1, [Tree(2), Tree(3)])
  >>> print(t)
  1
    2
    3
  >>> print(sprout_leaves(t, [4, 5]))
  1
    2
      4
      5
    3
      4
      5

  >>> u = Tree(1, [Tree(2, [Tree(3)])])
  >>> print(u)
  1
    2
      3
  >>> print(sprout_leaves(u, [6, 1, 2]))
  1
    2
      3
        6
        1
        2
  """
  "*** YOUR CODE HERE ***"  # replace the code below
  if is_leaf(t):
    t.branches = [Tree(label) for label in leaves]
  else:
    for branch in t.branches:
      sprout_leaves(branch, leaves)
  return t


def pathsum(t: Tree[int], n: int) -> bool:
  """Return whether there is a path from the root of t to a leaf whose
  labels sum to n.

  >>> t = Tree(2, [Tree(3, [Tree(5), Tree(7)]), Tree(4)])
  >>> pathsum(t, 12) # 2 -> 3 -> 7
  True
  >>> pathsum(t, 5)  # A path that doesn't reach a leaf such as 2 -> 3 doesn't count
  False
  """
  "*** YOUR CODE HERE ***"  # replace the code below
  if is_leaf(t):
    return t.label == n
  return any(pathsum(branch, n - t.label) for branch in t.branches)


def prune_leaves[T](t: Tree[T], vals: tuple[T, ...]) -> Tree[T] | None:
  """Return a version of t with all leaves that have a label
  that appears in vals removed.  Return None if the entire tree is
  pruned away.

  >>> t = Tree(2)
  >>> print(prune_leaves(t, (1, 2)))
  None
  >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
  >>> print(numbers)
  1
    2
    3
      4
      5
    6
      7
  >>> print(prune_leaves(numbers, (3, 4, 6, 7)))
  1
    2
    3
      5
    6
  """
  "*** YOUR CODE HERE ***"  # replace the code below
  if is_leaf(t) and t.label in vals:
    return None
  else:
    new_branches = []
    for b in t.branches:
      new_branch = prune_leaves(b, vals)
      if new_branch is not None:
        new_branches.append(new_branch)
    t.branches = new_branches
    return t


def sum_tree(t: Tree[int]) -> int:
  """Add all elements in a tree.

  >>> t = Tree(4, [Tree(2, [Tree(3)]), Tree(6)])
  >>> sum_tree(t)
  15
  """
  "*** YOUR CODE HERE ***"  # replace the code below
  if is_leaf(t):
    return t.label
  return t.label + sum(sum_tree(branch) for branch in t.branches)

def balanced(t: Tree[int]) -> bool:
  """Checks if each branch has same sum of all elements and
  if each branch is balanced.

  >>> t = Tree(1, [Tree(3), Tree(1, [Tree(2)]), Tree(1, [Tree(1), Tree(1)])])
  >>> balanced(t)
  True
  >>> u = Tree(1, [t, Tree(1)])
  >>> balanced(u)
  False
  >>> t = Tree(1, [Tree(4), Tree(1, [Tree(2), Tree(1)]), Tree(1, [Tree(3)])])
  >>> balanced(t)
  False
  """
  "*** YOUR CODE HERE ***"  # replace the code below
  if is_leaf(t):
    return True
  
  sums = [sum_tree(branch) for branch in t.branches]
  if len(set(sums)) != 1:
    return False
  return all(balanced(branch) for branch in t.branches)
    
