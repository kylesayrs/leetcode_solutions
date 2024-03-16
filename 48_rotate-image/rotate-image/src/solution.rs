pub struct Solution {}

impl Solution {
    fn get_rotation_start_positions(size: usize) -> Vec<(usize, usize)> {
        // to avoid double counting rotations in odd-dimension images,
        // do not rotate the bottom row (round the height down)
        let half_size = size as f32 / 2.0;
        let half_round_down = half_size.floor() as usize;
        let half_round_up = half_size.ceil() as usize;

        (0 .. half_round_down).map(move |i|
            (0 .. half_round_up).map(move |j|
                (i, j)
            )
        ).flatten().collect::<Vec<(usize, usize)>>()
    }


    fn get_right_rotation_pos(size: usize, pos: (usize, usize)) -> (usize, usize) {
        (pos.1, size - pos.0 - 1)
    }


    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let size = matrix.len();

        let positions = Solution::get_rotation_start_positions(size);

        for &(mut pos) in positions.iter() {
            let mut pos_value = matrix[pos.0][pos.1];

            for _index in 0 .. 4 {
                let next_pos = Solution::get_right_rotation_pos(size, pos);
                let next_pos_value = matrix[next_pos.0][next_pos.1];

                matrix[next_pos.0][next_pos.1] = pos_value;

                pos = next_pos;
                pos_value = next_pos_value;
            }
        }
    }
}


fn matrices_equal(matrix1: &Vec<Vec<i32>>, matrix2: &Vec<Vec<i32>>) -> bool {
    if matrix1.len() != matrix2.len() {
        return false;
    }

    for i in 0 .. matrix1.len() {
        if matrix1[i].len() != matrix2[i].len() {
            return false;
        }

        for j in 0 .. matrix1[i].len() {
            if matrix1[i][j] != matrix2[i][j] {
                return false;
            }
        }
    }

    true
}


#[test]
fn test_leetcode_3x3() {
    let mut image3x3: Vec<Vec<i32>> = vec![
        vec![1, 2, 3],
        vec![4, 5, 6],
        vec![7, 8, 9],
    ];

    let image3x3_rotated: Vec<Vec<i32>> = vec![
        vec![7, 4, 1],
        vec![8, 5, 2],
        vec![9, 6, 3],
    ];

    Solution::rotate(&mut image3x3);
    assert!(matrices_equal(&image3x3, &image3x3_rotated));
}


#[test]
fn test_leetcode_4x4() {
    let mut image4x4: Vec<Vec<i32>> = vec![
        vec![5,1,9,11],
        vec![2,4,8,10],
        vec![13,3,6,7],
        vec![15,14,12,16]
    ];

    let image4x4_rotated: Vec<Vec<i32>> = vec![
        vec![15,13,2,5],
        vec![14,3,4,1],
        vec![12,6,8,9],
        vec![16,7,10,11]
    ];

    Solution::rotate(&mut image4x4);
    assert!(matrices_equal(&image4x4, &image4x4_rotated));
}
