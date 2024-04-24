struct Solution {}

impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        /*
        Dynamic programming with max subarray ending with index
        */
        
        let mut max_subarray = 0;
        let mut prev_max_subarray = 0;
        for num in &nums {
            // can choose to not include
            let current_max_subarray = std::cmp::max(prev_max_subarray + num, 0);

            // update max cache
            max_subarray = std::cmp::max(max_subarray, current_max_subarray);

            // iterate
            prev_max_subarray = current_max_subarray;
        }

        // if decided not to take any positive numbers, use the max of the array
        if max_subarray == 0 {
            return nums.iter().max().unwrap().clone();
        }

        return max_subarray;
    }
}


fn main() {
    println!("Hello, world!");
}


#[test]
fn test_leetcode() {
    assert_eq!(Solution::max_sub_array(vec![-2,1,-3,4,-1,2,1,-5,4]), 6);
    assert_eq!(Solution::max_sub_array(vec![1]), 1);
    assert_eq!(Solution::max_sub_array(vec![-1]), -1);
}
