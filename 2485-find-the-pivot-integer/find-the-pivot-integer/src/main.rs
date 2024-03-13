mod solution;

fn main() {
    println!("Hello, world!");

    for num in 0..10 {
        println!("Pivot integer for {:?} is {:?}", num, solution::Solution::pivot_integer(num));
    }
}
