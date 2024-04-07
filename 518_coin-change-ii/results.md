Runtime
343ms
Beats 34.88% of users with Python3

Memory
27.24MB
Beats 50.94% of users with Python3

The idea here is to avoid duplicate sequences by at each decision choosing between two options:
    1. continue adding the coin at index i
    2. move on and never use coins before index i again

This guarantees never duplicating a sequence, since each separate path is not allowed to reuse
previously used coins. It is fully expressive too. It's like guaranteeing an ordering by only
considering sets of coins where the coins are ordered from least to greatest
