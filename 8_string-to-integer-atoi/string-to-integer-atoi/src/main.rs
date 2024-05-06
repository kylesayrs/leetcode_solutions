pub struct Solution {}

impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        if chars.len() <= 0 {
            return 0;
        }

        let mut integer: i32 = 0;
        let mut is_negative = false;
        let mut integer_started = false;
        for c in chars {
            // skip leading whitespaces
            if !integer_started && c == ' ' {
                continue;
            }

            // check for positive
            if !integer_started && c == '+' {
                is_negative = false;
                integer_started = true;
                continue;
            }

            // check for negative
            if !integer_started && c == '-' {
                is_negative = true;
                integer_started = true;
                continue;
            }

            // stop at non-digits
            if c < '0' || c > '9' {
                break;
            }

            // leading zeros are handled implicitly
            integer_started = true;
            if !is_negative {
                integer = integer
                    .checked_mul(10)
                    .and_then(|integer| integer.checked_add(c as i32 - '0' as i32))
                    .unwrap_or(i32::MAX);

            } else {
                integer = integer
                    .checked_mul(10)
                    .and_then(|integer| integer.checked_sub(c as i32 - '0' as i32))
                    .unwrap_or(i32::MIN);
            }
        }

        integer
    }
}


fn main() {
    println!("Hello, world!");
}

#[test]
fn test_leetcode() {
    println!("{}", Solution::my_atoi(String::from("3147483648")));
    println!("{}", Solution::my_atoi(String::from("-3147483648")));

    assert!(false);
    //let int_min: i32 = -(2 as i32).pow(31);

    //assert_eq!(Solution::my_atoi(String::from("3147483648")), int_max);
    //assert_eq!(Solution::my_atoi(String::from("-3147483648")), int_min);
}
