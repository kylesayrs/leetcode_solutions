struct Solution {}

impl Solution {
    pub fn largest_perimeter(nums: Vec<i32>) -> i64 {
        // sort
        let mut nums = nums.iter().map(|&x| x as i64).collect::<Vec<i64>>();
        nums.sort_unstable();

        // compute total sum
        let mut sum: i64 = nums.iter().sum();

        // starting with max num, see if remainder is greater than num 
        for &num in nums.iter().rev() {
            sum -= num;

            if sum > num {
                return (sum + num) as i64;
            }
        }

        return -1;
    }
}


fn main() {
    println!("{:?}", Solution::largest_perimeter(vec![1, 2, 3]));
}


#[test]
fn test_leetcode() {
    assert_eq!(Solution::largest_perimeter(vec![5, 5, 5]), 15);
    assert_eq!(Solution::largest_perimeter(vec![1,12,1,2,5,50,3]), 12);
    assert_eq!(Solution::largest_perimeter(vec![5,5,50]), -1);
}
