use std::collections::VecDeque;

pub struct Solution {}

impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut queue: VecDeque<(Vec<i32>, Vec<i32>)> = VecDeque::from([
            (vec![], nums)
        ]);

        let mut power_set = vec![];
        
        while ! queue.is_empty() {
            match queue.pop_front() {
                Some((set, remainder)) => {
                    if remainder.len() <= 0 {
                        power_set.push(set);
                        continue;
                    }

                    let mut set_includes = set.clone();
                    set_includes.push(remainder[0]);
                    let set_excludes = set.clone();

                    let _ = queue.push_back((set_includes, (&remainder[1..]).to_vec()));
                    let _ = queue.push_back((set_excludes, (&remainder[1..]).to_vec()));
                }
                None => panic!("Failed to pop from queue")
            }
        }

        return power_set;
    }
}
