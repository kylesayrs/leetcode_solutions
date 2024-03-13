pub struct Solution {}

impl Solution {
    pub fn pivot_integer(n: i32) -> i32 {
        let candidate_float: f32 = f32::sqrt(
            (
                i32::pow(n, 2) + n
            ) as f32 / 2.0
        );
        let candidate_floored = candidate_float.floor();
        
        if candidate_float == candidate_floored {
            candidate_floored as i32
        } else {
            -1
        } 
    }
}


#[test]
fn leetcode_tests() {
    assert_eq!(Solution::pivot_integer(8), 6);
    assert_eq!(Solution::pivot_integer(1), 1);
    assert_eq!(Solution::pivot_integer(4), -1);
}
