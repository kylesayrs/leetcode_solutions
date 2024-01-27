#[derive(Debug)]
pub enum MinimumCostError {
    VecUnderflow,
    VecOverflow,
}

pub struct Solution {}

impl Solution {
    pub fn minimum_cost(nums: Vec<i32>) -> Result<i32, MinimumCostError> {
        if nums.len() < 3 {
            return Err(MinimumCostError::VecUnderflow);
        }

        if nums.len() > 30 {
            return Err(MinimumCostError::VecOverflow);
        }

        let mut min_small = i32::MAX;
        let mut min_large = i32::MAX;

        for num in nums[1..].iter() {
            if *num < min_small {
                min_large = min_small;
                min_small = *num;
            } else if *num < min_large {
                min_large = *num;
            }
        }

        println!("min_small: {}, min_large: {}", min_small, min_large);
        
        Ok(nums[0] + min_small + min_large)
    }
}


/* Unit tests */


#[test]
fn error_tests() {
    match Solution::minimum_cost(vec![]) {
        Err(MinimumCostError::VecUnderflow) => assert!(true),
        _ => assert!(false)
    }

    match Solution::minimum_cost(vec![]) {
        Err(MinimumCostError::VecUnderflow) => assert!(true),
        _ => assert!(false)
    }
}



#[test]
fn leetcode_tests() {
    match Solution::minimum_cost(vec![1, 2, 3]) {
        Ok(min_cost) => assert_eq!(min_cost, 6),
        _ => assert!(false)
    }

    match Solution::minimum_cost(vec![5, 4, 3]) {
        Ok(min_cost) => assert_eq!(min_cost, 12),
        _ => assert!(false)
    }

    match Solution::minimum_cost(vec![10, 3, 1, 1]) {
        Ok(min_cost) => assert_eq!(min_cost, 12),
        _ => assert!(false)
    }
}


#[test]
fn basic_tests() {
    match Solution::minimum_cost(vec![1; 10]) {
        Ok(min_cost) => assert_eq!(min_cost, 3),
        _ => assert!(false)
    }

    match Solution::minimum_cost(vec![9, 8, 7, 1, 9]) {
        Ok(min_cost) => assert_eq!(min_cost, 17),
        _ => assert!(false)
    }

    match Solution::minimum_cost(vec![3, 2, 1, 2, 1]) {
        Ok(min_cost) => assert_eq!(min_cost, 5),
        _ => assert!(false)
    }
}
