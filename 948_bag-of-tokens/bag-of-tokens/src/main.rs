pub struct Solution {}

impl Solution {
    pub fn bag_of_tokens_score(mut tokens: Vec<i32>, power: i32) -> i32 {
        if tokens.len() <= 0 {
            return 0;
        }

        tokens.sort_unstable();

        let mut left = 0;
        let mut right = tokens.len() - 1;

        let mut score = 0;
        let mut power = power;
        let mut max_score = 0;

        while left <= right {
            if tokens[left] <= power {
                score += 1;
                power -= tokens[left];
                left += 1;
                max_score = std::cmp::max(max_score, score);
                continue;
            }

            if score > 0 {
                score -= 1;
                power += tokens[right];
                right -= 1;
                continue;
            }

            break;
        }

        return max_score;
    }
}

fn main() {
    println!("{:?}", Solution::bag_of_tokens_score(vec![], 54));
}
