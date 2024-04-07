struct Solution {
}

impl Solution {
    pub fn arrange_coins(mut n: i32) -> i32 {
        let mut column_index: i32 = 0;
        loop {
            n -= column_index;
            
            // exact match
            if n == 0 {
                return column_index;
            }

            // overstep by one, borrow from first column
            if n == -1 {
                return column_index - 1;
            }

            // overstep by more than one, revert last column
            if n < -1 {
                return column_index - 1;
            }

            column_index += 1;
        }
    }
}

fn main() {}

#[test]
fn test_leetcode() {
    assert_eq!(Solution::arrange_coins(0), 0);
    assert_eq!(Solution::arrange_coins(1), 1);
    assert_eq!(Solution::arrange_coins(2), 1);
    assert_eq!(Solution::arrange_coins(3), 2);
}
