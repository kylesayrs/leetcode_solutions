use std::collections::HashSet;

struct Solution {}

#[allow(unused_parens)]
impl Solution {
    fn can_reach_target(
        i: i32,
        j: i32,
        char_index: usize,
        board: &Vec<Vec<char>>,
        height: usize,
        width: usize,
        word_chars: &Vec<char>,
        seen: &mut HashSet<(i32, i32)>
    ) -> bool {
        // end string condition
        if char_index >= word_chars.len() {
            return true;
        }

        // out of bounds condition
        if (
            i < 0 ||
            i >= height as i32 ||
            j < 0 ||
            j >= width as i32
        ) {
            return false;
        }

        // character failure condition
        if board[i as usize][j as usize] != word_chars[char_index] {
            return false;
        }

        // seen condition
        if seen.contains(&(i, j)) {
            return false;
        }
        seen.insert((i, j));

        // character success, recurse
        let found_solution = (
            Solution::can_reach_target(i - 1, j, char_index + 1, board, height, width, word_chars, seen) ||
            Solution::can_reach_target(i + 1, j, char_index + 1, board, height, width, word_chars, seen) ||
            Solution::can_reach_target(i, j - 1, char_index + 1, board, height, width, word_chars, seen) ||
            Solution::can_reach_target(i, j + 1, char_index + 1, board, height, width, word_chars, seen)
        );

        if !found_solution {
            seen.remove(&(i, j));
        }

        return found_solution;
    }

    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let height = board.len();
        if height <= 0 {
            return false;
        }
        let width = board[0].len();
        let word_chars: Vec<char> = word.chars().collect::<Vec<char>>();

        let positions = (0..height).flat_map(|i|
            (0..width).map(move |j|
                (i as i32, j as i32)
            )
        );
        for (i, j) in positions {
            let mut seen: HashSet<(i32, i32)> = HashSet::new();
            if Solution::can_reach_target(i, j, 0, &board, height, width, &word_chars, &mut seen) {
                return true;
            }
        }

        return false;
    }
}


fn main() {
    let board = vec![
        vec!['A','B','C','E'],
        vec!['S','F','C','S'],
        vec!['A','D','E','E']
    ];

    let word = String::from("ABCCED");

    println!("{:?}", Solution::exist(board, word));
}


#[test]
fn test_leetcode() {
    /*
    assert_eq!(Solution::exist(
        vec![
            vec!['A','B','C','E'],
            vec!['S','F','C','S'],
            vec!['A','D','E','E']
        ],
        String::from("ABCCED")
    ), true);

    assert_eq!(Solution::exist(
        vec![
            vec!['A','B','C','E'],
            vec!['S','F','C','S'],
            vec!['A','D','E','E']
        ],
        String::from("SEE")
    ), true);

    assert_eq!(Solution::exist(
        vec![
            vec!['A','B','C','E'],
            vec!['S','F','C','S'],
            vec!['A','D','E','E']
        ],
        String::from("ABCB")
    ), false);
    */

    assert_eq!(Solution::exist(
        vec![
            vec!['A','B','C','E'],
            vec!['S','F','E','S'],
            vec!['A','D','E','E']
        ],
        String::from("ABCESEEEFS")
    ), true);
}
