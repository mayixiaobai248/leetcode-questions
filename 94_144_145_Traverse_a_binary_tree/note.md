We use recursion method to traverse binary tree. There are three orders to traversal: preorder, inorder and postorder.

**About Recursion**
>
>+ (1) determine the return value and parameters
>+ (2) determine the stopping condition
>+ (3) confirm the single-layer recursion logic

In these questions, we use left and right to record left-subtree and right-subtree, the data structure of them are list. 

Finally, we return the combination of list of three parts. (for example, left+[root.val]+right)

**Something need to know:**
add three list:[a,b,c]+[d,e,f,g]+[]+[h]=[a,b,c,d,e,f,g,h], we use this to return value.
