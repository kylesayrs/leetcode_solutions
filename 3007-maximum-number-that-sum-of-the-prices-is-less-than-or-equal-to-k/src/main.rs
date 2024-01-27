mod solution;
use solution::*;


fn main() {
    match Solution::find_maximum_number(3278539330613, 5) {
        Ok(max_num) => println!("solution: {}", max_num),
        Err(error) => println!("error: {}", error)
    }
}
