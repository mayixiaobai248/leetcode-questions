# 7.31第一次做

这道题目很简单，十分钟以内就可以做完

直接用字典储存零钱包，

>+ 如果是5元的话，直接存入零钱包
>+ 如果是10元，检查是否可以找零，同时存入零钱包
>+ 如果是20元，检查是否可以找零（两种情况）

如果不能找零，直接返回False，如果全部可以找零，返回True