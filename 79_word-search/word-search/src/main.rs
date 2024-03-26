/*
Implementing this in rust is really hard
You have to deal with a ton of recursive
borrowing and closures. I need to learn
more about rust and come back to this,
although I doubt that there's an easy
or best way to do this ¯\_(ツ)_/¯
*/

use std::collections::HashSet;

struct Solution {}

#[allow(unused_parens)]
impl Solution {
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let height = board.len();
        if height <= 0 {
            return false;
        }
        let width = board[0].len();

        let word_chars: Vec<char> = word.chars().collect::<Vec<char>>();

        let can_reach_target = |i: i32, j: i32, char_index: usize, mut seen: HashSet<(i32, i32)>| -> bool {
            // character success condition
            if char_index <= 0 {
                return true;
            }

            // out of bounds condition
            if (
                i < 0 ||
                i > height as i32 ||
                j < 0 ||
                j > width as i32
            ) {
                return false;
            }

            // character condition
            if board[i as usize][j as usize] != word_chars[char_index] {
                return false;
            }

            // seen condition
            if seen.contains(&(i, j)) {
                return false;
            }
            seen.insert((i, j));

            // recurse
            return (
                can_reach_target(i - 1, j, seen) ||
                can_reach_target(i + 1, j, seen) ||
                can_reach_target(i, j - 1, seen) ||
                can_reach_target(i, j + 1, seen)
            )
        };

        let positions = (0..height).flat_map(|i|
            (0..width).map(move |j|
                (i as i32, j as i32)
            )
        );

        for (i, j) in positions {
            let seen: HashSet<(i32, i32)> = HashSet::new();
            if can_reach_target(i, j, 0, seen) {
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
