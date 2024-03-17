mod solution;

use solution::Solution;

fn main() {
    println!("{:?}", Solution::shortest_palindrome(String::from("abcd")));
}
