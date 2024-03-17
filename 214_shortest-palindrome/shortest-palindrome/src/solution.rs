use rand::Rng;

pub struct Solution {}

impl Solution {
    fn is_palindrome(s: &String) -> bool {
        s.chars().eq(s.chars().rev())
    }

    pub fn shortest_palindrome(s: String) -> String {
        let mut string: String = s.clone();
        let mut addend: String = String::new();

        while !Solution::is_palindrome(&string) {
            match string.pop() {
                Some(last_character) => addend.push(last_character),
                None => panic!["Tried to pop from empty string"]
            }
        }

        return addend + &s.clone();
    }
}


#[test]
fn test_leetcode() {
    assert_eq![
        Solution::shortest_palindrome(String::from("aacecaaa")),
        String::from("aaacecaaa")
    ];

    assert_eq![
        Solution::shortest_palindrome(String::from("abcd")),
        String::from("dcbabcd")
    ];
}


#[test]
fn test_all_as() {
    match String::from_utf8(vec![b'A'; 1000000]) {
        Ok(s) => {
            assert_eq![
                Solution::shortest_palindrome(s.clone()),
                s
            ]
        }
        Err(_) => panic![]
    }
}


#[test]
fn test_random() {
    let mut rng = rand::thread_rng();
    let numbers: Vec<u8> = (0..1000000).map(|_| {
        rng.gen_range(65..=122)
    }).collect();

    match String::from_utf8(numbers) {
        Ok(s) => {
            assert![Solution::is_palindrome(&Solution::shortest_palindrome(s))]
        }
        Err(_) => panic![]
    }
}
