use crate::queues::Queue;
use crate::queues::IsQueue;

pub struct Solution {}

impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut queue: Queue<(Vec<i32>, Vec<i32>)> = queue![];
        let _ = queue.add((vec![], nums));

        let mut power_set = vec![];
        
        while queue.size() > 0 {
            match queue.remove() {
                Ok((set, remainder)) => {
                    if remainder.len() <= 0 {
                        power_set.push(set);
                        continue;
                    }

                    let mut set_includes = set.clone();
                    set_includes.push(remainder[0]);
                    let set_excludes = set.clone();

                    let _ = queue.add((set_includes, (&remainder[1..]).to_vec()));
                    let _ = queue.add((set_excludes, (&remainder[1..]).to_vec()));
                }
                Err(error) => panic!["{:?}", error]
            }
        }

        return power_set;
    }
}
