/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
    private:
        vector<int >result;
        void rightSide(TreeNode * root,int level)
        {
            if(root)
            {
                if(result.size()<=level)
                    result.push_back(root->val);
                rightSide(root->right,level+1);
                rightSide(root->left,level+1);
            }
        }
        
public:
    vector<int> rightSideView(TreeNode* root) 
    {

        result.clear();
        if(root==nullptr) return result;
        rightSide(root,0);
        return result;
    }
};