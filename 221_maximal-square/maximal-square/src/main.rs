struct Solution {}

impl Solution {
    pub fn max_square_cell(row: usize, column: usize, side_lens: &Vec<Vec<u32>>) -> u32 {
        let top_left = side_lens[row][column];
        if top_left <= 0 {
            return 0;
        }

        let right = match side_lens.get(row) {
            Some(inner_vec) => match inner_vec.get(column + 1) {
                Some(&num) => num,
                None => 0,
            },
            None => 0,
        };

        let bottom = match side_lens.get(row + 1) {
            Some(inner_vec) => match inner_vec.get(column) {
                Some(&num) => num,
                None => 0,
            },
            None => 0,
        };

        let bottom_right = match side_lens.get(row + 1) {
            Some(inner_vec) => match inner_vec.get(column + 1) {
                Some(&num) => num,
                None => 0,
            },
            None => 0,
        };
        
        let tmp = *[right, bottom, bottom_right].iter().min().unwrap() + 1;

        return tmp;
    }

    pub fn maximal_square(matrix: Vec<Vec<char>>) -> i32 {
        let height = matrix.len();
        let width = matrix.get(0).unwrap().len();

        let mut side_lens: Vec<Vec<u32>> = matrix
            .iter()
            .map(|row| row.iter().map(|&c| c.to_digit(10).unwrap()).collect())
            .collect();

        for layer_index in 0..std::cmp::min(width, height) {
            let layer_row = height - 1 - layer_index;
            let layer_column = width - 1 - layer_index;

            for row in (0..=layer_row).rev() {
                side_lens[row][layer_column] = Solution::max_square_cell(row, layer_column, &side_lens);
            }

            for column in (0..=layer_column).rev() {
                side_lens[layer_row][column] = Solution::max_square_cell(layer_row, column, &side_lens);
            }
        }

        side_lens
            .iter()
            .map(|row| row.iter().max().unwrap())
            .max().unwrap()
            .pow(2) as i32
    }
}

fn main() {
    println!("Hello, world!");
}


#[test]
fn test_leetcode() {
    assert_eq!(
        Solution::maximal_square(vec![
            vec!['0']
        ]),
        0
    );

    assert_eq!(
        Solution::maximal_square(vec![
            vec!['0', '1'],
            vec!['1', '0'],
        ]),
        1
    );

    assert_eq!(
        Solution::maximal_square(vec![
            vec!['1', '1'],
            vec!['1', '1'],
        ]),
        4
    );

    assert_eq!(
        Solution::maximal_square(vec![
            vec!['0', '1'],
            vec!['1', '1'],
        ]),
        1
    );

    assert_eq!(
        Solution::maximal_square(vec![
            vec!['1', '0'],
            vec!['1', '1'],
        ]),
        1
    );

    assert_eq!(
        Solution::maximal_square(vec![
            vec!['1', '1'],
            vec!['0', '1'],
        ]),
        1
    );

    assert_eq!(
        Solution::maximal_square(vec![
            vec!['1', '1'],
            vec!['1', '0'],
        ]),
        1
    );

    assert_eq!(
        Solution::maximal_square(vec![
            vec!['1', '1'],
            vec!['1', '0'],
        ]),
        1
    );

    assert_eq!(
        Solution::maximal_square(vec![
            vec!['1', '1', '1'],
            vec!['1', '0', '1'],
        ]),
        1
    );

    assert_eq!(
        Solution::maximal_square(vec![
            vec!['1', '1', '1'],
            vec!['1', '1', '1'],
        ]),
        4
    );

    assert_eq!(
        Solution::maximal_square(vec![
            vec!['0', '1', '1'],
            vec!['0', '1', '1'],
        ]),
        4
    );

    assert_eq!(
        Solution::maximal_square(vec![
            vec!['1','0','1','0','0'],
            vec!['1','0','1','1','1'],
            vec!['1','1','1','1','1'],
            vec!['1','0','0','1','0']
        ]),
        4
    );
}
