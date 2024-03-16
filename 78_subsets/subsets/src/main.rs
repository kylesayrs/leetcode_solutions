#[macro_use(queue)]
extern crate queues;

mod solution;

fn main() {
    let set = vec![1, 2, 3];
    println!("{:?}", solution::Solution::subsets(set));
}
