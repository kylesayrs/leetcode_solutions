use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn find_different_binary_string(nums: Vec<String>) -> String {
        let mut nums_set: HashSet<usize> = HashSet::new();

        for num in nums.iter() {
            nums_set.insert(usize::from_str_radix(num, 2).unwrap());
        }

        for num in 0..=nums.len().pow(2) {
            match nums_set.get(&num) {
                Some(_) => {},
                None => return format!("{:0>width$b}", num, width = nums.len())
            }
        }

        String::from("")
    }
}

fn main() {
    println!("Hello, world!");
}


#[test]
fn test_leetcode() {
    assert_eq!(
        Solution::find_different_binary_string(
            vec![String::from("01"), String::from("10")]
        ),
        String::from("00")
    );

    assert_eq!(
        Solution::find_different_binary_string(
            vec![String::from("0")]
        ),
        String::from("1")
    );
}
