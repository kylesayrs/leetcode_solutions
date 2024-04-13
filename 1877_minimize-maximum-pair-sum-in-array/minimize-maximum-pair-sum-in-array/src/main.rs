struct Solution {}

impl Solution {
    pub fn min_pair_sum(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();

        let mut max: i32 = i32::MIN;
        for i in 0..(nums.len() >> 1) {
            max = std::cmp::max(max, nums[i] + nums[nums.len() - i - 1]);
        }

        max
    }
}

fn main() {
    println!("Hello, world!");
}
