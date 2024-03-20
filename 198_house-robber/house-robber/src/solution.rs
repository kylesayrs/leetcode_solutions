pub struct Solution {}

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let mut max_loot_i_plus_two = 0;
        let mut max_loot_i_plus_one = 0;

        for num in nums.rev() {
            let take_loot = num + max_loot_i_plus_two;
            let leave_loot = max_loot_i_plus_one;
            let max_loot = std::cmp::max(take_loot, leave_loot);

            max_loot_i_plus_two = max_loot_i_plus_one;
            max_loot_i_plus_one = max_loot;
        }

        return max_loot_i_plus_one;
    }
}


#[test]
fn test_leetcode() {
    assert_eq![Solution::rob(vec![1, 2, 3, 1]), 4];
    assert_eq![Solution::rob(vec![2, 7, 9, 3, 1]), 12];
    assert_eq![Solution::rob(vec![10, 0, 0, 10]), 20];
}
