struct Solution {}

impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        if cost.len() <= 2 {
            cost.iter().min().unwrap();
        }

        let mut min_cost_i_plus_two = 0;
        let mut min_cost_i_plus_one = cost[cost.len().wrapping_sub(1)];

        for c in cost.iter().rev().skip(1).cloned().collect::<Vec<i32>>() {
            let cost_i = c + std::cmp::min(min_cost_i_plus_one, min_cost_i_plus_two);

            min_cost_i_plus_two = min_cost_i_plus_one;
            min_cost_i_plus_one = cost_i;
        }

        std::cmp::min(min_cost_i_plus_one, min_cost_i_plus_two)
    }
}

fn main() {
    println!("{:?}", Solution::min_cost_climbing_stairs(vec![10, 15, 20]));
    println!("{:?}", Solution::min_cost_climbing_stairs(vec![1,100,1,1,1,100,1,1,100,1]));
}
