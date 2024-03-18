pub struct Solution {}

impl Solution {
    pub fn find_min_arrow_shots(mut points: Vec<Vec<i32>>) -> i32 {
        // much much faster than sort_by
        points.sort_unstable_by_key(|point| point[1]);

        let mut num_arrows = 0;
        let mut arrow_position = -1;

        for point in points {
            if arrow_position == -1 || point[0] > arrow_position {
                arrow_position = point[1];
                num_arrows += 1;
                continue;
            }
        }
        return num_arrows;
    }
}


#[test]
fn test_leetcode() {
    assert_eq!(
        Solution::find_min_arrow_shots(vec![
            vec![10, 16],
            vec![2, 8],
            vec![1, 6],
            vec![7, 12]
        ]),
        2
    );

    assert_eq!(
        Solution::find_min_arrow_shots(vec![
            vec![1, 2],
            vec![3, 4],
            vec![5, 6],
            vec![7, 8]
        ]),
        4
    );

    assert_eq!(
        Solution::find_min_arrow_shots(vec![
            vec![1, 2],
            vec![2, 3],
            vec![3, 4],
            vec![4, 5]
        ]),
        2
    );
}
