#include "divide-and-conquer_2.h"

// Counts the paths that start at node, go downwards and have sum equal to sum.
int count(TreeNode *node, int sum) {
  if (node == nullptr) return 0;
  return (node->val == sum) + count(node->left, sum - node->val) +
         count(node->right, sum - node->val);
}

// Separately counts the paths lying entirely in the left and in the right subtree.
int pathSum(TreeNode *root, int sum) {
  if (root == nullptr) return 0;
  return count(root, sum) + pathSum(root->left, sum) +
         pathSum(root->right, sum);
}
