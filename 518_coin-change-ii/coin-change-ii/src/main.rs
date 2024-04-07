struct Solution {}

impl Solution {
    pub fn change(amount: i32, coins: Vec<i32>) -> i32 {
        if amount == 0 {
            return 1;
        }

        let mut cache = vec![vec![0; coins.len()]; amount as usize + 1];

        for coin_index in 0..coins.len() {
            cache[0][coin_index] = 1;
        }

        for amount_left in 1..(amount as usize + 1) {
            for coin_index in 0..coins.len() {
                cache[amount_left][coin_index] = (
                    if coin_index > 0 {
                        cache[amount_left][coin_index - 1]
                    } else {
                        0
                    } +
                    if amount_left >= coins[coin_index] as usize {
                        cache[amount_left - coins[coin_index] as usize][coin_index]
                    } else {
                        0
                    }
                );
            }
        }
        
        return cache[amount as usize][coins.len() - 1] as i32;
    }
}

fn main() {
    Solution::change(5, vec![1, 2, 5]);
}

#[test]
fn test_leetcode() {
    //assert_eq!(Solution::change(0, vec![]), 1);
    assert_eq!(Solution::change(5, vec![1, 2, 5]), 4);
}
