struct Solution {}

#[allow(unused_parens)]
#[allow(dead_code)]
impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut row_tables: [[bool; 9]; 9] = [[false; 9]; 9];
        let mut column_tables: [[bool; 9]; 9] = [[false; 9]; 9];
        let mut group_tables: [[[bool; 9]; 3]; 3] = [[[false; 9]; 3]; 3];

        for (row_index, row) in board.iter().enumerate() {
            for (col_index, &value_char) in row.iter().enumerate() {
                if value_char == '.' {
                    continue;
                }

                let value = value_char as usize - '1' as usize;
                let group_row = row_index / 3;
                let group_col = col_index / 3;

                if (
                    row_tables[row_index][value] ||
                    column_tables[col_index][value] ||
                    group_tables[group_row][group_col][value]
                ) {
                    return false;
                }

                row_tables[row_index][value] = true;
                column_tables[col_index][value] = true;
                group_tables[group_row][group_col][value] = true;
            }
        }

        return true;
    }
}


fn main() {}


#[test]
fn test_leetcode() {
    let board = vec![
        vec!['5','3','.','.','7','.','.','.','.'],
        vec!['6','.','.','1','9','5','.','.','.'],
        vec!['.','9','8','.','.','.','.','6','.'],
        vec!['8','.','.','.','6','.','.','.','3'],
        vec!['4','.','.','8','.','3','.','.','1'],
        vec!['7','.','.','.','2','.','.','.','6'],
        vec!['.','6','.','.','.','.','2','8','.'],
        vec!['.','.','.','4','1','9','.','.','5'],
        vec!['.','.','.','.','8','.','.','7','9']
    ];

    assert_eq!(Solution::is_valid_sudoku(board), true);

    let board = vec![
        vec!['8','3','.','.','7','.','.','.','.'],
        vec!['6','.','.','1','9','5','.','.','.'],
        vec!['.','9','8','.','.','.','.','6','.'],
        vec!['8','.','.','.','6','.','.','.','3'],
        vec!['4','.','.','8','.','3','.','.','1'],
        vec!['7','.','.','.','2','.','.','.','6'],
        vec!['.','6','.','.','.','.','2','8','.'],
        vec!['.','.','.','4','1','9','.','.','5'],
        vec!['.','.','.','.','8','.','.','7','9']
    ];

    assert_eq!(Solution::is_valid_sudoku(board), false);
}
