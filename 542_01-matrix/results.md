Runtime
504ms
Beats 35.43% of users with Python3

Memory
20.82MB
Beats 12.21% of users with Python3


The reason why dfs doesn't work is that the recursive definition implies that you
are dependent on your neighbors. However, if your neighbors are part of the
dfs stack, then you cannot depend on them.

Using bfs is better, since for this problem you only need to depend on neighbors
in order of closeness to a 0. Since bfs gets results in order of closeness to 0s,
this is okay.
