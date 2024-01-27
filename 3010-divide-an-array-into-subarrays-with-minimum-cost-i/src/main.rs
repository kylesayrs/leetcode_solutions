mod solution;
use solution::*;


fn main() {
    let input = vec![1, 2, 3];

    match Solution::minimum_cost(input) {
        Ok(min_cost) => println!("Minimum cost is {:?}", min_cost),
        Err(MinimumCostError::VecUnderflow) => eprintln!("Vector underflow!"),
        Err(MinimumCostError::VecOverflow) => eprintln!("Vector overflow!")
    }
}
