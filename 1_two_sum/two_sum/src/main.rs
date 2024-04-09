use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut addend_lookup: HashMap<i32, usize> = HashMap::new();
        
        for (index, &num) in nums.iter().enumerate() {
            let addend = target - num;
            match addend_lookup.get(&addend) {
                Some(addend_index) => {
                    return vec![
                        index as i32,
                        *addend_index as i32
                    ];
                },
                None => {}
            }

            addend_lookup.insert(num, index);
        }

        return vec![];
    }
}

fn main() {
    println!("Hello, world!");
}
