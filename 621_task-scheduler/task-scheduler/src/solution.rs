pub struct Solution {}

impl Solution {
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        // make frequency array
        let mut freqs = vec![0; 26];
        for task in &tasks {
            freqs[*task as usize - 'A' as usize] += 1;
        }

        // sort array
        freqs.sort_by_key(|e| std::cmp::Reverse(*e));

        // compute num free slots
        let num_gaps = freqs[0] - 1;
        let mut num_free_slots = num_gaps * (n + 1);

        // subtract free slots
        for freq in freqs {
            if freq <= 0 {
                break;
            }

            num_free_slots -= std::cmp::min(num_gaps, freq);
        }

        // add any free slots to the total
        return tasks.len() as i32 + std::cmp::max(num_free_slots, 0);
    }
}


#[test]
fn test_leetcode() {
    assert_eq!(
        Solution::least_interval(vec!['A', 'A', 'A', 'B', 'B' ,'B'], 2),
        8
    );

    assert_eq!(
        Solution::least_interval(vec!['A', 'C', 'A', 'B', 'D' ,'B'], 2),
        6
    );

    assert_eq!(
        Solution::least_interval(vec!['A', 'A', 'A', 'B', 'B' ,'B'], 3),
        10
    );
}
