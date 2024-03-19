mod solution;

use solution::Solution;

fn main() {
    //let tasks = vec!['A', 'A', 'A', 'Z', 'Z', 'Z'];
    let tasks = vec!['A', 'A', 'A', 'Z', 'Z' ,'Z'];
    let n = 2;
    println!("{:?}", Solution::least_interval(tasks, n));
}
