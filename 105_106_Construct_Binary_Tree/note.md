# construct a tree from 2 different orders

**<font color='red'>can do it again!!</font>**

For this question, I read the process from <https://programmercarl.com/0106.%E4%BB%8E%E4%B8%AD%E5%BA%8F%E4%B8%8E%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE> and done coding by myself in 10 min.

The process are as follows:
>
>+ if the list is null, there is no Node in tree, we return None.
>+ the root node is the last value of postorder, we get the value.
>+ find the corresponding value in inorder, and get its index.
>+ split the inorder list into left_inorder and right_inorder
>+ split the postorder list into left_post and right_post
>+ just recursion

something to pay attation:
>
>+ justify whether a list is null:         if not preorder
