#include "divide-and-conquer_2.h"

// Broji putove koji počinju u node, idu prema dolje i imaju zbroj sum.
int count(TreeNode *node, int sum) {
  if (node == nullptr) return 0;
  return (node->val == sum) + count(node->left, sum - node->val) +
         count(node->right, sum - node->val);
}

// Zasebno broji putove koji su u cijelosti u lijevom odnosno desnom podstablu.
int pathSum(TreeNode *root, int sum) {
  if (root == nullptr) return 0;
  return count(root, sum) + pathSum(root->left, sum) +
         pathSum(root->right, sum);
}
