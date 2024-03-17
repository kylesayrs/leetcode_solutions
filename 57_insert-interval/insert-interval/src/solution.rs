pub struct Solution {}

impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let mut new_interval = new_interval.clone();
        let mut new_intervals: Vec<Vec<i32>> = vec![];
        let mut inserted_p = false;

        for interval in intervals {
            // already inserted
            if inserted_p {
                new_intervals.push(interval.clone());
                continue;
            }

            // strictly less than
            if new_interval[1] < interval[0] {
                new_intervals.push(new_interval.clone());
                inserted_p = true;
                new_intervals.push(interval.clone());
                continue;
            }

            // strictly greater
            if new_interval[0] > interval[1] {
                new_intervals.push(interval.clone());
                continue;
            }

            // overlapping: merge
            new_interval[0] = std::cmp::min(new_interval[0], interval[0]);
            new_interval[1] = std::cmp::max(new_interval[1], interval[1]);
        }

        // strictly greater than all
        if !inserted_p {
            new_intervals.push(new_interval.clone());
        }

        return new_intervals;
    }
}


#[test]
fn test_leetcode() {
    assert_eq!(
        Solution::insert(
            vec![vec![1, 3], vec![6, 9]],
            vec![2, 5]
        ),
        vec![vec![1, 5], vec![6, 9]]
    );

    assert_eq!(
        Solution::insert(
            vec![vec![1, 2], vec![3, 5], vec![6, 7], vec![8, 10], vec![12, 16]],
            vec![4, 8]
        ),
        vec![vec![1, 2], vec![3, 10], vec![12, 16]]
    );
}
