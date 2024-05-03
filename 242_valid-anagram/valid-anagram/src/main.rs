use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut freq: HashMap<char, usize> = HashMap::new();

        for s_char in s.chars() {
            let prev_value = match freq.get(&s_char) {
                Some(value) => *value,
                None => 0
            };

            freq.insert(s_char, prev_value + 1);
        }

        for t_char in t.chars() {
            match freq.get_mut(&t_char) {
                Some(value) => {
                    if *value <= 0 {
                        return false;
                    }

                    *value -= 1;

                    if *value <= 0 {
                        freq.remove(&t_char);
                    }
                },
                None => { return false }
            };
        }

        if freq.keys().len() > 0 {
            return false;
        }

        return true;
    }
}


fn main() {
    println!("Hello, world!");
}

#[test]
fn test_leetcode() {
    assert_eq!(Solution::is_anagram(String::from("abc"), String::from("abc")), true);
    assert_eq!(Solution::is_anagram(String::from("aaa"), String::from("abc")), false);
    assert_eq!(Solution::is_anagram(String::from("cba"), String::from("abc")), true);
    assert_eq!(Solution::is_anagram(String::from("cba"), String::from("abcd")), false);
    assert_eq!(Solution::is_anagram(String::from("cbad"), String::from("abc")), false);
    assert_eq!(Solution::is_anagram(String::from(""), String::from("")), true);
    assert_eq!(Solution::is_anagram(String::from(""), String::from("d")), false);
    assert_eq!(Solution::is_anagram(String::from("d"), String::from("")), false);
}
