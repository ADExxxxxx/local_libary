#include "BinaryTree.h"
#include <iostream>


using namespace std;

int main(){
    BinaryTree* root;
    BinaryTree* other;

    cout << "create tree root:" << endl;
    root = BinaryTree::preCreateBinaryTree();
    cout << "\nthe pre order of root Sequence is: " << endl;
    BinaryTree::preOrder(root);

    cout << "\ncreate tree other:" << endl;
    other = BinaryTree::preCreateBinaryTree();
    cout << "\nthe pre order of other Sequence is: " << endl;
    BinaryTree::preOrder(other);

    bool flag = BinaryTree::isSubTree(root, other);
    cout << "\nflag is: " << flag << endl;

    root = BinaryTree::mirrorTree(root);
    cout << "\nthe pre order of mirror Sequence is: " << endl;
    BinaryTree::preOrder(root);


    
    // const int arr_pre[] = {20, 15, 10, 12, 18, 16, 17, 25, 30};
    // const int arr_in[] = {10, 12, 15, 16, 17, 18, 20, 25, 30};
    
    return 0;
}
