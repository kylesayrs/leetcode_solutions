use std::collections::BinaryHeap;

struct Solution {}

impl Solution {
    pub fn furthest_building(heights: Vec<i32>, mut bricks: i32, mut ladders: i32) -> i32 {
        let mut bricks_max_heap: BinaryHeap<i32> = BinaryHeap::new();

        let height_differences: Vec<i32> = heights.windows(2).map(|pair| pair[1] - pair[0]).collect();
        for (index, &height) in height_differences.iter().enumerate() {
            // steps down are free
            if height <= 0 {
                continue;
            }

            // greedly use bricks when enough are available
            if height <= bricks {
                bricks -= height;
                bricks_max_heap.push(height);
                continue;
            
            }

            // no more ladders left
            if ladders <= 0 {
                return index as i32;
            }

            // need to use a ladder somewhere
            ladders -= 1;

            // check heap for swaps
            match bricks_max_heap.peek() {
                Some(&max_bricks_height) => {
                    // replace 
                    if max_bricks_height > height {
                        bricks_max_heap.pop();
                        bricks_max_heap.push(height);
                        bricks += max_bricks_height - height;
                    }
                    // otherwise use ladder on new height
                },
                // no swaps available, use ladder on new height
                None => {}
            }
        }

        // reached end of list
        return heights.len() as i32 - 1;
    }
}

fn main() {
    println!("{:?}", Solution::furthest_building(vec![4,2,7,6,9,14,12], 5, 1));
}

#[test]
fn test_leetcode() {
    assert_eq!(Solution::furthest_building(vec![0], 0, 0), 0);
    assert_eq!(Solution::furthest_building(vec![4,2,7,6,9,14,12], 5, 1), 4);
    assert_eq!(Solution::furthest_building(vec![4,12,2,7,3,18,20,3,19], 10, 2), 7);
    assert_eq!(Solution::furthest_building(vec![14,3,19,3], 17, 0), 3);
}
