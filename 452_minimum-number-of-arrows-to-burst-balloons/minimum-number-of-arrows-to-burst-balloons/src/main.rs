mod solution;

use solution::Solution;

fn main() {
    let points = vec![vec![10, 16], vec![2, 8], vec![1, 6], vec![7, 12]];
    println!("{:?}", Solution::find_min_arrow_shots(points));
}
