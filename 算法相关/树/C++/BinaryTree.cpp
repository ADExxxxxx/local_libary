#include "BinaryTree.h"
#include <iostream>
#include <cstdlib>
#include <queue>
using namespace std;

/* 树的建立 */
BinaryTree* BinaryTree::preCreateBinaryTree(){
	BinaryTree* root;
	int a;
	cin >> a;
	if(a == 0){
		root = NULL;
	}
	else{
		root = (BinaryTree *)malloc(sizeof(BinaryTree));
		root -> data = a;
		root->lchild = preCreateBinaryTree();
		root->rchild = preCreateBinaryTree();
	}
	return root;
}

/* 树的遍历 */
void BinaryTree::preOrder(BinaryTree *root){
	if (!root){
		return; 
	}

	cout << root->data << " ";
	preOrder(root->lchild);
	preOrder(root->rchild);
}


void BinaryTree::postOrder(BinaryTree *root){
	if(!root){
		return;
	}

	postOrder(root->lchild);
	postOrder(root->rchild);
	cout << root->data << " ";
}
void BinaryTree::inOrder(BinaryTree *root){
	if(!root){
		return;
	}

	postOrder(root->lchild);
	cout << root->data << " ";
	postOrder(root->rchild);
}
void BinaryTree::levelOrder(BinaryTree *root){
	if (!root){
		return;
	}
	
	queue<BinaryTree* > Sequence;
	Sequence.push(root);
	while (!Sequence.empty()){
		BinaryTree* temp_node = Sequence.front();
		Sequence.pop();
		if(temp_node){
			cout << temp_node->data << " ";
			Sequence.push(temp_node->lchild);
			Sequence.push(temp_node->rchild);
		}
	}	
}

/*树的基本操作*/
int BinaryTree::depthOfBinaryTree(const BinaryTree *root){
	if(!root){
		return 0;
	}
	int ld = depthOfBinaryTree(root->lchild);
	int rd = depthOfBinaryTree(root->rchild);
	if(ld >= rd){
		return ld + 1; 
	}
	else{
		return rd + 1;
	}
	
} 

bool BinaryTree::findNodeOfBinaryTree(BinaryTree *root, int target, BinaryTree * &node, bool find){
	if(find){
		return true;
	}
	if (!root){
		return find; 
	}
	cout << "current node data is" << root->data << endl;
	if(root->data == target){
		cout << "find!" << endl;
		find = true;
		node = root;
		return find;
	}
	
	find = findNodeOfBinaryTree(root->lchild, target, node, find);
	find = findNodeOfBinaryTree(root->rchild, target, node, find);
	return find;
}

int BinaryTree::calNodeNum(BinaryTree* root){
	if(!root){
		return 0;
	}

	int num_l = calNodeNum(root->lchild);
	int num_r = calNodeNum(root->rchild);
	return num_l + num_r + root->data;
}

bool BinaryTree::isSubTree(BinaryTree *tree1, BinaryTree *tree2){
	if(!tree1){
		return false;
	}

	return BinaryTree::isSameNode(tree1, tree2) || BinaryTree::isSameNode(tree1->lchild, tree2) || BinaryTree::isSameNode(tree1->rchild, tree2);
}


BinaryTree* BinaryTree::mirrorTree(BinaryTree *root){
	if(!root){
		return NULL;
	}

	BinaryTree *temp;

	
	temp = root->lchild; 
	root->lchild = root->rchild;
	root->rchild = temp;

	mirrorTree(root->lchild);
	mirrorTree(root->rchild);

	return root;

}

BinaryTree* BinaryTree::pre_inCreate(const int arr_pre[], const int arr_in[], int n){
	int pos;
	for(int i = 0; i < n; i++){
		if(arr_in[i] == arr_pre[0]){
			pos = i; 
		}
	}
}