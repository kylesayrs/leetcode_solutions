mod solution;

use solution::Solution;

fn main() {
    println!("{:?}", Solution::insert(vec![vec![1, 3], vec![6, 9]], vec![2, 5]));
    assert_eq!(Solution::insert(vec![vec![1, 3], vec![6, 9]], vec![2, 5]), vec![vec![1, 5], vec![6, 9]]);
}
