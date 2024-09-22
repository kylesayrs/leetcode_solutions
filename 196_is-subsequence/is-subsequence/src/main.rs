struct Solution {}

impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        if s.len() <= 0 {
            return true;
        }

        let s_chars: Vec<char> = s.chars().collect();
        let mut s_index = 0;

        for t_char in t.chars() {
            if t_char == s_chars[s_index] {
                s_index += 1;
                if s_index == s.len() {
                    return true
                }
            }
        }

        return s_index == s.len();
    }
}


fn main() {
    println!("Hello, world!");
}
