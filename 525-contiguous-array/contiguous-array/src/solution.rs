use std::cmp::max;
use std::collections::HashMap;

pub struct Solution {}

impl Solution {
    pub fn find_max_length(nums: Vec<i32>) -> i32 {
        // since the maximum prefix sums are bounded, you could use an array here
        // but the math of accounting for the negative bound is annoying
        // and you have to do a lot of work to convince the Rust compiler that
        // your implementation is type-safe
        let mut prefix_sums_to_leftmost_indices: HashMap<i32, i32> = HashMap::from([
            (0, -1)  // empty set has prefix sum of zero
        ]);
        let mut longest_subsequence_length: i32 = 0;
        let mut prefix_sum: i32 = 0;

        for (index, value) in nums.iter().enumerate() {
            // update prefix sum
            prefix_sum += if *value == 0 { -1 } else { 1 };

            match prefix_sums_to_leftmost_indices.get(&prefix_sum) {
                // if we can subtract a leftmost index
                Some(leftmost_index) => {
                    let subsequence_length = index as i32 - leftmost_index;
                    longest_subsequence_length = max(longest_subsequence_length, subsequence_length);
                },

                // if no leftmost index exists, index is leftmost index
                None => {
                    prefix_sums_to_leftmost_indices.insert(prefix_sum, index as i32);
                }
            }
        }

        return longest_subsequence_length;
    }
}


#[test]
fn test_leetcode() {
    assert_eq!(Solution::find_max_length(vec![0, 1]), 2);
    assert_eq!(Solution::find_max_length(vec![0, 1, 0]), 2);
}


#[test]
fn test_others() {
    assert_eq!(Solution::find_max_length(vec![0, 0, 0, 1, 1, 1]), 6);
    assert_eq!(Solution::find_max_length(vec![1, 0, 0, 0, 1, 1, 1]), 6);
    assert_eq!(Solution::find_max_length(vec![0, 0, 0, 1, 1, 1, 0]), 6);
    assert_eq!(Solution::find_max_length(vec![0, 0, 1, 0, 0, 0, 1, 1]), 6);
}
