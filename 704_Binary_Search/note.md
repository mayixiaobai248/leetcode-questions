some little things to know:
>+ we use [left,right) to solve.
>+ the loop condition is left<right (left==right is nonsense)
>+ if: right=middle (because we don't need right), left=middle+1
>+ remember:middle=left+(right-left)//2