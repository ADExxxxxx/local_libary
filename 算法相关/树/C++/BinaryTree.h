#include <iostream>
using namespace std;
class BinaryTree {
public:

	BinaryTree* root = NULL;
	BinaryTree* lchild = NULL;
	BinaryTree* rchild = NULL;
	int data;

	
	static BinaryTree* preCreateBinaryTree(); 		//先序建立一个二叉树
	static BinaryTree* postCreateBinaryTree(); 		//后序建立一个二叉树
	static BinaryTree* inCreateBinaryTree(); 		//中序建立一个二叉树
	static BinaryTree* levelCreateBinaryTree(); 	//层序建立一个二叉树
	
	/*二叉树的遍历*/
	static void preOrder(BinaryTree *root); 		//先序遍历
	static void postOrder(BinaryTree *root);		//后序遍历
	static void inOrder(BinaryTree *root); 			//中序遍历
	static void levelOrder(BinaryTree *root);		//层序遍历

	/*二叉树的基本操作*/
	/*序列重构*/
	static BinaryTree* pre_postCreate(const int arr_pre[], const int arr_post[], int n);	//先序序列和后序序列重构二叉树
	static BinaryTree* pre_inCreate(const int arr_pre[], const int arr_in[], int n);		//先序序列和中序序列重构二叉树
	
	/*常用判断操作*/
	static bool isChildrenTree(const BinaryTree *root, const BinaryTree *other);	//判断other树是否是root树的子树
	static bool isSortTreePostSequence(const int arr_pre[]);						//判断是否序列是否是二叉搜索树的后序遍历序列
	
	/*其他*/
	static BinaryTree* mirrorTree( BinaryTree *root);							//得到树的镜像
	static int depthOfBinaryTree(const BinaryTree *root);							//得到二叉树的深度
	static bool findNodeOfBinaryTree(BinaryTree *root, int target, BinaryTree* &node, bool find);		//查找一个节点，若找到返回节点，若未找到返回false
	static int calNodeNum(BinaryTree *root);		//计算节点和
	static bool isSubTree(BinaryTree *tree1, BinaryTree *tree2);	//判断两棵树是否同构

private:
	static bool isSameNode(BinaryTree *tree1, BinaryTree *tree2){
		if(!tree1 && !tree2){
			return true;
		}
		if(!tree1 || !tree2){
			return false;
		}
		return tree1->data == tree2->data && isSameNode(tree1->lchild, tree2->lchild) && isSameNode(tree1->rchild, tree2->rchild);
	}
};