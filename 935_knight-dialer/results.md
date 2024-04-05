Runtime
3045ms
Beats 9.30% of users with Python3

Memory
27.44MB
Beats 43.51% of users with Python3

While this solution is technically O(n) since there are n many calls to each
of the spaces, it is memory inefficient since if we started each knight at
each of the spaces, then all knights traversed down each of their possible moves
all at once, we could remove the memory from the previous moves, therefore only
needing an array of size 10
